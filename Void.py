# Project V01D-Terminal

from subprocess import call
import platform
import os
import sys

def _import():
    from sys import exit as _exit
    import yaml
    import datetime
    import hashlib
    import ctypes
    from elevate import elevate

    # Prompt-toolkit - autocompletion library
    from prompt_toolkit import PromptSession
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.completion import merge_completers, FuzzyCompleter
    from PathCompleter import PathCompleter
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style
    from prompt_toolkit.output.color_depth import ColorDepth

    # Project stuff
    import database
    import osBased
    import utils

try:
    from sys import exit as _exit
    import yaml
    import datetime
    import hashlib
    import ctypes
    from elevate import elevate

    # Prompt-toolkit - autocompletion library
    from prompt_toolkit import PromptSession
    from prompt_toolkit.shortcuts import confirm
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.completion import merge_completers, FuzzyCompleter
    from PathCompleter import PathCompleter
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style
    from prompt_toolkit.output.color_depth import ColorDepth

    # Project stuff
    import database
    import osBased
    import utils


except Exception as e:
    print(e)
    # Install main lib
    if platform.system().lower() == "windows":
        os.system("pip install prompt-toolkit")
    else:
        os.system("sudo pip3 install prompt-toolkit")

    from prompt_toolkit.shortcuts import confirm

    # Ask to install all dependencies, if denied, import error will be raised
    if confirm("Install dependencies ? "):
        if platform.system().lower() == "windows":
            os.system("pip install clint elevate yaml")
        else:
            os.system(
                "sudo pip3 install clint elevate yaml")
    else:
        exit(0)

    # Reimport all dependencies
    _import()

# -------------------------------------------

try:
    if platform.system() == "Windows":
        USER = os.environ["USERNAME"]
    else:
        USER = os.environ["USER"]
except:
    USER = "ERROR"

defPath = os.getcwd()

LASTDIR = ""

__location__ = defPath + "\\V01D-Terminal.exe"

if platform.system() == "Windows":
    CONFIG = defPath + r"\config.yml"
else:
    CONFIG = defPath + r"/config.yml"

VERSION = "v0.5.0"

# -------------------------------------------

title = "Void Terminal" # Set title
aliases = database.GetAliases() # Get user defined aliases from database

def saveToYml(data,path) -> None:
    with open(path, "w") as f:
        f.flush()
        yaml.safe_dump(data, f)

# Load config or defaults
try:
    config = yaml.safe_load(open(CONFIG))
    type(config.keys())
except Exception as e:
    config = {
        "welcome":True,
        "downloadDict":("downloadDict.yml"),
        "multithreading":True,
        "fuzzycomplete":True,
        "completeWhileTyping":True,
        "wrapLines":True,
        "mouseSupport":True,
        "searchIgnoreCase":True,
        "default": "#ff0066",
        "pointer": "#b20000",
        "path": "#22ff00",
        "user": "#ff0066",
        "completion-menu.completion": "bg:#000000 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222"
    }
    print("config.yml not found, ignoring settings and using defaults")
    print(e)
    saveToYml(config,CONFIG)

DOWNLOAD = list(config.get("downloadDict"))

# Pick completer based on config and platform
if config["fuzzycomplete"] and platform.system() == "Windows":
    combinedcompleter = FuzzyCompleter(merge_completers([database.WinCompleter, PathCompleter()]))
elif platform.system() == "Windows":
    combinedcompleter = merge_completers([database.WinCompleter, PathCompleter()])
elif platform.system() == "Linux" and config["fuzzycomplete"]:
    combinedcompleter = FuzzyCompleter(merge_completers([database.LinuxCompleter, PathCompleter()]))
else:
    combinedcompleter = merge_completers([database.LinuxCompleter, PathCompleter()])

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

def argget(splitInput: list) -> str:
    "Returns rebuild string"
    text = splitInput
    out = ""
    for item in text:
        if item != text[-1]:
            out += item + " "
        else:
            out += item
    return out

def welcome() -> None:
    print(f"""
██╗   ██╗ ██████╗ ██╗██████╗     ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
██║   ██║██╔═══██╗██║██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
██║   ██║██║   ██║██║██║  ██║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
╚██╗ ██╔╝██║   ██║██║██║  ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
 ╚████╔╝ ╚██████╔╝██║██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

Welcome to Void-Terminal, Windows compatible terminal with predefined functions for advanced users

This help will be shown only once

Time: {datetime.datetime.now()}

Latest release: {utils.version()}

'help' - show available commands
            """)

