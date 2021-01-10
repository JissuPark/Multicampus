/**********************************************************
*	SQL Query & Function Example2
**********************************************************/
/**
-- Employees Table Columns
-- EMPLOYEE_ID
-- FIRST_NAME
-- LAST_NAME
-- EMAIL
-- PHONE_NUMBER
-- HIRE_DATE
-- JOB_ID
-- SALARY
-- COMMISSION_PCT
-- MANAGER_ID
-- DEPARTMENT_ID
**/

/**
--Departments Table Columns
--DEPARTMENT_ID
--DEPARTMENT_NAME
--MANAGER_ID
--LOCATION_ID
**/

/**
50번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
select avg(salary) as '평균',
		max(salary) as '최고',
        min(salary) as '최저',
        count(salary) as '인원수'
        from employees
        where department_id = 50
        group by department_id;

/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
select avg(salary) as '평균',
		max(salary) as '최고',
        min(salary) as '최저',
        count(salary) as '인원수'
        from employees
        group by department_id;

/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
select department_id as '부서번호',
		job_id as '업무명',
		count(job_id) as '인원수'
        from employees
        group by department_id, job_id;

/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
select job_id as '업무',
		count(job_id) as '인원수'
        from employees
        group by job_id
        having count(job_id) >= 4;

/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
select avg(salary) as '평균월급',
		sum(salary) as '최고월급',
		max(salary) as '최고월급',
		min(salary) as '최저월급'
        from employees
        group by department_id
        order by avg(salary);

/**
 부서번호, 부서명, 이름, 급여를 출력하라.
**/
select e.department_id as '부서번호',
		d.department_name as '부서명',
		concat(' ', e.first_name , e.last_name) as '이름',
        e.salary as '급여'
	from employees as e
	join departments as d 
		on e.department_id = d.department_id; 

/**
이름이 adam인 사원의 부서명을 출력하라.
**/
select d.department_name as '부서명'
	from departments as d
    join employees as e
		on d.department_id = e.department_id
	where e.first_name = 'adam';

/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하라
'smith'의 매니저는 'ford'이다.
**/
select concat(employee_id, '의 매니저는 ', manager_id, '이다.') as '관계'
	from employees;

/**
adam의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하라.
**/
select concat_ws(' ', e.first_name, e.last_name) as '이름',
		d.department_name as '부서명',
		e.salary as '급여',
        e.job_id as '직무'
	from employees as e
    join departments as d
		on e.department_id = d.department_id
	where job_id = (select job_id from employees where first_name = 'adam');

/**
전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
**/
select e.employee_id as '사원번호',
		concat_ws(' ', e.first_name, e.last_name) as '이름',
        d.department_name as '부서명',
        e.hire_date as '입사일',
        d.laction_id as '지역',
        e.salary as '급여'
	from employees as e
    join department as d
		on e.department_id = d.department_id
	group by e.salary
    having e.salary > avg(e.salary);

/**
50번 부서사람들 중에서 30번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하라.
**/
select e.employee_id as '사원번호',
		concat_ws(' ', e.first_name, e.last_name) as '이름',
        d.department_name as '부서명',
        e.hire_date as '입사일'
	from employees as e
    join departments as d
		on e.department_id = d.department_id
	where d.department_id = 50
		and e.job_id = (select job_id from employees where department_id = 30);

/**
급여가 30번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하라.
**/
select department_id as '사원번호', 
		concat_ws(' ', first_name, last_name) as '이름',
		salary as '급여'
	from employees 
    where salary > (select max(salary) from employees where department_id = 30 group by salary);