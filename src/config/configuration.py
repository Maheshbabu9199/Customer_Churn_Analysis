import os
import sys
from src.utils.logger import logging
from pathlib import Path
import yaml
from src.entity_configs.config_entity import DataIngestionConfig, DataPreparationConfig, ModelTrainingConfig, ModelPredictionConfig

class Configuration:
    def __init__(self):
        with open("src/config/config.yaml", 'r') as stream:
            self.config = yaml.safe_load(stream)

        logging.info(self.config)



    def get_ingestion_config(self):
        try:
            data_ingestion_config = self.config['data_ingestion']
            return DataIngestionConfig(raw_data_path=data_ingestion_config['data_source_path'])
        except Exception as e:
            logging.error(e)
            return None

    def get_preparation_config(self):
        try:
            data_preparation_config = self.config['data_preparation']
            return DataPreparationConfig(data_path = data_preparation_config['data_path'])
        except Exception as e:
            pass


    def get_model_training_config(self):
        try:
            model_training_config = self.config['model_training']


            return ModelTrainingConfig(cleaned_data_path=model_training_config['cleaned_data_path'], split_ratio = model_training_config['split_ratio'])

        except Exception as e:
            logging.error(e)

    def get_model_prediction_config(self):
        try:
            model_prediction_config = self.config['model_prediction']
            return ModelPredictionConfig(model_path=model_prediction_config['model_path'], test_data_path=model_prediction_config['test_data_path'])
        except Exception as e:
            logging.error(e)