def password() -> None: 
    "Get password of wifi network (Windows only)"

    os.system("netsh wlan show profiles")

    networkName = input("Network name > ")

    os.system(f"netsh wlan show profiles {networkName} key=clear")


def void(_splitinput) -> None: # Open new terminal or configure it
    try:
        if (_splitinput[1] == "multithreading"):
            if (_splitinput[2].lower() == "true"):
                config["multithreading"] = True
            elif (_splitinput[2].lower() == "false"):
                config["multithreading"] = False
            print(f"multithreading: {config['multithreading']}")

        elif (_splitinput[1] == "fuzzycomplete"):
            if (_splitinput[2].lower() == "true"):
                config["fuzzycomplete"] = True
            elif (_splitinput[2].lower() == "false"):
                config["fuzzycomplete"] = False
            print(f"fuzzycomplete: {config['fuzzycomplete']}")

        elif (_splitinput[1] == "mouseSupport"):
            if (_splitinput[2].lower() == "true"):
                config["mouseSupport"] = True
            elif (_splitinput[2].lower() == "false"):
                config["mouseSupport"] = False
            print(f"mouseSupport: {config['fuzzycomplete']}")

        elif (_splitinput[1] == "completeWhileTyping"):
            if (_splitinput[2].lower() == "true"):
                config["completeWhileTyping"] = True
            elif (_splitinput[2].lower() == "false"):
                config["completeWhileTyping"] = False
            print(f"completeWhileTyping: {config['fuzzycomplete']}")

        elif (_splitinput[1] == "wrapLines"):
            if (_splitinput[2].lower() == "true"):
                config["wrapLines"] = True
            elif (_splitinput[2].lower() == "false"):
                config["wrapLines"] = False
            print(f"wrapLines: {config['fuzzycomplete']}")

        elif (_splitinput[1] == "welcome"):
            if (_splitinput[2].lower() == "true"):
                config["welcome"] = True
            elif (_splitinput[2].lower() == "false"):
                config["welcome"] = False
            print(f"welcome: {config['fuzzycomplete']}")

        elif (_splitinput[1] == "start"):
            os.system(f"start {__location__}")

        elif (_splitinput[1] == "license"):
            try:
                if _splitinput[2] == "full":
                    if platform.system() == "Windows":
                        f = open(defPath +"\LICENSE")
                        print(f.read())
                    else:
                        f = open(defPath +"/LICENSE")
                        print(f.read())
            except Exception as e:
                print("""
    Void-Terminal  Copyright (C) 2020  Tomáš Novák
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `void license full' for details.
            """)

        elif (_splitinput[1] == "version"):
            if _splitinput[2] == "latest":
                print(utils.version())
            elif _splitinput[2] == "local":
                print(VERSION)

        elif _splitinput[1] == "updatePythonPackages":
            import pkg_resources
            packages = [dist.project_name for dist in pkg_resources.working_set]
            if platform.system().lower() == "windows":
                call("pip install --upgrade --use-feature=2020-resolver" + ' '.join(packages), shell=True)
            else:
                call("sudo pip3 install --upgrade --use-feature=2020-resolver" + ' '.join(packages), shell=True)

        elif _splitinput[1] == "title":
            os.system(f"title {_splitinput[-1]}")

        elif _splitinput[1] == "config":
            print(config)
    except:
        print("""
██╗   ██╗ ██████╗ ██╗██████╗     ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
██║   ██║██╔═══██╗██║██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
██║   ██║██║   ██║██║██║  ██║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
╚██╗ ██╔╝██║   ██║██║██║  ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
 ╚████╔╝ ╚██████╔╝██║██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                                  

Usage: V01D-Terminal.exe [command] [-h]

V01D-Terminal, easy to use Windows terminal with autocompletion

optional arguments:
    -h          Show help
    command     Command that shell will execute
""")
            
    saveToYml(config,CONFIG)


def is_admin() -> bool:
    "Ask if run with elevated privileges"
    try:
        _is_admin = os.getuid() == 0

    except AttributeError:
        _is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return _is_admin


def read(splitInput) -> None:
    "Prints text of file"
    if splitInput == []:
        print("""
Usage: read [target]

Print .txt, .py and other text filetypes from terminal

positional arguments:       
    target     File to read
""")
    else:
        try:
            path = splitInput[1]
            if '"' in path:
                path = path.split('"')[1]
            elif "'" in path:
                path = path.split("'")[1]
        except:
            print("Incorrrect path. Use path [pathToFile]")
            return
        
        print("\n")
        
        try:
            file = open(path)
        except:
            print("File not found")
            return
        
        try:
            content = file.read()
        except:
            print("File unreadable")
            return
        
        print(content)
        file.close()

