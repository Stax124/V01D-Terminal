import urllib.request
import database
import os
from clint.textui import progress


def gcd(a, b) -> float:
    if b > a:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return float(a)


def lcm(x, y) -> float:
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

def PlainToString(text, mode):
    

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
        urllib.request.urlretrieve(url, urlSplit[-1])
    except Exception as e:
        print(e)
        os.system("start "+ url)

if __name__ == "__main__":
    import Void
    Void.main()
