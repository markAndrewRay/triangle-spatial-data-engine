import requests
import json
import sys
import os

def fetch_data(url: str, where_clause: str, output_path: str):
    """
    Universally harvests GeoJSON data from any ArcGIS REST API.
    Enforces ethical headers, timeouts, and clean coordinate output.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    # Clean URL and set query parameters
    base_url = url.split('?')[0].strip()
    api_url = f"{base_url}/query"
    
    params = {
        'where': where_clause,
        'outFields': '*',      # Get all data 
        'outSR': '4326',       # Standard GPS coordinates (WGS84)
        'f': 'geojson'         # Modern, universal geographic format
    }
    
    print(f"\nHARVESTING DATA FROM: {base_url}")
    print(f"QUERY: {where_clause}")
    
    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=20)
        response.raise_for_status()
        
        # Save to the specified path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(response.json(), f)
            
        print(f"SUCCESS: Data saved to {output_path}")
        print(f"COUNT: {len(response.json().get('features', []))} locations found.")
            
    except Exception as e:
        print(f"ERROR: Extraction failed. {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python shared/utils/fetch_geojson.py <URL> <WHERE_CLAUSE> <OUTPUT_PATH>")
    else:
        fetch_data(sys.argv[1], sys.argv[2], sys.argv[3])
