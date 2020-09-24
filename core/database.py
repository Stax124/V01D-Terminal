from prompt_toolkit.completion import WordCompleter, NestedCompleter, DummyCompleter
from typing import Callable, Iterable, List, Optional
import os
import pickle
import core.utils as utils
import yaml
import platform
from pathlib import Path

def writedata(data, filename: str, location: str, mode: str) -> None:
    "Writes data to target file"
    target = os.path.join(location, filename)
    f = open(target,mode)
    f.write(data)
    f.close()

# -----------------------------------------------------------------

def WriteAliases(aliases: dict) -> list:
    "Writes aliases to aliase.picke file"
    f = open(os.path.join(__location__, "aliases.pickle"), "wb")
    pickle.dump(aliases,f)
    f.close()

def GetAliases() -> dict:
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

known_ports = [1,3,4,6,7,9,13,17,19,20,21,22,23,24,25,26,30,32,33,37,42,43,49,53,70,79,80,81,82,83,84,85,88,89,90,99,100,106,109,110,111,113,119,125,135,139,143,144,146,161,163,179,199,211,212,222,254,255,256,259,264,280,301,306,311,340,366,389,406,407,416,417,425,427,443,444,445,458,464,465,481,497,500,512,513,514,515,524,541,543,544,545,548,554,555,563,587,593,616,617,625,631,636,646,648,666,667,668,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800,801,808,843,873,880,888,898,900,901,902,903,911,912,981,987,990,992,993,995,999,1000,1001,1002,1007,1009,1010,1011,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1102,1104,1105,1106,1107,1108,1110,1111,1112,1113,1114,1117,1119,1121,1122,1123,1124,1126,1130,1131,1132,1137,1138,1141,1145,1147,1148,1149,1151,1152,1154,1163,1164,1165,1166,1169,1174,1175,1183,1185,1186,1187,1192,1198,1199,1201,1213,1216,1217,1218,1233,1234,1236,1244,1247,1248,1259,1271,1272,1277,1287,1296,1300,1301,1309,1310,1311,1322,1328,1334,1352,1417,1433,1434,1443,1455,1461,1494,1500,1501,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687,1688,1700,1717,1718,1719,1720,1721,1723,1755,1761,1782,1783,1801,1805,1812,1839,1840,1862,1863,1864,1875,1900,1914,1935,1947,1971,1972,1974,1984,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2013,2020,2021,2022,2030,2033,2034,2035,2038,2040,2041,2042,2043,2045,2046,2047,2048,2049,2065,2068,2099,2100,2103,2105,2106,2107,2111,2119,2121,2126,2135,2144,2160,2161,2170,2179,2190,2191,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381,2382,2383,2393,2394,2399,2401,2492,2500,2522,2525,2557,2601,2602,2604,2605,2607,2608,2638,2701,2702,2710,2717,2718,2725,2800,2809,2811,2869,2875,2909,2910,2920,2967,2968,2998,3000,3001,3003,3005,3006,3007,3011,3013,3017,3030,3031,3052,3071,3077,3128,3168,3211,3221,3260,3261,3268,3269,3283,3300,3301,3306,3322,3323,3324,3325,3333,3351,3367,3369,3370,3371,3372,3389,3390,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689,3690,3703,3737,3766,3784,3800,3801,3809,3814,3826,3827,3828,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000,4001,4002,4003,4004,4005,4006,4045,4111,4125,4126,4129,4224,4242,4279,4321,4343,4443,4444,4445,4446,4449,4550,4567,4662,4848,4899,4900,4998,5000,5001,5002,5003,5004,5009,5030,5033,5050,5051,5054,5060,5061,5080,5087,5100,5101,5102,5120,5190,5200,5214,5221,5222,5225,5226,5269,5280,5298,5357,5405,5414,5431,5432,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678,5679,5718,5730,5800,5801,5802,5810,5811,5815,5822,5825,5850,5859,5862,5877,5900,5901,5902,5903,5904,5906,5907,5910,5911,5915,5922,5925,5950,5952,5959,5960,5961,5962,5963,5987,5988,5989,5998,5999,6000,6001,6002,6003,6004,6005,6006,6007,6009,6025,6059,6100,6101,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565,6566,6567,6580,6646,6666,6667,6668,6669,6689,6692,6699,6779,6788,6789,6792,6839,6881,6901,6969,7000,7001,7002,7004,7007,7019,7025,7070,7100,7103,7106,7200,7201,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777,7778,7800,7911,7920,7921,7937,7938,7999,8000,8001,8002,8007,8008,8009,8010,8011,8021,8022,8031,8042,8045,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,8093,8099,8100,8180,8181,8192,8193,8194,8200,8222,8254,8290,8291,8292,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651,8652,8654,8701,8800,8873,8888,8899,8994,9000,9001,9002,9003,9009,9010,9011,9040,9050,9071,9080,9081,9090,9091,9099,9100,9101,9102,9103,9110,9111,9200,9207,9220,9290,9415,9418,9485,9500,9502,9503,9535,9575,9593,9594,9595,9618,9666,9876,9877,9878,9898,9900,9917,9929,9943,9944,9968,9998,9999,10000,10001,10002,10003,10004,10009,10010,10012,10024,10025,10082,10180,10215,10243,10566,10616,10617,10621,10626,10628,10629,10778,11110,11111,11967,12000,12174,12265,12345,13456,13722,13782,13783,14000,14238,14441,14442,15000,15002,15003,15004,15660,15742,16000,16001,16012,16016,16018,16080,16113,16992,16993,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221,20222,20828,21571,22939,23502,24444,24800,25734,25735,26214,27000,27352,27353,27355,27356,27715,28201,30000,30718,30951,31038,31337,32768,32769,32770,32771,32772,32773,32774,32775,32776,32777,32778,32779,32780,32781,32782,32783,32784,32785,33354,33899,34571,34572,34573,35500,38292,40193,40911,41511,42510,44176,44442,44443,44501,45100,48080,49152,49153,49154,49155,49156,49157,49158,49159,49160,49161,49163,49165,49167,49175,49176,49400,49999,50000,50001,50002,50003,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055,55056,55555,55600,56737,56738,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389]

