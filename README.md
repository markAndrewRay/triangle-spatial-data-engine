# Triangle Spatial Data Engine

A spatial ETL pipeline for the Research Triangle region. This framework implements a medallion architecture (bronze, silver, gold) to transform municipal data into normalized assets for ArcGIS Pro.

## Technical Stack
* **Processing:** DuckDB, Polars, GeoPandas, Pyogrio
* **Analysis & Profiling:** ydata-profiling, Scikit-learn, Scipy, Statsmodels
* **Infrastructure:** ArcGIS Pro, Git LFS, Pydantic
* **Standards:** WGS84 (EPSG:4326), snake_case schema enforcement

## Repository Structure
* **shared/utils/**: Reusable logic for data harvesting, normalization, and profiling.
* **projects/**: Individual capsules containing project-specific scripts, notebooks, and data.
* **data/**: Project-specific storage for raw, silver, and gold datasets.

## Pipeline Workflow

### 1. Ingestion (Bronze)
`python3 shared/utils/harvester.py`  
Downloads raw GeoJSON or CSV files from municipal portals into the project `data/raw/` directory.

### 2. Normalization (Silver)
`python3 shared/utils/refiner.py`  
Standardizes headers to snake_case, projects coordinates to EPSG:4326, and converts files to parquet format.

### 3. Validation (Profiler)
`python3 shared/utils/profiler.py`  
Runs health checks on silver assets to identify null values and schema anomalies before final filtering.

### 4. Logic & Filtering (Gold)
`python3 projects/<project_name>/scripts/04_create_gold.py`  
Applies project-specific filters and joins to create the final analysis-ready layer.

---

## Shared Utilities

### Harvester (`shared/utils/harvester.py`)
Automates the acquisition of spatial datasets from municipal api endpoints.
* **Functionality:** Handles http requests, manages response parsing for geojson/csv formats, and saves raw data to the project bronze layer.
* **Goal:** Provides a consistent entry point for all external data dependencies.

### Refiner (`shared/utils/refiner.py`)
Handles data cleaning and standardization.
* **Schema Enforcement:** Converts all field names to snake_case.
* **Spatial Projection:** Ensures all data uses WGS84 for ArcGIS compatibility.
* **Format Conversion:** Saves outputs as snappy-compressed parquet for performance.

### Profiler (`shared/utils/profiler.py`)
Provides data quality oversight.
* **Metrics:** Generates row counts, null-value distributions, and distinct-value checks.
* **Purpose:** Validates the silver layer to ensure data integrity before spatial modeling.

### OSM Data Harvester (`shared/utils/osm_harvester.py`)
A specialized module for programmatically fetching, filtering, and normalizing OpenStreetMap data.
* **Functionality:** A specialized module for fetching, filtering, and normalizing OpenStreetMap data.

## ArcGIS Pro Integration
This repository serves as the data engineering backend. 

Note on Data Format: All gold assets are saved as snappy-compressed parquet files to minimize storage footprint and optimize I/O. When bringing these into ArcGIS Pro, use the xy table to point tool to map the coordinates.

Validated gold assets are the primary inputs for spatial modeling and analysis in ArcGIS Pro.