from sqlalchemy import case, func
from sqlalchemy.sql import label

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


# case when的语法
def query_case_when():
    # 使用case when的情况很少. 因为 case when就算在sql语句里, 写的也很笨重. 所以, 很少使用.
    # 能够替换case when的 语句可能有 mysql里的 ifnull( a,b ) oracle里的 nvl, nvl2等等.
    # ifnull(a, b)意思是, 如果a是空的, 那么使用b的值, if(a, b, c) 意思是 如果a是true, 那么使用b, 否则使用c, 是三目运算符.
    # 如何使用 ifnull, if 等函数,分别使用 func.ifnull, func.IF(大写), 使用我上面说的 func.函数名 用法. 这里就不多说了.
    # 假设一个场景:
    #    我们根据员工的收入分等级, 奖金+工资 1500 美元以下的,都是低收入, 1500-3500之前的是 中等收入, 3500美元以上的是高收入
    #    包含下限, 不包含上限.
    from sqlalchemy import text
    income_level = case(
        [
            (text('(emp.sal + ifnull(emp.comm,0))<1500'), 'LOW_INCOME'),
            (text('1500<=(emp.sal + ifnull(emp.comm,0))<3500'), 'MIDDLE_INCOME'),
            (text('(emp.sal + ifnull(emp.comm,0))>=3500'), 'HIGH_INCOME'),
        ], else_='UNKNOWN'
    ).label('income_level')
    emps = sess.query(Emp.ename, label('income', Emp.sal + func.ifnull(Emp.comm, 0)),
                      income_level).all()
    for item in emps:
        print(item.ename, item.income, item.income_level)

    '''
    output:
    
    SMITH 2799.00 MIDDLE_INCOME
    ALLEN 1900.00 MIDDLE_INCOME
    WARD 1750.00 MIDDLE_INCOME
    JONES 2975.00 MIDDLE_INCOME
    MARTIN 2650.00 MIDDLE_INCOME
    BLAKE 2850.00 MIDDLE_INCOME
    CLARK 2450.00 MIDDLE_INCOME
    SCOTT 3000.00 MIDDLE_INCOME
    KING 5000.00 MIDDLE_INCOME
    TURNER 1500.00 MIDDLE_INCOME
    ADAMS 1100.00 LOW_INCOME
    JAMES 950.00 LOW_INCOME
    FORD 3000.00 MIDDLE_INCOME
    MILLER 1300.00 LOW_INCOME
    KATE None UNKNOWN
    
    
    note:
    
    case when真的好麻烦, 我已经不想多说了, 写的我好累. ￣□￣｜｜....
        
    '''


def query_with_exists():
    # exists 到底怎么用? 我很纠结要不要写这个.
    # 其实我的 exists 语句也写的很少.
    # 想要深刻理解 exists 语句, 请参见 https://www.cnblogs.com/mytechblog/articles/2105785.html
    # exists 可以类比于 in, 但是比 in的效率更好. 如果暂时没法理解 exits, 把exits 理解为in 也没关系, 慢慢就理解了.
    # 本例的场景:
    #       找出各个职位工资最高的员工!! 是不是很有挑战性.
    #       我们先想一下sql怎么写.
    # select *
    # from emp
    #   join (select
    #           job,
    #           max(sal) max_sal
    #         from emp
    #         group by job) j on emp.job = j.job and emp.sal = j.max_sal
    # order by emp.sal asc;
    # 但是如果用exists 写呢?
    #
    # select *
    # from emp e
    # where not exists(
    #     select *
    #     from emp e2
    #     where e2.job = e.job and e.sal < e2.sal and e.sal is not null
    # )
    # order by e.sal asc;
    # 读这个肯定很难吧,刚开始. 那么就作为一个难题留给亲爱的读者吧.
    # 我们 exits 实现这个语句.
    from sqlalchemy import exists
    from sqlalchemy.orm import aliased
    e2 = aliased(Emp)
    from sqlalchemy import and_
    stmt = exists().where(and_(e2.job == Emp.job, Emp.sal < e2.sal))
    emps = sess.query(Emp).filter(~stmt).filter(Emp.sal!=None).order_by(Emp.sal.asc()).all()
    for item in emps:
        print(item.ename, item.job, item.sal)
    '''
    output:
    
    MILLER CLERK 1300.00
    ALLEN SALESMAN 1600.00
    JONES MANAGER 2975.00
    SCOTT ANALYST 3000.00
    FORD ANALYST 3000.00
    KING PRESIDENT 5000.00
    
    
    note:
    
    我本来是很熟悉sql的, 一下子转到orm的写法, 一度非常的痛苦. 还好半年内慢慢适应过来了. 查了很多资料, 写了很多CRUD.
    我为orm浪费了很多时间, 为了写出所谓漂亮的代码.
    我的建议是: 这些并不是那么重要, 不值得投入过多时间去钻研. 能找到替代的就用替代的写法去实现.
    '''


def query_with_union():
    query1 = sess.query(Emp.ename, Emp.job, Emp.deptno).filter(Emp.deptno == 10)
    query2 = sess.query(Emp.ename, Emp.job, Emp.deptno).filter(Emp.deptno.in_((10, 20)))  # Emp.deptno in (10, 20) 注意, 这种写法是错的!!
    query = query1.union(query2)
    result = query.order_by(Emp.ename).all()
    for item in result:
        print(item.ename, item.job, item.deptno)
    '''
    output:
    
    ADAMS CLERK 20
    CLARK MANAGER 10
    FORD ANALYST 20
    JONES MANAGER 20
    KING PRESIDENT 10
    MILLER CLERK 10
    SCOTT ANALYST 20
    SMITH CLERK 20
    
    
    note:
    
    我们可以看到, 没有重复数据. 进行了去重操作.
    
    '''


def query_union_all():
    query1 = sess.query(Emp.ename, Emp.job, Emp.deptno).filter(Emp.deptno == 10)
    query2 = sess.query(Emp.ename, Emp.job, Emp.deptno).filter(
        Emp.deptno.in_((10, 20)))  # Emp.deptno in (10, 20) 注意, 这种写法是错的!!
    query = query1.union_all(query2).order_by(Emp.ename)
    result = query.all()
    for item in result:
        print(item.ename, item.job, item.deptno)
    '''
    output:
    
    ADAMS CLERK 20
    CLARK MANAGER 10
    CLARK MANAGER 10
    FORD ANALYST 20
    JONES MANAGER 20
    KING PRESIDENT 10
    KING PRESIDENT 10
    MILLER CLERK 10
    MILLER CLERK 10
    SCOTT ANALYST 20
    SMITH CLERK 20
    
    
    note:
    
    有重复数据. 
    注意了! mysql没有interset操作, 也就是相减操作, 想要实现相减, 需要借助 not exists, 所以, 如果还是需要了解一下 exits的用法.
    写在最后: exists难度偏大, 是选学内容. 
    '''


if __name__ == '__main__':
    query_with_union()
