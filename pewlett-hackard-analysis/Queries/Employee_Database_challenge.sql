-- Employee_Database_challenge.sql

-- Query employees and titles tables
SELECT emp_no, first_name, last_name
FROM employees limit 100;

SELECT title, from_date, to_date
FROM titles limit 100;

-- Join employees table to titles table
SELECT emp.emp_no, emp.first_name, emp.last_name,
		ti.title, ti.from_date, ti.to_date
INTO retirement_titles
FROM employees as emp
INNER JOIN titles as ti ON emp.emp_no = ti.emp_no
WHERE (emp.birth_date BETWEEN '1952-01-01' AND '1955-12-31')
ORDER BY emp_no;

-- Use Dictinct with Orderby to remove duplicate rows
SELECT DISTINCT ON (emp_no) emp_no, first_name, last_name, title
INTO unique_titles
FROM retirement_titles
WHERE to_date = '9999-01-01'
ORDER BY emp_no, to_date DESC;

-- Number of employees by their most recent job title
SELECT COUNT(emp_no) "Count", title
INTO retiring_titles
FROM unique_titles
GROUP BY title
ORDER BY "Count" DESC;


-- Create Mentorship Eligibility table
--

-- employees table
SELECT emp_no, first_name, last_name, birth_date
FROM employees LIMIT 100;

-- dept_emp table
SELECT from_date, to_date
FROM dept_emp LIMIT 100;

-- titles table
SELECT title FROM titles LIMIT 100;

-- Join employees to dept_emp and titles table
SELECT DISTINCT ON (emp.emp_no) emp.emp_no, emp.first_name, emp.last_name, emp.birth_date,
	de.from_date, de.to_date, ti.title
INTO mentorship_eligibilty
FROM employees as emp
INNER JOIN dept_emp as de ON emp.emp_no = de.emp_no
INNER JOIN titles as ti ON emp.emp_no = ti.emp_no
WHERE de.to_date = '9999-01-01'
AND emp.birth_date BETWEEN '1965-01-01' and '1965-12-31'
ORDER BY emp.emp_no;

--
-- Create non-retirement table
SELECT emp.emp_no, emp.first_name, emp.last_name,
		ti.title, ti.from_date, ti.to_date
INTO non_retirement_titles
FROM employees as emp
INNER JOIN titles as ti ON emp.emp_no = ti.emp_no
WHERE (emp.birth_date > '1955-12-31')
ORDER BY emp_no;

SELECT DISTINCT ON (emp_no) emp_no, first_name, last_name, title
INTO unique_titles_non_retiring
FROM non_retirement_titles
WHERE to_date = '9999-01-01'
ORDER BY emp_no;

-- Non-retiring titles
SELECT COUNT(emp_no) "Count", title
INTO non_retiring_titles
FROM unique_titles_non_retiring
GROUP BY title
ORDER BY "Count" DESC;

-- Compare retiring count to non-retiring count
SELECT r.title, r."Count" as retiring_count, nr."Count" as non_retiring_count, 
	ROUND(.1*r."Count",0) as ten_pct_attrition,
	r."Count" - ROUND(.1*r."Count",0) as retiring_count_minus_attr
INTO retiring_comparison
FROM retiring_titles as r
LEFT JOIN non_retiring_titles as nr ON r.title = nr.title
ORDER BY r."Count" DESC;

-- retiring comparison query
select * from retiring_comparison

-- Mentorship
select title, Count(*) as "Employee Count"
from mentorship_eligibilty
group by title
order by title;



