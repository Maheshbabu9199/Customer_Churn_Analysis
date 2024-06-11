import os
import sys
from src.utils.logger import logging
import pandas as pd 
import numpy as np 
from src.utils.utils import save_artifacts


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def initiate_data_ingestion(self):
        try:
            logging.warning('starting data ingestion component')
            data_set = pd.read_excel(io=self.config.raw_data_path, sheet_name='Data')
            logging.info(f'dataset loaded of shape: {data_set.shape}')

            save_artifacts(object=data_set, name='raw_data',type='csv')

        except Exception as e:
            logging.error(e)