use bridgelabz;
CREATE TABLE customers (
    id INT NOT NULL,
    first_name  VARCHAR(50) NOT NULL,
    country     VARCHAR(50),
    score       INT,
    CONSTRAINT PK_customers PRIMARY KEY (id)
);


INSERT INTO customers (id, first_name, country, score) VALUES
    (1, 'Maria',     'Germany', 350),
    (2, ' John',     'USA',     900),
    (3, 'Georg',   'UK',      750),
    (4, 'Martin', 'Germany', 500),
    (5, 'Peter',   'USA',     0);
GO



