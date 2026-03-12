import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from shared.utils.osm_processor import fetch_osm_data

raw_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/raw/raleigh_groceries.parquet'))

fetch_osm_data(
    place_name="Raleigh, North Carolina",
    tags={"shop": ["supermarket", "grocery"]},
    output_path=raw_path
)