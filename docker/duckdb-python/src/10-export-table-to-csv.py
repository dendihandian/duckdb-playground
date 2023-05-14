import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# query the table
con.sql("COPY example_1 TO 'src/_example_1.csv' (HEADER, DELIMITER ',');")

# query the table
con.sql("COPY example_1 TO 'src/_example_1_headless.csv' (DELIMITER ',');")

# query
con.sql("SELECT * FROM 'src/_example_1.csv' LIMIT 50").show()

"""
docker-compose exec duckdb-python python src/10-export-table-to-csv.py
"""