if platform.system() == "Windows":
    WinCompleter = NestedCompleter.from_nested_dict(
    {
        "tcp-scan":None,
        "refreshenv":None,
        "ytdown":None,
        "grantfiles": None,
        "back": None,
        "downloadeta":None,
        "poweroff":None,
        "reboot":None,
        "instaloader":None,
        "pwd":None,
        "autoclicker":None,
        "brightness":None,
        "plain2string": None,
        "cryptocurrency":{"btc":None,"eth":None,"xrp":None,"usdt":None,"bch":None,"ltc":None,"ada":None,"bnb":None},
        "eval": None,
        "sizeof": None,
        "godmode": None,
        "cheat": None,
        "threads": None,
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
        "wifipassword": None,
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
        "cd":None,
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
        "%": None,
        "download": None,
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
    "play","player-volume","player-terminate","player-pause",'append','arp','assoc','at','atmadm','attrib','auditpol','backup','bcdboot','bcdedit','bdehdcfg','bitsadmin','bootcfg','bootsect','break','cacls','call','cd','certreq','certutil','cipher','clip','cls','cmd','cmdkey','cmstp','color','command','comp','compact','copy','cscript','ctty','date','dblspace','debug','defrag','del','deltree','diantz','dir','diskcomp','diskcopy','diskpart','diskperf','diskraid','dism','dispdiag','djoin','doskey','dosshell','dosx','driverquery','drvspace','edit','edlin','echo','emm386','endlocal','erase','esentutl','eventcreate','eventtriggers','exe2bin','exit','expand','extrac32','extract','fasthelp','fastopen','fc','fdisk','find','findstr','finger','fltmc','fondue','for','forcedos','forfiles','format','fsutil','ftp','ftype','getmac','goto','gpresult','gpupdate','graftabl','graphics','help','hostname','hwrcomp','hwrreg','change','chcp','chdir','checknetisolation','chglogon','chgport','chgusr','chkdsk','chkntfs','choice','icacls','if','interlnk','intersvr','ipconfig','ipxroute','irftp','iscsicli','kb16','keyb','klist','ksetup','ktmutil','label','lh','licensingdiag','loadfix','loadhigh','lock','lodctr','logman','logoff','lpq','lpr','makecab','manage-bde','md','mem','memmaker','mkdir','mklink','mode','mofcomp','more','mount','mountvol','move','mrinfo','msav','msbackup','mscdex','msd','msg','msiexec','muiunattend','nbtstat','net','net1','netcfg','netsh','netstat','nfsadmin','nlsfunc','nltest','nslookup','ntbackup','ntsd','ocsetup','openfiles','path','pathping','pause','pentnt','ping','pkgmgr','pnpunattend','pnputil','popd','powercfg','print','prompt','pushd','pwlauncher','qappsrv','qbasic','qprocess','query','quser','qwinsta','rasautou','rasdial','rcp','rd','rdpsign','reagentc','recimg','recover','reg','regini','register-cimprovider','regsvr32','relog','rem','ren','rename','repair-bde','replace','reset','restore','rexec','rmdir','robocopy','route','rpcinfo','rpcping','rsh','rsm','runas','rwinsta','sc','scandisk','scanreg','sdbinst','secedit','set','setlocal','setspn','setver','setx','sfc','shadow','share','shift','showmount','shutdown','schtasks','smartdrv','sort','start','subst','sxstrace','sys','systeminfo','takeown','taskkill','tasklist','tcmsetup','telnet','tftp','time','timeout','title','tlntadmn','tpmvscmgr','tracerpt','tracert','tree','tscon','tsdiscon','tskill','tsshutdn','type','typeperf','tzutil','umount','undelete','unformat','unlock','unlodctr','vaultcmd','ver','verify','vol','vsafe','vssadmin','w32tm','waitfor','wbadmin','wecutil','wevtutil','where','whoami','winmgmt','winrm','winrs','winsat','wmic','wsmanhttpconfig','xcopy','xwizard'
])

if platform.system() == "Linux":
    if os.path.exists("commands.txt") == False:
        from Void import defPath
        os.system(f'bash -c "compgen -c >{defPath}/commands.txt"')
    f = open("commands.txt","r")
    l = f.read().splitlines()
    l = list(dict.fromkeys(l))
    LinuxCompleter = WordCompleter(list(dict.fromkeys(l + ["tcp-scan","autoclicker","threads","instaloader","play","player-volume","player-terminate","player-pause","back","currencyconverter","downloadeta","sizeof","md5","sha1","sha224","sha256","sha384","sha512","void","plain2string","eval","welcome","help","elevate","admin","compile","cls","clear","read","gcd","lcm","rng","os","pwned","exit","quit","alias","delalias","+","-","*","/","**","//","download","cheat","checklastvid","checklasttweet","checktwitchonline","fileconverter","ping.gg","guid","dns","shorten","transfer","speedtest","weather","covid19","ip","geoip","qrcode","stonks","welcome"])))
else:
    LinuxCompleter = None

