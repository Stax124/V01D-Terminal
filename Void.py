# Project V01D-Terminal

import argparse
import os
import platform
import shlex
import subprocess
import sys
import threading
import traceback
from math import *
from subprocess import call, check_output
from threading import Thread
from webbrowser import open_new_tab

import core
import core.osBased
import core.elevate
import core.utils
from core.database import *

# Plugin loader -------------------------------------------
steam_api, pwned, hashing, player, autoclicker = None, None, None, None, None
from plugins import *

# Add to PATH ---------------------------------------------
os.environ["PATH"] = os.path.dirname(
    __file__) + os.pathsep + os.environ["PATH"]

# Setup parser --------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="Execute following command")
parser.add_argument("-d", "--directory", help="Start in specified directory")
parser.add_argument("--character-page",
                    help="Manualy select code page, defaults to 65001 (unicode)")
parser.add_argument("-v", "--verbose",
                    help="Output everything", action="store_true")
parser.add_argument(
    "-q", "--quiet", help="Do not output, works for internal commands only", action="store_true")
parser.add_argument(
    "-e", "--echo", help="Echoes all commands before executing", action="store_true")
parser.add_argument(
    "--welcome", help="Force welcome screen", action="store_true")
parser.add_argument("-s", "--skipconfig",
                    help="Terminal will skip loading config", action="store_true")
args = parser.parse_args()


class c:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def iswindows() -> bool:
    return True if platform.system() == "Windows" else False


if iswindows():
    from subprocess import check_output
    if not args.character_page:
        check_output("chcp 65001", shell=True)
    else:
        print(check_output(f"chcp {args.character_page}", shell=True))


def _import():
    import ctypes
    import datetime
    import hashlib
    from sys import exit as _exit

    import GPUtil
    import psutil
    import requests
    import yaml
    from packaging import version
    from prompt_toolkit import PromptSession, print_formatted_text
    from prompt_toolkit.auto_suggest import (AutoSuggestFromHistory,
                                             DummyAutoSuggest)
    from prompt_toolkit.completion import (DummyCompleter, FuzzyCompleter,
                                           ThreadedCompleter, merge_completers)
    from prompt_toolkit.enums import EditingMode
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.output.color_depth import ColorDepth
    from prompt_toolkit.patch_stdout import patch_stdout
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.styles import Style

    from core.PathCompleter import PathCompleter


try:
    import ctypes
    import datetime
    import hashlib
    from sys import exit as _exit

    import GPUtil
    import psutil
    import requests
    import yaml
    from packaging import version
    from prompt_toolkit import PromptSession, print_formatted_text
    from prompt_toolkit.auto_suggest import (AutoSuggestFromHistory,
                                             DummyAutoSuggest)
    from prompt_toolkit.completion import (DummyCompleter, FuzzyCompleter,
                                           ThreadedCompleter, merge_completers)
    from prompt_toolkit.enums import EditingMode
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.output.color_depth import ColorDepth
    from prompt_toolkit.patch_stdout import patch_stdout
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.styles import Style

    from core.PathCompleter import PathCompleter


except Exception as e:
    if "python" in sys.executable.lower():
        if not args.quiet:
            print(e)
        # Install main lib
        if iswindows():
            os.system("pip install prompt-toolkit")
        else:
            os.system("sudo pip3 install prompt-toolkit")

        from prompt_toolkit.shortcuts import confirm

        # Ask to install all dependencies, if denied, exit application
        if confirm("Install dependencies: "):
            if iswindows():
                os.system(
                    "pip3 install -r requirements.txt {0}".format("--user" if not confirm("Root (Admin) user: ") else ""))
            else:
                root = confirm("Root (Admin) user: ")
                os.system(
                    "{0}pip3 install -r requirements.txt {1}".format("sudo " if root else "","--user" if not root else ""))
                os.system("{0}apt-get install -y libmpv-dev".format("sudo " if root else ""))
        else:
            exit(0)

        # Reimport all dependencies
        _import()
    else:
        if not args.quiet:
            print(e)
        if iswindows():
            os.system("pause")

# -------------------------------------------

# Get Username
try:
    if iswindows():
        USER = os.environ["USERNAME"]
    else:
        USER = os.environ["USER"]
except:
    USER = "UNKNOWN"


try:
    if iswindows():
        USERDOMAIN = os.environ["USERDOMAIN"]
    else:
        USERDOMAIN = os.environ["NAME"]
except:
    USERDOMAIN = "UNKNOWN"

defPath = os.getcwd()
defcompleter = {'append': None, 'arp': None, 'assoc': None, 'at': None, 'atmadm': None, 'attrib': None, 'auditpol': None, 'backup': None, 'bcdboot': None, 'bcdedit': None,
'bdehdcfg': None, 'bitsadmin': None, 'bootcfg': None, 'bootsect': None, 'break': None, 'cacls': None, 'call': None, 'cd': None, 'certreq': None, 'certutil': None, 'cipher': None,
'clip': None, 'cls': None, 'cmd': None, 'cmdkey': None, 'cmstp': None, 'color': None, 'command': None, 'comp': None, 'compact': None, 'copy': None, 'cscript': None, 'ctty': None, 
'date': None, 'dblspace': None, 'debug': None, 'defrag': None, 'del': None, 'deltree': None, 'diantz': None, 'dir': None, 'diskcomp': None, 'diskcopy': None, 'diskpart': None, 
'diskperf': None, 'diskraid': None, 'dism': None, 'dispdiag': None, 'djoin': None, 'doskey': None, 'dosshell': None, 'dosx': None, 'driverquery': None, 'drvspace': None, 'edit': None,
'edlin': None, 'echo': None, 'emm386': None, 'endlocal': None, 'erase': None, 'esentutl': None, 'eventcreate': None, 'eventtriggers': None, 'exe2bin': None, 'exit': None, 'expand': None, 
'extrac32': None, 'extract': None, 'fasthelp': None, 'fastopen': None, 'fc': None, 'fdisk': None, 'find': None, 'findstr': None, 'finger': None, 'fltmc': None, 'fondue': None, 'for': None,
'forcedos': None, 'forfiles': None, 'format': None, 'fsutil': None, 'ftp': None, 'ftype': None, 'getmac': None, 'goto': None, 'gpresult': None, 'gpupdate': None, 'graftabl': None, 'graphics': None,
'help': None, 'hostname': None, 'hwrcomp': None, 'hwrreg': None, 'change': None, 'chcp': None, 'chdir': None, 'checknetisolation': None, 'chglogon': None, 'chgport': None, 'chgusr': None, 'chkdsk': None,
'chkntfs': None, 'choice': None, 'icacls': None, 'if': None, 'interlnk': None, 'intersvr': None, 'ipconfig': None, 'ipxroute': None, 'irftp': None, 'iscsicli': None, 'kb16': None, 'keyb': None, 'klist': None,
'ksetup': None, 'ktmutil': None, 'label': None, 'lh': None, 'licensingdiag': None, 'loadfix': None, 'loadhigh': None, 'lock': None, 'lodctr': None, 'logman': None, 'logoff': None, 'lpq': None, 'lpr': None, 'makecab': None, 'manage-bde': None, 'md': None, 'mem': 
None, 'memmaker': None, 'mkdir': None, 'mklink': None, 'mode': None, 'mofcomp': None, 'more': None, 'mount': None, 'mountvol': None, 'move': None, 'mrinfo': None, 'msav': None, 
'msbackup': None, 'mscdex': None, 'msd': None, 'msg': None, 'msiexec': None, 'muiunattend': None, 'nbtstat': None, 'net': None, 'net1': None, 'netcfg': None, 'netsh': None, 'netstat': None, 'nfsadmin': None,
'nlsfunc': None, 'nltest': None, 'nslookup': None, 'ntbackup': None, 'ntsd': None, 'ocsetup': None, 'openfiles': None, 'path': None, 'pathping': None, 'pause': None, 'pentnt': None,
'ping': {'/?': None, '-t': None, '-a': None, '-n': None, '-l': None, '-f': None, '-i': None, '-v': None, '-r': None, '-s': None, '-j': None, 
'-k': None, '-w': None, '-R': None, '-S': None, '-C': None, '-p': None, '-4': None, '-6': None}, 'pkgmgr': None, 'pnpunattend': None, 'pnputil': None, 'popd': None, 'powercfg': 
None, 'print': None, 'prompt': None, 'pushd': None, 'pwlauncher': None, 'qappsrv': None, 'qbasic': None, 'qprocess': None, 'query': None, 'quser': None, 'qwinsta': None, 'rasautou': None, 'rasdial': None,
'rcp': None, 'rd': None, 'rdpsign': None, 'reagentc': None, 'recimg': None, 'recover': None, 'reg': None, 'regini': None, 'register-cimprovider': None, 'regsvr32': None, 'relog': None, 'rem': None, 'ren': None,
'rename': None, 'repair-bde': None, 'replace': None, 'reset': None, 'restore': None, 'rexec': None, 'rmdir': None, 'robocopy': None, 'route': None, 'rpcinfo': None, 'rpcping': None, 'rsh': None, 'rsm': None, 'runas': None,
'rwinsta': None, 'sc': None, 'scandisk': None, 'scanreg': None, 'sdbinst': None, 'secedit': None, 'set': None, 'setlocal': None, 'setspn': None, 'setver': None, 'setx': None, 'sfc': None, 'shadow': None, 'share': None,
'shift': None, 'showmount': None, 'shutdown': None, 'schtasks': None, 'smartdrv': None, 'sort': None, 'start': None, 'subst': None, 'sxstrace': None, 'sys': None, 'systeminfo': None, 'takeown': None, 'taskkill': None, 'tasklist': None,
'tcmsetup': None, 'telnet': None, 'tftp': None, 'time': None, 'timeout': None, 'title': None, 'tlntadmn': None, 'tpmvscmgr': None, 'tracerpt': None, 'tracert': None, 'tree': None, 'tscon': None, 'tsdiscon': None, 'tskill': None, 'tsshutdn': None,
'type': None, 'typeperf': None, 'tzutil': None, 'umount': None, 'undelete': None, 'unformat': None, 'unlock': None, 'unlodctr': None, 'vaultcmd': None, 'ver': None, 'verify': None, 'vol': None, 'vsafe': None, 'vssadmin': None, 'w32tm': None, 'waitfor': None,
'wbadmin': None, 'wecutil': None, 'wevtutil': None, 'where': None, 'whoami': None, 'winmgmt': None, 'winrm': None, 'winrs': None, 'winsat': None, 'wmic': None, 'wsmanhttpconfig': None, 'xcopy': None, 'xwizard': None, 'player': {'play': None, 'volume': None,
'pause': None, 'next': None, 'prev': None, 'terminate': None}, 'tcp-scan': None, 'refreshenv': None, 'ytdown': None, 'grantfiles': None, 'back': None, 'downloadeta': None, 'poweroff': None, 'reboot': None, 'instaloader': None, 'pwd': None, 'prime': None,
'steam': {'user': None, 'friends': None, 'me': None, 'game': None}, 'game-deals': None, 'thread': None, 'autoclicker': None, 'brightness': None, 'plain2string': None, 'cryptocurrency': {'btc': None, 'eth': None, 'xrp': None, 'usdt': None, 'bch': None,
'ltc': None, 'ada': None, 'bnb': None}, 'eval': None, 'sizeof': None, 'godmode': None, 'cheat': None, 'threads': None, 'currencyconverter': None, 'checklastvid': None, 'checklasttweet': None, 'checktwitchonline': None, 'fileconverter': None, 'ping.gg': None,
'guid': None, 'dns': None, 'shorten': None, 'transfer': None, 'speedtest': None, 'weather': None, 'covid19': None, 'ip': None, 'geoip': None, 'qrcode': None, 'stonks': None, 'md5': None, 'welcome': None, 'startup': None, 'open': None, 'settings': None, 'sha1': None,
'sha224': None, 'sha256': None, 'sha384': None, 'sha512': None, 'md5sum': None, 'sha1sum': None, 'sha224sum': None, 'sha256sum': None, 'sha384sum': None, 'sha512sum': None, 'elevate': None, 'admin': None, 'compile': None, 'interface': {'enable': None, 'disable': None},
'online': {'http://localhost': None}, 'clear': None, 'search': None, 'void': {'config': None, 'perfmon': {'true': None, 'false': None}, 'mode': {'CMD': None, 'POWERSHELL': None}, 'install': {'chocolatey': None}, 'multithreading': {'true': None, 'false': None}, 'license': {'full': None},
'version': {'latest': None, 'local': None}, 'mouseSupport': {'true': None, 'false': None}, 'fuzzycomplete': {'true': None, 'false': None}, 'completeWhileTyping': {'true': None, 'false': None}, 'wrapLines': {'true': None, 'false': None}, 'welcome': {'true': None, 'false': None},
'start': None, 'title': None}, 'read': None, 'power': None, 'wifipassword': None, 'gcd': None, 'lcm': None, 'rng': None, 'pagefile': None, 'motherboard': None, 'ram': None, 'cpu': None, 'gpu': None, 'network': None, 'bootinfo': None, 'disk': None,
'control': None, 'msconfig': None, 'msinfo32': None, 'regedit': None, 'sysdm.cpl': None, 'firewall': None, 'component': None, 'services': None, 'manager': None, 'event': None, 'os': None, 'pwned': None, 'quit': None, 'alias': {'-list': None}, 'delalias': None, '+': None, '-': None, '*': None, '/': None, '**': None, '//': None, '%': None, 'download': None}

