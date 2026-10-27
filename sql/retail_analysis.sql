
-- 1. Overall business KPIs
SELECT
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(SUM(Cost), 2) AS total_cost,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(100.0 * SUM(Profit) / SUM(Revenue), 2) AS profit_margin_pct,
    SUM(Quantity) AS units_sold,
    COUNT(DISTINCT Order_ID) AS order_count
FROM retail_sales;

-- 2. Product profitability
SELECT Product,
       ROUND(SUM(Revenue), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY Product
ORDER BY profit DESC;

-- 3. Regional performance
SELECT Region,
       ROUND(SUM(Revenue), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY Region
ORDER BY revenue DESC;

-- 4. Monthly trends
SELECT SUBSTR(Order_Date, 1, 7) AS sales_month,
       ROUND(SUM(Revenue), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY sales_month
ORDER BY sales_month;

-- 5. Sales channel performance
SELECT Sales_Channel,
       COUNT(*) AS order_lines,
       SUM(Quantity) AS units_sold,
       ROUND(SUM(Revenue), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY Sales_Channel
ORDER BY revenue DESC;
