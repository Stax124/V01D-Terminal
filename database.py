import sys
import os
import osBased
from pathlib import Path
from getpass import getpass 
import pickle


def writedata(data,filename,location,mode):
    target = os.path.join(location, filename)
    f = open(target,mode)
    f.write(data)
    f.close()



def RequestUser():
    
    global users
    global passwords
    
    users = GetUsers()
    passwords = GetPasswords()

    logged = False
    
    name = input("Name:  ")
    password = getpass("Password:  ",sys.stderr)

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
    password = getpass("Password:  ",sys.stderr)
    password2 = getpass("Repeat Password:  ",sys.stderr)
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
        writedata(f" {name}","users.txt",__location__,"a")
        writedata(f" {password}","passwords.txt",__location__,"a")
        writedata(f" {permision}","permisions.txt",__location__,"a")
        
        
        if (permision == 1):
            permisions.append(True)
        else:
            permisions.append(False)


def GetUsers():
    path = Path(os.path.join(__location__, "users.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "users.txt"),"r")
        usersComplete = f.readline()
        usersSplit = usersComplete.split()
        users = usersSplit
    else:
        f = open(os.path.join(__location__, "users.txt"),"w+")
        f.write("admin")
        usersComplete = f.readline()
        usersSplit = usersComplete.split()
        users = usersSplit
    
    return users

# ---------------------------------------------------------------------------------------


def GetPasswords():
    path = Path(os.path.join(__location__, "passwords.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "passwords.txt"),"r")
        passwordsComplete = f.readline()
        passwordsSplit = passwordsComplete.split()
        passwords = passwordsSplit
    else:
        f = open(os.path.join(__location__, "passwords.txt"),"w+")
        f.write("admin")
        passwordsComplete = f.readline()
        passwordsSplit = passwordsComplete.split()
        passwords = passwordsSplit
    
    return passwords

 
    
# -----------------------------------------------------------------------------


def GetPermisions():
    path = Path(os.path.join(__location__, "permisions.txt"))

    if path.exists():
        f = open(os.path.join(__location__, "permisions.txt"),"r")
        permisionsComplete = f.readline()
        permisionsSplit = permisionsComplete.split()
        permisions = permisionsSplit
    else:
        f = open(os.path.join(__location__, "permisions.txt"),"w+")
        f.write("True")
        permisionsComplete = f.readline()
        permisionsSplit = permisionsComplete.split()
        permisions = permisionsSplit
    
    return permisions
  
# -----------------------------------------------------------------

def WriteAliases(aliases):
    f = open(os.path.join(__location__, "aliases.pickle"), "wb")
    pickle.dump(aliases,f)
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

# --------------------------------------------------------------------

downloadDict = {
    "eset":"https://download.eset.com/com/eset/tools/installers/live_essp/latest/eset_smart_security_premium_live_installer.exe",
    "afterburner":"http://download.msi.com/uti_exe/vga/MSIAfterburnerSetup.zip",
    "steam":"https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe",
    "vscode":"https://aka.ms/win32-x64-user-stable",
    "discord":"https://discordapp.com/api/download?platform=win",
    "minecraft":"https://launcher.mojang.com/download/MinecraftInstaller.msi",
    "overwolf":"https://download.overwolf.com/install/Download?Channel=web_dl_btn",
    "libreoffice":"https://download.documentfoundation.org/libreoffice/stable/6.4.2/win/x86_64/LibreOffice_6.4.2_Win_x64.msi",
    "bloody6":"http://download.a4tech.com.tw:8080/BloodyMouse/Bloody7_V2020.0213_MUI.exe",
    "keydominator2":"http://download.a4tech.com.tw:8080/BloodyKeyboard/KeyDominator2_V2020.0109_MUI.exe",
    "geforceexperience":"https://uk.download.nvidia.com/GFE/GFEClient/3.20.2.34/GeForce_Experience_v3.20.2.34.exe",
    "gimp":"https://download.gimp.org/mirror/pub/gimp/v2.10/windows/gimp-2.10.18-setup-2.exe",
    "chrome":"https://www.google.com/intl/cs_CZ/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#",
    "firefox":"https://download.mozilla.org/?product=firefox-stub&os=win&lang=cs",
    "operagx":"https://net.geo.opera.com/opera_gx/stable/windows?utm_tryagain=yes&utm_source=google_via_opera_com&utm_medium=ose&utm_campaign=(none)_via_opera_com_https&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&utm_lastpage=opera.com/",
    "orcalevm":"https://download.virtualbox.org/virtualbox/6.1.4/VirtualBox-6.1.4-136177-Win.exe",
    "python":"https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe",
    "winrar":"https://www.rar.cz/files/winrar-x64-580cz.exe",
    "uplay":"http://ubi.li/4vxt9",
    "battlenet":"https://www.battle.net/download/getInstallerForGame?os=win&locale=enUS&version=LIVE&gameProgram=BATTLENET_APP",
    "epicgameslauncher":"https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?productName=unrealtournament",
    "geforcenow":"https://download.nvidia.com/gfnpc/GeForceNOW-release.exe",
    "vlc": "http://get.videolan.org/vlc/3.0.8/win64/vlc-3.0.8-win64.exe",
    "notepad++": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.5/npp.7.8.5.Installer.x64.exe",
    "Malwarebytes": "https://www.malwarebytes.com/mwb-download/thankyou/"
}

# -----------------------------------------

userName = ""
admin = False

users = GetUsers()
    
passwords = GetPasswords()

permisions = GetPermisions()

if __name__ == "__main__":
    import Void
    Void.Run()
