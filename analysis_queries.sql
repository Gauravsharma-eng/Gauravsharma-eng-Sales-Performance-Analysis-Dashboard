-- Table: sales(order_id, order_date, segment, region, category, sub_category, product, quantity, discount, sales, profit)

-- 1. Headline KPIs
SELECT COUNT(*) AS orders, SUM(sales) AS revenue, SUM(profit) AS profit,
       ROUND(100.0*SUM(profit)/SUM(sales),1) AS profit_margin_pct
FROM sales;

-- 2. Monthly revenue, profit and month-over-month growth
WITH m AS (SELECT strftime('%Y-%m',order_date) AS mon, SUM(sales) AS rev, SUM(profit) AS pr FROM sales GROUP BY 1)
SELECT mon, rev, pr, ROUND(100.0*(rev-LAG(rev) OVER (ORDER BY mon))/LAG(rev) OVER (ORDER BY mon),1) AS mom_growth_pct FROM m;

-- 3. Category performance
SELECT category, SUM(sales) AS revenue, SUM(profit) AS profit, ROUND(100.0*SUM(profit)/SUM(sales),1) AS margin_pct
FROM sales GROUP BY category ORDER BY revenue DESC;

-- 4. Top 5 products by revenue
SELECT product, SUM(sales) AS revenue, SUM(profit) AS profit FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 5;

-- 5. Seasonal demand: avg monthly revenue in Oct-Dec vs rest of the year
WITH m AS (SELECT strftime('%Y-%m',order_date) AS mon, CAST(strftime('%m',order_date) AS INT) AS mo, SUM(sales) AS rev FROM sales GROUP BY 1)
SELECT AVG(CASE WHEN mo IN (10,11,12) THEN rev END) AS peak_avg, AVG(CASE WHEN mo NOT IN (10,11,12) THEN rev END) AS normal_avg,
       ROUND(100.0*(AVG(CASE WHEN mo IN (10,11,12) THEN rev END)/AVG(CASE WHEN mo NOT IN (10,11,12) THEN rev END)-1),1) AS seasonal_lift_pct
FROM m;

-- 6. Discount impact on margin
SELECT discount, COUNT(*) AS orders, ROUND(100.0*SUM(profit)/SUM(sales),1) AS margin_pct FROM sales GROUP BY discount ORDER BY discount;
