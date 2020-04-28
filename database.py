import sys
import os
import osBased
from pathlib import Path
import pickle
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def writedata(data,filename,location,mode):
    target = os.path.join(location, filename)
    f = open(target,mode)
    f.write(data)
    f.close()

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

completer = WordCompleter(
    [
        "cls",
        "clear",
        "void",
        "read",
        "power",
        "password",
        "sin",
        "cos",
        "pagefile",
        "motherboard",
        "ram",
        "cpu",
        "gpu",
        "component",
        "firewall",
        "services",
        "manager",
        "event",
        "color",
        "help",
        "ping",
        "os",
        "read",
        "pwned",
        "cd",
        "exit",
        "quit",
        "alias",
        "delalias",
        "aliases",
        "+",
        "-",
        "*",
        "/",
        "**",
        "//",
        "root",
        "cos",
        "sin",
        "!",
        "%",
        "tan",
        "ln",
        "download",
    ],
    ignore_case=True,
)

# -----------------------------------------

if __name__ == "__main__":
    import Void
    Void.Run()
