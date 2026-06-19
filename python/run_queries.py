query = """
SELECT
    c.region,
    SUM(p.payment_value) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.region
ORDER BY revenue DESC;
"""