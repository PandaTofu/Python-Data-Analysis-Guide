#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# 定义数据表的映射类Student，并继承Base类
class Student(Base):
    # 指定本类映射到students表
    __tablename__ = 'students'

    # 指定id字段为主键，自动增长
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name字段，存放学生名字
    name = Column(String(20))
    # 指定height字段，存放学生的身高
    height = Column(Integer)

