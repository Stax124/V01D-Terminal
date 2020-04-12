import requests
import database
from clint.textui import progress

def Download(target):
    url = ""
    urlSplit = ""

    try:
        url = database.downloadDict.get(target)
        urlSplit = url.split("/")
    except:
        try:
            url = target
            urlSplit = url.split("/")
        except:
            print("Target is not availible")

    

    f = requests.get(url, stream=True)

    with open(urlSplit[-1], "wb") as _target:

        total_length = int(f.headers.get('content-length'))

        print(str(total_length / 1000000) + " MB")

        for ch in progress.bar(f.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):

            if ch:
                _target.write(ch)

if __name__ == "__main__":
    import Void
    Void.Run()