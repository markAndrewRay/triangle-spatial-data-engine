import duckdb
from pathlib import Path

class SpatialRefiner:
    def __init__(self):
        self.con = duckdb.connect()
        self.con.execute("INSTALL spatial; LOAD spatial;")

    def refine_geojson(self, input_path, output_path, column_mapping, geom_column="geometry", source_crs=None):
        try:
            select_items = []
            for raw_col, clean_name in column_mapping.items():
                select_items.append(f"TRIM(BOTH '_' FROM REGEXP_REPLACE(LOWER(\"{raw_col}\"::VARCHAR), '[^a-z0-9]+', '_', 'g')) AS {clean_name}")
            
            select_clause = ",\n".join(select_items)

            if not source_crs:
                check_srid = self.con.execute(f"SELECT ST_SRID({geom_column}) FROM ST_Read('{input_path}') LIMIT 1").fetchone()[0]
                if check_srid == 0 or check_srid is None:
                    raise ValueError(f"CRS unknown for {input_path}. Specify 'source_crs' (e.g., 'EPSG:4326').")
                source_crs = f"EPSG:{check_srid}"

            query = f"""
            COPY (
                SELECT 
                    {select_clause},
                    ST_Transform({geom_column}, '{source_crs}', 'EPSG:4326') AS geometry
                FROM ST_Read('{input_path}')
            ) TO '{output_path}' (FORMAT 'PARQUET');
            """
            
            self.con.execute(query)
            print(f"[STATUS] COMPLETED | ASSET: {Path(output_path).name} (Source: {source_crs})")
            
        except Exception as e:
            print(f"[STATUS] FAILED | ASSET: {Path(output_path).name} | ERROR: {e}")

if __name__ == "__main__":
    pass
