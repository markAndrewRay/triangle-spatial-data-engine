import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[3]
sys.path.append(str(repo_root))

from shared.utils.profiler import DataProfiler

def main():
    project_root = Path(__file__).resolve().parents[1]
    proc_dir = project_root / "data/processed"
    
    profiler = DataProfiler()
    
    silver_files = [
        proc_dir / "silver_wake_food_facilities.parquet",
        proc_dir / "silver_goraleigh_bus_stops.parquet"
    ]
    
    for file_path in silver_files:
        if file_path.exists():
            profiler.profile_parquet(file_path)
        else:
            print(f"[ERROR] Missing file: {file_path}")

if __name__ == "__main__":
    main()
