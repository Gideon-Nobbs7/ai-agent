CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, price, category) VALUES 
    ('Samsung Galaxy S23', 1200.00, 'Smartphone'),
    ('Nokia Lumia', 700.00, 'Smartphone'),
    ('iPhone 14', 1500.50, 'Smartphone'),
    ('Tecno Spark 10', 400.00, 'Smartphone');
