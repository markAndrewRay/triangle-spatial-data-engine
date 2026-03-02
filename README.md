# Triangle Spatial Data Engine

A modular spatial ELT pipeline for the Research Triangle region. This framework implements a standardized Medallion Architecture to transform raw urban data into high-precision spatial assets for ArcGIS Pro.

## Technical Stack
* **Processing:** DuckDB, Polars, GeoPandas
* **Analysis:** Scikit-learn, Scipy, Statsmodels
* **Infrastructure:** ArcGIS Pro, GeoJSON, Git LFS
* **Standards:** WGS84 (EPSG:4326), snake_case schema enforcement

## Repository Structure
* **shared/**: Centralized logic for API harvesting and data normalization.
* **projects/**: Self-contained capsules for specific spatial studies.
* **data_warehouse/**: Persistence layer for normalized, GIS-ready outputs.

## System Features
* Automated API ingestion (EL) via universal harvester.
* SQL-based transformation (T) using DuckDB for high-performance spatial processing.
* Programmatic schema normalization and coordinate projection.
* Git LFS management for raw and processed datasets.

## Pipeline Execution

The engine uses a standardized CLI pattern. For a live implementation, see the **projects/01_food_desert_transit/** directory.

### 1. Ingestion (Bronze)
python3 shared/utils/harvester.py --url [SOURCE_URL] --output projects/<project_name>/data/raw/

### 2. Normalization (Silver)
python3 shared/utils/refiner.py --input projects/<project_name>/data/raw/data.geojson

### 3. Feature Engineering (Gold)
python3 projects/<project_name>/scripts/03_create_gold_assets.py

## Technical Reference: Shared Utilities

### Harvester (shared/utils/harvester.py)
Automates the acquisition of spatial datasets from municipal api endpoints.
* **Functionality:** Handles http requests, manages response parsing for geojson/csv formats, and saves raw data to the project bronze layer.
* **Goal:** Provides a consistent, programmatic entry point for all external data dependencies.

### Refiner (shared/utils/refiner.py)
The core normalization engine for the pipeline.
* **Functionality:**
    * **Schema Standardization:** Converts all headers to snake_case.
    * **Coordinate Transformation:** Projects all spatial data to epsg:4326 for universal compatibility.
    * **Format Optimization:** Transcodes raw inputs into snappy-compressed parquet files for high-performance i/o.
* **Goal:** Ensures a reliable silver layer with strictly enforced data types and geometry.

### Inspector (shared/utils/inspector.py)
A validation utility for data exploration and quality assurance.
* **Functionality:** Generates summary statistics and schema overviews to identify data drift or anomalies before promotion to the gold layer.
* **Goal:** Provides visibility into the pipeline to prevent downstream analysis errors.
