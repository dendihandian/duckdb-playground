import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query the table
con.sql('SHOW TABLES').show()

"""
docker-compose exec duckdb-python python src/06-show-tables.py
"""