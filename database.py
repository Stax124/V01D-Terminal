from prompt_toolkit.completion import WordCompleter, NestedCompleter
from typing import Callable, Iterable, List, Optional
import os
import pickle
import utils
import yaml
import platform
from pathlib import Path

def writedata(data, filename, location, mode) -> None:
    target = os.path.join(location, filename)
    f = open(target,mode)
    f.write(data)
    f.close()

# -----------------------------------------------------------------

def WriteAliases(aliases) -> list:
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

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# --------------------------------------------------------------------

if platform.system() == "Windows":
    WinCompleter = NestedCompleter.from_nested_dict(
    {
        "refreshenv":None,
        "ytdown":None,
        "downloadeta":None,
        "brightness":None,
        "plain2string": {"line":None,"file":None,"fileline":None},
        "cryptocurrency":{"btc":None,"eth":None,"xrp":None,"usdt":None,"bch":None,"ltc":None,"ada":None,"bnb":None},
        "eval": None,
        "sizeof": None,
        "cheat": None,
        "currencyconverter":None,
        "checklastvid": None,
        "checklasttweet": None,
        "checktwitchonline": None,
        "fileconverter": None,
        "ping.gg": None,
        "guid": None,
        "dns": None,
        "shorten": None,
        "transfer": None,
        "speedtest": None,
        "weather": None,
        "covid19": None,
        "ip": None,
        "geoip": None,
        "qrcode": None,
        "stonks": None,
        "md5": None,
        "welcome":None,
        "startup": None,
        "open": None,
        "settings": None,
        "sha1": None,
        "sha224": None,
        "sha256": None,
        "sha384": None,
        "sha512": None,
        "md5sum": None,
        "sha1sum": None,
        "sha224sum": None,
        "sha256sum": None,
        "sha384sum": None,
        "sha512sum": None,
        # "help": {"/?": None},
        "elevate": None,
        "admin": None,
        "compile": None,
        # "cls": {"/?": None},
        "clear": None,
        "search": None,
        "void":{"config":None,"mode":{"CMD":None,"POWERSHELL":None},"install":{"chocolatey":None},"multithreading":{"true":None,"false":None},"license":{"full":None},"version":{"latest":None,"local":None},"mouseSupport":{"true":None,"false":None},"fuzzycomplete":{"true":None,"false":None},"completeWhileTyping":{"true":None,"false":None},"wrapLines":{"true":None,"false":None},"welcome":{"true":None,"false":None}, "start":None,"updatePythonPackages":None, "title":None},
        "read": None,
        "power": None,
        "password": None,
        "gcd": None,
        "lcm": None,
        "rng": None,
        "pagefile": None,
        "motherboard": None,
        "ram": None,
        "cpu": None,
        "gpu": None,
        "network": None,
        "bootinfo": None,
        "disk": None,
        "control": None,
        "msconfig": None,
        "msinfo32": None,
        "regedit": None,
        "sysdm.cpl": None,
        "firewall": None,
        "component": None,
        "services": None,
        "manager": None,
        "event": None,
        # "color": {"/?": None, "0": None, "1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "7": None, "8": None, "9": None, "a": None, "b": None, "c": None, "d": None, "e": None, "f": None},
        "ping": {"/?": None, "-t": None, "-a": None, "-n": None, "-l": None, "-f": None, "-i": None, "-v": None, "-r": None, "-s": None, "-j": None, "-k": None, "-w": None, "-R": None, "-S": None, "-C": None, "-p": None, "-4": None, "-6": None},
        "os":None,
        "pwned":None,
        "cd":{"/?":None,'""':None},
    #   "exit": {"/?": None, "/B": None},
        "quit":None,
        "alias":{"-list":None},
        "delalias": None,
        "+": None,
        "-": None,
        "*": None,
        "/": None,
        "**": None,
        "//": None,
        "root": None,
        "%": None,
        "download": {"-list":None},
    #     "assoc": {"/?": None},
    #     "attrib": {"-list": None, "+": None, "-": None, "R": None, "A": None, "S": None,"H": None,"O": None,"I": None,"X": None,"V": None,"P": None,"U": None,"B": None,"/S": None,"/D": None,"/L": None},
    #     "break":{"/?":None},
    #     "bcdedit": {"/?": None, "/store": None, "/createstore": None, "/export": None, "/import": None, "/sysstore": None, "/copy": None, "/create": None, "/delete": None, "/mirror": None, "/deletevalue": None, "/set": None, "/enum": None, "/v": None, "/bootsequence": None, "/default": None, "/displayorder": None, "/timeout": None, "/toolsdisplayorder": None, "/bootems": None, "/ems": None, "/emssettings": None, "/bootdebug": None, "/debug": None, "/dbgsettings": None, "/hypervisorsettings": None, "/eventsettings": None, "/event": None},
    #     "cacls": {"/?": None, "/T": None, "/L":None,"/M":None,"/S":None,"/S:SDDL":None,"/E":None,"/C":None,"/G":None,"/R":None,"/P":None,"/D":None},
    #     "call":{"/?":None},
    #     "chcp":{"/?":None},
    #     "chdir": {"/?": None},
    #     "chkdsk": {"/?": None, "/F": None, "/V": None, "/R": None, "/L": None, "/X": None, "/I": None, "/C": None, "/B": None, "/scan": None, "/forceofflinefix": None, "/perf": None, "/spotfix": None, "/sdcleanup": None, "/offlinescanandfix": None, "/freeorphanedchains": None, "/markclean": None},
    #     "chkntfs": {"/?": None,"/D": None,"/T": None,"/X": None,"/C": None,},
    #     "cmd": {"/?": None, "/C": None, "/K": None, "/S": None, "/Q": None,  "/D": None, "/A": None, "/U": None, "/T": None, "/E": None, "/F": None, "/V": None},
    #     "comp": {"/?": None, "/D": None, "/A": None, "/L": None, "/N": None, "/C": None, "/OFF": None, "/M": None},
    #     "compact": {"/?": None, "/C": None, "/U": None, "/S": None, "/A": None, "/I": None, "/F": None, "/Q": None, "/EXE": None, "/CompactOs": None, "/WinDir": None},
        "convert": {"decimal":{"hexadecimal":None,"octal": None, "binary":None},"roman":{"int": None},"celsius":{"kelvin": None,"fahrenheint": None,"rankine": None},"fahrenheint":{"kelvin": None,"celsius": None,"rankine": None},"kelvin":{"celsius": None,"fahrenheint": None,"rankine": None},"rankine":{"kelvin": None,"fahrenheint": None,"celsius": None},"color":{"rgb": None,"hex": None,"list": None}, "mp3": None, "wav": None, "m4a": None, "combine": None},
    #     "copy": {"/?": None, "/A": None, "/B": None, "/D": None, "/V": None, "/N": None, "/Y": None, "/Z": None, "/L": None},
    #     "date": {"/?": None, "/T": None},
    #     "del": {"/?": None, "/P": None, "/F": None, "/S": None, "/Q": None, "/A": None},
    #     "dir": {"/?": None, "/A": None, "/B": None, "/C": None, "/D": None, "/L": None, "/N": None, "/O": None, "/P": None, "/Q": None, "/R": None, "/S": None, "/T": None, "/W": None, "/X": None, "/Y": None,"/4": None},
    #     "diskpart":None,
    #     "doskey": {"/?": None, "/REINSTALL": None, "/LISTSIZE": None, "/MACROS": None, "/HISTORY": None, "/INSERT": None, "/OVERSTRIKE": None, "/EXENAME": None, "/MACROFILE": None},
    #     "driverquery": {"/?": None, "/S": None, "/U": None, "/P": None, "/FO": None, "/NH": None, "/SI": None, "/V": None},
    #     "echo": {"/?": None},
    #     "endlocal": {"/?": None},
    #     "erase": {"/?": None, "/P": None, "/F": None, "/S": None, "/Q": None, "/A": None},
    #     "fc": {"/?": None, "/A": None, "/B": None, "/C": None, "/L": None, "/Lbn": None, "/N": None, "/OFF": None, "/T": None, "/U": None, "/W": None},
    #     "find": {"/?": None, "/V": None, "/C": None, "/N": None, "/I": None, "/OFF": None},
    #     "findstr": {"/?": None},
    #     "for": {"/?": None, "/D": None, "/R": None, "/L": None, "/F": None},
    #     "format": {"/?": None, "/FS": None, "/V": None, "/Q": None, "/C": None, "/X": None, "/R": None, "/D": None, "/L": None, "/A": None, "/F": None, "/T": None, "/N": None, "/P": None, "/S": None, "/TXF": None, "/I": None, "/DAX": None, "/LogSize": None, "/NoRepairLogs": None},
    #     "fsutil": {"/?": None, "8dot3name": None, "behavior": None, "dax": None, "dirty": None, "file": None, "fsInfo": None, "hardlink": None, "objectID": None, "quota": None, "repair": None, "reparsePoint": None, "resource": None, "sparse": None, "tiering": None, "transaction": None, "usn": None, "volume": None, "wim": None},
    #     "ftype": {"/?": None},
    #     "goto": {"/?": None},
    #     "gpresult": {"/?": None, "/S": None, "/U": None, "/P": None, "/SCOPE": None, "/USER": None, "/R": None, "/V": None, "/Z": None},
    #     "graftabl": None,
    #     "icacls": {"/?": None, "/save": None, "/setowner": None, "/findsid": None, "/verify": None, "/reset": None, "/grant": None, "/deny": None, "/remove": None, "/setintegritylevel": None, "/inheritance": None, "/T": None, "/C": None, "/L": None, "/Q": None},
    #     "if": {"/?": None},
    #     "label": {"/?": None,"/MP":None},
    #     "md": {"/?": None},
    #     "mkdir": {"/?": None},
    #     "mklink": {"/?": None, "/D": None, "/H": None, "/J": None},
    #     "mode": {"/?": None},
    #     "more": {"/?": None, "/E": None, "/C": None, "/P": None, "/S": None, "/Tn": None},
    #     "mode": {"/?": None, "/Y":None},
    #     "openfiles": {"/?": None, "/Disconnect": None, "/Query": None, "/Local": None},
    #     "path": {"/?": None},
    #     "pause": {"/?": None},
    #     "popd": {"/?": None},
    #     "print": {"/?": None, "/D":None},
    #     "prompt": {"/?": None},
    #     "pushd": {"/?": None},
    #     "rd": {"/?": None, "/S": None,"/Q": None},
    #     "recover": {"/?": None},
    #     "rem": {"/?": None},
    #     "ren": {"/?": None},
    #     "rename": {"/?": None},
    #     "replace": {"/?": None, "/A": None, "/P": None, "/R": None, "/S": None, "/W": None, "/U": None},
    #     "rmdir": {"/?": None, "/S": None, "/Q": None},
    #     "robocopy": {"/?": None, "/S": None, "/E": None, "/LEV": None, "/Z": None, "/B": None, "/ZB": None, "/J": None, "/EFSRAW": None, "/COPY": None, "/SEC": None, "/COPYALL": None, "/NOCOPY": None, "/SECFIX": None, "/TIMFIX": None, "/PURGE": None, "/MIR": None, "/MOV": None, "/MOVE": None, "/A+": None, "/A-": None, "/CREATE": None, "/FAT": None, "/256": None, "/MON": None, "/MOT": None, "/RH": None, "/IPG": None, "/SL": None, "/MT": None, "/DCOPY": None, "/NODCOPY": None, "/NOOFFLOAD": None, "/A": None, "/M": None, "/IA": None, "/XA": None, "/XF": None, "/XD": None, "/XC": None, "/XN": None, "/XO": None, "/XX": None, "/XL": None, "/IS": None, "/IT": None, "/MAX": None, "/MIN": None, "/MAXAGE": None, "/MINAGE": None, "/MAXLAD": None, "/MINLAD": None, "/XJ": None, "/FFT": None, "/DST": None, "/XJD": None, "/XJF": None, "/R": None, "/W": None, "/REG": None, "/TBD": None, "/L": None, "/X": None, "/V": None, "/TS": None, "/FP": None, "/BYTES": None, "/NS": None, "/NC": None, "/NFL": None, "/NDL": None, "/NP": None, "/ETA": None, "/LOG": None, "/LOG+": None, "/UNILOG": None, "/UNILOG+": None, "/TEE": None, "/NJH": None, "/NJS": None, "/UNICODE": None, "/JOB": None, "/SAVE": None, "/QUIT": None, "/NOSD": None, "/NODD": None, "/IF": None},
    #     "set": {"/?": None, "/A": None, "/P": None, "%CD%": None, "%DATE%": None, "%TIME%": None, "%RANDOM%": None, "%ERRORLEVEL%": None, "%CMDEXTVERSION%": None, "%CMDCMDLINE%": None, "%HIGHESTNUMANODENUMBER%": None},
    #     "setlocal": {"/?": None},
    #     "sc": {"/?": None, "query": None, "queryex": None, "start": None, "pause": None, "interrogate": None, "continue": None, "stop": None, "config": None, "description": None, "failiture": None, "failitureflag": None, "sidtype": None, "privs": None, "managedaccount": None, "qc": None, "qdescription": None, "qfailiture": None, "qfailitureflag": None, "qsidtype": None, "qprivs": None, "qtriggerinfo": None, "qpreferrednode": None, "qmanagedaccount": None, "qprotection": None, "quserservice": None, "delete": None, "create": None, "control": None, "sdshow": None, "sdset": None, "showsid": None, "triggerinfo": None, "preferrednode": None, "GetDisplayName": None, "GetKeyName": None, "EnumDepend": None, "boot": None, "Lock": None, "QueryLock": None},
    #     "schtasks": {"/?": None, "/Create": None,"/Delete": None,"/Query": None,"/Change": None,"/Run": None,"/End": None,"/ShowSid": None},
    #     "shift": {"/?": None, "/n":None},
    #     "shutdown": {"/?": None, "/i": None, "/l": None, "/s": None, "/sg": None, "/r": None, "/g": None, "/a": None, "/p": None, "/h": None, "/hybrid": None, "/fw": None, "/e": None, "/o": None, "/m": None, "/t": None, "/c": None, "/f": None, "/d": None},
    #     "sort": {"/?": None, "/+n": None, "/L": None, "/M": None, "/REC": None, "/O": None, "/R": None, "/T": None},
    #     "start": {"/?": None, "/D": None, "/I": None, "/MIN": None, "/MAX": None, "/SEPARATE": None, "/SHARED": None, "/LOW": None, "/NORMAL": None, "/HIGH": None, "/REALTIME": None, "/ABOVENORMAL": None, "/BELOWNORMAL": None, "/NODE": None, "/AFFINITY": None, "/WAIT": None, "/B": None},
    #     "subst": {"/?": None, "/D": None},
    #     "systeminfo": {"/?": None, "/S": None, "/U": None, "/P": None, "/FO": None, "/NH": None},
    #     "tasklist": {"/?": None, "/U": None, "/P": None, "/M": None, "/SVC": None, "/S": None},
    #     "taskkill": {"/?": None, "/S": None, "/U": None, "/P": None, "/FI": None, "/PID": None, "/IM": None, "/T": None, "/F": None},
    #     "time": {"/?": None, "/T": None},
    #     "title": {"/?": None},
    #     "tree": {"/?": None, "/F": None, "/A": None},
    #     "type": {"/?": None},
    #     "ver": {"/?": None},
    #     "verify": {"/?": None},
    #     "vol": {"/?": None},
    #     "xcopy": {"/?": None, "/A": None, "/M": None, "/D": None, "/EXCLUDE": None, "/P": None, "/S": None, "/E": None, "/V": None, "/W": None, "/C": None, "/I": None, "/Q": None, "/F": None, "/L": None, "/G": None, "/H": None, "/R": None, "/T": None, "/U": None, "/K": None, "/N": None, "/O": None, "/X": None, "/Y": None, "/-Y": None, "/Z": None, "/B": None, "/J": None},
    #     "wmic": {"/?": None, "/NAMESPACE": None, "/ROLE": None, "/NODE": None, "/IMPLEMENT": None, "/AUTHLEVEL": None, "/LOCALE": None, "/PRIVILIGES": None, "/TRACE": None, "/RECORD": None, "/INTERACTIVE": None, "/FAILFAST": None, "/USER": None, "/PASSWORD": None, "/OUTPUT": None, "/APPEND": None, "/AGGREGATE": None, "/AUTHORITY": None, "ALIAS": None, "BASEBOARD": None, "BIOS": None, "BOOTCONFIG": None, "CDROM": None, "COMPUTERSYSTEM": None, "CPU": None, "CSPRODUCT": None, "DATAFILE": None, "DCOMAPP": None, "DESKTOP": None, "DESKTOPMONITOR": None, "DEVICEMEMORYADDRESS": None, "DISKDRIVE": None, "DISKQUOTA": None, "DMACHANNEL": None, "ENVIROMENT": None, "FSDIR": None, "GROUP": None, "IDECONTROLLER": None, "IRQ": None, "JOB": None, "LOADORDER": None, "LOGICALDISK": None, "LOGON": None, "MEMCACHE": None, "MEMORYCHIP": None, "MEMPHYSICAL": None, "NETCLIENT": None, "NETLOGIN": None, "NETPROTOCOL": None, "NETUSE": None, "NIC": None, "NICCONFIG": None, "NTDOMAIN": None, "NTEVENT": None, "NTEVENTLOG": None, "ONBOARDDEVICE": None, "OS": None, "PAGEFILE": None, "PAGEFILESET": None, "PARTITION": None, "PORT": None, "PORTCONNECTOR": None, "PRINTER": None, "PRINTERCONFIG": None, "PRINTJOB": None, "PROCESS": None, "PRODUCT": None, "QFE": None, "QUOTASETTING": None, "RDACCOUNT": None, "RDNIC": None, "RDPERMISSIONS": None, "RDTOGGLE": None, "RECOVEROS": None, "REGISTRY": None, "SCSICONTROLLER": None, "SERVER": None, "SERVICE": None, "SHADOWCOPY": None, "SHADOWSTORAGE": None, "SHARE": None, "SOFTWAREELEMENT": None, "SOFTWAREFEATURE": None, "SOUNDDEV": None, "STARTUP": None, "SYSACCOUNT": None, "SYSDRIVER": None, "SYSTEMENCLOSURE": None, "SYSTEMSLOT": None, "TAPEDRIVE": None, "TEMPERATURE": None, "TIMEZONE": None, "UPS": None, "USERACCOUNT": None, "VOLTAGE": None, "VOLUME": None, "VOLUMEQUOTASETTING": None, "VOLUMEUSERQUOTA": None, "WMISET": None},
    }
)

