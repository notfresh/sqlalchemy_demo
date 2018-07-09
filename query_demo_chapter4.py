from models import *


# 别名
def query_with_column_alias():
    emps = sess.query(Emp.ename.label('name')).all()
    for item in emps:
        print(item)
    '''
    output:
    
    ('SMITH',)
    ('ALLEN',)
    ('WARD',)
    ('JONES',)
    ('MARTIN',)
    ('BLAKE',)
    ('CLARK',)
    ('SCOTT',)
    ('KING',)
    ('TURNER',)
    ('ADAMS',)
    ('JAMES',)
    ('FORD',)
    ('MILLER',)
    ('KATE',)
    
    note:
    
    输出的结果是元祖. 请注意写法, 括号里面带一个逗号, 表明是元祖tuple, 如果没有这个逗号, 讲不被python认为是tuple.
    例如:
    
    In [1]: a = (1)

    In [2]: type(a)
    Out[2]: int

    In [3]: b = (1,)
    
    In [4]: type(b)
    Out[4]: tuple


    '''


# 别名查询, 并且在查询结果中引用.
def query_with_column_alias_and_call_it():
    emps = sess.query(Emp.ename.label('name')).limit(3).all()  # 请注意, limit(3)意思是查三条. 这是mysql的特殊用法.
    emp1 = emps[0]
    print(type(emp1))  # 我们查看一下 emp1是什么类型的.
    # 如何引用name属性呢?
    name1 = emp1.name  # 用属性的方式引用
    print('name1', name1)
    name2 = emp1[0]  # 用数组的方式引用.
    print('name2', name2)
    '''
    output:
    
    <class 'sqlalchemy.util._collections.result'>
    name1 SMITH
    name2 SMITH
    
    note:
    
    查询结果单个对象是一个实现了 tuple 的类, 既可以当数组用, 又可以当对象用. 
    但是这是一个冻结的数组和对象. 不可以修改. 也就是不能当普通的数组和对象用.不能添加属性和元素.
    
    '''


# 函数的用法
def query_with_function():
    from sqlalchemy import func
    from sqlalchemy.sql import label
    # 这次, 我想查员工的工资. 但是不显示十位和各位. 比如 9124, 我只显示为9100. 怎么做呢? 使用python的方法吗. 太笨了. 我们直接调用mysql的内置方法.
    comms = sess.query(Emp.ename, Emp.comm, label('comm_trunc', func.truncate(Emp.comm, -2))).limit(3).all()
    for item in comms:
        print(item.ename, item.comm, item.comm_trunc)

    '''
    output:
    
    SMITH 1999.00 1900
    ALLEN 300.00 300
    WARD 500.00 500
    
    note:
    
    这里的label用法的另一种写法.
    之前我们直接使用 Emp.ename.label('name')
    这里我们使用 label('comm_trunc', func.truncate(Emp.comm, -2)), 这是对函数的其中一种写法.
    
    func.XXX 可以使用原生的数据库里的所有方法, 只需要加个前缀func. 既可. 
    喜欢原生数据方法的请大胆使用.
    
    关于truncate方法, 请参考 https://www.w3schools.com/sql/func_mysql_truncate.asp
    
    '''


# 分组的用法
def query_and_group():
    # 本次, 我们要统计每个职业有多少员工.
    from sqlalchemy import func
    results = sess.query(Emp.job, func.count(Emp.empno).label('job_count')).group_by(Emp.job).all()
    for item in results:
        print(item.job, item.job_count)

    '''
    output: 
    
    ANALYST 2
    CLERK 4
    MANAGER 4
    PRESIDENT 1
    SALESMAN 4
    
    
    note:
    
    group_by的用法:
    通过查看终端的打印的语句,我们看到sql是这样的
    SELECT emp.job AS emp_job, count(emp.job) AS job_count 
        FROM emp GROUP BY emp.job
    
    我们这样理解:
        先根据job分组, 然后查看每组有多少人.
    select 子查询里面, 单独查询的列, 比如select emp.job, 这个job一定是分组依据. 否则出现在select语句里面.
           子查询里面的聚合函数列, 则没有限制, 可以随意使用聚合函数对任意列进行数据处理.
    为什么我们本次要使用count呢?
    回到我们的目的, 我们要查询每组有多少人.
    
    label的第三种写法:
    在函数后面直接使用.label这种链式写法. 我之前没想过还可以这么写, 这样写完全是我尝试出来的. 
    原因是, 英语文档没有细读, 不知道这么用. 其次, 英语文档读的太慢了, 英语水平有限, 无法深入挖掘sqlalchemy的用法 ￣□￣｜｜.
    '''


# 分组的用法
def query_and_group_plus():
    # 本次, 我们要统计每个职业有多少员工. 而且我们要增加额外的分组依据, 员工所在的位置(部门表里的loc字段), 所以我们要进行联合查询
    from sqlalchemy import func
    results = sess.query(Dept.loc, Emp.job, func.count(Emp.empno).label('job_count')) \
        .join(Emp, Emp.deptno == Dept.deptno) \
        .group_by(Dept.loc, Emp.job).all()
    for item in results:
        print(item.loc, item.job, item.job_count)

    '''
    output:
    
    CHICAGO CLERK 1
    CHICAGO MANAGER 1
    CHICAGO SALESMAN 4
    DALLAS ANALYST 2
    DALLAS CLERK 2
    DALLAS MANAGER 1
    NEW YORK CLERK 1
    NEW YORK MANAGER 1
    NEW YORK PRESIDENT 1
    
    
    note:
    
    通过本次的查询, 大家应该可以清楚的看到各个地区各个职位的分布了. 也能从查询结果中挖掘到一些信息. 这就是统计的作用.
    这次, 也告诉大家, 我们可以使用 多列进行分组统计.
    

    '''


if __name__ == '__main__':
    query_and_group_plus()
