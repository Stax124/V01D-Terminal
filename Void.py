# Project V01D

import os
import math
import numpy as np
import ctypes
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

# Project stuff
import database
import osBased
import utils

terminal_color = database.getcolor() # Get saved color
title = "V01D Terminal" # Set title
aliases = database.GetAliases() # Get user defined aliases


def Password(): # Get password of wifi network
    os.system("netsh wlan show profiles")

    networkName = input("Network name > ")

    os.system(f"netsh wlan show profiles {networkName} key=clear")


def Void(): # Open new terminal
    os.startfile("Void.py")


def Read(): # Read file
    path = input("Path:  ")
    print("\n")
    
    try:
        file = open(path)
    except:
        print("Incorrect path")
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
    while True:
        cd = os.getcwd() # Get current working directory
        userInput = prompt(cd + " > ", completer=database.completer, complete_while_typing=True)  # Get user input (autocompetion allowed)
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

        elif splitInput[0].lower() == "color": # Change terminal color and update save file
            try:
                splitInput[1]
                os.system(f"color {splitInput[1]}")
                if splitInput[1] != "/?":
                    database.writedata(splitInput[1],"color.txt",database.__location__,"w")
            except:
                os.system("color /?") # show help on colors
            continue

        elif userInput.lower() == "help": # Print cmd help and defined help at the same time
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
        
        elif userInput.lower() == "read":
            Read()
            continue
        
        elif userInput.lower() == "void":
            Void()
            continue

        elif splitInput[0].lower() == "pwned": # Check if your password is in someones dictionary
            try:
                import pwned
                print(pwned.lookup_pwned_api(splitInput[1]))
            except:
                print("Error")
            
            continue

        elif splitInput[0].lower() == "cd": # Change directory based on input
            try:
                os.chdir(splitInput[1])
            except:
                os.system(userInput)
            continue

        elif userInput.lower() == "exit" or userInput.lower() == "quit": # Terminate application
            os.system("exit")

        elif splitInput[0].lower() == "alias": # Define own function and save it
            try:
                l = splitInput[2:]
                complete = ""
                for i in l:
                    complete += i + " "
                aliases[splitInput[1]] = complete
                database.WriteAliases(aliases)
            except:
                print("Fatal error")
            

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
            try:  # Basic calculator
                splitInput = userInput.split()
                
                try:
                    num1 = float(splitInput[0])
                    num2 = float(splitInput[2])
                    character = splitInput[1]
                except:
                    num1 = float(splitInput[0])
                    character = splitInput[1]
                

                if character == "+":
                    print(num1, "+", num2, "=", num1 + num2)

                elif character == "-":
                    print(num1, "-", num2, "=", num1 - num2)

                elif character == "*":
                    print(num1, "*", num2, "=", num1 * num2)

                elif character == "/":
                    print(num1, "/", num2, "=", num1 / num2)

                elif character == "**":
                    print(num1, "**", num2, "=", num1 ** num2)

                elif character == "//":
                    print(num1, "//", num2, "=", num1 // num2)

                elif character == "root":
                    print(num1, "root", num2,
                        "=", num2 ** (1 / num1))

                elif character == "%":
                    print(num1, "%", num2, "=", num1 % num2)

                #factorial
                elif character == "!":
                    theNumber = num1 = num2
                    num2 = 1
                    while num1 > 1:
                        num2 *= num1
                        num1 = num1 - 1
                    print("n!(", theNumber, ")=", num2)

                elif character == "sin":
                    print("sin(", num1, ")=", math.sin(num1))

                elif character == "cos":
                    print("cos(", num1, ")=", math.cos
                        (num1))

                elif character == "tan":
                    print("tan(", num1, ")=", math.tan(num1))

                elif character == "ln":
                    print("ln(", num1, ")= ", math.log(num1))

            except: # Try if input is alias
                try:
                    value = aliases.get(userInput)
                    os.system(value)
                except: # Pass input to cmd to decide
                    os.system(userInput)


os.system(f"color {terminal_color}") # Set color
os.system(f"title {title}") # Set title
osBased.Clear() # Clear terminal

main() # Run
