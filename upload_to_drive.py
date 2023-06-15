import os
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()

# Load credentials from JSON file
gauth.LoadCredentialsFile('credentials_with_secret.json')

if gauth.credentials is None:
    # Authenticate if credentials don't exist
    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:
    # Refresh the access token if it's expired
    gauth.Refresh()

else:
    # Initialize the saved credentials
    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile('credentials_with_secret.json')

drive = GoogleDrive(gauth)

upload_folder = "/"  # Path to the folder you want to upload

upload_file = []  # List of files to upload

url = "https://api.github.com/repos/Mewwaa/upload_to_drive_test/branches/main"
response = requests.get(url)
data = response.json()
tree_url = data["commit"]["commit"]["tree"]["url"]
print(tree_url)
response_tree = requests.get(tree_url)

if response_tree.status_code == 200:
    tree_data = response_tree.json()
    if "tree" in tree_data:
        print("Files found in the repository.")
        for item in tree_data["tree"]:
            if item["type"] == "blob":
                upload_file.append(item["path"])
                print("Files found here too.")
    else:
        print("No files found in the repository.")
else:
    print("Failed to retrieve tree data.")

# Upload files
for file_path in upload_file:
    file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
    r = requests.get(file_url, allow_redirects=True)
    file_name = os.path.basename(file_path)
    open(file_name, 'wb').write(r.content)
    gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
    gfile.SetContentFile(file_name)
    gfile.Upload()
    os.remove(file_name)





# import os
# import requests
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth(settings_file='settings.yml')
# drive = GoogleDrive(gauth)

# upload_folder = "/"  # Path to the folder you want to upload

# upload_file = []  # List of files to upload

# # Fetch all files from GitHub repository root
# repo_root_url = "https://api.github.com/repos/USERNAME/REPO_NAME/git/trees/main?recursive=1"
# response = requests.get(repo_root_url)
# data = response.json()

# # Make a request to the GitHub API
# response = requests.get("https://api.github.com/repos/Mewwaa/upload_to_drive_test/git/trees/main?recursive=1")

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Print the JSON response
#     print(response.json())
# else:
#     print("Request failed with status code:", response.status_code)


# for item in data["tree"]:
#     if item["type"] == "blob" and (item["path"].endswith(".txt") or item["path"].endswith(".pdf")):
#         upload_file.append(item["path"])

# # Upload files
# for file_path in upload_file:
#     file_url = f"https://raw.githubusercontent.com/Mewwaa/upload_to_drive_test/main/{file_path}"
#     r = requests.get(file_url, allow_redirects=True)
#     file_name = os.path.basename(file_path)
#     open(file_name, 'wb').write(r.content)
#     gfile = drive.CreateFile({'parents': [{"id": "10wd3StRU5zWgARvINrG9Amu09h9L_AhD"}]})
#     gfile.SetContentFile(file_name)
#     gfile.Upload()
#     os.remove(file_name)


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


