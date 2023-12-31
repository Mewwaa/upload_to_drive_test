import os
import io
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Set the path to the credentials JSON file for your service account
SERVICE_ACCOUNT_FILE = 'service_account_credentials.json'

# Set the ID of the destination folder in Google Drive
DESTINATION_FOLDER_ID = '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'

# Authenticate and create a Drive service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive']
)
drive_service = build('drive', 'v3', credentials=credentials)

def upload_file(file_path):
    file_name = os.path.basename(file_path)

    # Create the metadata for the file
    file_metadata = {
        'name': file_name,
        'parents': [DESTINATION_FOLDER_ID]
    }

    # Download the file from GitHub
    file_content = requests.get(file_path).content

    # Create an IO buffer and write the downloaded file content to it
    file_buffer = io.BytesIO(file_content)

    # Create a media object for the file upload
    media = MediaIoBaseUpload(file_buffer, mimetype='application/octet-stream')

    # Upload the file to Google Drive
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f'File "{file_name}" uploaded. File ID: {file["id"]}')

# GitHub repository details
github_username = 'Mewwaa'
github_repository = 'upload_to_drive_test'

# API endpoint to retrieve repository contents
api_url = f'https://api.github.com/repos/{github_username}/{github_repository}/contents'

# Retrieve the list of files from the GitHub repository
response = requests.get(api_url)
files_data = response.json()

# Upload each file (PDF or TXT) to Google Drive
for file_data in files_data:
    download_url = file_data.get('download_url')
    if download_url:
        file_extension = os.path.splitext(download_url)[1].lower()
        if file_extension in ['.pdf', '.txt']:
            upload_file(download_url)


# import os
# import io
# import requests
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseUpload

# # Set the path to the credentials JSON file for your service account
# SERVICE_ACCOUNT_FILE = 'service_account_credentials.json'

# # Set the ID of the destination folder in Google Drive
# DESTINATION_FOLDER_ID = '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'

# # Authenticate and create a Drive service
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive']
# )
# drive_service = build('drive', 'v3', credentials=credentials)

# def upload_file(file_path):
#     file_name = os.path.basename(file_path)

#     # Create the metadata for the file
#     file_metadata = {
#         'name': file_name,
#         'parents': [DESTINATION_FOLDER_ID]
#     }

#     # Download the file from GitHub
#     file_content = requests.get(file_path).content

#     # Create an IO buffer and write the downloaded file content to it
#     file_buffer = io.BytesIO(file_content)

#     # Create a media object for the file upload
#     media = MediaIoBaseUpload(file_buffer, mimetype='application/octet-stream')

#     # Upload the file to Google Drive
#     file = drive_service.files().create(
#         body=file_metadata,
#         media_body=media,
#         fields='id'
#     ).execute()

#     print(f'File "{file_name}" uploaded. File ID: {file["id"]}')

# # GitHub repository details
# github_username = 'Mewwaa'
# github_repository = 'upload_to_drive_test'

# # API endpoint to retrieve repository contents
# api_url = f'https://api.github.com/repos/{github_username}/{github_repository}/contents'

# # Retrieve the list of files from the GitHub repository
# response = requests.get(api_url)
# files_data = response.json()

# # Upload each file (PDF or TXT) to Google Drive
# for file_data in files_data:
#     download_url = file_data.get('download_url')
#     if download_url:
#         file_extension = os.path.splitext(download_url)[1].lower()
#         if file_extension in ['.pdf', '.txt']:
#             upload_file(download_url)





# import os
# import requests
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload

# def upload_single_file(file_name, file_path):
#     drive_folder_id = '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'
#     drive_service = build('drive', 'v3')

#     file_metadata = {
#         'name': file_name,
#         'parents': [drive_folder_id]
#     }

#     media = MediaFileUpload(file_path, mimetype='application/pdf')

#     file = drive_service.files().create(
#         body=file_metadata,
#         media_body=media,
#         fields='id,name'
#     ).execute()

#     print('File Uploaded:', file.get('name'), file.get('id'))

# url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
# response = requests.get(url)
# data = response.json()
# tree_url = data["commit"]["commit"]["tree"]["url"]
# print(tree_url)
# response_tree = requests.get(tree_url)