# For use in "back"
LASTDIR = ""


# Find config file
if iswindows():
    CONFIG = os.environ["userprofile"] + r"\.void"
else:
    CONFIG = os.environ["HOME"] + r"/.void"

# Local version
VERSION = "v0.8.5"

# -------------------------------------------


def isadmin() -> bool:
    "Ask if run with elevated privileges"
    try:
        _is_admin = os.getuid() == 0

    except AttributeError:
        _is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return _is_admin

def default_completer():
    config["completer"] = defcompleter
    saveToYml(config,CONFIG)

if iswindows():
    os.system("title Void-Terminal")

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, shell=True)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip(b"\n").decode("utf-8"))
    rc = process.poll()
    return rc

def saveToYml(data, path) -> None:
    try:
        with open(path, "w") as f:
            f.flush()
            yaml.safe_dump(data, f)
    except:
        if not args.quiet:
            print(f"Unable to save data to {path}")


# Load config or defaults
try:
    if not args.skipconfig:
        config = yaml.safe_load(open(CONFIG))
        type(config.keys())
    else:
        raise Exception
except Exception as e:
    config = {
        "mode": "CMD",
        "welcome": False,
        "multithreading": True,
        "fuzzycomplete": True,
        "completeWhileTyping": True,
        "wrapLines": False,
        "mouseSupport": True,
        "searchIgnoreCase": True,
        "default": "greenyellow",
        "pointer": "#ff4500",
        "path": "aqua",
        "user": "#ff4500",
        "completion-menu.completion": "bg:#000000 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
        "exeptions": tuple(),
        "perfmon": False,
        "steamapikey":"",
        "steamurl":"",
        "volume":100,
        "completer": defcompleter,
        "prompt": f"\n┏━━(<user>USER</user> at <user>USERDOMAIN</user>)━[<path>PATH</path>]━(T:<user>TCOUNT</user> V:<user>VOLUME</user>)\n┗━<pointer>ROOT</pointer> "
    }

    if not args.skipconfig:
        if not args.quiet:
            print(e)
        try:
            print(f"{c.bold}Creating new config file:{c.end} {c.okgreen}{CONFIG}{c.end}")
            saveToYml(config, CONFIG)  # Create new config file
        except:
            if not args.quiet:
                print(
                    f"Error writing config file, please check if you have permission to write in this location {CONFIG}")

aliases = GetAliases()
if platform.system() == "Windows":
    WinCompleter = NestedCompleter.from_nested_dict(config["completer"])

MODE = config.get("mode", "CMD")
VOLUME = config.get("volume", 100)

# Pick completer based on config and platform
if config["fuzzycomplete"] and iswindows():
    combinedcompleter = ThreadedCompleter(FuzzyCompleter(merge_completers([WinCompleter, PathCompleter(
    ), WordCompleter(list(aliases.keys()))])))
elif iswindows():
    combinedcompleter = ThreadedCompleter(merge_completers(
        [WinCompleter, PathCompleter(), WordCompleter(list(aliases.keys()))]))
elif platform.system() == "Linux" and config["fuzzycomplete"]:
    combinedcompleter = ThreadedCompleter(FuzzyCompleter(
        merge_completers([LinuxCompleter, PathCompleter(),WordCompleter(list(aliases.keys()))])))
else:
    combinedcompleter = ThreadedCompleter(merge_completers(
        [LinuxCompleter, PathCompleter(),WordCompleter(list(aliases.keys()))]))

# Define console style
_style = Style.from_dict(
    {
        # Default style
        "": config.get("default"),

        # Specific style
        "pointer": config.get("pointer"),
        "path": config.get("path"),
        "user": config.get("user"),

        # Completor
        "completion-menu.completion": config.get("completion-menu.completion"),
        "completion-menu.completion.current": config.get("completion-menu.completion.current"),
        "scrollbar.background": config.get("scrollbar.background"),
        "scrollbar.button": config.get("scrollbar.button")
    }
)

# ---------------------------------------------------------------------------------------------------------------------------------------------

