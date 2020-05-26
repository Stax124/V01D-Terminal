# Project V01D
try:
    import os
    import math
    import yaml
    import platform

    # Prompt-toolkit - autocompletion library
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import InMemoryHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.completion import merge_completers, PathCompleter, FuzzyCompleter
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.styles import Style

    # Project stuff
    import database
    import osBased
    import utils

except:
    raise ImportError

__all__ = [
    "PathCompleter",
    "ExecutableCompleter",
]

# -------------------------------------------

_style = Style.from_dict(
    {
        "pointer": "#b20000",
        "path": "#00fff0",
    }
)
title = "V01D Terminal" # Set title
aliases = database.GetAliases() # Get user defined aliases
config = yaml.safe_load(open("config.yml"))
CONFIG = r"config.yml"

if config["fuzzycomplete"] and platform.system() == "Windows":
    combinedcompleter = FuzzyCompleter(merge_completers([PathCompleter(), database.WinCompleter]))
elif platform.system() == "Windows":
    combinedcompleter = merge_completers([PathCompleter(), database.WinCompleter])
elif platform.system() == "Linux" and config["fuzzycomplete"]:
    combinedcompleter = FuzzyCompleter(merge_completers([PathCompleter(), database.LinuxCompleter]))
else:
    combinedcompleter = merge_completers([PathCompleter(), database.LinuxCompleter])


def saveToYml(data,path):
    with open(path, "w") as file:
        doc = yaml.dump(data, file)

def exist(var,index):
    try:
        var[index]
        return True
    except:
        return False

def Password(): # Get password of wifi network
    os.system("netsh wlan show profiles")

    networkName = input("Network name > ")

    os.system(f"netsh wlan show profiles {networkName} key=clear")


def Void(_splitinput): # Open new terminal
    try:
        if (_splitinput[1] == "multithreading"):
            if (_splitinput[2].lower() == "true"):
                config["multithreading"] = True
            elif (_splitinput[2].lower() == "false"):
                config["multithreading"] = False
            print(f"Multithreading: {config['multithreading']}")
        if (_splitinput[1] == "fuzzycomplete"):
            if (_splitinput[2].lower() == "true"):
                config["fuzzycomplete"] = True
            elif (_splitinput[2].lower() == "false"):
                config["fuzzycomplete"] = False
            print(f"Fuzzycomplete: {config['fuzzycomplete']}")

        if (_splitinput[1] == "start"):
            os.startfile(__file__)
            
        saveToYml(config,CONFIG)
    except:
        pass

    


def Read(splitInput) -> None:  # Read file
    try:
        path = splitInput[1]
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

def Power() -> None: # Change Windows power shemes
    "Change Windows 10 power scheme"
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


# --------------------------------------------

