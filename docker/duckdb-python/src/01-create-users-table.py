import duckdb

# create a connection to a file called 'demo.duckdb'
con = duckdb.connect('db/demo.duckdb')

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