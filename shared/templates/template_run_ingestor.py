import sys
import os
from pathlib import Path

sys.path.append(os.getcwd())

from shared.utils.io.ingestor import harvest_arcgis_data

def main():
    project_root = Path(__file__).resolve().parents[2]
    bronze_path = project_root / "data/bronze"
    
    # Configuration
    url = "YOUR_ARCGIS_URL_HERE"
    layer_id = 0
    file_name = "your_data_name"
    
    os.makedirs(bronze_path, exist_ok=True)
    
    harvest_arcgis_data(url, layer_id, str(bronze_path), file_name)

if __name__ == "__main__":
    main()
