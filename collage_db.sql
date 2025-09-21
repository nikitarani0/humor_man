create database college;
use college;

create table students(
id int primary key auto_increment,
name varchar(50),
age int ,
dept varchar(30),
marks int
);
insert into students
values
(1,"ishan",23,"cyber",3000),
(2,"isa",22,"finance",2000),
(3,"kni",22,"marketing",1000),
(4,"shi",23,"sales",500),
(5,"no_one",23,"cyber",3000);

select * from students where marks>70;
select dept, count(*) as total_student
from students
group by dept;

select * from students
where marks = (select max(marks) from students)