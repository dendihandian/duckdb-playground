import duckdb

example = duckdb.sql('SELECT * FROM "src/example.csv"')
example.show()

"""
docker-compose exec duckdb-python python src/05-directly-query-from-csv.py
"""