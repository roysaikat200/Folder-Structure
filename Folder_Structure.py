from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : [%(message)s]')

paths_to_create = [
    "readme.md"
]

for path_str in paths_to_create:
    path = Path(path_str)

    if path_str.endswith('/'):
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {path}")
        else:
            logging.info(f"Directory already exists: {path}")
    else:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created parent directory: {path.parent}")
        if not path.exists():
            path.touch()
            logging.info(f"Created empty file: {path}")
        else:
            logging.info(f"File already exists: {path}")

logging.info("Folder structure created successfully.")
