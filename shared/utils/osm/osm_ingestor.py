import osmnx as ox
import os

def harvest_osm_features(place_name, tags, output_path):
    gdf = ox.features_from_place(place_name, tags=tags)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    gdf.to_parquet(output_path)
    print(f"Success: Raw data saved to {output_path}")