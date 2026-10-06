import random, csv, sqlite3, json
from datetime import date, timedelta
random.seed(42)
# category, sub_category, product, unit_price, margin
P = [("Technology","Phones","Smartphone X",18000,.14),("Technology","Accessories","Wireless Earbuds",2500,.30),
("Technology","Machines","Laser Printer",9000,.12),("Furniture","Chairs","Ergo Office Chair",6500,.18),
("Furniture","Tables","Standing Desk",12000,.10),("Furniture","Bookcases","Wooden Bookcase",4500,.15),
("Office Supplies","Paper","A4 Paper Pack",350,.35),("Office Supplies","Binders","Heavy Binder Set",600,.28),
("Office Supplies","Storage","Storage Box",900,.25),("Technology","Accessories","Laptop Bag",1800,.32)]
REG = ["North","South","East","West"]; SEG = ["Consumer","Corporate","Home Office"]
SEAS = {m:(0.99 if m<10 else 1.10) for m in range(1,13)}
days = [date(2023,1,1)+timedelta(d) for d in range(731)]
w = [SEAS[d.month] for d in days]
rows=[]
for i in range(10500):
    d = random.choices(days, w)[0]; c,s,p,pr,m = random.choice(P)
    q = random.randint(1,5); disc = random.choice([0,0,0,.05,.1,.2])
    sales = round(pr*q*(1-disc),2)
    mg = m - disc*0.6 + random.uniform(-.04,.04)
    rows.append((f"ORD-{10000+i}",d.isoformat(),random.choice(SEG),random.choice(REG),c,s,p,q,disc,sales,round(sales*mg,2)))
hdr=["order_id","order_date","segment","region","category","sub_category","product","quantity","discount","sales","profit"]
with open("sales_data.csv","w",newline="") as f:
    cw=csv.writer(f); cw.writerow(hdr); cw.writerows(rows)
db=sqlite3.connect(":memory:")
db.execute("create table sales(order_id,order_date,segment,region,category,sub_category,product,quantity,discount,sales,profit)")
db.executemany("insert into sales values(?,?,?,?,?,?,?,?,?,?,?)",rows)
q=lambda s:db.execute(s).fetchall()
out={}
out["kpi"]=q("select count(*),round(sum(sales)),round(sum(profit)),round(100*sum(profit)/sum(sales),1) from sales")[0]
out["monthly"]=q("""with m as(select strftime('%Y-%m',order_date) mon,sum(sales) rev,sum(profit) pr from sales group by 1)
select mon,round(rev),round(pr),round(100.0*(rev-lag(rev) over(order by mon))/lag(rev) over(order by mon),1) from m""")
out["category"]=q("select category,round(sum(sales)),round(sum(profit)),round(100*sum(profit)/sum(sales),1) from sales group by 1 order by 2 desc")
out["top"]=q("select product,round(sum(sales)),round(sum(profit)) from sales group by 1 order by 2 desc limit 5")
out["region"]=q("select region,round(sum(sales)) from sales group by 1 order by 2 desc")
out["season"]=q("""with m as(select strftime('%Y-%m',order_date) mon,cast(strftime('%m',order_date) as int) mo,sum(sales) rev from sales group by 1)
select round(avg(case when mo in(10,11,12) then rev end)),round(avg(case when mo not in(10,11,12) then rev end)) from m""")[0]
out["season_pct"]=round(100*(out["season"][0]/out["season"][1]-1),1)
json.dump(out,open("results.json","w"))
print(json.dumps(out["kpi"]),out["season"],out["season_pct"]); print(out["category"]); print(out["top"])
