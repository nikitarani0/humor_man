create database company_db;
use company_db;

create table employees(
emp_id int primary key,
emp_name varchar(50),
salary int ,
dept_id int
);

create table departments(
dept_id int,
dept_name varchar(50)
);

insert into employees 
values
(1,"isahn",70000,2),
(2,"isahn",60000,1),
(3,"ishan",90000,3),
(4,"sahn",60000,3),
(5,"qisahn",50000,2);

insert into departments 
values
(1,"offence cyber"),
(2,"defence cyber"),
(3,"digital for");

select emp_name, salary ,dept_name
from employees
join departments on employees.dept_id = departments.dept_id
;

select * from employees 
where salary > (select avg(salary) from employees);