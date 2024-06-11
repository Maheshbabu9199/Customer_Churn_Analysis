import os, sys
from src.utils.logger import logging
import pandas as pd
import pickle
from src.utils.utils import save_artifacts, load_objects

class ModelPrediction:
    def __init__(self, config):
        self.config = config
        self.data = None
        self.features = None
        self.target = None

    
    def initiate_model_prediction(self):
        try:
            logging.info('inside initiate model prediction')

            self.data = pd.read_csv(self.config.test_data_path)

            logging.info(f'dataset loaded of shape: {self.data.shape}')
            
            self.features = self.data.drop('Churn', axis=1)

            self.target = self.data['Churn']

            self.prediction = self.make_prediction(self.features)

            logging.info(f'prediction completed of shape: {self.prediction.shape}')

            self.prediction = pd.Series(self.prediction, name='Churn_predictions')

            self.data_prediction = pd.concat([self.data, self.prediction], axis=1)

            save_artifacts(object=self.data_prediction, name='data_prediction', type='csv')
            
        except Exception as e:
            logging.error(e)

        
    @staticmethod
    def make_prediction(features=None):
        try:
            logging.info('inside make prediction')


            model = load_objects(name='model.pkl')

            predictions = model.predict(features)

            return predictions
        except Exception as e:
            logging.error(e)