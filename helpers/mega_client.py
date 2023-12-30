from mega import Mega

class MegaClient:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.mega = Mega()
        self.mega_login()

    def mega_login(self):
        self.mega_user = self.mega.login(self.email, self.password)

    def create_folder(self, folder_name):
        """Create a new folder if does not exist.

        Args:
            folder_name: name of the new folder.
        """
        self.mega_user.create_folder(folder_name)

    def upload_file(self, local_file_path, remote_folder, new_file_name):
        """Uploads a file from the local disk to Mega.

        Args:
            local_file_path: The path to the local file to be uploaded.
            remote_file_path: The path to the remote file to be created.
        """
        folder = self.mega_user.find(remote_folder)
        self.mega_user.upload(local_file_path, folder[0], new_file_name)


    def list_files(self, remote_directory_path):
        """Lists all files in a remote directory.

        Args:
            remote_directory_path: The path to the remote directory to list.

        Returns:
            A list of MegaFile objects, representing the files in the remote directory.
        """

        remote_directory = self.mega_user.get_directory(remote_directory_path)
        return remote_directory.get_files()

    def get_file_size(self, remote_file_path):
        """Gets the size of a remote file.

        Args:
            remote_file_path: The path to the remote file.

        Returns:
            The size of the remote file in bytes.
        """

        remote_file = self.mega_user.get_file(remote_file_path)
        return remote_file.get_size()

    def download_file(self, remote_file_path, local_file_path):
        """Downloads a file from Mega to the local disk.

        Args:
            remote_file_path: The path to the remote file to be downloaded.
            local_file_path: The path to the local file to be created.
        """

        remote_file = self.mega_user.get_file(remote_file_path)
        remote_file.download(local_file_path)

# Example usage:
if __name__ == '__main__':
    mega_email = ''
    mega_password = ''
    mega_client = MegaClient(mega_email, mega_password)

    mega_client.create_folder("")
    mega_client.upload_file("", "", "")

    # Download a file from MEGA
