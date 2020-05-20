# Project V01D

import os
import math
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory

from typing import Callable, Iterable, List, Optional
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

# Project stuff
import database
import osBased
import utils

__all__ = [
    "PathCompleter",
    "ExecutableCompleter",
]
title = "V01D Terminal" # Set title
aliases = database.GetAliases() # Get user defined aliases


def Password(): # Get password of wifi network
    os.system("netsh wlan show profiles")

    networkName = input("Network name > ")

    os.system(f"netsh wlan show profiles {networkName} key=clear")


def Void(): # Open new terminal
    os.startfile("Void.py")


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return a


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def Read(splitInput): # Read file
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

def Power(): # Change Windows power shemes
    print("If you want best powerscheme paste this and then paste ID of the new scheme: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
    os.system("powercfg -list")
    _input = input("Select scheme: ")

    if _input == "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61":
        os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
        os.system("powercfg -list")
        _input = input("Select scheme: ")
        os.system("powercfg /setactive " + _input)

    else:
        os.system("powercfg /setactive " + _input)

# --------------------------------------------


def main(): # Main loop
    try:
        session = PromptSession(completer=database.combinedcompleter,complete_while_typing=True,complete_in_thread=True,mouse_support=True, wrap_lines=True,auto_suggest=AutoSuggestFromHistory())

        while True:
            cd = os.getcwd() # Get current working directory
            userInput = session.prompt(cd + " > ")  # Get user input (autocompetion allowed)
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
                osBased.Os()
                continue

            elif userInput.lower() == "clear" or userInput.lower() == "cls": # Clear terminal
                osBased.Clear()
                continue
            
            elif splitInput[0].lower() == "read":
                Read(splitInput)
                continue
            
            elif userInput.lower() == "void":
                Void()
                continue

            elif splitInput[0].lower() == "lcm":
                nums = str(splitInput[1]).split(",")
                num = [float(nums[0]),float(nums[1])]
                print(lcm(num[0],num[1]))
                continue

            elif splitInput[0].lower() == "gcd":
                nums = str(splitInput[1]).split(",")
                num = [float(nums[0]), float(nums[1])]
                print(gcd(num[0], num[1]))
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

            elif splitInput[0].lower() == "cd": # Change directory based on input
                out = ""
                for i in range(splitInput[1:].__len__()):
                    out += splitInput[i+1] + " "
                os.chdir(out)
                continue

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
                    print(eval(userInput.lower()))
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

main()  # Run

