# Triangle Spatial Data Engine
A modular, configuration-driven geospatial ETL pipeline designed for municipal data analysis in the Research Triangle.

## System Architecture
This repository implements a **Virtualized Spatial Warehouse** model. Instead of traditional database ingestion, the engine uses **DuckDB Views** to point directly to standardized **GeoParquet** files. This ensures zero data redundancy, 100% portability, and native compatibility with external GIS tools like ArcGIS Pro.

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
│   └── utils/                     # Global Utilities Folder
│       └── io/
│           └── ingestor.py        # Core Modular Ingestion Engine
└── requirements.txt               # Environment Dependencies
```

## Core Components
* **Virtual Data Warehouse**: Uses DuckDB Views to query external Parquet files, keeping the `.db` file under 100KB while processing millions of rows.
* **Shared Utilities (shared/)**: Reusable utilities for high-precision acquisition and relational database management.
* **Project Capsules (projects/)**: Self-contained capsules with localized data, scripts, and notebooks for modular scaling.
* **Industry Standards**: Enforces standardized data normalization, EPSG projection logic, and strict ethical data guidelines.

## Getting Started

### Prerequisites
This engine requires **Python 3.12+**. All core logic is tested against **DuckDB v1.1.0+** and the **DuckDB Spatial Extension**.

### Environment Setup 
To ensure high-precision spatial operations and dependency isolation, this project uses a local virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Verify the Engine
Run the following to ensure the Spatial Engine and CRS (Coordinate Reference System) logic are operational:
```bash
python -c "import duckdb; con=duckdb.connect(':memory:'); con.execute('INSTALL spatial; LOAD spatial;'); res=con.execute(\"SELECT ST_AsText(ST_SetCRS(ST_GeomFromText('POINT(0 0)'), 'EPSG:4326'))\").fetchall(); print(f'🚀 Engine Status: {res}')"
```

### Execution
To execute a specific project capsule and refresh the Bronze GeoParquet files, run the following from the root directory:

```bash
export PYTHONPATH=\$PYTHONPATH:.
python projects/01_food_desert_transit/main.py
```