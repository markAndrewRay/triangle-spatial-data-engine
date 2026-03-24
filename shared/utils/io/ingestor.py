import geopandas as gpd
import pandas as pd
import requests
import yaml
from pathlib import Path
import os
from shapely.geometry import Point

class Ingestor:
    def __init__(self, config_path):
        self.project_dir = os.path.dirname(config_path)
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
            
    def run(self):
        bronze_dir = Path(self.project_dir) / self.config['paths']['bronze_dir']
        bronze_dir.mkdir(parents=True, exist_ok=True)
        
        for name, info in self.config['sources'].items():
            try:
                if info.get('format') == 'osm':
                    response = requests.get(info['url'], params={'data': info['query']})
                    response.raise_for_status()
                    
                    data = response.json()
                    elements = []
                    for el in data.get('elements', []):
                        node = el.copy() 
                        if 'tags' in el:
                            node.update(el['tags'])
                        
                        node['geometry'] = Point(el.get('lon'), el.get('lat'))
                        elements.append(node)
                    
                    gdf = gpd.GeoDataFrame(elements, crs="EPSG:4326")
                else:
                    gdf = gpd.read_file(info['url'])

                output_path = bronze_dir / f"{name}.parquet"
                gdf.to_parquet(output_path, index=False)
                print(f"Processed Raw Bronze: {name}")

            except Exception as e:
                print(f"Error ingesting {name}: {e}")