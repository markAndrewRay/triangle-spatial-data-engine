import requests
import sys

def peek_field(url: str, field_name: str):
    """
    Retrieves distinct values for a specific field from an ArcGIS REST API.
    Explicitly disables geometry to avoid API 'DISTINCT' errors.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    base_url = url.split('?')[0].strip()
    # Adding /query to the base URL for the data request
    api_url = f"{base_url}/query"
    
    params = {
        'where': '1=1',
        'outFields': field_name,
        'returnDistinctValues': 'true',
        'returnGeometry': 'false',  # THE FIX: Prevents the 'Geometry not supported' error
        'f': 'json'
    }
    
    print(f"\nPEEKING UNIQUE VALUES: {field_name}")
    
    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            print(f"API ERROR: {data['error'].get('message', 'Unknown Error')}")
            print(f"DETAILS: {data['error'].get('details', 'No details provided')}")
            return

        features = data.get('features', [])
        # Extract unique values from the JSON attributes
        values = sorted(list(set([str(f['attributes'][field_name]) for f in features if f['attributes'].get(field_name)])))
        
        print("-" * 50)
        for v in values:
            print(f" - {v}")
        print("-" * 50)
        print(f"TOTAL UNIQUE CATEGORIES: {len(values)}")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python shared/utils/peek_values.py <URL> <FIELD_NAME>")
    else:
        peek_field(sys.argv[1], sys.argv[2])
