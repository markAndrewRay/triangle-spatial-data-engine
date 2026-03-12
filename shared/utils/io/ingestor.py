import requests
import json
import os
from datetime import datetime

def harvest_arcgis_data(base_url, layer_id, save_path, filename):
    """
    Interfaces with ArcGIS REST APIs to programmatically extract full datasets.
    """
    
    # Construct the query endpoint
    query_url = f"{base_url}/{layer_id}/query"
    
    # Initialize parameters for the REST request
    params = {
        'where': '1=1',
        'outFields': '*',
        'f': 'geojson',
        'resultOffset': 0,
        'resultRecordCount': 2000 
    }
    
    all_features = []
    more_data = True
    
    while more_data:
        response = requests.get(query_url, params=params)
        response.raise_for_status() # Ensure the request was successful
        data = response.json()
        
        features = data.get('features', [])
        all_features.extend(features)
        
        # Handle pagination if the server limit is exceeded
        if 'exceededTransferLimit' in data and data['exceededTransferLimit']:
            params['resultOffset'] += params['resultRecordCount']
        else:
            more_data = False
            
    # Define the standardized GeoJSON structure with lineage metadata
    final_geojson = {
        "type": "FeatureCollection",
        "features": all_features,
        "metadata": {
            "harvest_date": datetime.now().isoformat(),
            "source": query_url,
            "record_count": len(all_features)
        }
    }
    
    # Standardized file naming convention for the Bronze layer
    timestamp = datetime.now().strftime('%Y%m%d')
    output_filename = f"raw_{filename}_{timestamp}.geojson"
    full_save_path = os.path.join(save_path, output_filename)
    
    # Ensure directory exists and save payload
    os.makedirs(save_path, exist_ok=True)
    with open(full_save_path, 'w') as f:
        json.dump(final_geojson, f)
        
    return full_save_path