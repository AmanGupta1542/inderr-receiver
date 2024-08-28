import logging
import logging.handlers
import os
from datetime import datetime

# Create logs directory if it does not exist
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logger
logger = logging.getLogger('DailyErrorLogger')
logger.setLevel(logging.ERROR)  # Log only errors and above (critical)

# Create a TimedRotatingFileHandler
log_file = os.path.join(log_directory, 'error.log')
handler = logging.handlers.TimedRotatingFileHandler(
    log_file, when='midnight', interval=1, backupCount=7
)
handler.suffix = "%Y-%m-%d_%H-%M-%S"  # Append date to log file name

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)