# Triangle Spatial Decision Engine
A modular, Virtual Spatial Lakehouse designed for municipal data analysis in the Research Triangle.

## System Architecture
This repository implements a **Virtualized Spatial Lakehouse** model. Instead of traditional database ingestion, the engine uses **DuckDB Views** to point directly to standardized **GeoParquet** files. This ensures zero data redundancy, 100% portability, and native compatibility with external GIS tools like ArcGIS Pro.

## Repository Structure
```text
.
├── projects/                      # Self-contained analytical capsules
│   └── 01_food_desert_transit/
│       ├── data/
│       │   ├── bronze/            # Project-specific raw ingestion 
│       │   ├── silver/            # Hardened GeoParquet 
│       │   └── gold/              # Final Decision Layers (GeoPackage/CSV)
│       ├── notebooks/             # Experimental Analysis
│       └── scripts/               # Production-grade SQL and Python
├── shared/                        # Global Reference Library & Utilities
│   ├── data/
│   │   ├── bronze/                # Global raw reference data (e.g., Zoning)
│   │   ├── silver/                # Refined global reference data
│   │   └── triangle_engine.db     # Centralized DuckDB Warehouse
│   └── utils/                     
│       ├── db/                    # Database initialization & maintenance
│       └── io/
│           └── ingestor.py        # Core Modular Ingestion Engine
└── requirements.txt               # Environment Dependencies
```

## Core Components
* **Virtual Data Warehouse**: Uses DuckDB Views to query external Parquet files, keeping the `.db` file lightweight while processing millions of rows.
* **Shared Reference Library (shared/data/)**: Centralized repository for universal municipal layers used across multiple project capsules.
* **Project Capsules (projects/)**: Self-contained "Capsule Corp" style units with localized data, scripts, and notebooks for modular scaling.
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
To execute a specific project capsule and refresh the data pipeline, run the following from the root directory:

```bash
export PYTHONPATH=\$PYTHONPATH:.
python projects/01_food_desert_transit/main.py
```