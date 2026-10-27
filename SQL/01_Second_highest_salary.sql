-- 1. Write a query to find the second highest salary in an employee Table.
select max(salary) from employees
where salary < (select max(salary) from employees);