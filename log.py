import sys
import logging
import os

### Logging

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'log.log')

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def do_logging():
    logger.info("code ran")
    # After your logging statements
    sys.stdout.flush()

###
