import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query
con.sql("COPY example_1 FROM 'src/example_headless.csv';")

# query
con.sql("SELECT * FROM example_1 LIMIT 50").show()

"""
docker-compose exec duckdb-python python src/09-copy-to-table-from-csv.py
"""