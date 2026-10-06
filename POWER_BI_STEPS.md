# Power BI mein dashboard kaise banaye (15-20 min)

1. Power BI Desktop > Get Data > Text/CSV > `sales_data.csv` > Transform Data.
2. Power Query: `order_date` ko Date type karo, `sales` aur `profit` ko Decimal. Duplicates hatao (Remove Duplicates on order_id). Load.
3. Date table banao (Modeling > New Table):
   `DateTable = ADDCOLUMNS(CALENDARAUTO(), "Year", YEAR([Date]), "Month", FORMAT([Date],"MMM"), "MonthNo", MONTH([Date]))`
   Relationship: DateTable[Date] -> sales[order_date]. Month ko MonthNo se sort karo.
4. DAX measures:
   ```
   Revenue = SUM(sales[sales])
   Profit = SUM(sales[profit])
   Profit Margin % = DIVIDE([Profit],[Revenue])
   Prev Month Revenue = CALCULATE([Revenue], DATEADD(DateTable[Date],-1,MONTH))
   MoM Growth % = DIVIDE([Revenue]-[Prev Month Revenue],[Prev Month Revenue])
   ```
5. Visuals: 3 Cards (Revenue, Profit, Profit Margin %), Line chart (Month vs Revenue), Clustered bar (Category vs Revenue/Profit), Bar (Top 5 Product by Revenue, Top N filter), Donut (Region).
6. Slicers: Year, Category, Region. Publish to Power BI Service ya screenshot GitHub README mein daalo.
