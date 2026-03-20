import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from shared.utils.osm.osm_ingestor import ingest_osm_features

raw_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/raw/raleigh_groceries.parquet'))

ingest_osm_features(
    place_name="Raleigh, North Carolina",
    tags={"shop": ["supermarket", "grocery"]},
    output_path=raw_path
)