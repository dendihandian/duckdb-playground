import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query the table
con.table('users').show()

"""
docker-compose exec duckdb-python python src/03-show-data-in-users-table.py
"""