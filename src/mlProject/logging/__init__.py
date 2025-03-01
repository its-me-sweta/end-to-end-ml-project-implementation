import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"# time&data , folder name, file name, message

log_dir = "logs" #make log directory or folder 

log_filepath = os.path.join(log_dir , "runnins_log.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectlogger")
