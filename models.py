from sqlalchemy import Column, Integer, String

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
