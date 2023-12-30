import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
import json

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.metadata',
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.scripts',
]
class GoogleDriveClient:
    def __init__(self, credentials_file):
        # Load the credentials from the provided JSON file
        self.creds = self.load_credentials(credentials_file)
        # Build the Drive API service
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        

    def load_credentials(self, credentials_file):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds


    def list_files(self):
        # List the files in Google Drive
        results = self.drive_service.files().list().execute()
        files = results.get('files', [])
        if not files:
            print("No files found in Google Drive.")
        else:
            print("Files in Google Drive:")
            for file in files:
                print(f"{file['name']} ({file['mimeType']})")

    def upload_file(self, local_file_path, drive_folder_id=None, description=None, new_name=None):
        # Upload a file to Google Drive
        if new_name:
            file_metadata = {'name': new_name, 'description': description}
        else:
            file_metadata = {'name': os.path.basename(local_file_path), 'description': description}
    
        if drive_folder_id:
            file_metadata['parents'] = [drive_folder_id]
        media = MediaFileUpload(local_file_path, resumable=True)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File '{file_metadata['name']}' uploaded with ID: {file.get('id')}")

    def get_file_description(self, file_id):
        # Get the description of a file
        file = self.drive_service.files().get(fileId=file_id, fields='name, description').execute()
        print(f"File Name: {file['name']}")
        print(f"Description: {file.get('description', 'No description available')}")

    def list_all_file_ids(self):
        # List all file IDs in Google Drive
        file_ids = []
        page_token = None
        while True:
            response = self.drive_service.files().list(
                q="trashed=false",  # Exclude trashed files
                fields="nextPageToken, files(id)",
                pageToken=page_token
            ).execute()
            files = response.get('files', [])
            for file in files:
                file_ids.append(file['id'])
            page_token = response.get('nextPageToken')
            if not page_token:
                break
        return file_ids

    def list_file_descriptions(self):
        """Lists all file descriptions in Google Drive.

        Returns:
            A list of file descriptions, where each description is a dictionary
            containing the following keys:
                * id: The ID of the file.
                * name: The name of the file.
                * description: The description of the file.
                * mimeType: The MIME type of the file.
        """

        results = self.drive_service.files().list(fields='files(id, name, description, mimeType)').execute()
        files = results.get('files', [])

        # Filter out folders.
        file_descriptions = []
        for file in files:
            if file['mimeType'] != 'application/vnd.google-apps.folder':
                file_descriptions.append({
                    'id': file['id'],
                    'name': file['name'],
                    'description': file['description'],
                    'mimeType': file['mimeType'],
                })

        return file_descriptions



    def create_folder(self, folder_name, parent_id=None):
        """Creates a new folder in Google Drive.

        Args:
            folder_name: The name of the folder to create.
            parent_id: The ID of the parent folder in which to create the new folder.
            If omitted, the folder will be created in the root of the user's Drive.

        Returns:
            The ID of the newly created folder.
        """



        # Create a file metadata object.
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        # If a parent ID is specified, set it in the file metadata.
        if parent_id:
            file_metadata['parents'] = [parent_id]

        # Create the folder.
        file = self.drive_service.files().create(body=file_metadata, fields='id').execute()

        return file['id']
    

    def get_folder_id_by_folder_name(self, folder_name):
        """Gets the ID of a Google Drive folder by folder name.

        Args:
            drive_service: A Google Drive service object.
            folder_name: The name of the folder to find.

        Returns:
            The ID of the folder if it exists, or None if the folder is not found.
        """
        query = "name = '{}' and mimeType = 'application/vnd.google-apps.folder'".format(folder_name)
        files = self.drive_service.files().list(q=query, fields='files(id)').execute()

        if 'files' in files and files['files']:
            return files['files'][0]['id']

        return None

    def upload_file_to_directory_with_description(self, local_file_path, directory_name, description, new_name=None):
        """Uploads a file to a specific directory in Google Drive, with a description.

        Args:
            local_file_path: The path to the file to upload.
            directory_name: The name of the directory to upload the file to.
            description: The description to add to the file.

        Raises:
            HttpError: If the directory does not exist and could not be created.
        """

        # Get the directory ID.
        directory_id = self.get_folder_id_by_folder_name(directory_name)

        # If the directory does not exist, create it.
        if not directory_id:
            directory_id = self.create_folder(directory_name)

        # Upload the file to the directory, with the description.
        self.upload_file(local_file_path, directory_id, description, new_name)

    def get_files_id_viewLink_downloadLink_description(self):
        """Lists all files in Google Drive and returns a dictionary with ID, URL, and descriptions.

        Returns:
            A dictionary where keys are file IDs and values are dictionaries with 'url' and 'description' keys.
        """
        results = self.drive_service.files().list(fields='files(id, webViewLink, webContentLink, description, mimeType)').execute()
        files = results.get('files', [])
        return files
        # Filter out folders and create a dictionary with ID, URL, and descriptions.
        file_dict = []
        for file in files:
            if file['mimeType'] != 'application/vnd.google-apps.folder':
                file_id = file['id']
                view_link = file.get('webViewLink', '')
                download_link = file.get('webContentLink', '')
                description = file.get('description', '')
                parsed_description = json.loads(description)
                parsed_description['view_link'] = view_link
                parsed_description['download_link'] = download_link
                file_dict.append(parsed_description)

        return file_dict

# Example usage:
if __name__ == '__main__':
    file_to_import = os.path.join('', '', '')
    drive_client = GoogleDriveClient("")
    drive_client.list_files_with_urls_and_descriptions()