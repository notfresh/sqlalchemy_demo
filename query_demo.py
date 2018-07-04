from models import *


def query_emp():
    emp1 = sess.query(Emp).first()
    print(emp1)


# 查询名字叫Smith的员工
def query_emp_with_filter():
    emp1 = sess.query(Emp).filter(Emp.ename == 'Smith').first()
    print(emp1)


# 查询名字叫Smith, 职务为CLERK的一个员工
def query_emp_with_filters():
    emp1 = sess.query(Emp).filter(Emp.ename == 'Smith', Emp.job == 'CLERK').first()
    print(emp1)


# 查询职务为CLERK的全部员工
def query_emp_all_clerks():
    emp_clerks = sess.query(Emp).filter(Emp.job == 'CLERK').all()
    for clerk in emp_clerks:
        print(clerk)


# 查询员工的名字和工号, 并按入职日期排序
def query_emp_empno_ename_order_by_hiredate():
    emps = sess.query(Emp.empno, Emp.ename, Emp.job, Emp.hiredate).order_by(Emp.hiredate.asc()).all()
    for item in emps:
        print(item.empno, item.ename, item.job, item.hiredate)


if __name__ == '__main__':
    query_emp_empno_ename_order_by_hiredate()