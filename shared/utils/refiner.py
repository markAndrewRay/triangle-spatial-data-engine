import duckdb
from pathlib import Path

class SpatialRefiner:
    def __init__(self):
        self.con = duckdb.connect(database=':memory:')
        self.con.execute("INSTALL spatial; LOAD spatial;")

    def refine_geojson(self, input_path: Path, output_path: Path, column_mapping: dict, geom_column: str = "geometry"):
        if not input_path.exists():
            raise FileNotFoundError(f"Source file not found: {input_path}")

        select_clause = ", ".join([
            f"TRIM(BOTH '_' FROM REGEXP_REPLACE(LOWER(\"{old}\"::VARCHAR), '[^a-z0-9]+', '_', 'g')) AS {new}" 
            for old, new in column_mapping.items()
        ])
        
        query = f"""
            COPY (
                SELECT {select_clause}, {geom_column} AS geometry 
                FROM st_read('{input_path}')
            ) TO '{output_path}' (FORMAT PARQUET);
        """
        
        try:
            self.con.execute(query)
            count = self.con.execute(f"SELECT COUNT(*) FROM '{output_path}'").fetchone()[0]
            print(f"[STATUS] COMPLETED | ASSET: {output_path.name} | RECORDS: {count}")
        except Exception as e:
            print(f"[STATUS] FAILED | ASSET: {output_path.name} | ERROR: {e}")

    def __del__(self):
        try:
            self.con.close()
        except:
            pass
