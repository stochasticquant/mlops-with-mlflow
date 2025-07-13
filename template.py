import os
from pathlib import Path
import logging


# initialize logging 
logging.basicConfig(level=logging.INFO, format='[%asctime)s]: %(message)s:')

project_name = 'mlProject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "main.py",
    "schema.yaml",
    "app.py",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != '':
        # Create directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        # Create an empty file if it does not exist or is empty
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating file: {filepath}")
    else:
        # Log that the file already exists
        logging.info(f"File already exists: {filepath}")