-- Create table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT ( order_id , customer_name , order_date , quantity ,  status, product_id) FROM orders;
SELECT (product_id , product_name , price  ,  category) FROM products;