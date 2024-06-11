import os
import sys
from src.utils.logger import logging
from src.components.model_training import ModelTraining
from src.config.configuration import Configuration

if __name__ == '__main__':
    try:
        logging.info('Starting model training pipeline')
        config = Configuration()

        model_training_config = config.get_model_training_config()

        model_training = ModelTraining(config=model_training_config)

        model_training.initiate_model_training()

    except Exception as e:
        logging.info(e)