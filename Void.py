#! /usr/bin/env python3
# Project V01D-Terminal

import argparse
import shlex
from subprocess import call
import threading
from threading import Thread
from webbrowser import open_new_tab
from math import *
import platform
import os
import sys

os.environ["PATH"] = os.path.dirname(
    __file__) + os.pathsep + os.environ["PATH"]

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
    from sys import exit as _exit
    import yaml
    import requests
    import datetime
    import hashlib
    import ctypes
    import mpv

    # Prompt-toolkit - autocompletion library
    from prompt_toolkit.enums import EditingMode
    from prompt_toolkit import PromptSession, print_formatted_text
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.patch_stdout import patch_stdout
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory, DummyAutoSuggest
    from prompt_toolkit.completion import merge_completers, FuzzyCompleter, ThreadedCompleter, DummyCompleter
    from core.PathCompleter import PathCompleter
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style
    from prompt_toolkit.output.color_depth import ColorDepth

    # Project stuff
    import core.database
    import core.osBased
    import core.utils
    from core.elevate import elevate
    from core.utils import prime
    from core.vectors import Vector2, Vector3


try:
    from sys import exit as _exit
    import yaml
    import datetime
    import hashlib
    import requests
    import ctypes
    import mpv

    # Prompt-toolkit - autocompletion library
    from prompt_toolkit.enums import EditingMode
    from prompt_toolkit import PromptSession, print_formatted_text
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.patch_stdout import patch_stdout
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory, DummyAutoSuggest
    from prompt_toolkit.completion import merge_completers, FuzzyCompleter, ThreadedCompleter, DummyCompleter
    from core.PathCompleter import PathCompleter
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style
    from prompt_toolkit.output.color_depth import ColorDepth

    # Project stuff
    import core.database
    import core.osBased
    import core.utils
    from core.elevate import elevate
    from core.utils import prime
    from core.vectors import Vector2, Vector3


except Exception as e:
    if "python" in sys.executable:
        if not args.quiet:
            print(e)
        # Install main lib
        if iswindows():
            os.system("pip install prompt-toolkit")
        else:
            os.system("sudo pip3 install prompt-toolkit")

        from prompt_toolkit.shortcuts import confirm

        # Ask to install all dependencies, if denied, import error will be raised
        if confirm("Install dependencies: "):
            if iswindows():
                os.system(
                    "pip install python-mpv youtube-dl clint pyyaml requests psutil gputil tabulate pypickle screen-brightness-control pathlib typing pynput webcolors instaloader")
            else:
                os.system(
                    "sudo pip3 install python-mpv youtube-dl clint pyyaml requests pypickle screen-brightness-control pathlib typing pynput tabulate psutil gputil webcolors instaloader")
                os.system("sudo apt-get install -y libmpv-dev")
        else:
            exit(0)

        # Reimport all dependencies
        _import()
    else:
        if not args.quiet:
            print(e)
        if iswindows():
            os.system("pause")
        else:
            os.system("bash -c pause")

# -------------------------------------------

# Get Username
try:
    if iswindows():
        USER = os.environ["USERNAME"]
    else:
        USER = os.environ["USER"]
except:
    USER = "ERROR"


try:
    if iswindows():
        USERDOMAIN = os.environ["USERDOMAIN"]
    else:
        USERDOMAIN = os.environ["NAME"]
except:
    USERDOMAIN = "ERROR"

defPath = os.getcwd()

# For use in "back"
LASTDIR = ""

VOLUME = 100

playing = False
playerInitialized = False

# Path to executable
__location__ = defPath + "\\V01D-Terminal.exe"

# Find config file
if iswindows():
    CONFIG = defPath + r"\config.yml"
else:
    CONFIG = defPath + r"/config.yml"

# Local version
VERSION = "v0.8.0"

# -------------------------------------------


def isadmin() -> bool:
    "Ask if run with elevated privileges"
    try:
        _is_admin = os.getuid() == 0

    except AttributeError:
        _is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return _is_admin


if iswindows():
    os.system("title Void-Terminal")

aliases = core.database.GetAliases()  # Get user alias from database


