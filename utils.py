import requests
import sys
import database
import os
from clint.textui import progress


def gcd(a, b) -> float:
    "Returs greatest common dividor"
    if b > a:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return float(a)


def lcm(x, y) -> float:
    "Returs lowest common multiple"
    greater = 0
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return float(lcm)

def PlainToString(text, mode) -> str:
    "Returns list of strings from plain text file (hello world -> 'hello','world')"

    split = ""

    if mode == "line":
        split = text.splitlines()
    elif mode == "file":
        try:
            f = open(text, "r")
            text = f.read()
            split = text.split()
        except:
            print("File not found")
    else:
        split = text.split()

    out = ""

    for item in split:
        out += "'" + item + "'" + ","

    return(out)

def Download(target) -> None:
    try:
        url = database.downloadDict.get(target)
        urlSplit = url.split("/")
    except:
        try:
            url = target
            urlSplit = url.split("/")
        except:
            print("Target is not availible")

    try:
        file_name = urlSplit[-1]
        with open(file_name, "wb") as f:
            print("Downloading %s" % file_name)
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                    f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                    sys.stdout.flush()
        print()
            
    except Exception as e:
        print(e)
        os.system("start "+ url)

if __name__ == "__main__":
    import Void
    Void.main()
