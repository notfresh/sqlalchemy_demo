from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey

from db_util import Base, Session

sess = Session()


class Dept(Base):
    __tablename__ = 'dept'
    deptno = Column(Integer, primary_key=True)
    dname = Column(String(14))
    loc = Column(String(13))

    def __repr__(self):
        return str({
            'deptno': self.deptno,
            'dname': self.dname,
            'loc': self.loc
        })


class Emp(Base):
    __tablename__ = 'emp'
    empno = Column(Integer, primary_key=True)
    ename = Column(String(10))
    job = Column(String(9))
    mgr = Column(Integer)
    hiredate = Column(Date)
    comm = Column(DECIMAL(7, 2))
    deptno = Column(Integer, ForeignKey('dept.deptno'))

    def __repr__(self):
        return str({
            'empno': self.empno,
            'ename': self.ename,
            'job': self.job,
            'deptno': self.deptno,
            'comm': self.comm
        })
