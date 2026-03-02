import sys
from pathlib import Path

# Add shared folder to path
sys.path.append(str(Path(__file__).parents[3]))
from shared.utils.refiner import SpatialRefiner

def main():
    # 1. Setup Paths
    base_path = Path(__file__).parents[1]
    input_file = base_path / "data/raw/REPLACE_WITH_RAW_FILE.geojson"
    output_file = base_path / "data/processed/silver_output.parquet"

    # 2. Define Schema Mapping (Source Column: Target snake_case)
    column_mapping = {
        "ORIGINAL_NAME": "new_name"
    }

    # 3. Execute Refinement
    refiner = SpatialRefiner()
    refiner.refine_geojson(input_file, output_file, column_mapping)

if __name__ == "__main__":
    main()
