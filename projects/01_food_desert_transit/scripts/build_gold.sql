COPY (
    WITH consolidated_data AS (
        SELECT 
            Stop_ID AS id, 
            Stop_Name AS feature_name, 
            'Bus Stop' AS feature_type,
            ST_X(ST_Centroid(ST_Collect(list(geometry)))) AS lon,
            ST_Y(ST_Centroid(ST_Collect(list(geometry)))) AS lat
        FROM bus_stops 
        GROUP BY id, feature_name
        
        UNION ALL
        
        SELECT 
            row_number() OVER ()::VARCHAR AS id, 
            name AS feature_name, 
            'Grocery Store' AS feature_type,
            lon,
            lat
        FROM grocery_stores
        WHERE shop IN ('supermarket', 'grocery')
          AND name IS NOT NULL
    )
    SELECT * FROM consolidated_data
) TO 'projects/01_food_desert_transit/data/gold/raleigh_final_points.csv' (HEADER, DELIMITER ',');
