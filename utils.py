import requests
import database
from clint.textui import progress


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return a


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


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
