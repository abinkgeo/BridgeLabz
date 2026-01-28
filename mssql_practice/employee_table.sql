use bridgelabz;
CREATE TABLE employee(
    e_id int NOT NULL,
    e_name VARCHAR(20),
    e_age int,
    e_dept VARCHAR(20),
    PRIMARY KEY(e_id)
);

INSERT INTO employee VALUES(1,'Abin',22,'Developer');

INSERT INTO employee (e_id, e_name, e_age, e_dept)
VALUES
(2,'Madhan',21,'Developer'),
(3, 'Alice', 28, 'HR'),
(4, 'Bob', 32, 'IT'),
(5, 'Charlie', 26, 'Finance'),
(6, 'David', 35, 'Sales');


