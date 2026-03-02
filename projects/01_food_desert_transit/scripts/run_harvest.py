import sys
import os

# 1. Path Correction
# We are in projects/01_food_desert_transit/scripts/
# We need to go up 3 levels to reach the root folder
sys.path.append(os.path.abspath('../../../'))

from shared.utils.harvester import harvest_arcgis_data

# 2. Source Configuration
BUS_URL = "https://services.arcgis.com/v400IkDOw1ad7Yad/arcgis/rest/services/GoRaleigh_BusStops/FeatureServer"
FOOD_URL = "https://maps.wake.gov/arcgis/rest/services/Inspections/RestaurantInspectionsOpenData/MapServer"

# 3. Execution Logic
def main():
    print("Initializing Multi-Source Spatial Harvest...")
    
    # Define relative save path from the root where the script is executed
    # This will land in: projects/01_food_desert_transit/data/raw/
    save_path = "../data/raw"
    
    # Harvest Dataset 1: Transit
    harvest_arcgis_data(
        base_url=BUS_URL, 
        layer_id=0, 
        save_path=save_path, 
        filename="goraleigh_bus_stops"
    )
    
    # Harvest Dataset 2: Food Access
    harvest_arcgis_data(
        base_url=FOOD_URL, 
        layer_id=0, 
        save_path=save_path, 
        filename="wake_food_facilities"
    )
    
    print("\n--- Harvest Complete: Bronze Layer Populated ---")

if __name__ == "__main__":
    main()