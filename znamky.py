import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

marks = [3,1,1,1,1]
weights = [0.8,0.8,0.5,0.5,0.5]
_sumM = 0
_sumW = 0.0

for i in range(0,marks.__len__()):
    _sumM += marks[i] * weights[i]

for i in range(0,weights.__len__()):
    _sumW += weights[i]

print(f"{color.YELLOW}_sumM: {_sumM}")
print(f"_sumW: {_sumW}")

print(f"output: {_sumM / _sumW} {color.END}")

os.system("pause")