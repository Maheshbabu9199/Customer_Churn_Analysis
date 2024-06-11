import os 
import sys
from src.utils.logger import logging
import pickle

def save_artifacts(object=None, name=None, type=None):
    try:
        logging.info(f'inside the artifacts folder for saving {name}')
        if not os.path.exists('Artifacts'):
            os.makedirs('Artifacts')
        
        if type=='csv':
            object.to_csv('Artifacts'+'/'+name+'.csv', index=False)
            logging.info(f'{name} has been saved')
        
        elif type=='pkl':
            pickle.dump(object, open('Artifacts'+'/'+name+'.pkl', 'wb'))
            logging.info(f'{name} has been saved')


    except Exception as e:
        logging.error(e)


def load_objects(name=None):
    try:
        logging.info(f'inside the load_objects folder for loading {name}')

        if name[-3:]=='pkl':
            logging.critical(f'{name} has been loaded')
            return pickle.load(open('Artifacts'+'/'+name, 'rb'))
            
        
    except Exception as e:
        logging.error(e)