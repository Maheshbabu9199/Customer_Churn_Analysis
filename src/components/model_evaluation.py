import os
import sys
from src.utils.logger import logging
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np


def create_models():
    try:
        logistic_reg = LogisticRegression()
        decision_tree = DecisionTreeClassifier()
        random_forest = RandomForestClassifier()
        knn = KNeighborsClassifier()
        models = [logistic_reg, decision_tree, random_forest, knn]
        return models

    except Exception as e:
        logging.error(e)

def evaluate_models(models, dataset):
    try:
        fold_method = StratifiedKFold(n_splits=10)
        for model in models:
            scores = cross_val_score(model, dataset.drop(['Churn'], axis=1), dataset['Churn'], cv=fold_method, scoring='accuracy')
            print(f"{model}'s average accuracy score is: {np.mean(scores)}")

    except Exception as e:
        logging.error(e)



if __name__ == '__main__':
    try:
        logging.info('model evaluation has been started..')
        models = create_models()
        dataset = pd.read_csv('Artifacts\data_prediction.csv')
        evaluate_models(models, dataset)
        

    except Exception as e:
        logging.error(e)
        