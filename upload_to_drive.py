# import os
# import pickle
# from googleapiclient.discovery import build
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from googleapiclient.http import MediaFileUpload
# from google_auth_oauthlib.flow import InstalledAppFlow

# def upload_files(directory_path, folder_id):
#     creds = None

#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 '.github/workflows/client_secret_152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com.json',
#                 ['https://www.googleapis.com/auth/drive'])
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     drive_service = build('drive', 'v3', credentials=creds)

#     print(f"Directory Path: {directory_path}")

#     for file_name in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, file_name)
#         print(f"Processing file: {file_path}")

#         if os.path.isfile(file_path) and (file_name.endswith('.pdf') or file_name.endswith('.txt')):
#             file_metadata = {
#                 'name': file_name,
#                 'parents': [folder_id]
#             }

#             media = MediaFileUpload(file_path, resumable=True)

#             file = drive_service.files().create(
#                 body=file_metadata,
#                 media_body=media,
#                 fields='id'
#             ).execute()

#             print(f'Uploaded: {file_name} (File ID: {file.get("id")})')

# if __name__ == '__main__':
#     directory_path = ''
#     folder_id = '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'
#     upload_files(directory_path, folder_id)



# import requests
# import json
# import os

# # Get refresh token from Google Drive API
# def getToken():
#     oauth = 'https://www.googleapis.com/oauth2/v4/token'  # Google API OAuth URL
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     data = {
#         'grant_type': 'refresh_token',
#         'client_id': '152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com',
#         'client_secret': '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',
#         'refresh_token': '1//04NaMgLSpxEUeCgYIARAAGAQSNwF-L9Irp-Ym8TTsEGOkqCYhDXtWInx98ntgtDGmMMlxiKHBJ1bHti9_rVKr0hq7sYmjiE8tUgo',  # Replace with your refresh token
#     }

#     token = requests.post(oauth, headers=headers, data=data)
#     _key = json.loads(token.text)
#     return _key['access_token']

# # Upload files to Google Drive using access token
# def upload2Drive(file_path):
#     TOKEN_KEY = getToken()
#     headers = {"Authorization": "Bearer " + TOKEN_KEY}
    
#     file_name = os.path.basename(file_path)
#     para = {
#         "name": file_name,  # File name to be uploaded
#         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID where files should be uploaded
#     }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(file_path, "rb")
#     }

#     upload = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#     )
#     print(upload.text)


# if __name__ == '__main__':
#     file_path = "test.txt"  # Replace with the path to your file

#     file_extension = os.path.splitext(file_path)[1]
#     if file_extension == ".txt" or file_extension == ".pdf":
#         upload2Drive(file_path)
#     else:
#         print("Invalid file extension. Only .txt and .pdf files are supported.")


# import requests
# import json
# import os

# # Get access token directly from the provided value
# def getToken():
#     return 'ya29.a0AWY7CknIY0CW-fPmmyb6VlbAFNfsMwvQxUdi730Ql_d-8dXTMvS9YvygGkLc8JD8uG6P2uCv4zBKvJFg6xUdcbQ9ht75SfWRDDaCBj-2zLQsSytoTm7txN-JLvOeCLoTRFnS4jkCUsybUekPDp2laYEZEJ-eaCgYKATkSARASFQG1tDrpAIhHZ488E407Hvzjs9b1dQ0163'

# # Upload files to Google Drive using access token
# def upload2Drive(file_path):
#     TOKEN_KEY = getToken()
#     headers = {"Authorization": "Bearer " + TOKEN_KEY}
    
#     file_name = os.path.basename(file_path)
#     para = {
#         "name": file_name,  # File name to be uploaded
#         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID where files should be uploaded
#     }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(file_path, "rb")
#     }

#     upload = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#     )
#     print(upload.text)


# if __name__ == '__main__':
#     file_path = "test.txt"  # Replace with the path to your file

#     file_extension = os.path.splitext(file_path)[1]
#     if file_extension == ".txt" or file_extension == ".pdf":
#         upload2Drive(file_path)
#     else:
#         print("Invalid file extension. Only .txt and .pdf files are supported.")


# import requests
# import json
# import os

# # Get access token directly from the provided value
# def getToken():
#     return 'ya29.a0AWY7CknHFPyPSWXuFjbVT45MtnEArZvhRZHS2v2S1u6kJkaenjWJYKVbL7_s778KH5y8H_7JajKg8R-ckFz6dq0ohiYSg1wFdNFDEkb3psf033D9g-JzebResE-s7HIX-xxO4t0a3pZq5HqrDsX9RufaO-JgaCgYKARwSARASFQG1tDrpaRoz8bZI3pThqXUhhiwQuA0163'

# # Upload a single file to Google Drive using access token
# def uploadFile(file_path):
#     TOKEN_KEY = getToken()
#     headers = {"Authorization": "Bearer " + TOKEN_KEY}
    
#     file_name = os.path.basename(file_path)
#     para = {
#         "name": file_name,  # File name to be uploaded
#         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID where files should be uploaded
#     }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(file_path, "rb")
#     }

#     upload = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#     )
#     print(upload.text)

# # Upload only the files with .txt and .pdf extensions from the root directory of the repository
# def uploadAllFiles():
#     root_dir = os.getcwd()  # Get the current working directory (root directory of the repository)

#     for file_name in os.listdir(root_dir):
#         file_path = os.path.join(root_dir, file_name)
#         if os.path.isfile(file_path):
#             file_extension = os.path.splitext(file_path)[1]
#             if file_extension == ".txt" or file_extension == ".pdf":
#                 uploadFile(file_path)

# if __name__ == '__main__':
#     uploadAllFiles()



# import requests
# import json
# import os

# # Fetch a new access token using the refresh token
# def getAccessToken():
#     oauth = 'https://www.googleapis.com/oauth2/v4/token'  # Google API OAuth URL
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     data = {
#         'grant_type': 'refresh_token',
#         'client_id': '152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com',
#         'client_secret': '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',
#         'refresh_token': '1//04NaMgLSpxEUeCgYIARAAGAQSNwF-L9Irp-Ym8TTsEGOkqCYhDXtWInx98ntgtDGmMMlxiKHBJ1bHti9_rVKr0hq7sYmjiE8tUgo',  # If something is not working get new token from https://developers.google.com/oauthplayground/
#     }

#     token = requests.post(oauth, headers=headers, data=data)
#     _key = json.loads(token.text)
#     return _key['access_token']

# # Upload a single file to Google Drive using access token
# def uploadFile(file_path, access_token):
#     headers = {"Authorization": "Test " + access_token}
    
#     file_name = os.path.basename(file_path)
#     para = {
#         "name": file_name,  # File name
#         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID
#     }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(file_path, "rb")
#     }

#     upload = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#     )
#     print(upload.text)

# # Upload only the files with .txt and .pdf extensions from the root directory of the repository
# def uploadAllFiles():
#     root_dir = os.getcwd()  # Get the current working directory (root directory of the repository)
#     access_token = getAccessToken()

#     for file_name in os.listdir(root_dir):
#         file_path = os.path.join(root_dir, file_name)
#         if os.path.isfile(file_path):
#             file_extension = os.path.splitext(file_path)[1]
#             if file_extension == ".txt" or file_extension == ".pdf":
#                 uploadFile(file_path, access_token)

# if __name__ == '__main__':
#     uploadAllFiles()

import requests
import json
import os

# Fetch access token from OAuth endpoint
def getToken():
    url = "https://oauth2.googleapis.com/token"
    payload = {
        "code": "4%2F0AbUR2VN4vj40ZoCg-Y9Sv5v6sKv2VhxYlq00CDl4uFgJFnnubrphdmOAhJTBro9Bb7caXg",
        "redirect_uri": "https%3A%2F%2Fdevelopers.google.com%2Foauthplayground",
        "client_id": "152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com",
        "client_secret": "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",
        "scope": "",
        "grant_type": "authorization_code"
    }

    response = requests.post(url, data=payload)
    response_data = response.json()
    authorization_code = response_data.get('access_token')
    return authorization_code

# Upload a single file to Google Drive using access token
def uploadFile(file_path):
    TOKEN_KEY = getToken()
    headers = {"Authorization": "Bearer " + TOKEN_KEY}
    
    file_name = os.path.basename(file_path)
    para = {
        "name": file_name,  # File name to be uploaded
        "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID where files should be uploaded
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file_path, "rb")
    }

    upload = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(upload.text)

# Upload only the files with .txt and .pdf extensions from the root directory of the repository
def uploadAllFiles():
    root_dir = os.getcwd()  # Get the current working directory (root directory of the repository)

    for file_name in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_path)[1]
            if file_extension == ".txt" or file_extension == ".pdf":
                uploadFile(file_path)

if __name__ == '__main__':
    uploadAllFiles()

