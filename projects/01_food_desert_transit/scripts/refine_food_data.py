import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[3]))
from shared.utils.refiner import SpatialRefiner

def main():
    project_root = Path(__file__).parents[1]
    input_file = project_root / "data/raw/raw_wake_food_facilities_20260301.geojson"
    output_file = project_root / "data/processed/silver_wake_food_facilities.parquet"

    column_mapping = {
        "OBJECTID": "id",
        "HSISID": "facility_id",
        "NAME": "facility_name",
        "ADDRESS1": "address",
        "CITY": "city",
        "POSTALCODE": "zip_code",
        "FACILITYTYPE": "facility_type",
        "RESTAURANTOPENDATE": "open_date"
    }

    refiner = SpatialRefiner()
    refiner.refine_geojson(input_file, output_file, column_mapping, geom_column="geom")

if __name__ == "__main__":
    main()
