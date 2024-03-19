import logging
import os

log_level = os.getenv("LOG_LEVEL", "info").upper()
log = logging.getLogger(__name__)

# Validate the log level
valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
if log_level not in valid_log_levels:
    log_level = 'INFO'  # Default to INFO if an invalid log level is provided
log.setLevel(getattr(logging, log_level))
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)
