-- 部门 表
-- Create table
create table DEPT
(
deptno int(2) not null,
dname varchar(14),
loc varchar(13)
)
;
-- Create/Recreate primary, unique and foreign key constraints
alter table DEPT
add constraint PK_DEPT primary key (DEPTNO);

insert into dept (DEPTNO, DNAME, LOC)
values (10, 'ACCOUNTING', 'NEW YORK');

insert into dept (DEPTNO, DNAME, LOC)
values (20, 'RESEARCH', 'DALLAS');

insert into dept (DEPTNO, DNAME, LOC)
values (30, 'SALES', 'CHICAGO');

insert into dept (DEPTNO, DNAME, LOC)
values (40, 'OPERATIONS', 'BOSTON');

-- 员工表
create table EMP
(
empno int(4) not null,
ename varchar(10),
job varchar(9),
mgr int(4),
hiredate DATE,
sal DECIMAL(7,2),
comm DECIMAL(7,2),
deptno int(2),
desc2 varchar(30) default 2
)
;
-- Create/Recreate primary, unique and foreign key constraints
alter table EMP
add constraint PK_EMP primary key (EMPNO);
alter table EMP
add constraint FK_DEPTNO foreign key (DEPTNO)
references DEPT (DEPTNO);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7369, 'SMITH', 'CLERK', 7902, str_to_date('17-12-1980', '%d-%m-%Y'), 800.00, 1999.00, 20, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7499, 'ALLEN', 'SALESMAN', 7698, str_to_date('20-02-1981', '%d-%m-%Y'), 1600.00, 300.00, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7521, 'WARD', 'SALESMAN', 7698, str_to_date('22-02-1981', '%d-%m-%Y'), 1250.00, 500.00, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7566, 'JONES', 'MANAGER', 7839, str_to_date('02-04-1981', '%d-%m-%Y'), 2975.00, null, 20, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7654, 'MARTIN', 'SALESMAN', 7698, str_to_date('28-09-1981', '%d-%m-%Y'), 1250.00, 1400.00, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7698, 'BLAKE', 'MANAGER', 7839, str_to_date('01-05-1981', '%d-%m-%Y'), 2850.00, null, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7782, 'CLARK', 'MANAGER', 7839, str_to_date('09-06-1981', '%d-%m-%Y'), 2450.00, null, 10, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7788, 'SCOTT', 'ANALYST', 7566, str_to_date('19-04-1987', '%d-%m-%Y'), 3000.00, null, 20, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7839, 'KING', 'PRESIDENT', null, str_to_date('17-11-1981', '%d-%m-%Y'), 5000.00, null, 10, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7844, 'TURNER', 'SALESMAN', 7698, str_to_date('08-09-1981', '%d-%m-%Y'), 1500.00, 0.00, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7876, 'ADAMS', 'CLERK', 7788, str_to_date('23-05-1987', '%d-%m-%Y'), 1100.00, null, 20, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7900, 'JAMES', 'CLERK', 7698, str_to_date('03-12-1981', '%d-%m-%Y'), 950.00, null, 30, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7902, 'FORD', 'ANALYST', 7566, str_to_date('03-12-1981', '%d-%m-%Y'), 3000.00, null, 20, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7934, 'MILLER', 'CLERK', 7782, str_to_date('23-01-1982', '%d-%m-%Y'), 1300.00, null, 10, null);

insert into emp (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, DESC2)
values (7935, 'KATE', 'MANAGER', null, null, null, null, null, null);



