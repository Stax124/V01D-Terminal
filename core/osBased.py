import os
import platform

def Clear() -> None:
    "Clears the console"
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def Os() -> str:
    "Returs current platform"
    if platform.system() == "Windows":
        return "Windows"
    elif platform.system() == "Linux":
        return "Linux"
    else:
        return "Other"


if __name__ == "__main__":
    import Void
    Void.Run()