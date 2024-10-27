import sqlalchemy as sa
from sqlalchemy import create_engine, text

# Connection string format
conn_str = 'access+pyodbc:///?odbc_connect={}'.format(
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=CCLPIHN_be.accdb;'
)

# Create an engine
engine = sa.create_engine(conn_str)

# Establish a connection
with engine.connect() as connection:
    # Do something with the connection
    result = connection.execute("SELECT username FROM users")
    for row in result:
        print(row)
