--Combine the Orders table and the Customers table into one joined dataset so that every order shows its customer’s name, region, and email.
--Keep all orders, even those that don’t have matching customers, because we’ll handle missing data later.

DROP TABLE IF EXISTS orders_customers_joined;

CREATE TABLE orders_customers_joined AS
SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.total_amount,
    c.customer_name,
    c.region,
    c.email
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id;

SELECT * FROM orders_customers_joined;

-- ##Reflection:
-- I joined Orders and Customers using LEFT JOIN so ever order appears, even if a customer record is missing. 
-- This prepares a complete dataset for analysis and prevents data loss.
 