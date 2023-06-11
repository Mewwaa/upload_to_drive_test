import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def upload_file(file_path, 10wd3StRU5zWgARvINrG9Amu09h9L_AhD):
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '.github/workflows/client_secret_152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com.json', ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)

    file_name = os.path.basename(file_path)

    file_metadata = {
        'name': file_name,
        'parents': [10wd3StRU5zWgARvINrG9Amu09h9L_AhD]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f'File ID: {file.get("id")}')

if __name__ == '__main__':
    upload_file('path_to_file.pdf', '10wd3StRU5zWgARvINrG9Amu09h9L_AhD')
