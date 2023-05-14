import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('data/demo.duckdb')

# create a users table
con.sql("""
    CREATE TABLE IF NOT EXISTS users(
        id BIGINT,
        email VARCHAR,
        username VARCHAR,
        active BOOLEAN,
        created_at TIMESTAMP
    )
""")

"""
docker-compose exec duckdb-python python src/01-create-users-table.py
"""