import logging
import os
from datetime import datetime

log_name = 'logs'

log_folder = os.path.join(os.getcwd(), log_name)

os.makedirs(log_folder, exist_ok=True)

log_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.log'

log_file = os.path.join(log_folder, log_file_name)

logging.basicConfig(
    filename=log_file,
    filemode='w',
    format='%(asctime)s - [%(levelname)s] - %(filename)s:%(lineno)d - %(message)s', 
    level=logging.INFO
    )


if __name__ == '__main__':
    logging.warning('this is warning')