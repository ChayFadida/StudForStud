from helpers.handle_files import HandleData
from helpers.local_client import LocalClient
import os
base_dir = os.getenv("BASE_DIR")
file_client = LocalClient(base_dir)
data_handler = HandleData(file_client)
backup_dir = os.getenv("BACKUP_DIR")
backup_cloud_username = os.getenv("BACKUP_CLOUD_USERNAME")
backup_cloud_password = os.getenv("BACKUP_CLOUD_PASSWORD")