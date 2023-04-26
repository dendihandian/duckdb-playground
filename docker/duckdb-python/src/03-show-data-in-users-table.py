import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('db/demo.duckdb')

# query the table
con.table('users').show()