import requests
import sys

def audit_layer(url: str):
    """
    Performs a schema audit on an ArcGIS REST API endpoint to identify 
    available fields and data types.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    # Clean the URL and enforce JSON response
    base_url = url.split('?')[0].strip()
    api_url = f"{base_url}?f=json"
    
    print(f"\nINTERROGATING: {base_url}")
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            print(f"API ERROR: {data['error'].get('message', 'Unknown API Error')}")
            return

        layer_name = data.get('name', 'Unknown')
        print(f"\nLAYER NAME: {layer_name}")
        print("-" * 90)
        print(f"{'FIELD NAME':<30} | {'DATA TYPE':<25} | {'ALIAS'}")
        print("-" * 90)
        
        fields = data.get('fields', [])
        for f in fields:
            name = str(f.get('name', 'N/A'))
            dtype = str(f.get('type', 'N/A'))
            alias = str(f.get('alias', 'N/A'))
            print(f"{name:<30} | {dtype:<25} | {alias}")
            
    except requests.exceptions.Timeout:
        print("ERROR: Connection timed out.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shared/utils/inspect_schema.py <ARCGIS_URL>")
    else:
        audit_layer(sys.argv[1])
