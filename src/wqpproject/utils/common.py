import os
from box.exceptions import BoxValueError
import yaml
from wqpproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Reads yaml file and returns it

    Args:
        path_to_yaml (str) : yaml file path

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Creates list of directories

    Args:
        path_to_directories (list): list of paths of directories
        verbose (bool, optional): If logging is required. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """ Saves json data

    Args:
        path (Path): path of json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Json file is saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ Loads json files data

    Args:
        path (Path): path of json file

    Returns:
        ConfigBox
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Json file loaded succesfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ Saves binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path of binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at : {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ loads binary data

    Args:
        path (Path): path of binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """ Get file size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"