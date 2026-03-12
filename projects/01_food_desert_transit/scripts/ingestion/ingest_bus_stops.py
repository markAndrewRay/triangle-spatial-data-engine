import sys
import os
from pathlib import Path
import geopandas as gpd

sys.path.append(os.getcwd())

from shared.utils.io.ingestor import harvest_arcgis_data

def main():
    project_root = Path(__file__).resolve().parents[2]
    bronze_path = project_root / "data/bronze"
    silver_path = project_root / "data/silver"
    
    url = "https://services.arcgis.com/v400IkDOw1ad7Yad/arcgis/rest/services/GoRaleigh_BusStops/FeatureServer"
    layer_id = 0
    file_name = "goraleigh_bus_stops"
    
    os.makedirs(bronze_path, exist_ok=True)
    os.makedirs(silver_path, exist_ok=True)
    
    raw_file = harvest_arcgis_data(url, layer_id, str(bronze_path), file_name)
    
    print("[STATUS] Refining data to project data folder...")
    gdf = gpd.read_file(raw_file)
    gdf = gdf.rename(columns={"OBJECTID": "id", "STOP_NAME": "stop_name", "STOP_ID": "stop_id"})
    gdf = gdf.to_crs("EPSG:4326")
    
    gdf.to_parquet(silver_path / "silver_goraleigh_bus_stops.parquet")
    
    print("[STATUS] Ingestion and Refinement complete.")

if __name__ == "__main__":
    main()
