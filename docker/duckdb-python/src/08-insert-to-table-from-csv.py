import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query
con.sql("INSERT INTO example_1 SELECT * FROM read_csv_auto('src/example.csv');")

# query
con.sql("SELECT * FROM example_1 LIMIT 50").show()

"""
docker-compose exec duckdb-python python src/08-insert-to-table-from-csv.py
"""