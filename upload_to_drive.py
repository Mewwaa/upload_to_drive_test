import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
def upload_files(directory_path, folder_id):
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '.github/workflows/client_secret_152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com.json',
                ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path) and (file_name.endswith('.pdf') or file_name.endswith('.txt')):
            file_metadata = {
                'name': file_name,
                'parents': [folder_id]
            }

            media = MediaFileUpload(file_path, resumable=True)

            file = drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()

            print(f'Uploaded: {file_name} (File ID: {file.get("id")})')

if __name__ == '__main__':
    directory_path = ''
    folder_id = '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'
    upload_files(directory_path, folder_id)
