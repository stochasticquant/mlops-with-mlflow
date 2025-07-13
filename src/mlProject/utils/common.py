import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations   
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"File not found: {path_to_yaml}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    

@ensure_annotations
def create_directories(path_to_dirs: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_dirs (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        try:
            if verbose:
                logger.info(f"Directory created: {path}")
        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise e
    
@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """
    Saves data to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (Any): Data to save in the JSON file.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data saved to JSON file: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {e}")
        raise e
    
@ensure_annotations
def load_json(path: Path) -> Any:
    """
    Loads data from a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        Any: Data loaded from the JSON file.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data loaded from JSON file: {path}")
            return data
    except FileNotFoundError as e:
        logger.error(f"File not found: {path}")
        raise e
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON file: {e}")
        raise e
    
@ensure_annotations
def load_binary(path: Path) -> Any:
    """
    Loads binary data from a file.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary data loaded from: {path}")
        return data
    except FileNotFoundError as e:
        logger.error(f"File not found: {path}")
        raise e
    except Exception as e:
        logger.error(f"Error loading binary data: {e}")
        raise e
    
@ensure_annotations
def get_size(path: Path) -> int:
    """
    Gets the size of a file in bytes.
    
    Args:
        path (Path): Path to the file.
        
    Returns:
        int: Size of the file in bytes.
    """
    try:
        size = os.path.getsize(path)
        logger.info(f"Size of file {path}: {size} bytes")
        return size
    except FileNotFoundError as e:
        logger.error(f"File not found: {path}")
        raise e
    except Exception as e:
        logger.error(f"Error getting file size: {e}")
        raise e