DROP TABLE IF EXISTS employees;

create table if not exists employees (
id_employees serial primary key,
first_name varchar(15),
last_name varchar(15),
company_name varchar(50),
address varchar(100),
city  varchar(25),
state varchar(20),
zip varchar(10),
phone1 varchar(15),
phone2 varchar(15),
email varchar(100),
department varchar(50)
);

