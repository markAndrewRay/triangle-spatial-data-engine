import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[3]))
from shared.utils.refiner import SpatialRefiner

def main():
    project_root = Path(__file__).parents[1]
    input_file = project_root / "data/raw/raw_goraleigh_bus_stops_20260301.geojson"
    output_file = project_root / "data/processed/silver_goraleigh_bus_stops.parquet"

    column_mapping = {
        "Stop_ID": "stop_id",
        "Stop_Name": "stop_name",
        "Street": "street_address",
        "ADA_Compliant": "is_ada",
        "Shelter": "has_shelter"
    }

    refiner = SpatialRefiner()
    refiner.refine_geojson(input_file, output_file, column_mapping, geom_column="geom")

if __name__ == "__main__":
    main()
