import os
import sys
from src.utils.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.utils.utils import save_artifacts

class ModelTraining:
    def __init__(self, config):
        self.config = config
        self.data = None
        self.features = None
        self.target = None
        self.train_data = None
        self.test_data = None
        self.train_target = None
        self.test_target = None



    def initiate_model_training(self):
        logging.info('Starting model training')
        try:
            self.data = pd.read_csv(self.config.cleaned_data_path)

            logging.warning(f'dataset loaded of shape: {self.data.shape}')
            self.req_columns = ['Tenure', 'CC_Contacted_LY', 'rev_growth_yoy', 'rev_per_month', 'CC_Agent_Score', 'Account_user_count', 'City_Tier', 'Churn']
            logging.info(f'required columns: {self.req_columns}')

            self.data = self.data[self.req_columns]

            self.features = self.data.drop('Churn', axis=1)
            self.target = self.data['Churn']

            self.train_data, self.test_data, self.train_target, self.test_target = train_test_split(self.features, self.target, test_size=self.config.split_ratio, random_state=42)
            
            self.train_dataset = pd.concat([self.train_data, self.train_target], axis=1)

            self.test_dataset = pd.concat([self.test_data, self.test_target], axis=1)

            save_artifacts(object=self.train_dataset, name='train_data', type='csv')
            save_artifacts(object=self.test_dataset, name='test_data', type='csv')

            logging.info(f'train data shape: {self.train_data.shape}')

            logging.info(f'test data shape:  {self.test_data.shape}')

            logging.info('Data splitting completed')

            model = RandomForestClassifier()

            model.fit(self.train_data, self.train_target)

            save_artifacts(object=model, name='model', type='pkl')
            
        except Exception as e:
            logging.error(e)