from prompt_toolkit.document import Document
from prompt_toolkit.completion import CompleteEvent, Completer, Completion, merge_completers
from typing import Callable, Iterable, List, Optional
import sys
import os
import osBased
from pathlib import Path
import pickle
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter, NestedCompleter


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
    "Malwarebytes": "https://www.malwarebytes.com/mwb-download/thankyou/",
    "audacity": "https://www.fosshub.com/Audacity.html?dwl=audacity-win-2.3.3.exe",
    "tor": "https://www.torproject.org/dist/torbrowser/9.0.9/torbrowser-install-win64-9.0.9_en-US.exe",
    "anaconda": "https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe"
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
        "!",
        "%",
        "tan",
        "ln",
        "download",
        "assoc",
        "attrib",
        "break",
        "bcdedit",
        "cacls",
        "call",
        "chcp",
        "chdir",
        "chkdsk",
        "chkntfs",
        "cmd",
        "comp",
        "compact",
        "convert",
        "copy",
        "date",
        "del",
        "dir",
        "diskpart",
        "doskey",
        "driverquery",
        "echo",
        "endlocal",
        "erase",
        "fc",
        "find",
        "findstr",
        "for",
        "format",
        "fsutil",
        "ftype",
        "goto",
        "gpresult",
        "graftabl",
        "icacls",
        "if",
        "label",
        "md",
        "mkdir",
        "mklink",
        "mode",
        "more",
        "move",
        "openfiles",
        "path",
        "pause",
        "popd",
        "print",
        "prompt",
        "pushd",
        "rd",
        "recover",
        "rem",
        "ren",
        "rename",
        "replace",
        "rmdir",
        "robocopy",
        "set",
        "setlocal",
        "sc",
        "schtasks",
        "shift",
        "shutdown",
        "sort",
        "start",
        "subst",
        "systeminfo",
        "tasklist",
        "taskkill",
        "time",
        "title",
        "tree",
        "type",
        "ver",
        "verify",
        "vol",
        "xcopy",
        "wmic",
        "/?",
        "startup",
        "calc",
        "cfgwiz32",
        "charmap",
        "chkdisk",
        "cleanmgr",
        "clipbrd",
        "dcomcnfg",
        "control",
        "debug",
        "defrag",
        "drwatson",
        "dxdiag",
        "explorer",
        "fontview",
        "hostname",
        "ipconfig",
        "jview",
        "mmc",
        "msconfig",
        "msinfo32",
        "nbtstat",
        "netstat",
        "nslookup",
        "odbcad32",
        "regedit",
        "regsvr32",
        "regwiz",
        "sfc /scannow",
        "sndrec32",
        "sndvol32",
        "sysedit",
        "systeminfo",
        "taskmgr",
        "telnet",
        "tskill",
        "tracert",
        "winchat",
        "winipcfg",
        "winword",
        "excel",
        "powerpnt",
        "msaccess",
        "outlook",
        "ois",
        "winproj",
        "certmgr.msc",
        "ciadv.msc",
        "compmgmt.msc",
        "devmgmt.msc",
        "dfrg.msc",
        "diskmgmt.msc",
        "fsmgmt.msc",
        "eventvwr.msc",
        "gpedit.msc",
        "iis.msc",
        "lusrmgr.msc",
        "mscorcfg.msc",
        "ntmsmgr.msc",
        "perfmon.msc",
        "secpol.msc",
        "services.msc",
        "wmimgmt.msc",
        "access.cpl",
        "hdwwiz.cpl",
        "appwiz.cpl",
        "timedate.cpl",
        "desk.cpl",
        "inetcpl.cpl",
        "joy.cpl",
        "main.cpl keyboard",
        "main.cpl",
        "ncpa.cpl",
        "ncpl.cpl",
        "telephon.cpl",
        "powercfg.cpl",
        "intl.cpl",
        "mmsys.cpl sounds",
        "mmsys.cpl",
        "sysdm.cpl",
        "nusrmgr.cpl",
        "firewall.cpl",
        "wscui.cpl",
        "wupdmgr",
        "settings",
        "temp",
        "powershell",
        "%APPDATA%",
        "%ALLUSERSPROFILE%",
        "%CommonProgramFiles%",
        "%CommonProgramFiles(x86)%",
        "%CommonProgramW6432%",
        "%COMPUTERNAME%",
        "%ComSpec%",
        "%DriverData%",
        "%HOMEDRIVE%",
        "%HOMEPATH%",
        "%LOCALAPPDATA%",
        "%LOGONSERVER%",
        "%NUMBER_OF_PROCESSORS%",
        "%OneDrive%",
        "%OneDriveConsumer%",
        "%OS%",
        "%Path%",
        "%PATHEXT%",
        "%PROCESSOR_ARCHITECTURE%",
        "%PROCESSOR_IDENTIFIER%",
        "%PROCESSOR_LEVEL%",
        "%PROCESSOR_REVISION%",
        "%ProgramData%",
        "%ProgramFiles%",
        "%ProgramFiles(x86)%",
        "%ProgramW6432%",
        "%PROMPT%",
        "%PSModulePath%",
        "%PUBLIC%",
        "%SESSIONNAME%",
        "%SystemDrive%",
        "%SystemRoot%",
        "%SystemRoot%",
        "%TEMP%",
        "%TMP%",
        "%USERDOMAIN%",
        "%USERDOMAIN_ROAMINGPROFILE%",
        "%USERNAME%",
        "%USERPROFILE%",
        "%windir%",
    ],
    ignore_case=True,
    match_middle=True
)