logo = """
██╗   ██╗  ██████╗  ██╗ ██████╗         ████████╗ ███████╗ ██████╗  ███╗   ███╗ ██╗ ███╗   ██╗  █████╗  ██╗
██║   ██║ ██╔═══██╗ ██║ ██╔══██╗        ╚══██╔══╝ ██╔════╝ ██╔══██╗ ████╗ ████║ ██║ ████╗  ██║ ██╔══██╗ ██║
██║   ██║ ██║   ██║ ██║ ██║  ██║ █████╗    ██║    █████╗   ██████╔╝ ██╔████╔██║ ██║ ██╔██╗ ██║ ███████║ ██║
╚██╗ ██╔╝ ██║   ██║ ██║ ██║  ██║ ╚════╝    ██║    ██╔══╝   ██╔══██╗ ██║╚██╔╝██║ ██║ ██║╚██╗██║ ██╔══██║ ██║
 ╚████╔╝  ╚██████╔╝ ██║ ██████╔╝           ██║    ███████╗ ██║  ██║ ██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║  ██║ ███████╗
  ╚═══╝    ╚═════╝  ╚═╝ ╚═════╝            ╚═╝    ╚══════╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝ ╚══════╝
"""

def argget(_splitInput: list) -> str:
    "Returns rebuild string"
    return " ".join(_splitInput)


def welcome() -> None:
    if not args.quiet:
        print(f"""{c.bold}{logo}{c.end}

    {c.okblue}Welcome to Void-Terminal, Windows compatible terminal with functions for advanced users{c.end}

    For full functionality, please use commands one after another: {c.okgreen}'void install chocolatey'{c.end}, {c.okgreen}'choco install mpv'{c.end}, {c.okgreen}'choco install ffmpeg'{c.end}
    Linux users may use: {c.okgreen}'sudo apt install ffmpeg'{c.end}, {c.okgreen}'sudo apt install mpv'{c.end}

    {c.okgreen}Time{c.end}: {datetime.datetime.now()}

    {c.okgreen}Latest release{c.end}: {core.utils.version()}

    {c.okgreen}'help'{c.end} - show available commands
                """)


def wifipassword() -> None:
    "Get password of wifi network (Windows only)"
    os.system("netsh wlan show profiles")
    networkName = input("Network name > ")
    os.system(f"netsh wlan show profiles {networkName} key=clear")


