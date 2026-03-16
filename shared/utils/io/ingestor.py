import geopandas as gpd
import yaml
import requests
from pathlib import Path
import os
import pandas as pd

class Ingestor:
    def __init__(self, config_path):
        self.project_dir = os.path.dirname(config_path)
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
            
    def run(self):
        bronze_dir = Path(self.project_dir) / self.config['paths']['bronze_dir']
        bronze_dir.mkdir(parents=True, exist_ok=True)
        
        target_crs = self.config.get('crs', 'EPSG:2264') # Default to NC State Plane
        
        for name, info in self.config['sources'].items():
            print(f" Processing {name}...")
            
            try:
                if info.get('format') == 'osm':
                    response = requests.get(info['url'], params={'data': info['query']})
                    if response.status_code != 200:
                        print(f" OSM Error: {response.status_code} - {response.text[:100]}")
                        continue
                    
                    data = response.json()
                    elements = []
                    for el in data.get('elements', []):
                        node = {'id': el.get('id'), 'lat': el.get('lat'), 'lon': el.get('lon')}
                        if 'tags' in el:
                            node.update(el['tags'])
                        elements.append(node)
                    
                    df = pd.DataFrame(elements)
                    gdf = gpd.GeoDataFrame(
                        df, 
                        geometry=gpd.points_from_xy(df.lon, df.lat),
                        crs="EPSG:4326"
                    )
                else:
                    gdf = gpd.read_file(info['url'])

                # Normalize and Save
                gdf = gdf.to_crs(target_crs)
                output_path = bronze_dir / f"{name}.parquet"
                gdf.to_parquet(output_path)
                print(f" Saved {len(gdf)} records to {output_path}")

            except Exception as e:
                print(f" Failed to process {name}: {e}")
