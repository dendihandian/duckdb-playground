import duckdb

# create a connection to a file called 'file.db'
con = duckdb.connect('example.duckdb')

# create a table and load data into it
con.sql('CREATE TABLE test(i INTEGER)')
con.sql('INSERT INTO test VALUES (42)')

# query the table
con.table('test').show()