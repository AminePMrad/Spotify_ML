import requests

# Replace these values with your Zenodo dataset URL and file name
zenodo_url = 'https://zenodo.org/records/10253415'
file_name = 'Spotify_Youtube.csv'

# Zenodo API base URL
api_base_url = 'https://zenodo.org/api/records/'

# Extracting record ID from the provided Zenodo URL
record_id = zenodo_url.split('/')[-1]

# Constructing the API endpoint URL for the specified record ID
api_url = f'{api_base_url}{record_id}'

# Fetching the metadata information from Zenodo
response = requests.get(api_url)
data = response.json()

# Extracting the download URL for the specified file
file_url = data['files'][0]['links']['self']

# Downloading the file
response = requests.get(file_url)

# Saving the file locally
with open(file_name, 'wb') as file:
    file.write(response.content)

print(f'Dataset downloaded successfully as {file_name}')