def void(_splitinput) -> None:  # Open new terminal or configure it
    try:
        if (_splitinput[1] == "multithreading"):
            if (_splitinput[2].lower() == "true"):
                config["multithreading"] = True
            elif (_splitinput[2].lower() == "false"):
                config["multithreading"] = False
            if not args.quiet:
                print(
                    f"multithreading: {c.okgreen}{config['multithreading']}{c.end}")

        elif (_splitinput[1] == "perfmon"):
            if (_splitinput[2].lower() == "true"):
                config["perfmon"] = True
            elif (_splitinput[2].lower() == "false"):
                config["perfmon"] = False
            if not args.quiet:
                print(
                    f"perfmon: {c.okgreen}{config['perfmon']}{c.end}")

        elif (_splitinput[1] == "fuzzycomplete"):
            if (_splitinput[2].lower() == "true"):
                config["fuzzycomplete"] = True
            elif (_splitinput[2].lower() == "false"):
                config["fuzzycomplete"] = False
            if not args.quiet:
                print(
                    f"fuzzycomplete: {c.okgreen}{config['fuzzycomplete']}{c.end}")

        elif (_splitinput[1] == "mouseSupport"):
            if (_splitinput[2].lower() == "true"):
                config["mouseSupport"] = True
            elif (_splitinput[2].lower() == "false"):
                config["mouseSupport"] = False
            if not args.quiet:
                print(
                    f"mouseSupport: {c.okgreen}{config['fuzzycomplete']}{c.end}")

        elif (_splitinput[1] == "completeWhileTyping"):
            if (_splitinput[2].lower() == "true"):
                config["completeWhileTyping"] = True
            elif (_splitinput[2].lower() == "false"):
                config["completeWhileTyping"] = False
            if not args.quiet:
                print(
                    f"completeWhileTyping: {c.okgreen}{config['completeWhileTyping']}{c.end}")

        elif (_splitinput[1] == "wrapLines"):
            if (_splitinput[2].lower() == "true"):
                config["wrapLines"] = True
            elif (_splitinput[2].lower() == "false"):
                config["wrapLines"] = False
            if not args.quiet:
                print(
                    f"wrapLines: {c.okgreen}{config['fuzzycomplete']}{c.end}")

        elif (_splitinput[1] == "welcome"):
            if (_splitinput[2].lower() == "true"):
                config["welcome"] = True
            elif (_splitinput[2].lower() == "false"):
                config["welcome"] = False
            if not args.quiet:
                print(f"welcome: {c.okgreen}{config['welcome']}{c.end}")

        elif (_splitinput[1] == "mode"):
            if (_splitinput[2].lower() == "powershell"):
                config["mode"] = "POWERSHELL"
                MODE = "POWERSHELL"
            elif (_splitinput[2].lower() == "cmd"):
                config["mode"] = "CMD"
                MODE = "CMD"
            if not args.quiet:
                print(f"mode: {c.okgreen}{config['mode']}{c.end}")

        elif (_splitinput[1] == "linux") and platform.system() == "Linux":
            if (_splitinput[2].lower() == "generate"):
                if not args.quiet:
                    print_formatted_text(f"{c.okgreen}This will take a while...{c.end}")
                target = "commands.txt"
                os.system(f'bash -c "compgen -c >{defPath+"/"+target}"')
                if not args.quiet:
                    print(f"generated: {c.okgreen}{target}{c.end}")

        elif (_splitinput[1] == "license"):
            try:
                if _splitinput[2] == "full":
                    if iswindows():
                        f = open(defPath + r"\LICENSE")
                        if not args.quiet:
                            print(f.read())
                    else:
                        f = open(defPath + r"/LICENSE")
                        if not args.quiet:
                            print(f.read())
            except:
                if not args.quiet:
                    print(r"""
    Void-Terminal  Copyright (C) 2020  Tomáš Novák
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `void license full' for details.
            """)

        elif (_splitinput[1] == "version"):
            print(c.okgreen+VERSION+c.end)

        elif (_splitinput[1] == "install"):
            if _splitinput[2] == "chocolatey":
                if isadmin() == True and iswindows():
                    os.system(
                        "powershell -Command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
                elif iswindows():
                    if not args.quiet:
                        print(
                            f"{c.warning}Rerun with administrative privileges: use 'admin' or 'elevate'{c.end}")
                else:
                    if not args.quiet:
                        print(f"{c.fail}Only available on Windows{c.end}")

        elif _splitinput[1] == "title":
            os.system(f"title {_splitinput[-1]}")

        elif _splitinput[1] == "config":
            if not args.quiet:
                print(config)
    except:
        if not args.quiet:
            print(f"{c.fail}Not found{c.end}")

    if not args.skipconfig:
        saveToYml(config, CONFIG)


def read(splitInput) -> None:
    "if not args.quiet: prints text of file"
    fparser = argparse.ArgumentParser(prog="read")
    fparser.add_argument("filename", help="Target filename")
    try:
        fargs = fparser.parse_args(splitInput[1:])
    except SystemExit:
        return

    file = open(fargs.filename, encoding="utf-8")
    content = file.read()

    if not args.quiet:
        print(content)
    file.close()


def performance_toobar():
    gpus = GPUtil.getGPUs()
    try:
        gpu_util = gpus[0].load*100
        gpu_temperature = gpus[0].temperature
    except:
        gpu_util = "0"
        gpu_temperature = "0"

    return HTML(f"CPU: {psutil.cpu_percent()}%  GPU: {gpu_util}% {gpu_temperature}°C")


def power() -> None:
    "Change Windows power scheme"
    if not args.quiet:
        print(f"{c.warning}If you want best powerscheme paste this, then paste ID of the new scheme{c.end}: {c.okgreen}powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61{c.end}")
    os.system("powercfg -list")
    _input = input("Select scheme: ")

    if _input == "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61":
        os.system(_input)
        os.system("powercfg -list")
        _input = input("Paste scheme id: ")
        os.system("powercfg /setactive " + _input)

    else:
        os.system("powercfg /setactive " + _input)

# --------------------------------------------


class Void_Terminal(PromptSession):
    def __init__(self, completer=combinedcompleter, complete_while_typing=config.get("completeWhileTyping"), mouse_support=config.get("mouseSupport"), wrap_lines=config.get("wrapLines"), auto_suggest=AutoSuggestFromHistory(), search_ignore_case=config.get("searchIgnoreCase"), enable_open_in_editor=True, refresh_interval=0, color_depth=ColorDepth.TRUE_COLOR, editing_mode=EditingMode.VI):
        super().__init__(completer=completer,
                         complete_while_typing=complete_while_typing,
                         mouse_support=mouse_support,
                         wrap_lines=wrap_lines,
                         auto_suggest=auto_suggest,
                         search_ignore_case=search_ignore_case,
                         enable_open_in_editor=enable_open_in_editor,
                         refresh_interval=refresh_interval,
                         color_depth=color_depth,
                         editing_mode=editing_mode)
        self.exceptions = config.get("exeptions", tuple())
        self.default_completer = completer
        self.default_auto_suggest = auto_suggest
        self.skipsteam = False if config.get("steamapikey") != "" and config.get("steamurl") != "" else True

        try:
            if not self.skipsteam: steam_api.connect(config["steamapikey"])
            if not self.skipsteam: steam_api.profile(config["steamurl"])
        except: print(f"{c.warning}Cannot contact steam servers{c.end}")

    def password(self, text="Password: "):
        return self.prompt(text, is_password=True, completer=DummyCompleter(
        ), auto_suggest=DummyAutoSuggest(), enable_history_search=False)

    def help(self):
        print("\n" +
              "\n MATH: \n\n"
              f"       {c.fail}+{c.end}   -    Addition\n"
              f"       {c.fail}-{c.end}   -    Subtraction\n"
              f"       {c.fail}*{c.end}   -    Multiplication\n"
              f"       {c.fail}/{c.end}   -    Division\n"
              f"       {c.fail}%{c.end}   -    Modulus\n"
              f"       {c.fail}**{c.end}  -    Exponentiation\n"
              f"       {c.fail}//{c.end}  -    floor division\n\n"

              f"   Other fuctions and constants for chaining from math library, functions need to be called like this: {c.okgreen}f(arguments){c.end}\n\n"
              f"   {c.okgreen}acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cos, cosh, degrees, dist, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp, fsum, gamma, gcd, hypot, inf, isclose, isfinite, isinf, isnan, isqrt, ldexp, lgamma, log, log10, log1p, log2, modf, nan, perm, pi, pow, prime, prod, radians, remainder, sin, sinh, sqrt, tan, tanh, tau, trunc{c.end}\n\n"

              f"   {c.okblue}gcd{c.end} - greatest common divisor: {c.okgreen}gcd [value] [value]{c.end}\n"
              f"   {c.okblue}lcm{c.end} - least common multiple: {c.okgreen}lcm [value] [value]{c.end}\n"
              f"   {c.okblue}rng{c.end} - random number generator: {c.okgreen}rng [min(included)] [max(excluded)]{c.end}\n"

              "\n COMPUTER: \n\n"

              f"   {c.okblue}component{c.end} - info about workstation\n"
              f"   {c.okblue}motherboard, cpu, gpu, ram, disk, network, bootinfo{c.end} - info about your workstation´s component\n"
              f"   {c.okblue}pagefile{c.end} - show pagefile location and size\n"

              "\n WINDOWS DEFINED: \n\n"

              f"   {c.okblue}control{c.end} - control panel\n"
              f"   {c.okblue}diskpart{c.end} - open diskpart\n"
              f"   {c.okblue}msconfig{c.end} - configure your system\n"
              f"   {c.okblue}msinfo32{c.end} - show windows configuration\n"
              f"   {c.okblue}regedit{c.end} - tool for editing registers\n"
              f"   {c.okblue}sysdm.cpl{c.end} - system properties\n"
              f"   {c.okblue}firewall{c.end} - configure firewall settings\n"
              f"   {c.okblue}services{c.end} - configure services\n"
              f"   {c.okblue}manager{c.end} - computer management\n"
              f"   {c.okblue}event{c.end} - event viewer\n"
              f"   {c.okblue}dxdiag{c.end} - DirectX diagnostics tool\n"

              "\n CORE: \n\n"

              f"""   {c.okblue}void{c.end}: - {c.okblue}config{c.end}: prints out current configuration
            - {c.okblue}mode{c.end} {c.okgreen}[ POWERSHELL | CMD ]{c.end}: change mode of executing system commands
            - {c.okblue}install{c.end} {c.okgreen}[ chocolatey ]{c.end}: install packages (will be replaced by winget)
            - {c.okblue}multithreading{c.end} {c.okgreen}[ true | false ]{c.end}: enable multithreading for some commands
            - {c.okblue}mouseSupport{c.end} {c.okgreen}[ true | false ]{c.end}: enable mouse support in terminal
            - {c.okblue}fuzzyComplete{c.end} {c.okgreen}[ true | false ]{c.end}: enable fuzzy completion
            - {c.okblue}completeWhileTyping{c.end} {c.okgreen}[ true | false ]{c.end}: show context menu for autocompletion automatically
            - {c.okblue}wrapLines{c.end} {c.okgreen}[ true | false ]{c.end}: enable wrapping lines in terminal
            - {c.okblue}license{c.end} {c.okgreen}[ full ]{c.end}: show license, show full license
            - {c.okblue}version{c.end} {c.okgreen}[ local | latest ]{c.end}: show current version, pull latest github version tag
            - {c.okblue}welcome{c.end}: show welcome message
            - {c.okblue}updatePythonPackages{c.end}: updates all installed packages
            - {c.okblue}title{c.end} {c.okgreen}[ title ]{c.end}: change title of terminal
\n"""

              f"   {c.okblue}exit, quit{c.end} - quit application\n"
              f"   {c.okblue}os{c.end} - show operating system\n"
              f"   {c.okblue}pwd{c.end} - print out current working directory\n"
              f"   {c.okblue}thread{c.end} - run function in thread: {c.okgreen}thread [function]{c.end}\n"
              f"   {c.okblue}threads{c.end} - print out currently running threads\n"
              f"   {c.okblue}open{c.end} - open file explorer in current directory: {c.okgreen}open [target]{c.end}\n"
              f"   {c.okblue}elevate, admin{c.end} - grant admin permission for shell\n"
              f"   {c.okblue}read{c.end} - read specified file: {c.okgreen}read [target]{c.end}\n"
              f"   {c.okblue}sizeof{c.end} - get size of directory: {c.okgreen}sizeof [folder]{c.end}\n"
              f"   {c.okblue}godmode{c.end} - opens Windows 10 god mode control panel\n"

              "\n ALIAS: \n\n"

              f"   {c.okblue}alias{c.end} - define your own function: {c.okgreen}alias [name | -list] [command(if name)]{c.end}\n"
              f"   {c.okblue}delalias{c.end} - remove alias: {c.okgreen}delalias [name]{c.end}\n"

              "\n HASHING: \n\n"

              f"   {c.okblue}md5, sha1 , sha224, sha256, sha384, sha512{c.end} - hash string\n"
              f"   {c.okblue}md5sum, sha1sum, sha224sum, sha256sum, sha384sum, sha512sum{c.end} - hash file: {c.okgreen}(function) [target]{c.end}\n"

              "\n MULTIMEDIA: \n\n"

              f"   {c.okblue}instaloader{c.end} - download instagram profile: {c.okgreen}instaloader [your username] [target username]{c.end}\n"
              f"   {c.okblue}player{c.end} - play audio or video file from URL or path and configure player class: {c.okgreen}play [url | file]{c.end}\n"
              f"   {c.okblue}ytdown{c.end} - download video from URL: {c.okgreen}ytdown [url]{c.end}\n"

              "\n CURL: \n\n"

              f"   {c.okblue}cheat{c.end} - programmer cheat sheet: {c.okgreen}cheat [querry]{c.end}\n"
              f"   {c.okblue}checklastvid{c.end} - get last youtube video of specified channel: {c.okgreen}checklastvid [channel]{c.end}\n"
              f"   {c.okblue}checklasttweet{c.end} - get last tweet of specified user: {c.okgreen}checklasttweet [channel]{c.end}\n"
              f"   {c.okblue}checktwitchonline{c.end} - get information about specified twitch channel: {c.okgreen}checklastvid [channel]{c.end}\n"
              f"   {c.okblue}fileconverter{c.end} - convert files to other types: {c.okgreen}fileconverter [input type] [output type] [target] [new file name]{c.end}\n"
              f"   {c.okblue}ping.gg{c.end} - server monitoring utility\n"
              f"   {c.okblue}guid{c.end} - generate random GUID\n"
              f"   {c.okblue}dns{c.end} - get dns information\n"
              f"   {c.okblue}shorten{c.end} - make url shorter: {c.okgreen}shorten [target]{c.end}\n"
              f"   {c.okblue}transfer{c.end} - temporarily upload a file to server: {c.okgreen}transfer [target]{c.end}\n"
              f"   {c.okblue}speedtest{c.end} - check internet connection speed\n"
              f"   {c.okblue}weather{c.end} - check weather, if no location specified, check local weather: {c.okgreen}weather [location(optional) | moon(optional)]{c.end}\n"
              f"   {c.okblue}covid19{c.end} - display status of current covid19 situation in country: {c.okgreen}covid19 [location(optional)]{c.end}\n"
              f"   {c.okblue}ip{c.end} - get your external IP address\n"
              f"   {c.okblue}geoip{c.end} - get your external IP address and location: {c.okgreen}geoip [target(optional)]{c.end}\n"
              f"   {c.okblue}qrcode{c.end} - make qrcode out of user input: {c.okgreen}qrcode [text]{c.end}\n"
              f"   {c.okblue}stonks{c.end} - get stock information: {c.okgreen}stonks [target]{c.end}\n"
              f"   {c.okblue}cryptocurrency{c.end} - get cryptocurrency information: {c.okgreen}cryptocurrency [currency | currency@time | :help]{c.end}\n"

              "\n OTHER FUNCTIONS \n\n"

              f"   {c.okblue}downloadeta{c.end} - calculate estimated time of arival: {c.okgreen}downloadeta [target](GB,MB,KB) [speed](GB,MB,KB){c.end}\n"
              f"   {c.okblue}convert{c.end} - function for converting temperatures, colors to hex, audio or video files\n"
              f"   {c.okblue}power{c.end} - change your Windows powerplan\n"
              f"   {c.okblue}plain2string{c.end} - convert plain text to strings: {c.okgreen}plain2string mode[space,file, fileline] text/[filename]{c.end}\n"
              f"   {c.okblue}autoclicker{c.end} - integrated autoclicker\n"
              f"   {c.okblue}steam{c.end} - get Steam information (requires steamapikey in config): {c.okgreen}steam [name]{c.end}\n"
              f"   {c.okblue}game-deals{c.end} - get best deals on games from more than 30 stores\n"
              )

    def switch(self, userInput: str) -> None:
        userInput = userInput.replace("\\", "\\\\")
        splitInput = shlex.split(userInput)

        global LASTDIR
        global VOLUME
        try:
            arg = argget(splitInput[1:])
        except:
            pass
        if splitInput == []:
            return

        if splitInput[0].lower() in self.exceptions:
            if iswindows():
                if MODE == "CMD":
                    os.system(userInput)
                elif MODE == "POWERSHELL":
                    os.system(f"powershell -Command {userInput}")
            else:
                os.system(f'bash -c "{userInput}"')
            return

        if splitInput[0].lower() == "wifipassword":
            wifipassword()
            return

        if splitInput[0].lower() == "thread":
            fparser = argparse.ArgumentParser(prog="thread")
            fparser.add_argument("function", help="Fuction to run")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            thread = Thread(target=self.switch, args=splitInput[1:])
            thread.start()
            return

        if splitInput[0].lower() == "ls" and iswindows():
            os.system("dir")
            return

        if splitInput[0].lower() == "pwd" and iswindows():
            print(c.okgreen+os.getcwd()+c.end)
            return

        if splitInput[0].lower() == "instaloader":
            fparser = argparse.ArgumentParser(prog="instaloader")
            fparser.add_argument("login", help="Your instagram username")
            fparser.add_argument("target", help="Targeted instagram profile")
            fparser.add_argument(
                "-q", "--quiet", type=bool, choices=[False, True])
            fparser.add_argument("--user-agent")
            fparser.add_argument("--sleep", type=bool, choices=[False, True])
            fparser.add_argument("--download-pictures")
            fparser.add_argument("--dirname-pattern")
            fparser.add_argument("--filename-pattern",
                                 type=bool, choices=[False, True])
            fparser.add_argument("--download-videos",
                                 type=bool, choices=[False, True])
            fparser.add_argument("--download-video-thumbnails",
                                 type=bool, choices=[False, True])
            fparser.add_argument("--download-geotags",
                                 type=bool, choices=[False, True])
            fparser.add_argument("--download-comments",
                                 type=bool, choices=[False, True])
            fparser.add_argument(
                "--save-metadata", type=bool, choices=[False, True])
            fparser.add_argument(
                "--compress-json", type=bool, choices=[False, True])
            fparser.add_argument("--post-metadata-pattern")
            fparser.add_argument("--storyitem-metadata-txt-pattern")
            fparser.add_argument("--max-connection-attempts",
                                 type=int, choices=[False, True])
            fparser.add_argument("--request-timeout",
                                 type=int, choices=[False, True])
            fparser.add_argument("--rate-controller")
            fparser.add_argument("--resume-prefix")
            fparser.add_argument("--check-resume-bbd",
                                 type=bool, choices=[False, True])
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            import instaloader
            loader = instaloader.Instaloader(
                quiet=fargs.quiet if fargs.quiet else False,
                user_agent=fargs.user_agent if fargs.user_agent else None,
                sleep=fargs.sleep if fargs.sleep else True,
                dirname_pattern=fargs.dirname_pattern if fargs.dirname_pattern else None,
                filename_pattern=fargs.filename_pattern if fargs.filename_pattern else None,
                download_pictures=fargs.download_pictures if fargs.download_pictures else True,
                download_videos=fargs.download_videos if fargs.download_videos else True,
                download_video_thumbnails=fargs.download_video_thumbnails if fargs.download_video_thumbnails else True,
                download_geotags=fargs.download_geotags if fargs.download_geotags else True,
                download_comments=fargs.download_comments if fargs.download_comments else True,
                save_metadata=fargs.save_metadata if fargs.save_metadata else True,
                compress_json=fargs.compress_json if fargs.compress_json else True,
                post_metadata_txt_pattern=fargs.post_metadata_pattern if fargs.post_metadata_pattern else None,
                storyitem_metadata_txt_pattern=fargs.storyitem_metadata_txt_pattern if fargs.storyitem_metadata_txt_pattern else None,
                max_connection_attempts=fargs.max_connection_attempts if fargs.max_connection_attempts else 3,
                request_timeout=fargs.request_timeout if fargs.request_timeout else None,
                rate_controller=fargs.rate_controller if fargs.rate_controller else None,
                resume_prefix=fargs.resume_prefix if fargs.resume_prefix else 'iterator',
                check_resume_bbd=fargs.check_resume_bbd if fargs.check_resume_bbd else True
            )

            loader.login(fargs.login, self.password())
            loader.download_profile(fargs.target, download_stories=True)
            return

        if splitInput[0] == "downloadeta":
            fparser = argparse.ArgumentParser(prog="downloadeta")
            fparser.add_argument("target", help="Targeted download size")
            fparser.add_argument("speed", help="Speed of your connection")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            out = []
            mdict = {
                "KB": "1000",
                "MB": "1000000",
                "GB": "1000000000",
                "TB": "1000000000000",
                "PB": "1000000000000000",
            }
            for item in [fargs.target, fargs.speed]:
                for multiplier in ["KB", "MB", "GB", "TB", "PB"]:
                    if str(item).find(multiplier) != -1:
                        item = item.replace(multiplier, "")
                        m = mdict.get(multiplier)
                        out.append(float(item) * float(m))
            target = out[0]
            speed = out[1]

            if not args.quiet:
                print(core.utils.time_reformat(target / speed))
            return

        if splitInput[0].lower() == "back":
            __placeholder = os.getcwd()
            if LASTDIR == "":
                return
            os.chdir(LASTDIR)
            if __placeholder != LASTDIR:
                LASTDIR = __placeholder
            return

        elif (splitInput[0].lower() == "elevate" or splitInput[0].lower() == "admin"):
            core.elevate.elevate()
            return

        elif splitInput[0].lower() == "tcp-scan":
            fparser = argparse.ArgumentParser(prog="tcp-scan")
            fparser.add_argument(
                "--target", help="Remote target to scan", type=str, default="127.0.0.1")
            fparser.add_argument("--threads", type=int,
                                 help="Number of threads", default=250)
            fparser.add_argument("--port", "-p", type=int, help="Port to scan")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            import socket
            import time
            from queue import Queue

            threading_lock = threading.Lock()
            target = socket.gethostbyname(fargs.target)
            q = Queue()

            def portscanTCP(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target, known_ports[port-1]))
                    with threading_lock:
                        print_formatted_text(HTML(
                            f'<style fg="red">TCP</style> <style fg="blue">{target}</style> <style fg="green">{known_ports[port-1]}</style> is open (<style fg="green">{known_port_names.get(str(known_ports[port-1]), "unknown")}</style>)'))
                    con.close()
                except:
                    pass

            def threader():
                worker = q.get()
                portscanTCP(worker)
                q.task_done()

            for i in range(len(known_ports)):
                t = threading.Thread(target=threader)
                t.setName("TCP-Scanner-"+str(i))
                t.start()

            start = time.time()

            if fargs.port:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((target, fargs.port))
                    print_formatted_text(
                        f'{c.fail}TCP{c.end} {c.okblue}{target}{c.end} {c.okgreen}{fargs.port}{c.end} is open')
                    print_formatted_text(HTML(
                        f'<style fg="red">TCP</style> <style fg="blue">{target}</style> <style fg="green">{fargs.port}</style> is open (<style fg="green">{known_port_names.get(str(fargs.port),"unknown")}</style>)'))
                    s.close()
                except:
                    s.close()
            else:
                for worker in range(1, 1001):
                    q.put(worker)

            q.join()
            end = time.time()
            print(f"It took: {c.okgreen}{end-start}{c.end} seconds")

        elif splitInput[0].lower() == "convert":
            core.utils.convert(splitInput)

        elif splitInput[0].lower() == "ytdown":
            try:
                core.utils.ytdown(splitInput)
            except: pass
            return

        elif splitInput[0].lower() == "player":
            parent_parser = argparse.ArgumentParser("player")
            sub_parsers = parent_parser.add_subparsers(dest="function")
            
            play_parser = sub_parsers.add_parser("play")
            play_parser.add_argument(
                "TARGET", help="Filename, URL or text file with URLs", type=str)
            play_parser.add_argument(
                "--volume", help="Set default volume ( 0 - 130 )", type=int, default=VOLUME)
            play_parser.add_argument("-r", "--resolution",
                                help="Set resolution target", type=int)
            play_parser.add_argument("--fps", help="Set fps target", type=int)
            play_parser.add_argument(
                "--raw", help="Raw argumets to pass to the MPV", type=str)
            play_parser.add_argument(
                "--maxvolume", help="Set maximum volume ( 100 - 1000 )", type=int, default=130)
            play_parser.add_argument(
                "-f", "--format", help="Select stream ( best,worst,140 etc. )")
            play_parser.add_argument(
                "-t", "--title", help="Querry instead of URL", action="store_true", default=False)

            volume_parser = sub_parsers.add_parser("volume")
            volume_parser.add_argument(
                    "volume", help="Set default volume ( 0 - MAXVOLUME )", type=int)
            volume_parser.add_argument(
                "-n", "--no-updating", help="Do not update global variable VOLUME", action="store_true")

            pause_parser = sub_parsers.add_parser("pause")
            next_parser = sub_parsers.add_parser("next")
            prev_parser = sub_parsers.add_parser("prev")
            terminate_parser = sub_parsers.add_parser("terminate")

            try:
                fargs = parent_parser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if fargs.function == "play":
                if fargs.format: _format = fargs.format
                elif fargs.fps or fargs.resolution: _format = f"bestvideo{f'[height<=?{fargs.resolution}]' if fargs.resolution else ''}{f'[fps<=?{fargs.resolution}]' if fargs.resolution else ''}+bestaudio/best"
                else: _format = "bestvideo+bestaudio"

                try:
                    self.mpv
                except:
                    self.mpv = player.Player(volume=fargs.volume, volume_max=fargs.maxvolume, _format=_format, search=True if fargs.title else False)

                def run():
                    self.mpv.global_play(fargs.TARGET)
                thread = Thread(target=run)
                thread.start()

            elif fargs.function == "volume":
                try:
                    self.mpv["volume"] = fargs.volume
                    VOLUME = fargs.volume
                    config["volume"] = fargs.volume
                    saveToYml(config, CONFIG)
                except:
                    print(f"{c.fail}Player not initialized{c.end}")
                    if fargs.no_updating:
                        return
                    else:
                        VOLUME = fargs.volume
                        config["volume"] = fargs.volume
                        saveToYml(config, CONFIG)
                        print(
                            f"{c.okgreen}Default volume for new instances updated{c.end}")

            elif fargs.function == "pause":
                try:
                    self.mpv.keypress("p")
                except:
                    print(f"{c.fail}Player not initialized{c.end}")

            elif fargs.function == "next":
                try:
                    self.mpv.playlist_next()
                except:
                    print(f"{c.fail}Player not initialized{c.end}")

            elif fargs.function == "prev":
                try:
                    self.mpv.playlist_prev()
                except:
                    print(f"{c.fail}Player not initialized{c.end}")

            elif fargs.function == "terminate":
                try:
                    self.mpv.terminate()
                except:
                    print(f"{c.fail}Player not initialized{c.end}")

        elif splitInput[0].lower() == "steam" and not self.skipsteam:
            parent_parser = argparse.ArgumentParser(prog="steam")
            sub_parsers = parent_parser.add_subparsers(dest="function")
            
            user_parser = sub_parsers.add_parser("user")
            user_parser.add_argument("ID",type=int)
            friends_parser = sub_parsers.add_parser("friends")
            me_parser = sub_parsers.add_parser("me")

            game_parser = sub_parsers.add_parser("game")
            game_parser.add_argument("name", help="Name of game", type=str)
            
            try:
                fargs = parent_parser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if fargs.function == "user":
                try:
                    steam_api.profileID(fargs.ID)
                except Exception as e: print(f"{c.fail}{e}{c.end}")
                return

            elif fargs.function == "friends":
                try:
                    print(steam_api.friends())
                except Exception as e: print(f"{c.fail}{e}{c.end}")
                return

            elif fargs.function == "me":
                try:
                    me = steam_api.SteamUser(steam_api.me.id)
                    print(f"""
{c.bold}Name{c.end}: {c.okgreen}{me.name}{c.end}

Real name: {c.okgreen}{me.real_name}{c.end}
ID: {c.okgreen}{me.id}{c.end}
URL: {c.okgreen}{me.profile_url}{c.end}
Avatar: {c.okgreen}{me.avatar_full}{c.end}
State: {c.okgreen}{me.state}{c.end}
Games owned: {c.okgreen}{len(me.owned_games)}{c.end}
Friends: {c.okgreen}{len(me.friends)}{c.end}
Badges: {c.okgreen}{len(me.badges)}{c.end}

Last online: {c.okgreen}{me.last_logoff}{c.end}
Recently played: {c.okgreen}{me.recently_played}{c.end}
Playing: {c.okgreen}{me.currently_playing}{c.end}
Group: {c.okgreen}{me.group}{c.end}
Level: {c.okgreen}{me.level}{c.end}
Privacy: {c.okgreen}{me.privacy}{c.end}

VAC: {c.okgreen}{me.is_vac_banned}{c.end}
Country code: {c.okgreen}{me.country_code}{c.end}
""") 
                except Exception as e: print(f"{c.fail}{e}{c.end}")
                return

            elif fargs.function == "game":
                try:
                    import difflib
                    print_formatted_text("Loading Steam store details...")

                    initial_list = requests.get(
                        r"http://api.steampowered.com/ISteamApps/GetAppList/v0001/").json()["applist"]["apps"]["app"]
                    game_list = dict()
                    games = []

                    for i in initial_list:
                        game_list[i["name"].lower()] = i["appid"]
                        games.append(i["name"].lower())

                    print_formatted_text(
                        f"Closest results: {difflib.get_close_matches(fargs.name.lower(), games)}")
                    id = game_list[difflib.get_close_matches(
                        fargs.name.lower(), games)[0]]

                    content = requests.get(
                        f"https://store.steampowered.com/api/appdetails?appids={id}").json()
                    content = content.get(str(id))["data"]

                    name = content.get("name", "Unknown")
                    age = content.get("required_age", "Unknown")
                    publisher = content.get("publishers", "Unknown")
                    discount = content.get("price_overview", {}).get(
                        "discount_percent", "Unknown")
                    price = content.get("price_overview", {}).get(
                        "final_formatted", "Unknown")
                    metacritic = content.get("metacritic", {})
                    categories = content.get("categories", "Unknown")
                    genres = content.get("genres", "Unknown")
                    recommendations = content.get(
                        "recommendations", {}).get("total", "Unknown")
                    achievements = content.get(
                        "achievements", {}).get("total", "Unknown")
                    release_date = content.get(
                        "release_date", {}).get("date", "Unknown")
                    game_type = content.get("type", "Unknown")

                    category_names = []
                    for i in categories:
                        category_names.append(i.get("description", "Unknown"))

                    genre_names = []
                    for i in genres:
                        genre_names.append(i.get("description", "Unknown"))

                    print(f"""
{c.bold}Name{c.end}: {c.okgreen}{name}{c.end}

Release date: {c.okgreen}{release_date}{c.end}

Publisher: {c.okgreen}{publisher}{c.end}
Category: {c.okgreen}{category_names}{c.end}
Genre: {c.okgreen}{genre_names}{c.end}
Age: {c.okgreen}{age}{c.end}

Metacritic: {c.okgreen}{metacritic.get("score", "Unknown")} ({c.end}{c.okblue}{metacritic.get("url", "Unknown")}{c.end})
Recommendations: {c.okgreen}{recommendations}{c.end}
Price: {c.okgreen}{price}{c.end}
Discount: {c.okgreen}{discount}%{c.end}
Achievements: {c.okgreen}{achievements}{c.end}
Type: {c.okgreen}{game_type}{c.end}

URL: {c.okgreen}{f"https://store.steampowered.com/app/{id}"}{c.end}
            """)
                except Exception as e: print(f"{c.fail}{e}{c.end}")
                return

        elif splitInput[0].lower() == "game-deals":
            try:
                from tabulate import TableFormat, tabulate
                response = requests.get(
                    "https://www.cheapshark.com/api/1.0/deals").json()

                l = list()

                for game in response:
                    l.append([game["title"], game["salePrice"], game["savings"]+"%", storeID.get(
                        game["storeID"]), f"https://www.cheapshark.com/redirect?dealID={game['dealID']}"])
                print(tabulate(l,["Title", "Price", "Discount", "Store", "URL"]))
            except Exception as e: print(f"{c.fail}{e}{c.end}")
            return

        elif splitInput[0].lower() == "grantfiles" and iswindows():
            fparser = argparse.ArgumentParser(prog="grantfiles")
            fparser.add_argument(
                "--target", "-t", help="Target folder", type=str)
            fparser.add_argument(
                "--user", "-u", help="User who grants permisions to those files", type=str)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            os.system(
                f'ICACLS "{fargs.target if fargs.target else "."}" /INHERITANCE:e /GRANT:r {fargs.user if fargs.user else "%USERNAME%"}:(F) /T /C ')
            return

        elif splitInput[0].lower() == "brightness":
            try:
                target = splitInput[1]
                core.utils.setbrightness(target)
                if args.verbose:
                    if not args.quiet:
                        print(f"Brightness set to {c.okgreen}{target}{c.end}")
            except:
                core.utils.getbrightness()
            return

        elif splitInput[0].lower() == "cheat":
            text = splitInput[1:]
            out = ""
            for item in text:
                if item != text[-1]:
                    out += item + "/"
                else:
                    out += item
            os.system(f"curl cht.sh/{out}")
            return

        elif splitInput[0].lower() == "checklastvid":
            os.system(
                f'curl -s "https://decapi.me/youtube/latest_video?user={argget(splitInput[1:])}"')
            print()
            return

        elif splitInput[0].lower() == "checklasttweet":
            os.system(
                f'curl -s "https://decapi.me/twitter/latest?name={argget(splitInput[1:])}"')
            print()
            return

        elif splitInput[0].lower() == "checktwitchonline":
            os.system(
                f'curl -s "https://decapi.me/twitch/uptime?channel={argget(splitInput[1:])}"')
            print()
            return

        elif splitInput[0].lower() == "fileconvert":
            fparser = argparse.ArgumentParser(prog="fileconvert")
            fparser.add_argument("fromformat", help="From format", type=str)
            fparser.add_argument("to", help="To format", type=str)
            fparser.add_argument("file", help="File to convert", type=str)
            fparser.add_argument("output", help="Output file", type=str)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            os.system(
                f'curl "http://c.docverter.com/convert" -F from={fargs.fromformat} -F to={fargs.to} -F "input_files[]=@{fargs.file}" -o "{splitInput[4]}"')
            return

        elif splitInput[0].lower() == "ping.gg":
            try:
                os.system("curl ping.gg/"+splitInput[1])
            except:
                os.system("curl ping.gg")
            return

        elif splitInput[0].lower() == "guid":
            os.system("curl givemeguid.com")
            if not args.quiet:
                print()
            return

        elif splitInput[0].lower() == "shorten":
            os.system(f'curl -F shorten="{splitInput[1]}" https://ttm.sh')
            return

        elif splitInput[0].lower() == "transfer":
            os.system(
                f'curl -F file=@"{argget(splitInput[1])}" https://ttm.sh')
            return

        elif splitInput[0].lower() == "dns":
            os.system("curl -L https://edns.ip-api.com/json")
            print()
            return

        elif splitInput[0].lower() == "speedtest":
            os.system(
                "curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -")
            return

        elif splitInput[0].lower() == "cryptocurrency":
            try:
                os.system("curl rate.sx/"+splitInput[1])
            except:
                os.system("curl rate.sx")
            return

        elif splitInput[0].lower() == "weather":
            try:
                os.system("curl wttr.in/"+splitInput[1])
            except:
                os.system("curl wttr.in")
            return

        elif splitInput[0].lower() == "covid19":
            try:
                os.system("curl https://corona-stats.online/"+splitInput[1])
            except:
                os.system("curl https://corona-stats.online/")
            return

        elif splitInput[0].lower() == "ip":
            run_command("curl api.ipify.org")
            print()
            return

        elif splitInput[0].lower() == "geoip":
            try:
                run_command("curl ipinfo.io/"+splitInput[1])
            except:
                run_command("curl ipinfo.io")
            print()
            return

        elif splitInput[0].lower() == "qrcode":
            try:
                os.system("curl qrenco.de/"+splitInput[1])
            except:
                if not args.quiet:
                    print(f"{c.warning}Invalid argument{c.end}")
            return

        elif splitInput[0].lower() == "stonks":
            try:
                os.system("curl stonks.icu/"+splitInput[1])
            except:
                if not args.quiet:
                    print("Invalid argument: eg. stonks amd/intl/tsla")
            return

        elif splitInput[0].lower() == "pagefile":
            os.system("wmic pagefile list")
            return

        elif splitInput[0].lower() == "threads":
            print(
                f"Active threads: {c.warning}{threading.activeCount()}{c.end}\n")
            for t in threading.enumerate():
                print("{:<30} {:<30}".format(t.name, t.is_alive()))
            return

        elif splitInput[0].lower() == "interface":
            if splitInput[1].lower() == "enable":
                os.system("wmic nic get name, index")
                index = input("Device index: ")
                if index == "":
                    return
                os.system(
                    f"wmic path win32_networkadapter where index={index} call enable")
            elif splitInput[1].lower() == "disable":
                os.system("wmic nic get name, index")
                index = input("Device index: ")
                if index == "":
                    return
                os.system(
                    f"wmic path win32_networkadapter where index={index} call disable")
            return

        elif splitInput[0].lower() == "online":
            urls = splitInput[1:]
            for url in urls:
                try:
                    response = requests.get(url)
                    if not args.quiet:
                        print(f"{url} {c.okgreen}OK{c.end}: {response.elapsed.total_seconds()}s" if response.ok ==
                              True else f"{c.fail}SITE DOWN{c.end}")
                except:
                    if not args.quiet:
                        print(url + f" {c.fail}SITE DOWN{c.end}")

        elif splitInput[0].lower() == "poweroff":
            fparser = argparse.ArgumentParser(prog="poweroff")
            fparser.add_argument(
                "--time", "-t", help="Time to shutdown", type=int)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            os.system(f"shutdown /s /f /t {fargs.time if fargs.time else '0'}")
            return

        elif splitInput[0].lower() == "reboot":
            fparser = argparse.ArgumentParser(prog="reboot")
            fparser.add_argument(
                "--time", "-t", help="Time to reboot", type=int)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            os.system(f"shutdown /r /f /t {fargs.time if fargs.time else '0'}")
            return

        elif splitInput[0].lower() == "motherboard":
            os.system(
                "wmic baseboard get product,Manufacturer,version,serialnumber")
            return

        elif splitInput[0].lower() == "ram":
            core.utils.memory()
            return

        elif splitInput[0].lower() == "cpu":
            core.utils.cpu()
            return

        elif splitInput[0].lower() == "gpu":
            core.utils.gpu()
            return

        elif splitInput[0].lower() == "network":
            core.utils.network()
            return

        elif splitInput[0].lower() == "disk":
            core.utils.disk()
            return

        elif splitInput[0].lower() == "bootinfo":
            core.utils.bootinfo()
            return

        elif splitInput[0].lower() == "component":
            core.utils.sysinfo()
            core.utils.cpu()
            core.utils.gpu()
            core.utils.memory()
            core.utils.bootinfo()
            core.utils.disk()
            core.utils.network()
            return

        elif splitInput[0].lower() == "firewall":
            os.system("WF.msc")
            return

        elif splitInput[0].lower() == "services":
            os.system("services.msc")
            return

        elif splitInput[0].lower() == "manager":
            os.system("compmgmt.msc")
            return

        elif splitInput[0].lower() == "event":
            os.system("eventvwr.msc")
            return

        elif splitInput[0].lower() in ["sha1","sha224","sha256","sha384","sha384","sha512","md5","sha1sum","sha224sum","sha256sum","sha384sum","sha512sum","md5sum"]:
            print(hashing.hash(splitInput))

        elif splitInput[0].lower() == "power":
            power()
            return

        elif splitInput[0].lower() == "godmode" and iswindows():
            os.system("mkdir GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
            os.system(
                "explorer GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
            os.system("rmdir GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")

        # --------------------------------------------------------------

        elif splitInput[0].lower() == "plain2string":
            if not args.quiet:
                print(core.utils.PlainToString(splitInput))
            return

        # if not args.quiet: print cmd help and defined help at the same time
        elif splitInput[0].lower() == "help":
            if iswindows():
                os.system("help")
                if not args.quiet:
                    self.help()
            else:
                call("bash -c help", shell=True)
                self.help()

            return

        elif splitInput[0].lower() == "welcome":
            welcome()
            return

        elif splitInput[0].lower() == "search":
            open_new_tab(url="https://www.google.com/search?q=" +
                         " ".join(splitInput[1:]))

        elif splitInput[0].lower() == "sizeof":
            def get_size(start_path='.'):
                total_size = 0
                for dirpath, dirnames, filenames in os.walk(start_path):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        # skip if it is symbolic link
                        if not os.path.islink(fp):
                            total_size += os.path.getsize(fp)

                return total_size
            if not args.quiet:
                print(get_size(splitInput[1]) /
                      1000000, f"{c.okgreen}MB{c.end}")

        elif splitInput[0].lower() == "currencyconverter":
            fparser = argparse.ArgumentParser(prog="currencyconverter")
            fparser.add_argument("base", help="Base currency", type=str)
            fparser.add_argument("other", help="Target currency", type=str)
            fparser.add_argument(
                "amount", help="Amount to convert", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            try:
                rate = core.utils.currencyconverter(
                    fargs.base.upper(), fargs.other.upper())
                if not args.quiet:
                    print(
                        f"{(rate * float(fargs.amount)).__round__(2)} {c.okgreen}{fargs.other}{c.end}")
            except: print(f"{c.fail}Server unreachable{c.end}")
            return

        elif splitInput[0] == "os":  # Show os
            if not args.quiet:
                print(core.osBased.Os())
            return

        elif splitInput[0].lower() == "clear" or splitInput[0].lower() == "cls":  # Clear terminal
            core.osBased.Clear()
            return

        elif splitInput[0].lower() == "read":
            read(splitInput)
            return

        elif splitInput[0].lower() == "void":
            void(splitInput)
            return

        elif splitInput[0].lower() == "compile":
            call(f'auto-py-to-exe -c config.json', shell=True)
            return

        elif splitInput[0].lower() == "autoclicker":
            fparser = argparse.ArgumentParser(prog="autoclicker")
            fparser.add_argument(
                "--right", help="Use right mouse button instead of left", action="store_true")
            fparser.add_argument(
                "--delay", help="Delay in seconds", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            clicker = autoclicker.Autoclicker(
                autoclicker.Button.left if not fargs.right else autoclicker.Button.right, fargs.delay if fargs.delay else 0.05)
            clicker.start()
            return

        elif splitInput[0].lower() == "lcm":
            fparser = argparse.ArgumentParser(prog="lcm")
            fparser.add_argument("value", nargs="+",
                                 type=int, help="List of numbers")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                print(core.utils.lcm(fargs.value))
            return

        elif splitInput[0].lower() == "gcd":
            fparser = argparse.ArgumentParser(prog="gcd")
            fparser.add_argument("value", nargs="+",
                                 type=int, help="List of numbers")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                print(core.utils.find_gcd(fargs.value))
            return

        elif splitInput[0].lower() == "prime":
            fparser = argparse.ArgumentParser(prog="prime")
            fparser.add_argument("value", nargs="+",
                                 type=int, help="List of numbers")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                core.utils.prime(fargs.value)
            return

        elif splitInput[0].lower() == "rng":
            fparser = argparse.ArgumentParser(prog="rng")
            fparser.add_argument("first", help="First number", type=float)
            fparser.add_argument("second", help="Second number", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                print(core.utils.rng(fargs.first, fargs.second))
            return

        elif splitInput[0].lower() == "open" and iswindows():  # Open file explorer in cwd
            target = splitInput[1]
            if target != "":
                os.system(f"explorer {target}")
            else:
                os.system("explorer .\\")
            return

        elif splitInput[0].lower() == "settings" and iswindows():  # Open file explorer in cwd
            os.system("start ms-settings:")
            return

        elif splitInput[0].lower() == "startup" and iswindows():
            os.system(
                r"explorer %AppData%\Microsoft\Windows\Start Menu\Programs\Startup")

        # Check if your password is in someones dictionary
        elif splitInput[0].lower() == "pwned":
            try:
                if not args.quiet:
                    print(pwned.lookup_pwned_api(splitInput[1]))
            except:
                if not args.quiet:
                    print(f"{c.fail}Error{c.end}")

            return

        # Change directory based on input
        elif splitInput[0].lower() == "cd" and arg:
            if os.getcwd() != LASTDIR:
                LASTDIR = os.getcwd()
            os.chdir(splitInput[1])
            return

        # Terminate application
        elif splitInput[0].lower() == "exit" or splitInput[0].lower() == "quit":
            try:
                self.player.terminate()
            finally:
                _exit()

        elif splitInput[0].lower() == "alias":  # Define own function and save it
            if splitInput[1] == "-list":
                if not args.quiet:
                    print(aliases)
            else:
                l = splitInput[2:]
                try:
                    splitInput[2]
                except:
                    if not args.quiet:
                        print(f"{c.warning}No command specified{c.end}")
                    return
                complete = " ".join(l)
                aliases[splitInput[1]] = complete
                WriteAliases(aliases)
            return

        # Remove alias from dictionary and update save
        elif splitInput[0].lower() == "delalias":
            try:
                aliases.pop(splitInput[1])
                WriteAliases(aliases)
            except:
                if not args.quiet:
                    print(
                        f"{c.fail}Name is not in list !{c.end} \nUsage: {c.okgreen}delalias [name]{c.end}")

        elif splitInput[0].lower() == "eval":  # Show alias dictionary
            while True:
                try:
                    _eval = self.prompt(message=HTML(f"<user>{USER}</user> <path>eval</path>""<pointer> > </pointer>"), style=_style,
                                        complete_in_thread=config["multithreading"], set_exception_handler=True, color_depth=ColorDepth.TRUE_COLOR, completer=None,
                                        bottom_toolbar=performance_toobar() if config["perfmon"] else None)
                    if _eval.lower() == "quit" or _eval.lower() == "exit":
                        break
                    else:
                        eval(compile(_eval, "<string>", "exec"))
                except Exception as e:
                    if not args.quiet:
                        print(f"{c.fail}{e}{c.end}")
            return

        elif splitInput[0].lower() == "download":
            fparser = argparse.ArgumentParser(prog="download")
            fparser.add_argument("URL")
            fparser.add_argument("-o","--output", help="Output filename")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if fargs.output:
                filename = fargs.output
            else:
                filename = fargs.URL.split("/")[-1]

            os.system(f"curl {fargs.URL} -o {filename}")

        else:
            try:
                output = eval(userInput)
                if type(output) not in [object, type(dir)]:
                    if not args.quiet:
                        print(output)
                else:
                    raise Exception
            except:
                try:
                    if os.getcwd() != LASTDIR:
                        LASTDIR = os.getcwd()
                    os.chdir(userInput)
                except:
                    if MODE == "CMD":
                        os.system(userInput)
                    else:
                        if config["multithreading"]:
                            def run_async():
                                if iswindows():
                                    e = run_command(
                                        f'powershell -c "{userInput}"')
                                    print(f"{c.bold}Error code: {e}{c.end}")
                                else:
                                    e = run_command(f'bash -c "{userInput}"')
                                    print(f"{c.bold}Error code: {e}{c.end}")
                            __thread = Thread(target=run_async)
                            __thread.start()
                        else:
                            if iswindows():
                                os.system(f'powershell -c "{userInput}"')
                            else:
                                os.system(f'bash -c "{userInput}"')
                    

    def main(self) -> None:
        """
        Terminal main loop
        """
        try:
            remote = core.utils.version()
            if version.parse(VERSION) < version.parse(remote):
                print("Update is available")
        except: pass

        if args.directory:
            try:
                os.chdir(args.directory)
            except:
                if not args.quiet:
                    print(f"{c.fail}Directory not found or accessible{c.end}")
                return

        if config.get("welcome") or args.welcome:
            welcome()
        while True:
            try:
                cd = os.getcwd()  # Get current working directory
                promptMessage = HTML(str(config["prompt"]).replace("USERDOMAIN",USERDOMAIN).replace("USER",USER).replace("PATH",cd).replace("TCOUNT",str(threading.active_count())).replace("VOLUME", str(VOLUME)).replace("ROOT","#" if isadmin() == True else "$"))

                userInput = self.prompt(enable_history_search=True, completer=self.default_completer, auto_suggest=self.default_auto_suggest, is_password=False, message=promptMessage,
                                        style=_style, complete_in_thread=config[
                                            "multithreading"], color_depth=ColorDepth.TRUE_COLOR,
                                        bottom_toolbar=performance_toobar() if config["perfmon"] else None)  # Get user input (autocompetion allowed)

                userInput = self.envirotize(userInput)

                if args.echo:
                    if not args.quiet:
                        print(f"{c.okgreen}{userInput}{c.end}")

                if " & " in userInput:
                    for i in userInput.split("&"):
                        self.switch(userInput=i)
                else:
                    self.switch(userInput=userInput)

            except KeyboardInterrupt:
                if not args.quiet:
                    print()
            except Exception as error:
                if not args.quiet:
                    print_formatted_text(f"{c.fail}{traceback.format_exc()}{c.end}")
                    if iswindows():
                        os.system("pause")

    def envirotize(self, string) -> str:
        "Applies Environment variables"
        import re

        def expandvars(string, default=None, skip_escaped=False):
            """Expand environment variables of form $var and ${var}.
            If parameter 'skip_escaped' is True, all escaped variable references
            (i.e. preceded by backslashes) are skipped.
            Unknown variables are set to 'default'. If 'default' is None,
            they are left unchanged.
            """
            def replace_var(m):
                return os.environ.get(m.group(2) or m.group(1), m.group(0) if default is None else default)
            reVar = (r'(?<!\\)' if skip_escaped else '') + \
                r'\$(\w+|\{([^}]*)\})'
            return re.sub(reVar, replace_var, string)

        values = aliases.keys()
        if not "delalias" in string:
            for value in values:
                if string.find(value) != -1:
                    string = string.replace(value, aliases.get(value))

        splitInput = string.split()

        for i in splitInput:
            if i.find("%") != -1:
                spl = i.split("%")[1]
                env = os.environ[spl]
                splitInput[splitInput.index(i)] = splitInput[splitInput.index(
                    i)].replace(f"%{spl}%", env)

        rebuild = " ".join(splitInput)
        rebuild = expandvars(rebuild)

        if string != rebuild:
            string = rebuild

        return string

def main():
    app = Void_Terminal()

    if args.command:
        userInput = app.envirotize(args.command)

        app.switch(userInput)
        sys.exit(0)
    else:
        with patch_stdout(app):
            app.main()

if __name__ == "__main__":
    main()