def saveToYml(data, path) -> None:
    if not os.path.exists(path):
        if not confirm("config.yml not found, create new one ? "):
            if not args.quiet:
                print("config not saved !")
                return
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
        "downloadDict": ("downloadDict.yml"),
        "multithreading": True,
        "fuzzycomplete": True,
        "completeWhileTyping": True,
        "wrapLines": True,
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
        "exeptions": tuple()
    }

    if not args.skipconfig:
        if not args.quiet:
            print(e)
        try:
            if os.path.exists(CONFIG):
                saveToYml(config, CONFIG)  # Create new config file
            else:
                if confirm("config.yml not found, ignoring settings and using defaults, would you like to save new config? "):
                    saveToYml(config, CONFIG)  # Create new config file
        except:
            if not args.quiet:
                print(
                    f"Error writing config file, please check if you are not starting Terminal from PATH, otherwise you dont have permission to write in this folder {CONFIG}")

DOWNLOAD = list(config.get("downloadDict"))  # Get all download dictionaries
MODE = config.get("mode", "CMD")

# Pick completer based on config and platform
if config["fuzzycomplete"] and iswindows():
    combinedcompleter = ThreadedCompleter(FuzzyCompleter(merge_completers([core.database.WinCompleter, PathCompleter(
    ), core.database.winWordCompleter, core.database.WordCompleter(list(aliases.keys()))])))
elif iswindows():
    combinedcompleter = ThreadedCompleter(merge_completers(
        [core.database.WinCompleter, PathCompleter(), core.database.winWordCompleter]))
elif platform.system() == "Linux" and config["fuzzycomplete"]:
    combinedcompleter = ThreadedCompleter(FuzzyCompleter(
        merge_completers([core.database.LinuxCompleter, PathCompleter()])))
else:
    combinedcompleter = ThreadedCompleter(merge_completers(
        [core.database.LinuxCompleter, PathCompleter()]))

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


def argget(_splitInput: list) -> str:
    "Returns rebuild string"
    return " ".join(_splitInput)


