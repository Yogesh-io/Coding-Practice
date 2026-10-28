-- 2. Fetch all employees whose names contain the letter "a" exactly twice.
select * from employees 
where names like '%a%a%' and names not like '%a%a%a%';