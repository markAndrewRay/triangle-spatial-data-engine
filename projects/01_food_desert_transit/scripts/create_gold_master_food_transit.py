import geopandas as gpd
from pathlib import Path

def main():
    project_root = Path(__file__).parents[1]
    food_silver = project_root / "data/processed/silver_wake_food_facilities.parquet"
    transit_silver = project_root / "data/processed/silver_goraleigh_bus_stops.parquet"
    output_gold = project_root / "data/processed/gold_master_food_transit.parquet"

    # 1. Load Silver Assets
    gdf_food = gpd.read_parquet(food_silver)
    gdf_transit = gpd.read_parquet(transit_silver)

    # 2. Filter for "Real" Food Retailers
    primary_types = ['30_meat_market', '14_limited_food']
    include_kws = ['food_lion', 'lowes_food', 'whole_foods', 'harris_teeter', 'wegmans', 'aldi', 'lidl', 'grocery', 'market']
    exclude_kws = ['hotel', 'golf', 'club', 'service', 'inn', 'cafe']

    mask_primary = gdf_food['facility_type'].isin(primary_types)
    mask_include = gdf_food['facility_name'].str.contains('|'.join(include_kws), case=False, na=False)
    mask_exclude = gdf_food['facility_name'].str.contains('|'.join(exclude_kws), case=False, na=False)
    
    gdf_food_filtered = gdf_food[mask_primary | (mask_include & ~mask_exclude)].copy()

    # 3. Spatial Join (The "One-File" Integration)
    # Using NC State Plane (EPSG:2264) for accurate foot measurements
    gdf_food_filtered = gdf_food_filtered.to_crs(epsg=2264)
    gdf_transit = gdf_transit.to_crs(epsg=2264)

    # This joins transit stop info to our food store records
    gold_master = gpd.sjoin_nearest(
        gdf_food_filtered, 
        gdf_transit, 
        how="left", 
        distance_col="dist_to_stop_ft"
    )

    # 4. Final Export
    gold_master.to_parquet(output_gold)
    print(f"[STATUS] COMPLETED | ASSET: {output_gold.name} | RECORDS: {len(gold_master)}")

if __name__ == "__main__":
    main()
