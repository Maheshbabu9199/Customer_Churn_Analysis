import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
from src.components.data_ingestion import DataIngestion


if __name__ == '__main__':
    try:
        logging.info('Starting data ingestion pipeline')
        config = Configuration()
        data_ingestion_config = config.get_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info(e)