def main() -> None:  # Main loop
    """
    Terminal main loop
    """
    try:
        session = PromptSession(completer=combinedcompleter, complete_while_typing=True,mouse_support=True, wrap_lines=True,auto_suggest=AutoSuggestFromHistory(),search_ignore_case=True)

        while True:
            cd = os.getcwd() # Get current working directory
            userInput = session.prompt(HTML(f"<path>{cd}</path>""<pointer> > </pointer>"
            ),style=_style, complete_in_thread=config["multithreading"])  # Get user input (autocompetion allowed)
            splitInput = userInput.split() # Split input to get key words

            try:
                splitInput[0]
            except:
                continue

            if splitInput[0].lower() == "password":
                Password()
                continue           

            elif userInput.lower() == "pagefile":
                os.system("wmic pagefile list")
                continue

            elif userInput.lower() == "motherboard":
                os.system("wmic baseboard get product,Manufacturer,version,serialnumber")
                continue

            elif userInput.lower() == "ram":
                os.system("wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed")
                os.system("wmic memorychip list full")
                continue

            elif userInput.lower() == "cpu":
                os.system("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status")
                continue

            elif userInput.lower() == "gpu":
                os.system("wmic path win32_VideoController get Name")
                os.system("wmic path win32_VideoController get /all")
                continue

            elif userInput.lower() == "component":
                os.system("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status")
                os.system("wmic baseboard get product,Manufacturer,version,serialnumber")
                os.system("wmic path win32_VideoController get Name")
                os.system("wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed")
                os.system("wmic memorychip list full")
                continue

            elif userInput.lower() == "firewall":
                os.system("WF.msc")
                continue

            elif userInput.lower() == "services":
                os.system("services.msc")
                continue

            elif userInput.lower() == "manager":
                os.system("compmgmt.msc")
                continue

            elif userInput.lower() == "event":
                os.system("eventvwr.msc")
                continue

            elif userInput.lower() == "power":
                Power()
                continue

            elif userInput.lower() == "help" or userInput.lower() == "/?": # Print cmd help and defined help at the same time
                os.system("help")
                print("\n" +

                    "\n MATH: \n\n"

                        "   calculator availible in command line only for using only 2 numbers !! USE SPACE BETWEEN NUMBERS !!\n"
                        "       +   -    Addition\n"
                        "       -   -    Subtraction\n"
                        "       *   -    Multiplication\n"
                        "       /   -    Division\n"
                        "       %   -    Modulus\n"
                        "       **  -    Exponentiation\n"
                        "       //  -    floor division\n"
                        "       sin - sinus (input: num1 sin)\n"
                        "       cos - cosinus (input: num1 cos)\n"
                        "       root - number´s root (input: num2 root num1)\n"
                        "   gcd - greatest common divisor\n"
                        "   lcm - least common multiple\n"

                    "\n COMPUTER: \n\n"

                        "   component - info about workstation\n"
                        "   motherboard, cpu, gpu, ram - info about your workstation´s component\n"

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
                        "   temp - clear temp files\n"

                    "\n IN DEVELOPMENT \n\n"
                    )
                continue

            elif userInput.lower() == "ping": # Never ending ping loop
                os.system("start ping google.com -t")
                continue

            elif userInput.lower() == "os": # Show os
                print(osBased.Os())
                continue

            elif userInput.lower() == "clear" or userInput.lower() == "cls": # Clear terminal
                osBased.Clear()
                continue
            
            elif splitInput[0].lower() == "read":
                Read(splitInput)
                continue
            
            elif splitInput[0].lower() == "void":
                Void(splitInput)
                continue

            elif splitInput[0].lower() == "lcm":
                nums = str(splitInput[1]).split(",")
                num = [float(nums[0]),float(nums[1])]
                print(utils.lcm(num[0],num[1]))
                continue

            elif splitInput[0].lower() == "gcd":
                nums = str(splitInput[1]).split(",")
                num = [float(nums[0]), float(nums[1])]
                print(utils.gcd(num[0], num[1]))
                continue

            elif userInput.lower() == "open": # Open file explorer in cwd
                os.system("explorer .\\")
                continue

            elif userInput.lower() == "settings":  # Open file explorer in cwd
                os.system("start ms-settings:")
                continue

            elif userInput.lower() == "temp":
                os.system("start .\\temp.bat")

            elif userInput.lower() == "startup":
                os.system("explorer %AppData%\Microsoft\Windows\Start Menu\Programs\Startup")

            elif splitInput[0].lower() == "pwned": # Check if your password is in someones dictionary
                try:
                    import pwned
                    print(pwned.lookup_pwned_api(splitInput[1]))
                except:
                    print("Error")
                
                continue

            # Change directory based on input
            elif splitInput[0].lower() == "cd" and exist(splitInput, 1):
                out = ""
                for i in range(splitInput[1:].__len__()):
                    out += splitInput[i+1] + " "
                os.chdir(out)
                continue

            elif userInput.lower() == "cd":
                uIn = session.prompt("path: ")
                os.chdir(uIn)

            elif userInput.lower() == "exit" or userInput.lower() == "quit": # Terminate application
                return None
                

            elif splitInput[0].lower() == "alias": # Define own function and save it
                l = splitInput[2:]
                complete = ""
                for i in l:
                    complete += i + " "
                aliases[splitInput[1]] = complete
                database.WriteAliases(aliases)
                continue

                

            elif splitInput[0].lower() == "delalias": # Remove alias from dictionary and update save
                try:
                    aliases.pop(splitInput[1])
                    database.WriteAliases(aliases)
                except:
                    print("Name is not in list ! \nUsage: delalias [name]")
                

            elif userInput.lower() == "aliases": # Show alias dictionary
                print(aliases)

            elif splitInput[0].lower() == "download": # Dictionary for downloading (direct link to website mirror)
                try:
                    if splitInput[1].lower() == "-list":
                        print(database.downloadDict.keys())
                    else:
                        os.system(
                            "start " + database.downloadDict.get(splitInput[1]))
                except:
                    print("Not found\nTry: download -list")


            else:
                try: # Calculator
                    output = eval(userInput.lower())
                    print(float(output))
                except: # Try if input is alias
                    try:
                        value = aliases.get(userInput)
                        os.system(value)
                    except: # Pass input to cmd to decide
                        os.system(userInput)


        os.system(f"title {title}") # Set title
        osBased.Clear() # Clear terminal

    except Exception as error:
        print(error)
        os.system("pause")
        main()


if __name__ == "__main__":
    main()  # Run

