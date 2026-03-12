COPY (
    SELECT id, name, geometry 
    FROM 'projects/01_food_desert_transit/data/raw/raleigh_groceries.parquet'
    WHERE geometry IS NOT NULL
    ORDER BY name ASC
) TO 'projects/01_food_desert_transit/data/processed/silver_raleigh_groceries.parquet' (FORMAT 'parquet');