# if response_tree.status_code == 200:
#     tree_data = response_tree.json()
#     if "tree" in tree_data:
#         print("Files found in the repository.")
#         for item in tree_data["tree"]:
#             if item["type"] == "blob":
#                 file_path = item["path"]
#                 if file_path.endswith(".txt") or file_path.endswith(".pdf"):
#                     file_name = os.path.basename(file_path)
#                     upload_single_file(file_name, file_path)
#     else:
#         print("No files found in the repository.")
# else:
#     print("Failed to retrieve tree data.")




# # import os
# # import requests
# # import time
# # from google.oauth2 import service_account
# # from googleapiclient.discovery import build

# # # Path to the service account credentials JSON file
# # credentials_file = "service_account_credentials.json"

# # # Define the scopes for the service account
# # scopes = ["https://www.googleapis.com/auth/drive"]

# # # Load the service account credentials
# # credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)

# # # Build the Google Drive service
# # drive_service = build("drive", "v3", credentials=credentials)

# # upload_folder = "/"  # Path to the folder you want to upload
# # upload_file = []  # List of files to upload

# # url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
# # response = requests.get(url)
# # data = response.json()
# # tree_url = data["commit"]["commit"]["tree"]["url"]
# # print(tree_url)
# # response_tree = requests.get(tree_url)

# # if response_tree.status_code == 200:
# #     tree_data = response_tree.json()
# #     if "tree" in tree_data:
# #         print("Files found in the repository.")
# #         for item in tree_data["tree"]:
# #             if item["type"] == "blob":
# #                 file_path = item["path"]
# #                 if file_path.endswith(".txt") or file_path.endswith(".pdf"):
# #                     upload_file.append(file_path)
# #                     print("Files found in here too.")
# #     else:
# #         print("No files found in the repository.")
# # else:
# #     print("Failed to retrieve tree data.")


# # # Upload files
# # for file_path in upload_file:
# #     print("weszło w ostatniego fora")
# #     print(file_path)
# #     file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
# #     r = requests.get(file_url, allow_redirects=True)
# #     print("przeszło za requests.get")
# #     file_name = os.path.basename(file_path)
# #     print("przeszło za os.path.basename")
# #     open(file_name, 'wb').write(r.content)
# #     print("przeszło za open")

# #     # Create the file metadata
# #     file_metadata = {
# #         "name": file_name,
# #         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # ID of the parent folder
# #     }

# #     # Upload the file
# #     drive_service.files().create(body=file_metadata, media_body=file_name).execute()
# #     print("przeszło za Upload")










# # # import os
# # # import requests
# # # import time
# # # from pydrive.auth import GoogleAuth
# # # from pydrive.drive import GoogleDrive

# # # # Authenticate using a service account
# # # gauth = GoogleAuth()
# # # gauth.ServiceAuth()
# # # drive = GoogleDrive(gauth)

# # # upload_folder = "/"  # Path to the folder you want to upload
# # # upload_file = []  # List of files to upload

# # # url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
# # # response = requests.get(url)
# # # data = response.json()
# # # tree_url = data["commit"]["commit"]["tree"]["url"]
# # # print(tree_url)
# # # response_tree = requests.get(tree_url)

# # # if response_tree.status_code == 200:
# # #     tree_data = response_tree.json()
# # #     if "tree" in tree_data:
# # #         print("Files found in the repository.")
# # #         for item in tree_data["tree"]:
# # #             if item["type"] == "blob":
# # #                 file_path = item["path"]
# # #                 if file_path.endswith(".txt") or file_path.endswith(".pdf"):
# # #                     upload_file.append(file_path)
# # #                     print("Files found in here too.")
# # #     else:
# # #         print("No files found in the repository.")
# # # else:
# # #     print("Failed to retrieve tree data.")


# # # # Upload files
# # # for file_path in upload_file:
# # #     print("weszło w ostatniego fora")
# # #     print(file_path)
# # #     file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
# # #     r = requests.get(file_url, allow_redirects=True)
# # #     print("przeszło za requests.get")
# # #     file_name = os.path.basename(file_path)
# # #     print("przeszło za os.path.basename")
# # #     open(file_name, 'wb').write(r.content)
# # #     print("przeszło za open")
# # #     gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
# # #     gfile.SetContentFile(file_name)
# # #     print("przeszło za SetContentFile")
# # #     gfile.Upload()
# # #     print("przeszło za Upload")



