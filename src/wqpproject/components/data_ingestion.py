import urllib.request as request
import zipfile
from wqpproject import logger
from wqpproject.utils.common import get_size
from pathlib import Path
import os
from wqpproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def extract_zip_file(self):
        """
         Extracts zip file into the given directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        if not os.path.exists(Path("artifacts\data_ingestion\winequality-red.csv")):
            logger.info(f"Extracting file in path : {self.config.local_data_file} into folder : {unzip_path}")

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"Extracted file in path : {self.config.local_data_file} into folder : {unzip_path}")
        else:
            logger.info("File already extracted")