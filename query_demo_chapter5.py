from sqlalchemy import case, func
from sqlalchemy.sql import label

from models import *


# 测试分页功能
def query_paginate():
    emps = sess.query(Emp).order_by(Emp.empno.asc()).limit(3).offset(3).all()
    for item in emps:
        print(item)
    '''
    output:
    
    {'empno': 7566, 'ename': 'JONES', 'job': 'MANAGER', 'deptno': 20, 'sal': Decimal('2975.00'), 'comm': None}
    {'empno': 7654, 'ename': 'MARTIN', 'job': 'SALESMAN', 'deptno': 30, 'sal': Decimal('1250.00'), 'comm': Decimal('1400.00')}
    {'empno': 7698, 'ename': 'BLAKE', 'job': 'MANAGER', 'deptno': 30, 'sal': Decimal('2850.00'), 'comm': None}
    
    
    
    '''


# 测试分页功能2, 如果把 offset和limit调换顺序呢？其实也没问题好像。 目前我没有深究
def query_paginate2():
    emps = sess.query(Emp).order_by(Emp.empno.asc()).offset(3).limit(3).all()
    for item in emps:
        print(item)
    '''
    
    output:
    
    {'empno': 7566, 'ename': 'JONES', 'job': 'MANAGER', 'deptno': 20, 'sal': Decimal('2975.00'), 'comm': None}
    {'empno': 7654, 'ename': 'MARTIN', 'job': 'SALESMAN', 'deptno': 30, 'sal': Decimal('1250.00'), 'comm': Decimal('1400.00')}
    {'empno': 7698, 'ename': 'BLAKE', 'job': 'MANAGER', 'deptno': 30, 'sal': Decimal('2850.00'), 'comm': None}
    '''


'''
note:

请大家注意， sqlalchemy和flask-sqlalchemy是两个不同的包。
sqlalchemy是原生的，核心。
flask-sqlalchemy是根据sqlalchemy， 为flask量身定制开发的。 flask是一个web轻量级框架。
请注意sqlalchemy和flask-sqlalchemy的界限。
paginate函数是flask-sqlalchemy的方法， 不属于原生的sqlalchemy， 鉴于时间和精力的关系， 我不在这里写了。

'''


if __name__ == '__main__':
    query_paginate2()
