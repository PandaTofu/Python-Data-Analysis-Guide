run setup_db.py

from sqlalchemy import create_engine

db_engine = create_engine('sqlite:///examples/example_sqlite.db')

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db_engine)

db_session = Session()

from db_tables import Student

data_records = db_session.query(Student.name, Student.height).all()

data_records

from pandas import DataFrame

df = DataFrame(data_records, columns=['name', 'height'])

df

