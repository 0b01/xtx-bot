import requests, zipfile, io

zip_file_url = 'https://storage.googleapis.com/xtx-public-assets/data-training.csv.zip'

def download_data(zip_file_url):   
    r = requests.get(zip_file_url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    return