# # # # import os
# # # # import requests
# # # # from pydrive.auth import GoogleAuth
# # # # from pydrive.drive import GoogleDrive

# # # # gauth = GoogleAuth(settings_file='settings.yml')
# # # # drive = GoogleDrive(gauth)

# # # # upload_folder = "/"  # Path to the folder you want to upload
# # # # upload_file = []  # List of files to upload

# # # # url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
# # # # response = requests.get(url)
# # # # data = response.json()
# # # # tree_url = data["commit"]["commit"]["tree"]["url"]
# # # # print(tree_url)
# # # # response_tree = requests.get(tree_url)

# # # # if response_tree.status_code == 200:
# # # #     tree_data = response_tree.json()
# # # #     if "tree" in tree_data:
# # # #         print("Files found in the repository.")
# # # #         for item in tree_data["tree"]:
# # # #             if item["type"] == "blob":
# # # #                 file_path = item["path"]
# # # #                 if file_path.endswith(('.pdf', '.txt')):
# # # #                     upload_file.append(file_path)
# # # #                     print("Files found here too.")
# # # #     else:
# # # #         print("No files found in the repository.")
# # # # else:
# # # #     print("Failed to retrieve tree data.")

# # # # # Upload files
# # # # for file_path in upload_file:
# # # #     file_name = os.path.basename(file_path)
# # # #     file_id = None

# # # #     # Search for existing file in the upload folder
# # # #     file_list = drive.ListFile({'q': f"'10wd3StRU5zWgARvINrG9Amu09h9L_AhD' in parents and trashed=false"}).GetList()
# # # #     for file in file_list:
# # # #         if file['title'] == file_name:
# # # #             file_id = file['id']
# # # #             break

# # # #     # Create a copy of the file if it doesn't exist in the folder
# # # #     if not file_id:
# # # #         new_file = drive.CreateFile({'title': file_name, 'parents': [{'id': '10wd3StRU5zWgARvINrG9Amu09h9L_AhD'}]})
# # # #         new_file.SetContentFile(file_path)
# # # #         new_file.Upload()
# # # #         print(f"Uploaded file: {file_name}")
# # # #     else:
# # # #         print(f"File already exists: {file_name}")


# # # # import os
# # # # import requests
# # # # import time
# # # # from pydrive.auth import GoogleAuth
# # # # from pydrive.drive import GoogleDrive

# # # # gauth = GoogleAuth()
# # # # drive = GoogleDrive(gauth)

# # # # upload_folder = "/"  # Path to the folder you want to upload
# # # # upload_file = []  # List of files to upload

# # # # url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
# # # # response = requests.get(url)
# # # # data = response.json()
# # # # tree_url = data["commit"]["commit"]["tree"]["url"]
# # # # print(tree_url)
# # # # response_tree = requests.get(tree_url)

# # # # if response_tree.status_code == 200:
# # # #     tree_data = response_tree.json()
# # # #     if "tree" in tree_data:
# # # #         print("Files found in the repository.")
# # # #         for item in tree_data["tree"]:
# # # #             if item["type"] == "blob":
# # # #                 file_path = item["path"]
# # # #                 if file_path.endswith(".txt") or file_path.endswith(".pdf"):
# # # #                     upload_file.append(file_path)
# # # #                     print("Files found in here too.")
# # # #     else:
# # # #         print("No files found in the repository.")
# # # # else:
# # # #     print("Failed to retrieve tree data.")


# # # # # Upload files
# # # # for file_path in upload_file:
# # # #     print("weszło w ostatniego fora")
# # # #     print(file_path)
# # # #     file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
# # # #     r = requests.get(file_url, allow_redirects=True)
# # # #     print("przeszło za requests.get")
# # # #     file_name = os.path.basename(file_path)
# # # #     print("przeszło za os.path.basename")
# # # #     open(file_name, 'wb').write(r.content)
# # # #     print("przeszło za open")
# # # #     gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
# # # #     gfile.SetContentFile(file_name)
# # # #     print("przeszło za SetContentFile")
# # # #     gfile.Upload()
# # # #     print("przeszło za Upload")
# # # #     # os.remove(file_name)





