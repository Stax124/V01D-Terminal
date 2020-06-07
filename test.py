import urllib.request
import sys
import io

try:
    url = sys.argv[1]
except IndexError:
    print("usage: test.py url")
    exit(2)

resp = urllib.request.urlopen(url)
length = resp.getheader('content-length')
if length:
    length = int(length)
    blocksize = max(4096, length//100)
else:
    blocksize = 1000000  # just made something up

print(length, blocksize)

buf = io.BytesIO()
size = 0
while True:
    buf1 = resp.read(blocksize)
    if not buf1:
        break
    buf.write(buf1)
    size += len(buf1)
    if length:
        print('{:.2f}\r done'.format(size/length), end='')
print()
