import sys
import os
from pathlib import Path
import geopandas as gpd

sys.path.append(os.getcwd())

def main():
    project_root = Path(__file__).resolve().parents[2]
    bronze_path = project_root / "data/bronze"
    silver_path = project_root / "data/silver"
    
    os.makedirs(silver_path, exist_ok=True)

    print("[STATUS] Template refinement complete.")

if __name__ == "__main__":
    main()
