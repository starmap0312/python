# Level
#   DEBUG < INFO < WARNING < ERROR < CRITICAL
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
# create a logging format for the console handler
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)

# create a file handler
handler = logging.FileHandler('example.log')
handler.setLevel(logging.INFO)
# create a logging format for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
logger.addHandler(console_handler)

logger.debug('this is a debug message')
logger.info('this is a info message')
logger.error('this is a error message')
