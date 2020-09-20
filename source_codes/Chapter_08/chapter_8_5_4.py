import pandas

import sqlalchemy as sqla

db = sqla.create_engine('sqlite:///examples/example_sqlite.db')

df = pandas.read_sql('select * from students', db)

df