def welcome() -> None:
    if not args.quiet:
        print(f"""{c.fail}
 ██╗   ██╗  ██████╗  ██╗ ██████╗         ████████╗ ███████╗ ██████╗  ███╗   ███╗ ██╗ ███╗   ██╗  █████╗  ██╗
 ██║   ██║ ██╔═══██╗ ██║ ██╔══██╗        ╚══██╔══╝ ██╔════╝ ██╔══██╗ ████╗ ████║ ██║ ████╗  ██║ ██╔══██╗ ██║
 ██║   ██║ ██║   ██║ ██║ ██║  ██║ █████╗    ██║    █████╗   ██████╔╝ ██╔████╔██║ ██║ ██╔██╗ ██║ ███████║ ██║
 ╚██╗ ██╔╝ ██║   ██║ ██║ ██║  ██║ ╚════╝    ██║    ██╔══╝   ██╔══██╗ ██║╚██╔╝██║ ██║ ██║╚██╗██║ ██╔══██║ ██║
  ╚████╔╝  ╚██████╔╝ ██║ ██████╔╝           ██║    ███████╗ ██║  ██║ ██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║  ██║ ███████╗
   ╚═══╝    ╚═════╝  ╚═╝ ╚═════╝            ╚═╝    ╚══════╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝ ╚══════╝{c.end}

    {c.okblue}Welcome to Void-Terminal, Windows compatible terminal with predefined functions for advanced users{c.end}

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
            elif (_splitinput[2].lower() == "cmd"):
                config["mode"] = "CMD"
            if not args.quiet:
                print(f"mode: {c.okgreen}{config['mode']}{c.end}")

        elif (_splitinput[1] == "linux") and platform.system() == "Linux":
            if (_splitinput[2].lower() == "generate"):
                if not args.quiet:
                    print(f"{c.okgreen}This will take a while...")
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
            if _splitinput[2] == "latest":
                if not args.quiet:
                    print(c.okgreen+core.utils.version()+c.end)
            elif _splitinput[2] == "local":
                if not args.quiet:
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

        elif _splitinput[1] == "updatePythonPackages":
            import pkg_resources
            packages = [
                dist.project_name for dist in pkg_resources.working_set]
            if iswindows():
                call("pip install --upgrade --use-feature=2020-resolver" +
                     ' '.join(packages), shell=True)
            else:
                call("sudo pip3 install --upgrade --use-feature=2020-resolver" +
                     ' '.join(packages), shell=True)

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


def hashfilesum(splitInput, hashalg) -> None:
    with open(splitInput[1], "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashalg.update(chunk)

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
        self.player_active = False
        self.player = mpv.MPV()
        self.exceptions = config.get("exeptions", tuple())
        self.default_completer = completer
        self.default_auto_suggest = auto_suggest

    def password(self, text="Password: "):
        self.prompt(text, is_password=True, completer=DummyCompleter(
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

              f"""   {c.okblue}void{c.end}: - config: prints out current configuration
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
              f"   {c.okblue}play{c.end} - play audio or video file from URL or path: {c.okgreen}play [url | file]{c.end}\n"
              f"   {c.okblue}player-volume{c.end} - set target player volume: {c.okgreen}player-volume [value]{c.end}\n"
              f"   {c.okblue}player-pause{c.end} - pause or resume player: {c.okgreen}player-pause{c.end}\n"
              f"   {c.okblue}player-append{c.end} - append track to current playlist: {c.okgreen}player-append [target]{c.end}\n"
              f"   {c.okblue}player-terminate{c.end} - terminate active player: {c.okgreen}player-terminate{c.end}\n"
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

              f"   {c.okblue}downloadeta{c.end} - calculate estimated time of arival: {c.okgreen}downloadeta [target(GB)] [speed(MB)]{c.end}\n"
              f"   {c.okblue}convert{c.end} - function for converting temperatures, colors to hex, audio or video files\n"
              f"   {c.okblue}power{c.end} - change your Windows powerplan\n"
              f"   {c.okblue}download{c.end} - dictionary for downloading files: {c.okgreen}download [-list | target | URL]{c.end}\n"
              f"   {c.okblue}plain2string{c.end} - convert plain text to strings: {c.okgreen}plain2string mode[space,file, fileline] text/[filename]{c.end}\n"
              f"   {c.okblue}autoclicker{c.end} - integrated autoclicker\n"
              )

    def switch(self, userInput: str) -> None:
        userInput = userInput.replace("\\", "\\\\")
        splitInput = shlex.split(userInput)

        global LASTDIR
        global VOLUME
        global playing
        global playerInitialized
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

        elif splitInput[0].lower() == "elevate" or splitInput[0].lower() == "admin":
            elevate()
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

            from queue import Queue
            import time
            import socket

            known_ports = core.database.known_ports
            threading_lock = threading.Lock()
            target = socket.gethostbyname(fargs.target)
            q = Queue()

            def portscanTCP(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target, known_ports[port-1]))
                    with threading_lock:
                        print_formatted_text(HTML(
                            f'<style fg="red">TCP</style> <style fg="blue">{target}</style> <style fg="green">{known_ports[port-1]}</style> is open (<style fg="green">{core.database.known_port_names.get(str(known_ports[port-1]), "unknown")}</style>)'))
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
                    print_formatted_text(HTML(f'<style fg="red">TCP</style> <style fg="blue">{target}</style> <style fg="green">{fargs.port}</style> is open (<style fg="green">{core.database.known_port_names.get(str(fargs.port),"unknown")}</style>)'))
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
            core.utils.ytdown(splitInput)
            return

        elif splitInput[0].lower() == "play":
            fparser = argparse.ArgumentParser(prog="play")
            fparser.add_argument(
                "TARGET", help="Filename, URL or text file with URLs", type=str)
            fparser.add_argument(
                "--volume", help="Set default volume ( 0 - 130 )", type=int)
            fparser.add_argument("-r", "--resolution",
                                 help="Set resolution target", type=int)
            fparser.add_argument("--fps", help="Set fps target", type=int)
            fparser.add_argument(
                "--raw", help="Raw argumets to pass to the MPV", type=str)
            fparser.add_argument(
                "--shuffle", help="Shuffle playlist", action="store_true")
            fparser.add_argument(
                "--maxvolume", help="Set maximum volume ( 100 - 1000 )", type=int)
            fparser.add_argument(
                "-f", "--format", help="Select stream ( best,worst,140 etc. )")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            def my_log(loglevel, component, message):
                print('[{}] {}: {}'.format(
                    loglevel, component, message), flush=True)

            if fargs.format:
                self.player = mpv.MPV(
                    player_operation_mode='pseudo-gui',
                    log_handler=my_log,
                    input_default_bindings=True,
                    input_vo_keyboard=True,
                    osc=True,
                    load_unsafe_playlists=True,
                    ytdl_format=fargs.format,
                    volume=fargs.volume if fargs.volume else VOLUME,
                    volume_max=fargs.maxvolume if fargs.maxvolume else 130)
            elif fargs.resolution or fargs.fps:
                self.player = mpv.MPV(
                    player_operation_mode='pseudo-gui',
                    log_handler=my_log,
                    input_default_bindings=True,
                    input_vo_keyboard=True,
                    osc=True,
                    load_unsafe_playlists=True,
                    ytdl_format=f"bestvideo{f'[height<=?{fargs.resolution}]' if fargs.resolution else ''}{f'[fps<=?{fargs.resolution}]' if fargs.resolution else ''}+bestaudio/best",
                    volume=fargs.volume if fargs.volume else VOLUME,
                    volume_max=fargs.maxvolume if fargs.maxvolume else 130)
            else:
                self.player = mpv.MPV(
                    player_operation_mode='pseudo-gui',
                    log_handler=my_log,
                    input_default_bindings=True,
                    input_vo_keyboard=True,
                    osc=True,
                    load_unsafe_playlists=True,
                    volume=fargs.volume if fargs.volume else VOLUME,
                    volume_max=fargs.maxvolume if fargs.maxvolume else 130)

            if fargs.raw:
                string = str(fargs.raw).replace("-", "_")
                options = string.split(",")
                for option in options:
                    arg, value = option.split("=")
                    self.player[arg] = value

            def play():
                try:
                    f = open(fargs.TARGET, "r")
                    links = f.readlines()
                    for link in links:
                        self.player.playlist_append(link)
                except:
                    self.player.playlist_append(fargs.TARGET)

                if fargs.shuffle:
                    self.player.playlist_shuffle()

                self.player.playlist_pos = 0

                self.player_active = True
                self.player.wait_for_shutdown()
                self.player.terminate()

                self.player_active = False

            if not self.player_active:
                thread = Thread(target=play)
                thread.start()
            else: print(f"{c.warning}Player already started, use 'player-append [target] instead'{c.end}")

        elif splitInput[0].lower() == "player-volume":
            fparser = argparse.ArgumentParser(prog="player-volume")
            fparser.add_argument(
                "TARGET", help="Set default volume ( 0 - MAXVOLUME )", type=int)
            fparser.add_argument(
                "-n", "--no-updating", help="Do not update global variable VOLUME", action="store_true")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            try:
                self.player["volume"] = fargs.TARGET
                VOLUME = fargs.TARGET
            except:
                print(f"{c.fail}Player not initialized{c.end}")
                if fargs.no_updating:
                    return
                else:
                    VOLUME = fargs.TARGET
                    print(
                        f"{c.okgreen}Default volume for new instances updated{c.end}")

        elif splitInput[0].lower() == "player-pause":
            try:
                self.player.keypress("p")
            except:
                print(f"{c.fail}Player not initialized{c.end}")

        elif splitInput[0].lower() == "player-terminate":
            try:
                self.player.terminate()
            except:
                print(f"{c.fail}Player not initialized{c.end}")

        elif splitInput[0].lower() == "player-append":
            fparser = argparse.ArgumentParser(prog="player-append")
            fparser.add_argument(
                "target", help="Target file or URL", type=str)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            try:
                f = open(fargs.target, "r")
                links = f.readlines()
                for link in links:
                    self.player.playlist_append(link)
            except:
                self.player.playlist_append(fargs.target)
            finally:
                print(f"{fargs.target} added to active queue")

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
            os.system("curl api.ipify.org")
            print()
            return

        elif splitInput[0].lower() == "geoip":
            try:
                os.system("curl ipinfo.io/"+splitInput[1])
            except:
                os.system("curl ipinfo.io")
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

        elif splitInput[0].lower() == "power":
            power()
            return

        elif splitInput[0].lower() == "godmode" and iswindows():
            os.system("mkdir GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
            os.system(
                "explorer GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
            os.system("rmdir GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")

        # Hashing ----------------------------------------------------------

        elif splitInput[0].lower() == "sha1":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.sha1(bytes(text, "utf-8")
                                   ).hexdigest(), c.okgreen+text+c.end)
            return

        elif splitInput[0].lower() == "sha224":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.sha224(bytes(text, "utf-8")
                                     ).hexdigest(), c.okgreen+text+c.end)
            return

        elif splitInput[0].lower() == "sha256":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.sha256(bytes(text, "utf-8")
                                     ).hexdigest(), c.okgreen+text+c.end)
            return

        elif splitInput[0].lower() == "sha384":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.sha384(bytes(text, "utf-8")
                                     ).hexdigest(), c.okgreen+text+c.end)
            return

        elif splitInput[0].lower() == "sha512":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.sha512(bytes(text, "utf-8")
                                     ).hexdigest(), c.okgreen+text+c.end)
            return

        elif splitInput[0].lower() == "md5":
            text = argget(splitInput[1:])
            if not args.quiet:
                print(hashlib.md5(bytes(text, "utf-8")
                                  ).hexdigest(), c.okgreen+text+c.end)
            return

        # Hash sum -----------------------------------------------

        elif splitInput[0].lower() == "sha1sum":
            hashsum = hashlib.sha1()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

        elif splitInput[0].lower() == "sha224sum":
            hashsum = hashlib.sha224()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

        elif splitInput[0].lower() == "sha256sum":
            hashsum = hashlib.sha256()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

        elif splitInput[0].lower() == "sha384sum":
            hashsum = hashlib.sha384()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

        elif splitInput[0].lower() == "sha512sum":
            hashsum = hashlib.sha512()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

        elif splitInput[0].lower() == "md5sum":
            hashsum = hashlib.md5()
            hashfilesum(splitInput, hashsum)
            if not args.quiet:
                print(hashsum.hexdigest())
            return

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

        elif splitInput[0].lower() == "welcome":  # Show welcome screen
            welcome()
            return

        elif splitInput[0].lower() == "search":
            open_new_tab(url="https://www.google.com/search?q=" +
                         " ".join(splitInput[1:]))

        elif splitInput[0].lower() == "sizeof":  # Show welcome screen
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

        elif splitInput[0].lower() == "currencyconverter":  # Show welcome screen
            fparser = argparse.ArgumentParser(prog="currencyconverter")
            fparser.add_argument("base", help="Base currency", type=str)
            fparser.add_argument("other", help="Target currency", type=str)
            fparser.add_argument(
                "amount", help="Amount to convert", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            rate = core.utils.currencyconverter(
                fargs.base.upper(), fargs.other.upper())
            if not args.quiet:
                print(
                    f"{(rate * float(fargs.amount)).__round__(2)} {c.okgreen}{fargs.other}{c.end}")
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
            call(f'auto-py-to-exe -c config.json"', shell=True)
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

            from core.autoclicker import Autoclicker
            clicker = Autoclicker(
                core.autoclicker.Button.left if not fargs.right else core.autoclicker.Button.right, fargs.delay if fargs.delay else 0.05)
            clicker.start()
            return

        elif splitInput[0].lower() == "lcm":
            fparser = argparse.ArgumentParser(prog="lcm")
            fparser.add_argument("first", help="First number", type=float)
            fparser.add_argument("second", help="Second number", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                print(core.utils.lcm(fargs.first, fargs.second))
            return

        elif splitInput[0].lower() == "gcd":
            fparser = argparse.ArgumentParser(prog="gcd")
            fparser.add_argument("first", help="First number", type=float)
            fparser.add_argument("second", help="Second number", type=float)
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            if not args.quiet:
                print(core.utils.gcd(fargs.first, fargs.second))
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
                import core.pwned as pwned
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
            try: self.player.terminate()
            finally: _exit()

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
                core.database.WriteAliases(aliases)
            return

        # Remove alias from dictionary and update save
        elif splitInput[0].lower() == "delalias":
            try:
                aliases.pop(splitInput[1])
                core.database.WriteAliases(aliases)
            except:
                if not args.quiet:
                    print(
                        f"{c.fail}Name is not in list !{c.end} \nUsage: {c.okgreen}delalias [name]{c.end}")

        elif splitInput[0].lower() == "eval":  # Show alias dictionary
            while True:
                try:
                    _eval = self.prompt(message=HTML(f"<user>{USER}</user> <path>eval</path>""<pointer> > </pointer>"), style=_style,
                                        complete_in_thread=config["multithreading"], set_exception_handler=True, color_depth=ColorDepth.TRUE_COLOR, completer=None)
                    if _eval.lower() == "quit" or _eval.lower() == "exit":
                        break
                    else:
                        eval(compile(_eval, "<string>", "exec"))
                except Exception as e:
                    if not args.quiet:
                        print(f"{c.fail}{e}{c.end}")
            return

        # Dictionary for downloading (direct link to website mirror) or download straight to active folder
        elif splitInput[0].lower() == "download":
            fparser = argparse.ArgumentParser(prog="download")
            fparser.add_argument(
                "-l", "--list", help="List all dictionary keys", action="store_true")
            fparser.add_argument("-k", "--key", help="URL or dictionary key")
            try:
                fargs = fparser.parse_args(splitInput[1:])
            except SystemExit:
                return

            try:
                if fargs.list:
                    for i in DOWNLOAD:
                        try:
                            if not args.quiet:
                                print(dict(yaml.safe_load(open(i))).keys())
                        except:
                            pass
                else:
                    raise Exception
            except:
                try:
                    for item in splitInput[1:]:
                        core.utils.download(item)
                except Exception as e:
                    if not args.quiet:
                        print(f"{c.fail}{e}{c.end}")

        else:
            try:  # Calculator
                output = eval(userInput)
                if type(output) in [float, int, list, tuple, str, bool, Vector2, Vector3]:
                    if not args.quiet:
                        print(output)
                else:
                    raise Exception
            except:  # Try if input is alias
                try:
                    if os.getcwd() != LASTDIR:
                        LASTDIR = os.getcwd()
                    os.chdir(userInput)
                except:
                    if iswindows():
                        if MODE == "CMD":
                            os.system(userInput)
                        elif MODE == "POWERSHELL":
                            os.system(f"powershell -Command {userInput}")
                    else:
                        os.system(f'bash -c "{userInput}"')

    def main(self) -> None:
        """
        Terminal main loop
        """
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
                promptMessage = HTML(
                    f"""\n┏━━(<user>{USER}</user> Ʃ <user>{USERDOMAIN}</user>)━[<path>{cd}</path>]━(T:<user>{threading.active_count()}</user> V:<user>{VOLUME}</user>)\n┗━<pointer>{"#" if isadmin() == True else "$"}</pointer> """)

                userInput = self.prompt(enable_history_search=True, completer=self.default_completer, auto_suggest=self.default_auto_suggest, is_password=False, message=promptMessage,
                                        style=_style, complete_in_thread=config["multithreading"], color_depth=ColorDepth.TRUE_COLOR)  # Get user input (autocompetion allowed)

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
                    print(
                        f"{c.fail}{error.with_traceback(error.__traceback__)}{c.end}")
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


if __name__ == "__main__":
    app = Void_Terminal()

    if args.command:
        userInput = app.envirotize(args.command)

        app.switch(userInput)
        sys.exit(0)
    else:
        with patch_stdout(app):
            app.main()
