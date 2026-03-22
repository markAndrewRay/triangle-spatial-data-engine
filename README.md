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
│   └── utils/                     # Global Utilities Folder
│       └── io/
│           └── ingestor.py        # Core Modular Ingestion Engine
└── requirements.txt               # Environment Dependencies
```

## Core Components
* **Shared Utilities (shared/)**: Reusable utilities for high-precision acquisition and relational database management.
* **Project Capsules (projects/)**: Self-contained "Senior" way capsules with their own data, scripts, and notebooks.
* **Industry Standards**: Enforces standardized data normalization and strict ethical data guidelines.

## Getting Started

### Prerequisites
This engine requires **Python 3.12+**. All core logic is tested against **DuckDB v1.5.0** and the **DuckDB Spatial Extension**.

### Environment Setup 
To ensure high-precision spatial operations and dependency isolation, this project uses a local virtual environment.

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

### Verify the Engine
Run the following to ensure the 1.5.0 Spatial Engine and CRS (Coordinate Reference System) logic are operational:
```bash
python -c "import duckdb; con=duckdb.connect(':memory:'); con.execute('INSTALL spatial; LOAD spatial;'); res=con.execute(\"SELECT ST_AsText(ST_SetCRS(ST_GeomFromText('POINT(0 0)'), 'EPSG:4326'))\").fetchall(); print(f'🚀 Engine Status: {res}')"
```

### 3. Execution
To execute a specific project capsule, run the following from the root directory:

```bash
export PYTHONPATH=\\\$PYTHONPATH:.
python projects/01_food_desert_transit/main.py
```
