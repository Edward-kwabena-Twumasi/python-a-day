def download_from_online(url,destination):
    import urllib.request 
    import pathlib as path
    import os

    dest = path.Path(destination)
    
    print(dest)
    base = dest.parent   
    os.makedirs(base,exist_ok=True)

    output = urllib.request.urlretrieve(url, destination)
    return output

url = "https://storage.googleapis.com/download.tensorflow.org/data/palmer_penguins/penguins.csv"
filename = "penguins.csv"

print(download_from_online(url,filename))