winWordCompleter = WordCompleter([
    'append','arp','assoc','at','atmadm','attrib','auditpol','backup','bcdboot','bcdedit','bdehdcfg','bitsadmin','bootcfg','bootsect','break','cacls','call','cd','certreq','certutil','cipher','clip','cls','cmd','cmdkey','cmstp','color','command','comp','compact','copy','cscript','ctty','date','dblspace','debug','defrag','del','deltree','diantz','dir','diskcomp','diskcopy','diskpart','diskperf','diskraid','dism','dispdiag','djoin','doskey','dosshell','dosx','driverquery','drvspace','edit','edlin','echo','emm386','endlocal','erase','esentutl','eventcreate','eventtriggers','exe2bin','exit','expand','extrac32','extract','fasthelp','fastopen','fc','fdisk','find','findstr','finger','fltmc','fondue','for','forcedos','forfiles','format','fsutil','ftp','ftype','getmac','goto','gpresult','gpupdate','graftabl','graphics','help','hostname','hwrcomp','hwrreg','change','chcp','chdir','checknetisolation','chglogon','chgport','chgusr','chkdsk','chkntfs','choice','icacls','if','interlnk','intersvr','ipconfig','ipxroute','irftp','iscsicli','kb16','keyb','klist','ksetup','ktmutil','label','lh','licensingdiag','loadfix','loadhigh','lock','lodctr','logman','logoff','lpq','lpr','makecab','manage-bde','md','mem','memmaker','mkdir','mklink','mode','mofcomp','more','mount','mountvol','move','mrinfo','msav','msbackup','mscdex','msd','msg','msiexec','muiunattend','nbtstat','net','net1','netcfg','netsh','netstat','nfsadmin','nlsfunc','nltest','nslookup','ntbackup','ntsd','ocsetup','openfiles','path','pathping','pause','pentnt','ping','pkgmgr','pnpunattend','pnputil','popd','powercfg','print','prompt','pushd','pwlauncher','qappsrv','qbasic','qprocess','query','quser','qwinsta','rasautou','rasdial','rcp','rd','rdpsign','reagentc','recimg','recover','reg','regini','register-cimprovider','regsvr32','relog','rem','ren','rename','repair-bde','replace','reset','restore','rexec','rmdir','robocopy','route','rpcinfo','rpcping','rsh','rsm','runas','rwinsta','sc','scandisk','scanreg','sdbinst','secedit','set','setlocal','setspn','setver','setx','sfc','shadow','share','shift','showmount','shutdown','schtasks','smartdrv','sort','start','subst','sxstrace','sys','systeminfo','takeown','taskkill','tasklist','tcmsetup','telnet','tftp','time','timeout','title','tlntadmn','tpmvscmgr','tracerpt','tracert','tree','tscon','tsdiscon','tskill','tsshutdn','type','typeperf','tzutil','umount','undelete','unformat','unlock','unlodctr','vaultcmd','ver','verify','vol','vsafe','vssadmin','w32tm','waitfor','wbadmin','wecutil','wevtutil','where','whoami','winmgmt','winrm','winrs','winsat','wmic','wsmanhttpconfig','xcopy','xwizard'
])

if platform.system() == "Linux":
    if os.path.exists("commands.txt") == False:
        os.system(f'bash -c "compgen -c >{defPath}/commands.txt"')
    f = open("commands.txt","r")
    l = f.read().splitlines()
    l = list(dict.fromkeys(l))
    LinuxCompleter = WordCompleter(l + ["currencyconverter","downloadeta","sizeof","md5","sha1","sha224","sha256","sha384","sha512","void","plain2string","eval","welcome","help","elevate","admin","compile","cls","clear","read","gcd","lcm","rng","os","pwned","exit","quit","alias","delalias","+","-","*","/","**","//","download","cheat","checklastvid","checklasttweet","checktwitchonline","fileconverter","ping.gg","guid","dns","shorten","transfer","speedtest","weather","covid19","ip","geoip","qrcode","stonks","welcome"])
else:
    LinuxCompleter = None

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    import Void
    Void.main()
