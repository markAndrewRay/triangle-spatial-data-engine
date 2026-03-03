import duckdb
from pathlib import Path

class DataProfiler:
    def __init__(self):
        self.con = duckdb.connect()

    def profile_parquet(self, file_path):
        try:
            print(f"\n--- PROFILE REPORT: {Path(file_path).name} ---")
            
            row_count = self.con.execute(f"SELECT COUNT(*) FROM read_parquet('{file_path}')").fetchone()[0]
            print(f"TOTAL ROWS: {row_count}")

            columns = self.con.execute(f"DESCRIBE SELECT * FROM read_parquet('{file_path}')").fetchall()
            
            print(f"{'COLUMN':<25} | {'NULLS':<8} | {'DISTINCT':<10}")
            print("-" * 50)

            for col in columns:
                col_name = col[0]
                if col_name == 'geometry':
                    continue
                    
                null_count = self.con.execute(f"SELECT COUNT(*) FROM read_parquet('{file_path}') WHERE \"{col_name}\" IS NULL").fetchone()[0]
                distinct_count = self.con.execute(f"SELECT COUNT(DISTINCT \"{col_name}\") FROM read_parquet('{file_path}')").fetchone()[0]
                
                print(f"{col_name:<25} | {null_count:<8} | {distinct_count:<10}")
            
            print("-" * 50)
            
        except Exception as e:
            print(f"[ERROR] Could not profile {file_path}: {e}")

if __name__ == "__main__":
    pass
