import duckdb
import sys
from pathlib import Path

class SchemaInspector:
    """
    Standardized utility for discovering spatial data schemas.
    """
    def __init__(self):
        self.con = duckdb.connect(database=':memory:')
        self.con.execute("INSTALL spatial; LOAD spatial;")

    def get_columns(self, file_path: Path):
        """
        Extracts and prints column names from a spatial file.
        """
        if not file_path.exists():
            print(f"Error: File {file_path} not found.")
            return

        try:
            # We use LIMIT 0 to fetch metadata without loading rows
            query = f"SELECT * FROM st_read('{file_path}') LIMIT 0"
            df = self.con.execute(query).df()
            
            print(f"\n[SCHEMA INSPECTION] {file_path.name}")
            print("-" * 30)
            for col in df.columns:
                print(f"  - {col}")
            print("-" * 30 + "\n")
            
        except Exception as e:
            print(f"Inspection failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 shared/utils/inspector.py <path_to_spatial_file>")
    else:
        inspector = SchemaInspector()
        inspector.get_columns(Path(sys.argv[1]))
