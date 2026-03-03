import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[3]
sys.path.append(str(repo_root))

from shared.utils.refiner import SpatialRefiner

def main():
    project_root = Path(__file__).resolve().parents[1]
    raw_dir = project_root / "data/raw"
    proc_dir = project_root / "data/processed"
    
    proc_dir.mkdir(parents=True, exist_ok=True)
    
    refiner = SpatialRefiner()

    food_input = raw_dir / "raw_wake_food_facilities_20260301.geojson"
    food_output = proc_dir / "silver_wake_food_facilities.parquet"
    
    food_mapping = {
        "NAME": "facility_name",
        "FACILITYTYPE": "facility_type",
        "ADDRESS1": "address",
        "CITY": "city"
    }
    
    print(f"Refining Food Data...")
    refiner.refine_geojson(food_input, food_output, food_mapping, geom_column="geom", source_crs="EPSG:4326")

    bus_input = raw_dir / "raw_goraleigh_bus_stops_20260301.geojson"
    bus_output = proc_dir / "silver_goraleigh_bus_stops.parquet"
    
    bus_mapping = {
        "Stop_Name": "stop_name",
        "Stop_ID": "stop_id"
    }
    
    print(f"Refining Transit Data...")
    refiner.refine_geojson(bus_input, bus_output, bus_mapping, geom_column="geom", source_crs="EPSG:4326")

if __name__ == "__main__":
    main()
