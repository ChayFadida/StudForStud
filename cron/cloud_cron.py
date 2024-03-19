from helpers.mega_client import MegaClient
from datetime import datetime
from config.app_contex import backup_cloud_username, backup_cloud_password, backup_dir
import os
from config.logger_config import log


class BackupManager:
    def __init__(self, mega_email, mega_password):
        """
        Initialize the BackupManager with MegaClient credentials.

        Args:
            mega_email (str): The email address for MegaClient authentication.
            mega_password (str): The password for MegaClient authentication.
        """
        self.mega_client = MegaClient(mega_email, mega_password)

    def get_latest_backup_file_path(self, directory='.'):
        """
        Get the full path of the latest backup file in the current directory.

        This method looks for files in the current directory with names starting
        with 'backup_' and ending with '.tar.gz'. It then returns the full path of
        the file with the latest timestamp.

        Returns:
            str or None: The full path of the latest backup file, or None if no
            backup files are found.
        """
        backup_files = [filename for filename in os.listdir(directory) if filename.startswith('backup_') and filename.endswith('.tar.gz')]

        if backup_files:
            file_name = max(backup_files)
            full_path = os.path.join(directory, file_name)
            log.info(f"The latest backup file is: {full_path}")
            return full_path, file_name
        else:
            log.info("No backup files found.")
            return None

    def create_backup(self, directory):
        """
        Create a backup by uploading the latest backup file to Mega.

        This method gets the latest backup file name, creates a folder in Mega with
        the current date, and uploads the latest backup file to that folder.
        """
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the date as a string
        current_date_string = current_datetime.strftime("%Y-%m-%d")

        # Get the latest backup file name
        latest_backup_path, file_name = self.get_latest_backup_file_path(directory)

        if latest_backup_path:
            # Create a folder in Mega with the current date
            self.mega_client.create_folder(current_date_string)

            # Upload the latest backup file to Mega
            self.mega_client.upload_file(latest_backup_path, current_date_string, file_name)
            log.info("backup just created")
        else:
            log.error("Backup creation failed. No backup files found.")

if __name__ == '__main__':
    backupManager = BackupManager(backup_cloud_username, backup_cloud_password)
    backupManager.create_backup(backup_dir)