import duckdb
import os

def initialize_engine():
    """
    Sets up Medallion architecture infrastructure.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    db_path = os.path.join(base_dir, "data", "triangle_engine.db")
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    con = duckdb.connect(db_path)
    
    con.execute("INSTALL spatial; LOAD spatial;")
    
    print(f"--- Initializing Global Medallion Schemas at {db_path} ---")
    con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")
    con.execute("CREATE SCHEMA IF NOT EXISTS silver;")
    con.execute("CREATE SCHEMA IF NOT EXISTS gold;")
    
    print("Success! Infrastructure is ready.")
    con.close()

if __name__ == "__main__":
    initialize_engine()