from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:Dev@123@localhost:3306/sqlalchemy_demo?charset=utf8')

Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    # 创建表,如果不存在的话
    Base.metadata.create_all(engine)
