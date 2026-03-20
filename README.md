# Triangle Spatial Data Engine
A modular, configuration-driven geospatial ETL pipeline designed for municipal data analysis in the Research Triangle.

## System Architecture
This repository implements a metadata-driven ingestion model, separating core processing logic from project-specific data definitions. This architecture ensures scalability, reproducibility, and high-performance data handling.

## Repository Structure
```text
.
├── projects/
│   └── 01_food_desert_transit/    # Active Analysis Capsule
│       ├── config.yml             # Data Source Definitions
│       ├── main.py                # Pipeline Controller
│       └── data/
│           └── bronze/            # Standardized GeoParquet Files
├── shared/
│   └── utils/
│       └── io/
│           └── ingestor.py        # Core Modular Ingestion Engine
└── requirements.txt               # Environment Dependencies
```

## Core Components
* **Shared Utilities (shared/)**: A centralized ingestor engine that handles multi-format data acquisition (ArcGIS FeatureServer, OSM Overpass API, GeoJSON) and enforces standardized coordinate reference systems (CRS).
* **Project Capsules (projects/)**: Self-contained analytical units. Each project contains its own config.yml (data sources and parameters) and main.py controller.
* **Medallion Data Layering**: 
    * **Bronze**: Raw, immutable snapshots stored as GeoParquet for high-performance I/O.
    * **Silver**: Normalized and cleaned tables hosted in a local DuckDB instance.
    * **Gold**: Analysis-ready features optimized for ArcGIS Pro and web visualization.

## Getting Started

### Prerequisites
The environment is optimized for VS Code Dev Containers with the following core stack:
* **Engine**: Python 3.12
* **Spatial**: GeoPandas, Shapely, PyProj
* **Storage**: DuckDB, Polars, Apache Parquet

### Running a Project Pipeline
To execute the ingestion for a specific project capsule, run the following from the root directory:

```bash
export PYTHONPATH=$PYTHONPATH:.
python3 projects/01_food_desert_transit/main.py
```