# # # # import os
# # # # import requests
# # # # from pydrive.auth import GoogleAuth
# # # # from pydrive.drive import GoogleDrive

# # # # gauth = GoogleAuth(settings_file='settings.yml')
# # # # drive = GoogleDrive(gauth)

# # # # upload_folder = "/"  # Path to the folder you want to upload

# # # # upload_file = []  # List of files to upload

# # # # # Fetch all files from GitHub repository root
# # # # repo_root_url = "https://api.github.com/repos/USERNAME/REPO_NAME/git/trees/main?recursive=1"
# # # # response = requests.get(repo_root_url)
# # # # data = response.json()

# # # # # Make a request to the GitHub API
# # # # response = requests.get("https://api.github.com/repos/Mewwaa/upload_to_drive_test/git/trees/main?recursive=1")

# # # # # Check if the request was successful (status code 200)
# # # # if response.status_code == 200:
# # # #     # Print the JSON response
# # # #     print(response.json())
# # # # else:
# # # #     print("Request failed with status code:", response.status_code)


# # # # for item in data["tree"]:
# # # #     if item["type"] == "blob" and (item["path"].endswith(".txt") or item["path"].endswith(".pdf")):
# # # #         upload_file.append(item["path"])

# # # # # Upload files
# # # # for file_path in upload_file:
# # # #     file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
# # # #     r = requests.get(file_url, allow_redirects=True)
# # # #     file_name = os.path.basename(file_path)
# # # #     open(file_name, 'wb').write(r.content)
# # # #     gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
# # # #     gfile.SetContentFile(file_name)
# # # #     gfile.Upload()
# # # #     os.remove(file_name)


# # # # import requests
# # # # import json
# # # # import os

# # # # # Fetch access token from OAuth endpoint
# # # # def getToken():
# # # #     url = "https://oauth2.googleapis.com/token"
# # # #     payload = {
# # # #         "code": "4%2F0AbUR2VN4vj40ZoCg-Y9Sv5v6sKv2VhxYlq00CDl4uFgJFnnubrphdmOAhJTBro9Bb7caXg",
# # # #         "redirect_uri": "https://developers.google.com/oauthplayground",
# # # #         "client_id": "152312650973-s0vra8sl1uh2b19gvkickc26nm2ng9lg.apps.googleusercontent.com",
# # # #         "client_secret": "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",
# # # #         "scope": "",
# # # #         "grant_type": "authorization_code"
# # # #     }

# # # #     response = requests.post(url, data=payload)
# # # #     response_data = response.json()
# # # #     if 'access_token' in response_data:
# # # #         return response_data['access_token']
# # # #     else:
# # # #         print(response_data)  # Print response for debugging purposes
# # # #         return None

# # # # # Upload a single file to Google Drive using access token
# # # # def uploadFile(file_path):
# # # #     TOKEN_KEY = getToken()
# # # #     if TOKEN_KEY is None:
# # # #         print("Unable to retrieve access token.")
# # # #         return
    
# # # #     headers = {"Authorization": "Bearer " + TOKEN_KEY}
    
# # # #     file_name = os.path.basename(file_path)
# # # #     para = {
# # # #         "name": file_name,  # File name to be uploaded
# # # #         "parents": ["10wd3StRU5zWgARvINrG9Amu09h9L_AhD"]  # Folder ID where files should be uploaded
# # # #     }
# # # #     files = {
# # # #         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
# # # #         'file': open(file_path, "rb")
# # # #     }

# # # #     upload = requests.post(
# # # #         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
# # # #         headers=headers,
# # # #         files=files
# # # #     )
# # # #     print(upload.text)

# # # # # Upload only the files with .txt and .pdf extensions from the root directory of the repository
# # # # def uploadAllFiles():
# # # #     root_dir = os.getcwd()  # Get the current working directory (root directory of the repository)

# # # #     for file_name in os.listdir(root_dir):
# # # #         file_path = os.path.join(root_dir, file_name)
# # # #         if os.path.isfile(file_path):
# # # #             file_extension = os.path.splitext(file_path)[1]
# # # #             if file_extension == ".txt" or file_extension == ".pdf":
# # # #                 uploadFile(file_path)

# # # # if __name__ == '__main__':
# # # #     uploadAllFiles()


