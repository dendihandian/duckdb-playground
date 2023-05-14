import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query
con.sql("CREATE TABLE example_1 AS SELECT * FROM read_csv_auto('src/example.csv')")

# query
con.sql("SHOW TABLES").show()

"""
docker-compose exec duckdb-python python src/07-create-table-from-csv.py
"""