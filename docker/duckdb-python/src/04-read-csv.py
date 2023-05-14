import duckdb

example = duckdb.read_csv('src/example.csv')
example.show()

"""
docker-compose exec duckdb-python python src/04-read-csv.py
"""