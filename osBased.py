import os
import platform

def Clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def Os():
    if platform.system() == "Windows":
        print("Windows")
    elif platform.system() == "Linux":
        print("Linux")
    else:
        print("Other")


if __name__ == "__main__":
    import Void
    Void.Run()