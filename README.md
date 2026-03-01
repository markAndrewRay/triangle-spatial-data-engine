# Triangle Spatial Data Engine

A modular spatial ELT pipeline for the Research Triangle region.

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

---
*Spatial data engineering and modular systems design.*
