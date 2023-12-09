import requests
from zipfile import ZipFile
import os

#get Iris Dataset
Iris='https://archive.ics.uci.edu/static/public/53/iris.zip'

# check if the "data" and "iris" folder is in the current directory. if not, create it
path = "data/iris"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
# Create a new directory because it does not exist
    os.makedirs(path)


try:
    response_iris = requests.get(Iris)
    with open('data/iris.zip', mode='wb') as f:
        f.write(response_iris.content)
except:
    print("Error! Cannot get Bank Marketing Dataset")

#Compare bank marketing Hashes
import hashlib
filename = 'data/iris.zip'

with open(filename, mode='rb') as f:
    data_iris = f.read()
get_iris_hash = hashlib.sha256(data_iris).hexdigest()
iris_sha256 = 'd11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9'
if iris_sha256 != get_iris_hash:
    print("Computed Iris hash does not match expected hash")
else:
    print("Computed Iris hash matches expected hash")

with ZipFile("data/iris.zip",'r') as zObject:
    zObject.extractall("data/iris")