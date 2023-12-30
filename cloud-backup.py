from cron.cloud_cron import BackupManager
from config.app_contex import backup_cloud_username, backup_cloud_password, backup_dir

if __name__ == '__main__':
    backupManager = BackupManager(backup_cloud_username, backup_cloud_password)
    backupManager.create_backup(backup_dir)