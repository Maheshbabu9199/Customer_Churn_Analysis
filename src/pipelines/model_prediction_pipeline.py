import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
from src.components.model_prediction import ModelPrediction


if __name__ == '__main__':
    try:
        logging.info('Starting model prediction pipeline')
        config = Configuration()
        model_prediction_config = config.get_model_prediction_config()
        model_prediction = ModelPrediction(config=model_prediction_config)
        model_prediction.initiate_model_prediction()
    except Exception as e:
        logging.info(e) 