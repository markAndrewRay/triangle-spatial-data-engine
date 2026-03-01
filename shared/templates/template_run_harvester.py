import sys
import os

# 1. Reach the shared engine
# Note: Adjust the number of '../' based on your folder depth
sys.path.append(os.path.abspath('../../../'))
from shared.utils.harvester import harvest_arcgis_data

# 2. Project-Specific Settings (Bronze Layer)
# Replace these values for each new project
URL = "INSERT_URL_HERE"
LAYER_ID = 0
SAVE_PATH = "../data/raw"
FILE_NAME = "dataset_name_here"

if __name__ == "__main__":
    print(f"Starting harvest for: {FILE_NAME}...")
    
    # 3. Execute the harvest
    harvest_arcgis_data(
        base_url=URL, 
        layer_id=LAYER_ID, 
        save_path=SAVE_PATH, 
        filename=FILE_NAME
    )
    
    print("Harvest complete.")