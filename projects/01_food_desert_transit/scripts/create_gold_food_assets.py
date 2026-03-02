import geopandas as gpd
from pathlib import Path

def main():
    project_root = Path(__file__).parents[1]
    input_file = project_root / "data/processed/silver_wake_food_facilities.parquet"
    output_file = project_root / "data/processed/gold_food_retailers.parquet"

    # Load Silver Asset
    gdf = gpd.read_parquet(input_file)

    # Filtering Logic
    primary_types = ['30_meat_market', '14_limited_food']
    include_kws = ['food_lion', 'lowes_food', 'whole_foods', 'harris_teeter', 'wegmans', 'aldi', 'lidl', 'grocery', 'market']
    exclude_kws = ['hotel', 'golf', 'club', 'service', 'inn', 'cafe']

    mask_primary = gdf['facility_type'].isin(primary_types)
    mask_include = gdf['facility_name'].str.contains('|'.join(include_kws), case=False, na=False)
    mask_exclude = gdf['facility_name'].str.contains('|'.join(exclude_kws), case=False, na=False)
    
    gold_df = gdf[mask_primary | (mask_include & ~mask_exclude)].copy()

    # Save as the final Gold Food layer
    gold_df.to_parquet(output_file)
    print(f"[STATUS] COMPLETED | ASSET: {output_file.name} | RECORDS: {len(gold_df)}")

if __name__ == "__main__":
    main()
