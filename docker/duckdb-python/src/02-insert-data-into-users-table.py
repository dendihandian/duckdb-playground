from datetime import datetime
import duckdb

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('db/demo.duckdb')

con.sql(f"""
    INSERT INTO users VALUES 
        (1, 'users01@example.net', 'users01', TRUE, '{current_datetime}'),
        (2, 'users02@example.net', 'users02', FALSE, '{current_datetime}')
""")