import os
from shared.utils.io.ingestor import Ingestor

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, 'config.yml')
    
    engine = Ingestor(config_path)
    engine.run()
