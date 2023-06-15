from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth(settings_file='settings.yml')
drive = GoogleDrive(gauth)

upload_folder = "/"  # Ścieżka do folderu, który chcesz przesłać

upload_file = ["test.txt"]  # Lista plików do przesłania

# Przechodzenie przez wszystkie pliki w folderze
print(os.listdir(upload_folder))
for root, dirs, files in os.walk(upload_folder):
    for file in files:
        file_path = os.path.join(root, file)
        upload_file.append(file_path)

# Przesyłanie plików
for file_path in upload_file:
    gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
    gfile.SetContentFile(file_path.split('/')[-1])
    gfile.Upload()

# import requests
# import json
# import os

# # Fetch access token from OAuth endpoint
# def getToken():
#     url = "https://oauth2.googleapis.com/token"
#     payload = {
#         "code": "4%2F0AbUR2VN4vj40ZoCg-Y9Sv5v6sKv2VhxYlq00CDl4uFgJFnnubrphdmOAhJTBro9Bb7caXg",
#         "redirect_uri": "https://developers.google.com/oauthplayground",
#         "client_id": "152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com",
#         "client_secret": "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",
#         "scope": "",
#         "grant_type": "authorization_code"
#     }

#     response = requests.post(url, data=payload)
#     response_data = response.json()
#     if 'access_token' in response_data:
#         return response_data['access_token']
#     else:
#         print(response_data)  # Print response for debugging purposes
#         return None

# # Upload a single file to Google Drive using access token
# def uploadFile(file_path):
#     TOKEN_KEY = getToken()
#     if TOKEN_KEY is None:
#         print("Unable to retrieve access token.")
#         return
    
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


