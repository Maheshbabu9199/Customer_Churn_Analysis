import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
from src.components.data_preparation import DataPreparation

if __name__ == '__main__':
    logging.info('Starting data preparation pipeline')
    config = Configuration()
    data_preparation_config = config.get_preparation_config()
    data_preparation = DataPreparation(config=data_preparation_config)
    data_preparation.initiate_data_preparation()
