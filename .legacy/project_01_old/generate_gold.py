import geopandas as gpd
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[1]
    proc_dir = project_root / "data/processed"
    
    food_input = proc_dir / "silver_wake_food_facilities.parquet"
    food_output = proc_dir / "gold_food_retailers.parquet"

    gdf_food = gpd.read_parquet(food_input)

    primary_types = ['30_meat_market', '14_limited_food']
    include_kws = ['food_lion', 'lowes_food', 'whole_foods', 'harris_teeter', 'wegmans', 'aldi', 'lidl', 'grocery', 'market']
    exclude_kws = ['hotel', 'golf', 'club', 'service', 'inn', 'cafe']

    mask_primary = gdf_food['facility_type'].isin(primary_types)
    mask_include = gdf_food['facility_name'].str.contains('|'.join(include_kws), case=False, na=False)
    mask_exclude = gdf_food['facility_name'].str.contains('|'.join(exclude_kws), case=False, na=False)
    
    gold_food = gdf_food[mask_primary | (mask_include & ~mask_exclude)].copy()
    gold_food.to_parquet(food_output)
    print(f"[STATUS] COMPLETED | ASSET: {food_output.name} | RECORDS: {len(gold_food)}")

    bus_input = proc_dir / "silver_goraleigh_bus_stops.parquet"
    bus_output = proc_dir / "gold_goraleigh_bus_stops.parquet"

    if bus_input.exists():
        gdf_bus = gpd.read_parquet(bus_input)
        gdf_bus.to_parquet(bus_output)
        print(f"[STATUS] COMPLETED | ASSET: {bus_output.name} | RECORDS: {len(gdf_bus)}")

if __name__ == "__main__":
    main()
