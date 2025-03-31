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
    ('Tecno Spark 10', 400.00, 'Smartphone'),
    ('Dell XPS 13', 1200.99, 'Laptop'),
    ('Apple MacBook Air', 1500.73, 'Laptop'),
    ('Sony WH-1000XM4', 350.00, 'Headphones'),
    ('Samsung 4K UHD TV', 1800.50, 'Television'),
    ('Logitech MX Master 3', 100.94, 'Mouse');
