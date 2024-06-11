import os
import sys
from src.utils.logger import logging
from src.utils.utils import save_artifacts
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from src.utils.utils import save_artifacts

class DataPreparation:
    def __init__(self, config):
        self.config = config
        self.data_set = None

    def preparation_pipeline(self):
        try:
            
            logging.info('inside the preparation pipeline')
            # defining each type of columns
            categorical_cols = ['Payment','Gender','account_segment','Marital_Status', 'Login_device']
            object_cols = ['rev_growth_yoy', 'rev_per_month', 'cashback', 'coupon_used_for_payment', 'Tenure', 'Day_Since_CC_connect', 'Account_user_count']
            numerical_cols = ['AccountID', 'Churn', 'City_Tier', 'CC_Contacted_LY', 'Service_Score', 'CC_Agent_Score', 'Complain_ly']
            
            # handling numerical data
            numerical_cols = self.data_set.select_dtypes(include=['int64', 'float64']).columns.tolist()
            self.data_set = self.data_set[~self.data_set[numerical_cols].isnull().any(axis=1)]
            
            # handling object data
            for col in object_cols:
                # self.data_set[col][self.data_set[col].apply(lambda x: True if not str(x).isnumeric() else False)] = 0
                self.data_set.loc[:, col] = self.data_set[col].apply(lambda x: 0 if not str(x).isnumeric() else x)
                self.data_set[col] = self.data_set[col].astype('int64')
                self.data_set.loc[:, col] = self.data_set[col].fillna(self.data_set[col].mean())

            # print('handling object data after', self.data_set[object_cols].info())
            

            # handling categorical data
            
            for col in categorical_cols:
                self.data_set[col] = self.data_set[col].fillna(self.data_set[col].mode()[0])

            
            self.data_set.loc[:, 'Gender'] = self.data_set['Gender'].replace('M', 'Male')
            self.data_set.loc[:, 'Gender'] = self.data_set['Gender'].replace('F', 'Female')
            self.data_set.loc[:, 'account_segment'] = self.data_set['account_segment'].replace('Regular +', 'Regular Plus')
            self.data_set.loc[:, 'account_segment'] = self.data_set['account_segment'].replace('Super +','Super Plus')

            self.data_set.loc[:, 'Login_device'] = self.data_set['Login_device'].replace('&&&&','Computer')

            """for col in categorical_cols:
                print(col, self.data_set[col].unique())
            """

            label = LabelEncoder()

            for col in categorical_cols:
                self.data_set[col] = label.fit_transform(self.data_set[col])
                self.data_set[col] = self.data_set[col].astype('float64')

            # using SMOTE for balancing the classes

            # print('before sampling: ', self.data_set['Churn'].value_counts())
            
            sm = SMOTE(sampling_strategy='minority', random_state=42)


            X, y= sm.fit_resample(self.data_set.drop(['Churn'], axis=1), self.data_set['Churn'])
            oversampled = pd.concat([X,y], axis=1)

            # print('oversampled info', oversampled.info())

            # print('after sampling: ', oversampled['Churn'].value_counts())

            save_artifacts(object=oversampled, name='prepared_data',type='csv')

        except Exception as e:
            logging.error(e)   
    def initiate_data_preparation(self):
        try:
            logging.info('starting data preparation component')
            self.data_set = pd.read_csv(self.config.data_path)
            
            self.preparation_pipeline()
            
        except Exception as e:
            logging.error(e)

    