nestedCompleter = NestedCompleter.from_nested_dict(
    {
        "help": {"/?": None},
        "cls": {"/?": None},
        "clear": None,
        "void":None,
        "read": None,
        "power": None,
        "password": None,
        "sin": None,
        "cos": None,
        "pagefile": None,
        "motherboard": None,
        "ram": None,
        "cpu": None,
        "gpu": None,
        "component": None,
        "firewall": None,
        "services": None,
        "manager": None,
        "event": None,
        "color": {"/?": None, "0": None, "1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "7": None, "8": None, "9": None, "a": None, "b": None, "c": None, "d": None, "e": None, "f": None},
        "ping": {"/?": None, "-t": None, "-a": None, "-n": None, "-l": None, "-f": None, "-i": None, "-v": None, "-r": None, "-s": None, "-j": None, "-k": None, "-w": None, "-R": None, "-S": None, "-C": None, "-p": None, "-4": None, "-6": None},
        "os":None,
        "pwned":None,
        "cd":{"/?":None},
        "exit": {"/?": None, "/B": None},
        "quit":None,
        "alias":None,
        "delalias": None,
        "+": None,
        "-": None,
        "*": None,
        "/": None,
        "**": None,
        "//": None,
        "root": None,
        "!": None,
        "%": None,
        "tan": None,
        "ln": None,
        "download": {"-list":None},
        "assoc": {"/?": None},
        "attrib": {"-list": None, "+": None, "-": None, "R": None, "A": None, "S": None,"H": None,"O": None,"I": None,"X": None,"V": None,"P": None,"U": None,"B": None,"/S": None,"/D": None,"/L": None},
        "break":{"/?":None},
        "bcdedit": {"/?": None, "/store": None, "/store": None, "/createstore": None, "/export": None, "/store": None, "/import": None, "/store": None, "/sysstore": None, "/copy": None, "/create": None, "/delete": None, "/mirror": None, "/deletevalue": None, "/set": None, "/enum": None, "/v": None, "/bootsequence": None, "/default": None, "/displayorder": None, "/store": None, "/timeout": None, "/toolsdisplayorder": None, "/bootems": None, "/ems": None, "/emssettings": None, "/bootdebug": None, "/debug": None, "/dbgsettings": None, "/hypervisorsettings": None, "/eventsettings": None, "/event": None},
        "cacls": {"/?": None, "/T": None, "/L":None,"/M":None,"/S":None,"/S:SDDL":None,"/E":None,"/C":None,"/G":None,"/R":None,"/P":None,"/D":None},
        "call":{"/?":None},
        "chcp":{"/?":None},
        "chdir": {"/?": None},
        "chkdsk": {"/?": None, "/F": None, "/V": None, "/R": None, "/L": None, "/X": None, "/I": None, "/C": None, "/B": None, "/scan": None, "/forceofflinefix": None, "/perf": None, "/spotfix": None, "/sdcleanup": None, "/offlinescanandfix": None, "/freeorphanedchains": None, "/markclean": None},
        "chkntfs": {"/?": None,"/D": None,"/T": None,"/X": None,"/C": None,},
        "cmd": {"/?": None, "/C": None, "/K": None, "/S": None, "/Q": None,  "/D": None, "/A": None, "/U": None, "/T": None, "/E": None, "/F": None, "/V": None},
        "comp": {"/?": None, "/D": None, "/A": None, "/L": None, "/N": None, "/C": None, "/OFF": None, "/M": None},
        "compact": {"/?": None, "/C": None, "/U": None, "/S": None, "/A": None, "/I": None, "/F": None, "/Q": None, "/EXE": None, "/CompactOs": None, "/WinDir": None},
        "convert": {"/?": None, "/V": None, "/X": None, "/NoSecurity": None},
        "copy": {"/?": None, "/A": None, "/B": None, "/D": None, "/V": None, "/N": None, "/Y": None, "/Z": None, "/L": None},
        "date": {"/?": None, "/T": None},
        "del": {"/?": None, "/P": None, "/F": None, "/S": None, "/Q": None, "/A": None},
        "dir": {"/?": None, "/A": None, "/B": None, "/C": None, "/D": None, "/L": None, "/N": None, "/O": None, "/P": None, "/Q": None, "/R": None, "/S": None, "/T": None, "/W": None, "/X": None, "/Y": None,"/4": None},
        "diskpart":None,
        "doskey": {"/?": None, "/REINSTALL": None, "/LISTSIZE": None, "/MACROS": None, "/HISTORY": None, "/INSERT": None, "/OVERSTRIKE": None, "/EXENAME": None, "/MACROFILE": None},
        "driverquery": {"/?": None, "/S": None, "/U": None, "/P": None, "/FO": None, "/NH": None, "/SI": None, "/V": None},
        "echo": {"/?": None},
        "endlocal": {"/?": None},
        "erase": {"/?": None, "/P": None, "/F": None, "/S": None, "/Q": None, "/A": None},
        "fc": {"/?": None, "/A": None, "/B": None, "/C": None, "/L": None, "/Lbn": None, "/N": None, "/OFF": None, "/T": None, "/U": None, "/W": None},
        "find": {"/?": None, "/V": None, "/C": None, "/N": None, "/I": None, "/OFF": None},
        "findstr": {"/?": None},
        "for": {"/?": None, "/D": None, "/R": None, "/L": None, "/F": None},
        "format": {"/?": None, "/FS": None, "/V": None, "/Q": None, "/C": None, "/X": None, "/R": None, "/D": None, "/L": None, "/A": None, "/F": None, "/T": None, "/N": None, "/P": None, "/S": None, "/TXF": None, "/I": None, "/DAX": None, "/LogSize": None, "/NoRepairLogs": None},
        "fsutil": {"/?": None, "8dot3name": None, "behavior": None, "dax": None, "dirty": None, "file": None, "fsInfo": None, "hardlink": None, "objectID": None, "quota": None, "repair": None, "reparsePoint": None, "resource": None, "sparse": None, "tiering": None, "transaction": None, "usn": None, "volume": None, "wim": None},
        "ftype": {"/?": None},
        "goto": {"/?": None},
        "gpresult": {"/?": None, "/S": None, "/U": None, "/P": None, "/SCOPE": None, "/USER": None, "/R": None, "/V": None, "/Z": None},
        "graftabl": None,
        "icacls": {"/?": None, "/save": None, "/setowner": None, "/findsid": None, "/verify": None, "/reset": None, "/grant": None, "/deny": None, "/remove": None, "/setintegritylevel": None, "/inheritance": None, "/T": None, "/C": None, "/L": None, "/Q": None},
        "if": {"/?": None},
        "label": {"/?": None,"/MP":None},
        "md": {"/?": None},
        "mkdir": {"/?": None},
        "mklink": {"/?": None, "/D": None, "/H": None, "/J": None},
        "mode": {"/?": None},
        "more": {"/?": None, "/E": None, "/C": None, "/P": None, "/S": None, "/Tn": None},
        "mode": {"/?": None, "/Y":None},
        "openfiles": {"/?": None, "/Disconnect": None, "/Query": None, "/Local": None},
        "path": {"/?": None},
        "pause": {"/?": None},
        "popd": {"/?": None},
        "print": {"/?": None, "/D":None},
        "prompt": {"/?": None},
        "pushd": {"/?": None},
        "rd": {"/?": None, "/S": None,"/Q": None},
        "recover": {"/?": None},
        "rem": {"/?": None},
        "ren": {"/?": None},
        "rename": {"/?": None},
        "replace": {"/?": None, "/A": None, "/P": None, "/R": None, "/S": None, "/W": None, "/U": None},
        "rmdir": {"/?": None, "/S": None, "/Q": None},
        "robocopy": {"/?": None, "/S": None, "/E": None, "/LEV": None, "/Z": None, "/B": None, "/ZB": None, "/J": None, "/EFSRAW": None, "/COPY": None, "/SEC": None, "/COPYALL": None, "/NOCOPY": None, "/SECFIX": None, "/TIMFIX": None, "/PURGE": None, "/MIR": None, "/MOV": None, "/MOVE": None, "/A+": None, "/A-": None, "/CREATE": None, "/FAT": None, "/256": None, "/MON": None, "/MOT": None, "/RH": None, "/IPG": None, "/SL": None, "/MT": None, "/DCOPY": None, "/NODCOPY": None, "/NOOFFLOAD": None, "/A": None, "/M": None, "/IA": None, "/XA": None, "/XF": None, "/XD": None, "/XC": None, "/XN": None, "/XO": None, "/XX": None, "/XL": None, "/IS": None, "/IT": None, "/MAX": None, "/MIN": None, "/MAXAGE": None, "/MINAGE": None, "/MAXLAD": None, "/MINLAD": None, "/XJ": None, "/FFT": None, "/DST": None, "/XJD": None, "/XJF": None, "/R": None, "/W": None, "/REG": None, "/TBD": None, "/L": None, "/X": None, "/V": None, "/TS": None, "/FP": None, "/BYTES": None, "/NS": None, "/NC": None, "/NFL": None, "/NDL": None, "/NP": None, "/ETA": None, "/LOG": None, "/LOG+": None, "/UNILOG": None, "/UNILOG+": None, "/TEE": None, "/NJH": None, "/NJS": None, "/UNICODE": None, "/JOB": None, "/SAVE": None, "/QUIT": None, "/NOSD": None, "/NODD": None, "/IF": None},
        "set": {"/?": None, "/A": None, "/P": None, "%CD%": None, "%DATE%": None, "%TIME%": None, "%RANDOM%": None, "%ERRORLEVEL%": None, "%CMDEXTVERSION%": None, "%CMDCMDLINE%": None, "%HIGHESTNUMANODENUMBER%": None},
        "setlocal": {"/?": None},
        "sc": {"/?": None, "query": None, "queryex": None, "start": None, "pause": None, "interrogate": None, "continue": None, "stop": None, "config": None, "description": None, "failiture": None, "failitureflag": None, "sidtype": None, "privs": None, "managedaccount": None, "qc": None, "qdescription": None, "qfailiture": None, "qfailitureflag": None, "qsidtype": None, "qprivs": None, "qtriggerinfo": None, "qpreferrednode": None, "qmanagedaccount": None, "qprotection": None, "quserservice": None, "delete": None, "create": None, "control": None, "sdshow": None, "sdset": None, "showsid": None, "triggerinfo": None, "preferrednode": None, "GetDisplayName": None, "GetKeyName": None, "EnumDepend": None, "boot": None, "Lock": None, "QueryLock": None},
        "schtasks": {"/?": None, "/Create": None,"/Delete": None,"/Query": None,"/Change": None,"/Run": None,"/End": None,"/ShowSid": None},
        "shift": {"/?": None, "/n":None},
        "shutdown": {"/?": None, "/i": None, "/l": None, "/s": None, "/sg": None, "/r": None, "/g": None, "/a": None, "/p": None, "/h": None, "/hybrid": None, "/fw": None, "/e": None, "/o": None, "/m": None, "/t": None, "/c": None, "/f": None, "/d": None},
        "sort": {"/?": None, "/+n": None, "/L": None, "/M": None, "/REC": None, "/O": None, "/R": None, "/T": None},
        "start": {"/?": None, "/D": None, "/I": None, "/MIN": None, "/MAX": None, "/SEPARATE": None, "/SHARED": None, "/LOW": None, "/NORMAL": None, "/HIGH": None, "/REALTIME": None, "/ABOVENORMAL": None, "/BELOWNORMAL": None, "/NODE": None, "/AFFINITY": None, "/WAIT": None, "/B": None},
        "subst": {"/?": None, "/D": None},
        "systeminfo": {"/?": None, "/S": None, "/U": None, "/P": None, "/FO": None, "/NH": None},
        "tasklist": {"/?": None, "/S": None, "/U": None, "/P": None, "/M": None, "/SVC": None, "/S": None, "/S": None},
        "taskkill": {"/?": None, "/S": None, "/U": None, "/P": None, "/FI": None, "/PID": None, "/IM": None, "/T": None, "/F": None},
        "time": {"/?": None, "/T": None},
        "title": {"/?": None},
        "tree": {"/?": None, "/F": None, "/A": None},
        "type": {"/?": None},
        "ver": {"/?": None},
        "verify": {"/?": None},
        "vol": {"/?": None},
        "xcopy": {"/?": None, "/A": None, "/M": None, "/D": None, "/EXCLUDE": None, "/P": None, "/S": None, "/E": None, "/V": None, "/W": None, "/C": None, "/I": None, "/Q": None, "/F": None, "/L": None, "/G": None, "/H": None, "/R": None, "/T": None, "/U": None, "/K": None, "/N": None, "/O": None, "/X": None, "/Y": None, "/-Y": None, "/Z": None, "/B": None, "/J": None},
        "wmic": {"/?": None, "/NAMESPACE": None, "/ROLE": None, "/NODE": None, "/IMPLEMENT": None, "/AUTHLEVEL": None, "/LOCALE": None, "/PRIVILIGES": None, "/TRACE": None, "/RECORD": None, "/INTERACTIVE": None, "/FAILFAST": None, "/USER": None, "/PASSWORD": None, "/OUTPUT": None, "/APPEND": None, "/AGGREGATE": None, "/AUTHORITY": None, "ALIAS": None, "BASEBOARD": None, "BIOS": None, "BOOTCONFIG": None, "CDROM": None, "COMPUTERSYSTEM": None, "CPU": None, "CSPRODUCT": None, "DATAFILE": None, "DCOMAPP": None, "DESKTOP": None, "DESKTOPMONITOR": None, "DEVICEMEMORYADDRESS": None, "DISKDRIVE": None, "DISKQUOTA": None, "DMACHANNEL": None, "ENVIROMENT": None, "FSDIR": None, "GROUP": None, "IDECONTROLLER": None, "IRQ": None, "JOB": None, "LOADORDER": None, "LOGICALDISK": None, "LOGON": None, "MEMCACHE": None, "MEMORYCHIP": None, "MEMPHYSICAL": None, "NETCLIENT": None, "NETLOGIN": None, "NETPROTOCOL": None, "NETUSE": None, "NIC": None, "NICCONFIG": None, "NTDOMAIN": None, "NTEVENT": None, "NTEVENTLOG": None, "ONBOARDDEVICE": None, "OS": None, "PAGEFILE": None, "PAGEFILESET": None, "PARTITION": None, "PORT": None, "PORTCONNECTOR": None, "PRINTER": None, "PRINTERCONFIG": None, "PRINTJOB": None, "PROCESS": None, "PRODUCT": None, "QFE": None, "QUOTASETTING": None, "RDACCOUNT": None, "RDNIC": None, "RDPERMISSIONS": None, "RDTOGGLE": None, "RECOVEROS": None, "REGISTRY": None, "SCSICONTROLLER": None, "SERVER": None, "SERVICE": None, "SHADOWCOPY": None, "SHADOWSTORAGE": None, "SHARE": None, "SOFTWAREELEMENT": None, "SOFTWAREFEATURE": None, "SOUNDDEV": None, "STARTUP": None, "SYSACCOUNT": None, "SYSDRIVER": None, "SYSTEMENCLOSURE": None, "SYSTEMSLOT": None, "TAPEDRIVE": None, "TEMPERATURE": None, "TIMEZONE": None, "UPS": None, "USERACCOUNT": None, "VOLTAGE": None, "VOLUME": None, "VOLUMEQUOTASETTING": None, "VOLUMEUSERQUOTA": None, "WMISET": None},
    }
)


__all__ = [
    "PathCompleter",
    "ExecutableCompleter",
]


class PathCompleter(Completer):
    """
    Complete for Path variables.
    :param get_paths: Callable which returns a list of directories to look into
                      when the user enters a relative path.
    :param file_filter: Callable which takes a filename and returns whether
                        this file should show up in the completion. ``None``
                        when no filtering has to be done.
    :param min_input_len: Don't do autocompletion when the input string is shorter.
    """

    def __init__(
        self,
        only_directories: bool = False,
        get_paths: Optional[Callable[[], List[str]]] = None,
        file_filter: Optional[Callable[[str], bool]] = None,
        min_input_len: int = 0,
        expanduser: bool = False,
    ) -> None:

        self.only_directories = only_directories
        self.get_paths = get_paths or (lambda: ["."])
        self.file_filter = file_filter or (lambda _: True)
        self.min_input_len = min_input_len
        self.expanduser = expanduser

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor

        # Complete only when we have at least the minimal input length,
        # otherwise, we can too many results and autocompletion will become too
        # heavy.
        if len(text) < self.min_input_len:
            return

        try:
            # Do tilde expansion.
            if self.expanduser:
                text = os.path.expanduser(text)

            # Directories where to look.
            dirname = os.path.dirname(text)
            if dirname:
                directories = [
                    os.path.dirname(os.path.join(p, text)) for p in self.get_paths()
                ]
            else:
                directories = self.get_paths()

            # Start of current file.
            prefix = os.path.basename(text)

            # Get all filenames.
            filenames = []
            for directory in directories:
                # Look for matches in this directory.
                if os.path.isdir(directory):
                    for filename in os.listdir(directory):
                        if filename.startswith(prefix):
                            filenames.append((directory, filename))

            # Sort
            filenames = sorted(filenames, key=lambda k: k[1])

            # Yield them.
            for directory, filename in filenames:
                completion = filename[len(prefix):]
                full_name = os.path.join(directory, filename)

                if os.path.isdir(full_name):
                    # For directories, add a slash to the filename.
                    # (We don't add them to the `completion`. Users can type it
                    # to trigger the autocompletion themselves.)
                    filename += "/"
                elif self.only_directories:
                    continue

                if not self.file_filter(full_name):
                    continue

                yield Completion(completion, 0, display=filename)
        except OSError:
            pass


class ExecutableCompleter(PathCompleter):
    """
    Complete only executable files in the current path.
    """

    def __init__(self) -> None:
        super().__init__(
            only_directories=False,
            min_input_len=1,
            get_paths=lambda: os.environ.get("PATH", "").split(os.pathsep),
            file_filter=lambda name: os.access(name, os.X_OK),
            expanduser=True,
        ),

# ----------------------------------------------------------------------------

combinedcompleter = merge_completers([nestedCompleter,ExecutableCompleter])

if __name__ == "__main__":
    import Void
    Void.main()
