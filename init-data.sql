CREATE TABLE IF NOT EXISTS items
(
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price FLOAT,
    in_stock BOOLEAN
);

BEGIN;

INSERT INTO items (name, description, price, in_stock) VALUES

('Milk', '1 liter of whole milk', 1.99, TRUE),
('Eggs', 'A dozen organic eggs', 2.99, TRUE),
('Bread', 'Whole wheat bread loaf', 2.49, TRUE),
('Butter', 'Salted butter, 200g', 3.59, TRUE),
('Cheese', 'Cheddar cheese, 250g', 4.99, TRUE),
('Yogurt', 'Greek yogurt, 500g', 3.79, TRUE),
('Apples', 'Fresh red apples, 1kg', 3.49, TRUE),
('Bananas', 'Ripe yellow bananas, 1kg', 1.69, TRUE);

COMMIT;