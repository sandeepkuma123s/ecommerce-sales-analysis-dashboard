-- Total Revenue
SELECT SUM(payment_value) AS total_revenue
FROM payments;

-- Top Selling Products
SELECT product_id, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product_id
ORDER BY total_sold DESC;

-- Category-wise Revenue
SELECT category, SUM(payment_value) AS revenue
FROM sales_data
GROUP BY category
ORDER BY revenue DESC;

-- Best Customers
SELECT customer_name, SUM(payment_value) AS total_spent
FROM customer_sales
GROUP BY customer_name
ORDER BY total_spent DESC;

-- Region-wise Sales
SELECT region, SUM(payment_value) AS revenue
FROM customer_sales
GROUP BY region
ORDER BY revenue DESC;