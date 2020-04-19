# Project V01D

import os
import math
import numpy as np
import ctypes
import sys

# Project stuff
import database
import osBased
import utils
import neural_net

run = True
terminal_color = database.getcolor()
title = "V01D Terminal"
aliases = database.GetAliases()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def Password():
    os.system("netsh wlan show profiles")

    networkName = input("Network name > ")

    os.system(f"netsh wlan show profiles {networkName} key=clear")


def Void():
    os.startfile("Void.py")


def Read():
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

def Power():
    print("If you want best powerscheme use: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
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

def Initialize():
    os.system(f"title {title}")

    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 18
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Lucida Console"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))
        

def Run():
    while True:
        cd = os.getcwd()
        userInput = input(cd + " > ")
        splitInput = userInput.split()

        try:
            userInput.lower()
        except TypeError:
            continue

        if splitInput[0].lower() == "password":
            Password()
            continue

        elif userInput.lower() == "sin":
            sin = float(input("Sin: "))
            print(math.sin(sin))
            continue

        elif userInput.lower() == "cos":
            cos = float(input("Cos: "))
            print(math.cos(cos))
            continue

        elif userInput.lower() == "sqrt":
            num = float(input("Sqrt: "))

            try:
                print(math.sqrt(num))
            except:
                print("Math error")
            finally:
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
            continue

        elif userInput.lower() == "component":
            os.system("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status")
            os.system("wmic baseboard get product,Manufacturer,version,serialnumber")
            os.system("wmic path win32_VideoController get Name")
            os.system("wmic path win32_VideoController get /all")
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

        elif splitInput[0].lower() == "color":
            try:
                splitInput[1]
                os.system(f"color {splitInput[1]}")
                if splitInput[1] != "/?":
                    database.writedata(splitInput[1],"color.txt",database.__location__,"w")
            except:
                os.system("color /?")
            continue

        elif userInput.lower() == "help":
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
                    "   sin - sinus\n"
                    "   cos - cosinus\n"
                    "   sqrt - square root\n"

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

                    "   exit - quit application\n"
                    "   os - show operating system\n"
                
                "\n ALIAS: \n\n"

                    "   alias - define your own function (alias sayhello @echo Hello!!)\n"
                    "   delalias - remove alias\n"
                    "   aliases - show all user defined aliases\n"

                "\n OTHER FUNCTIONS \n\n"

                    "   ping - nekonečná smyčka odezvy\n"
                    "   pagefile - velikost a umístění pagefile\n"
                    "   read - read specified .txt file\n"
                    "   power - change your Windows powerplan\n"

                "\n IN DEVELOPMENT \n\n"

                    "   download - !experimental! download file from web\n"
                    "   nn - !experimental! neuralnetwork(20k iteration perceptron)\n"
                )
            continue

        elif userInput.lower() == "ping":
            os.system("start ping google.com -t")
            continue

        elif userInput.lower() == "os":
            osBased.Os()
            continue

        elif userInput.lower() == "clear" or userInput.lower() == "cls":
            osBased.Clear()
            continue
        
        elif userInput.lower() == "read":
            Read()
            continue
        
        elif userInput.lower() == "void":
            Void()
            continue

        elif splitInput[0].lower() == "pwned":
            try:
                import pwned
                print(pwned.lookup_pwned_api(splitInput[1]))
            except:
                print("Error")
            
            continue

        elif splitInput[0].lower() == "cd":
            try:
                os.chdir(splitInput[1])
            except:
                os.system(userInput)
            continue

        elif userInput.lower() == "exit" or userInput == "quit":
            exit()

        elif splitInput[0].lower() == "alias":
            l = splitInput[2:]
            complete = ""
            for i in l:
                complete += i + " "
            aliases[splitInput[1]] = complete
            database.WriteAliases(aliases)

        elif splitInput[0].lower() == "delalias":
            try:
                aliases.pop(splitInput[1])
                database.WriteAliases(aliases)
            except:
                print("Name is not in list ! \nUsage: delalias [name]")
            

        elif userInput.lower() == "aliases":
            print(aliases)

        elif splitInput[0].lower() == "download":
            try:
                if splitInput[1] == "-list":
                    print(database.downloadDict.keys())
                else:
                    os.system(
                        "start " + database.downloadDict.get(splitInput[1]))
            except:
                print("Not found\nTry: download -list")

        # In development

        elif userInput.lower() == "nn":
            neural_network = neural_net.NeuralNetwork()

            print("Random synaptic weights: ")
            print(neural_network.synaptic_weights)

            training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1],[0,1,0],[1,0,0],[1,1,0]])

            training_outputs = np.array([[0,1,0,1,1,0,1]]).T

            neural_network.train(training_inputs, training_outputs, 20000)

            print("Synaptic weights after training: ")
            print(neural_network.synaptic_weights)

            A = str(input("Input 1: "))
            B = str(input("Input 2: "))
            C = str(input("Input 3: "))

            print("New situation: input data = ", A, B, C)
            print("Output data: ")
            print(neural_network.think(np.array([A, B, C])))


        # / In development

        else:
            try:
                splitInput = userInput.split()
                num1 = splitInput[0]

                try:
                    num1 = float(splitInput[0])
                    num2 = float(splitInput[2])
                    character = splitInput[1]
                except:
                    pass

                if splitInput[0] == float:
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
                else:
                    if num1 == "pi":
                        print("Pi =", math.pi)
                    elif num1 == "e":
                        print("e =", math.e)
                    else:
                        raise


            except:
                try:
                    value = aliases.get(userInput)
                    os.system(value)
                except:
                    os.system(userInput)

            
                
       
os.system(f"color {terminal_color}")

osBased.Clear()

Initialize()
Run()
