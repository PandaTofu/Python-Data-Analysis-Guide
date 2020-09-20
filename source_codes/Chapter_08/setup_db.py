#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_tables import *

# 连接数据库
db_engine = create_engine('sqlite:///examples/example_sqlite.db')
Base.metadata.create_all(db_engine, checkfirst=True)

# 创建Session类实例
Session = sessionmaker(bind=db_engine)
db_session = Session()

# 往students数据表中插入数据
db_session.add_all([
    Student(name='wendy', height=122),
    Student(name='mary', height=134),
    Student(name='fred', height=120)]
)

# 提交操作
db_session.commit()

# 关闭会话
db_session.close()
