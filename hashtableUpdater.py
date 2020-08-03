import os
import hashlib
import yaml

def hashfilesum(_file,hashalg) -> None:
    try:
        with open(_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hashalg.update(chunk)
    except:
        print(f"{_file} is not accessible")

def hash(item):
    hashsum = hashlib.sha1()
    hashfilesum(item,hashsum)
    return hashsum.hexdigest()

dictionary = dict()

for i in os.listdir():
    dictionary[i] = hash(i)

yaml.safe_dump(dictionary,open("hashtable-server.yml","w"))
print("done")