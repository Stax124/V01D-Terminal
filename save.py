import sys
import os
import osBased
from pathlib import Path
from getpass import getpass
import pickle


def writedata(data, filename, location, mode):
    target = os.path.join(location, filename)
    f = open(target, mode)
    f.write(data)
    f.close()


def RequestUser():

    global users
    global passwords

    users = GetUsers()
    passwords = GetPasswords()

    logged = False

    name = input("Name:  ")
    password = getpass("Password:  ", sys.stderr)

    if name in users:
        index = -1
        i = 0

        # Check for valid name in users list and get his index
        while i < users.__len__():
            if name == users[i]:
                index = i
            i += 1

        if index == -1:
            logged = False
        if index != -1:
            global userName
            global admin

            if name != "guest":
                # Check if entered password is correct
                if password == passwords[index]:
                    logged = True
                    admin = permisions[index]
                    userName = name

                    osBased.Clear()

                else:
                    print("\n\n Incorrect password or name")
            else:
                logged = True
                admin = False
                userName = name

    return logged


def RegisterUser():
    name = input("Name:  ")
    password = getpass("Password:  ", sys.stderr)
    password2 = getpass("Repeat Password:  ", sys.stderr)
    permision = int(input("Give permisions (0 or 1):  "))

    if password != password2 and (permision == 0 or permision == 1):
        print("Incorrect password \n")
        RegisterUser()
    else:
        if (permision == 0):
            permision = False
        elif (permision == 1):
            permision = True

        users.append(name)
        passwords.append(password)
        permisions.append(permision)
        writedata(f" {name}", "users.txt", __location__, "a")
        writedata(f" {password}", "passwords.txt", __location__, "a")
        writedata(f" {permision}", "permisions.txt", __location__, "a")

        if (permision == 1):
            permisions.append(True)
        else:
            permisions.append(False)


def GetUsers():
    path = Path(os.path.join(__location__, "users.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "users.txt"), "r")
        usersComplete = f.readline()
        usersSplit = usersComplete.split()
        users = usersSplit
    else:
        f = open(os.path.join(__location__, "users.txt"), "w+")
        f.write("admin")
        usersComplete = f.readline()
        usersSplit = usersComplete.split()
        users = usersSplit

    return users

# ---------------------------------------------------------------------------------------


def GetPasswords():
    path = Path(os.path.join(__location__, "passwords.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "passwords.txt"), "r")
        passwordsComplete = f.readline()
        passwordsSplit = passwordsComplete.split()
        passwords = passwordsSplit
    else:
        f = open(os.path.join(__location__, "passwords.txt"), "w+")
        f.write("admin")
        passwordsComplete = f.readline()
        passwordsSplit = passwordsComplete.split()
        passwords = passwordsSplit

    return passwords


# -----------------------------------------------------------------------------


def GetPermisions():
    path = Path(os.path.join(__location__, "permisions.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "permisions.txt"), "r")
        permisionsComplete = f.readline()
        permisionsSplit = permisionsComplete.split()
        permisions = permisionsSplit
    else:
        f = open(os.path.join(__location__, "permisions.txt"), "w+")
        f.write("True")
        permisionsComplete = f.readline()
        permisionsSplit = permisionsComplete.split()
        permisions = permisionsSplit

    return permisions

# -----------------------------------------------------------------


def WriteAliases(aliases):
    f = open(os.path.join(__location__, "aliases.pickle"), "wb")
    pickle.dump(aliases, f)
    f.close()


def GetAliases():
    path = Path(os.path.join(__location__, "aliases.pickle"))

    if path.exists():
        f = open(os.path.join(__location__, "aliases.pickle"), "rb")
        aliases = pickle.load(f)
        return aliases
    else:
        return {}


# --------------------------------------------------------------------

def getcolor():
    path = Path(os.path.join(__location__, "color.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "color.txt"), "r")
        color = f.read()
        return color
    else:
        return "a"

# --------------------------------------------------------------------


def RequestName():
    if userName != "":
        return userName
    else:
        return "developer"


def RequestPermisions():
    from Void import developer
    if developer == True:
        return True
    else:
        return admin


# --------------------------------------------------------------------


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


userName = ""
admin = False

users = GetUsers()

passwords = GetPasswords()

permisions = GetPermisions()

if __name__ == "__main__":
    import Void
    Void.main()