def power() -> None:
    "Change Windows power scheme"
    print("If you want best powerscheme paste this, then paste ID of the new scheme: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
    os.system("powercfg -list")
    _input = input("Select scheme: ")

    if _input == "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61":
        os.system(_input)
        os.system("powercfg -list")
        _input = input("Paste scheme id: ")
        os.system("powercfg /setactive " + _input)

    else:
        os.system("powercfg /setactive " + _input)


def hashfilesum(splitInput,hashalg) -> None:
    with open(splitInput[1], "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashalg.update(chunk)

# --------------------------------------------

def switch(userInput,splitInput) -> None:
    global LASTDIR
    try:
        arg = argget(splitInput[1:])
    except:
        pass
    if splitInput[0].lower() == "password":
        password()
        return

    if userInput.lower() == "back":
        __placeholder = os.getcwd()
        os.chdir(LASTDIR)
        if __placeholder != LASTDIR:
            LASTDIR = __placeholder
        return

    elif userInput.lower() == "elevate" or userInput.lower() == "admin":
        elevate()
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

    elif userInput.lower() == "ip":
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
            print("Invalid argument")
        return

    elif splitInput[0].lower() == "stonks":
        try:
            os.system("curl stonks.icu/"+splitInput[1])
        except:
            print("Invalid argument: stonks amd/intl/tsla")
        return

    elif userInput.lower() == "pagefile":
        os.system("wmic pagefile list")
        return

    elif userInput.lower() == "motherboard":
        os.system("wmic baseboard get product,Manufacturer,version,serialnumber")
        return

    elif userInput.lower() == "ram":
        utils.memory()
        return

    elif userInput.lower() == "cpu":
        utils.cpu()
        return

    elif userInput.lower() == "gpu":
        utils.gpu()
        return

    elif userInput.lower() == "network":
        utils.network()
        return

    elif userInput.lower() == "disk":
        utils.disk()
        return

    elif userInput.lower() == "bootinfo":
        utils.bootinfo()
        return

    elif userInput.lower() == "component" and platform.system().lower() == "windows":
        utils.sysinfo()
        utils.cpu()
        utils.gpu()
        utils.memory()
        utils.bootinfo()
        utils.disk()
        utils.network()
        return

    elif userInput.lower() == "firewall":
        os.system("WF.msc")
        return

    elif userInput.lower() == "services":
        os.system("services.msc")
        return

    elif userInput.lower() == "manager":
        os.system("compmgmt.msc")
        return

    elif userInput.lower() == "event":
        os.system("eventvwr.msc")
        return

    elif userInput.lower() == "power":
        power()
        return

    # Hashing ----------------------------------------------------------

    elif splitInput[0].lower() == "sha1":
        text = argget(splitInput[1:])
        print(hashlib.sha1(bytes(text, "utf-8")).hexdigest(),text)
        return

    elif splitInput[0].lower() == "sha224":
        text = argget(splitInput[1:])
        print(hashlib.sha224(bytes(text, "utf-8")).hexdigest(),text)
        return

    elif splitInput[0].lower() == "sha256":
        text = argget(splitInput[1:])
        print(hashlib.sha256(bytes(text, "utf-8")).hexdigest(),text)
        return

    elif splitInput[0].lower() == "sha384":
        text = argget(splitInput[1:])
        print(hashlib.sha384(bytes(text, "utf-8")).hexdigest(),text)
        return

    elif splitInput[0].lower() == "sha512":
        text = argget(splitInput[1:])
        print(hashlib.sha512(bytes(text, "utf-8")).hexdigest(),text)
        return

    elif splitInput[0].lower() == "md5":
        text = argget(splitInput[1:])
        print(hashlib.md5(bytes(text, "utf-8")).hexdigest(),text)
        return

    # Hash sum -----------------------------------------------

    elif splitInput[0].lower() == "sha1sum":
        hashsum = hashlib.sha1()
        hashfilesum(splitInput,hashsum)
        print(hashsum.hexdigest())
        return

    elif splitInput[0].lower() == "sha224sum":
        hashsum = hashlib.sha224()
        hashfilesum(splitInput, hashsum)
        print(hashsum.hexdigest())
        return

    elif splitInput[0].lower() == "sha256sum":
        hashsum = hashlib.sha256()
        hashfilesum(splitInput, hashsum)
        print(hashsum.hexdigest())
        return

    elif splitInput[0].lower() == "sha384sum":
        hashsum = hashlib.sha384()
        hashfilesum(splitInput, hashsum)
        print(hashsum.hexdigest())
        return

    elif splitInput[0].lower() == "sha512sum":
        hashsum = hashlib.sha512()
        hashfilesum(splitInput, hashsum)
        print(hashsum.hexdigest())
        return

    elif splitInput[0].lower() == "md5sum":
        hashsum = hashlib.md5()
        hashfilesum(splitInput, hashsum)
        print(hashsum.hexdigest())
        return

    # --------------------------------------------------------------

    elif splitInput[0].lower() == "plain2string":
        print(utils.PlainToString(argget(splitInput[2:]), mode=splitInput[1]))
        return 

    elif userInput.lower() == "help" or userInput.find("-h") == 0 or userInput.find("--help") == 0: # Print cmd help and defined help at the same time
        if platform.system().lower() == "windows":
            os.system("help")
            print("\n" +

                "\n MATH: \n\n"
                    "       +   -    Addition\n"
                    "       -   -    Subtraction\n"
                    "       *   -    Multiplication\n"
                    "       /   -    Division\n"
                    "       %   -    Modulus\n"
                    "       **  -    Exponentiation\n"
                    "       //  -    floor division\n"
                    "   gcd - greatest common divisor\n"
                    "   lcm - least common multiple\n"
                    "   rng - random number generator (rng min[included],max[excluded])\n"

                "\n COMPUTER: \n\n"

                    "   component - info about workstation\n"
                    "   motherboard, cpu, gpu, ram, disk, network, bootinfo - info about your workstation´s component\n"

                "\n WINDOWS DEFINED: \n\n"

                    "   control - control panel\n"
                    "   diskpart - open diskpart\n"
                    "   msconfig - configure your system\n"
                    "   msinfo32 - show windows configuration\n"
                    "   regedit - tool for editing registers\n"
                    "   sysdm.cpl - system properties\n"
                    "   firewall - configure firewall settings\n"
                    "   services - configure services\n"
                    "   manager - computer management\n"
                    "   event - event viewer\n"

                "\n MANAGEMENT: \n\n"

                    "   exit | quit - quit application\n"
                    "   os - show operating system\n"
                
                "\n ALIAS: \n\n"

                    "   alias - define your own function (alias sayhello @echo Hello!!)\n"
                    "   delalias - remove alias\n"
                    "   aliases - show all user defined aliases\n"

                "\n OTHER FUNCTIONS \n\n"

                    "   ping - never ending ping loop\n"
                    "   pagefile - show pagefile location and size\n"
                    "   read - read specified .txt file\n"
                    "   power - change your Windows powerplan\n"
                    "   download - dictionary for downloading files (download -list)\n"
                    "   open - open file explorer in current directory\n"
                    "   plain2string - convert plain text to strings: plain2string mode[space,file, fileline] text/[filename]\n"
                    "   md5, sha1 , sha224, sha256, sha384, sha512 - hash string\n"
                    "   md5sum, sha1sum, sha224sum, sha256sum, sha384sum, sha512sum - hash file\n"
                    "   elevate, admin - grant admin permission for shell\n"

                "\n IN DEVELOPMENT \n\n"
            )
        else:
            call("help", shell=True)
            
        return

    elif userInput.lower() == "ping": # Never ending ping loop
        os.system("start ping google.com -t")
        return

    elif userInput.lower() == "welcome": # Show welcome screen
        welcome()
        return

    elif userInput.lower() == "os": # Show os
        print(osBased.Os())
        return

    elif userInput.lower() == "clear" or userInput.lower() == "cls": # Clear terminal
        osBased.Clear()
        return
    
    elif splitInput[0].lower() == "read":
        read(splitInput)
        return
    
    elif splitInput[0].lower() == "void":
        void(splitInput)
        return

    elif splitInput[0].lower() == "compile":
        call('auto-py-to-exe', shell=True)
        return

    elif splitInput[0].lower() == "lcm":
        nums = str(splitInput[1]).split(",")
        num = [float(nums[0]),float(nums[1])]
        print(utils.lcm(num[0],num[1]))
        return

    elif splitInput[0].lower() == "gcd":
        nums = str(splitInput[1]).split(",")
        num = [float(nums[0]), float(nums[1])]
        print(utils.gcd(num[0], num[1]))
        return

    elif splitInput[0].lower() == "rng":
        nums = str(splitInput[1]).split(",")
        num = [float(nums[0]), float(nums[1])]
        print(utils.rng(num[0], num[1]))
        return

    elif userInput.lower() == "open" and platform.system().lower() == "windows": # Open file explorer in cwd
        os.system("explorer .\\")
        return

    elif userInput.lower() == "settings" and platform.system().lower() == "windows":  # Open file explorer in cwd
        os.system("start ms-settings:")
        return

    elif userInput.lower() == "startup" and platform.system().lower() == "windows":
        os.system("explorer %AppData%\Microsoft\Windows\Start Menu\Programs\Startup")

    elif splitInput[0].lower() == "pwned": # Check if your password is in someones dictionary
        try:
            import pwned
            print(pwned.lookup_pwned_api(splitInput[1]))
        except:
            print("Error")
        
        return

    # Change directory based on input
    elif splitInput[0].lower() == "cd" and arg:
        if os.getcwd() != LASTDIR:
            LASTDIR = os.getcwd()
        if arg.startswith("%"):
            env = arg.split("%")[1]
            path = os.environ[env]
            os.chdir(path)
        else:
            if '"' in arg:
                path = argget(splitInput[1:]).split('"')[-2]
            else:
                path = argget(splitInput[1:])
            os.chdir(path)
        return

    elif userInput.lower() == "exit" or userInput.lower() == "quit": # Terminate application
        _exit()

    elif splitInput[0].lower() == "alias": # Define own function and save it
        if splitInput[1] == "-list":
            print(aliases)
        else:
            l = splitInput[2:]
            complete = ""
            for i in l:
                complete += i + " "
            aliases[splitInput[1]] = complete
            database.WriteAliases(aliases)
        return

        

    elif splitInput[0].lower() == "delalias": # Remove alias from dictionary and update save
        try:
            aliases.pop(splitInput[1])
            database.WriteAliases(aliases)
        except:
            print("Name is not in list ! \nUsage: delalias [name]")

    elif userInput.lower() == "eval": # Show alias dictionary
        while True:
            try:
                _eval = session.prompt(message=HTML(f"<user>{USER}</user> <path>eval</path>""<pointer> > </pointer>"), style=_style, complete_in_thread=config["multithreading"], set_exception_handler=True,color_depth=ColorDepth.TRUE_COLOR, completer=None)
                if _eval.lower() == "quit" or _eval.lower() == "exit":
                    break
                else:
                    eval(compile(_eval,"<string>","exec"))
            except Exception as e:
                print(e)
        return

    elif splitInput[0].lower() == "download": # Dictionary for downloading (direct link to website mirror) or download straight to active folder
        try:
            if splitInput[1].lower() == "-list":
                for i in DOWNLOAD:
                    try:
                        print(dict(yaml.safe_load(open(i))).keys())
                    except: pass
            else:
                raise
        except:
            try:
                for item in splitInput[1:]:
                    utils.download(item)
            except Exception as e:
                print(e)
                print("""
Usage: download [-list] [target]

Downloads files based on URL or dictionary

optional arguments:       
    -list       Show dictionary of URLs
positional arguments
    target      URL or key from 'download -list'
""")

    else:
        try: # Calculator
            output = eval(userInput.lower())
            print(float(output))
        except: # Try if input is alias
            try:
                value = aliases.get(userInput)
                os.system(value)
            except: # Pass input to cmd to decide
                if platform.system() == "Windows":
                    os.system(userInput)
                else:
                    os.system(f'bash -c "{userInput}"')

# --------------------------------------------

session = PromptSession(completer=combinedcompleter,
                        complete_while_typing=config.get("completeWhileTyping"),
                        mouse_support=config.get("mouseSupport"),
                        wrap_lines=config.get("wrapLines"),
                        auto_suggest=AutoSuggestFromHistory(),
                        search_ignore_case=config.get("searchIgnoreCase"),
                        enable_open_in_editor=True,
                        refresh_interval=0,
                        color_depth=ColorDepth.TRUE_COLOR,
                        )

# ---------------------------------------------

def main() -> None:
    """
    Terminal main loop
    """

    if sys.argv[1:] != []:
        switch(argget(sys.argv[1:]),sys.argv[1:])
    else:
        if config.get("welcome"):
            welcome()
            config["welcome"] = False
            saveToYml(config,CONFIG)
        while True:
            try:
                cd = os.getcwd() # Get current working directory
                userInput = session.prompt(message=HTML(f"<user>{USER}</user> <path>{cd}</path>""<pointer> > </pointer>"
                                                ), style=_style, complete_in_thread=config["multithreading"], set_exception_handler=True,color_depth=ColorDepth.TRUE_COLOR)  # Get user input (autocompetion allowed)
                splitInput = userInput.split() # Split input to get key words

                try:
                    splitInput[0]
                except:
                    continue

                switch(userInput=userInput, splitInput=splitInput)

            except KeyboardInterrupt:
                pass
            except Exception as error:
                print(error)
                os.system("pause")


if __name__ == "__main__":
    main()

