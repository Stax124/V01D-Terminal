from __future__ import print_function
from subprocess import call
from sys import argv
from datetime import datetime
import platform
import psutil
import webcolors
import math
import screen_brightness_control as screen
import GPUtil
from tabulate import tabulate
import requests
import sys
import pytube
import random
import time
import database
from download import Download
import os
from prompt_toolkit.shortcuts import confirm


def gcd(a, b) -> float:
    "Returs greatest common dividor"
    if b > a:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return float(a)

def lcm(x, y) -> float:
    "Returs lowest common multiple"
    greater = 0
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return float(lcm)

def version() -> str:
    url = "https://api.github.com/repos/Stax124/V01D-Terminal/releases/latest"
    response = requests.get(url)
    content = response.json()

    return content.get('html_url').split('/')[-1]

def ytvid(url):
    startdir = os.getcwd()
    if platform.system() == "Windows":
        downloads = os.environ["USERPROFILE"]+"\\Downloads"
    else:
        downloads = "/tmp"
    os.chdir(downloads)

    yt = pytube.YouTube(url)
    vids = yt.streams.filter(file_extension = "mp4")

    for i in range(len(vids)):
        print(i,'. ',vids[i])

    vnum = int(input("Enter video index: "))

    if platform.system() == 'Windows':
        parent_dir = downloads
    else:
        parent_dir = "/tmp"

    print(f"Downloading {yt.title} to {os.getcwd()}, Please wait...")
    vids[vnum].download()
    os.chdir(startdir)

def setbrightness(value:int):
    "Set screen brightness to value between 0 and 100"
    screen.set_brightness(value)

def getbrightness():
    "Get brightness of monitor"
    print(f"Brightness: {screen.get_brightness()}")

def currencyconverter(base:str,othercurrency:str) -> float:
    "Returns rate between currencies"
    response = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}")
    content = response.json()
    rates = content.get("rates")
    rate = rates.get(othercurrency)
    return rate

def PlainToString(text, mode) -> str:
    "Returns list of strings from plain text file (hello world -> 'hello','world')"

    split = ""
    
    if mode == "file":
        try:
            f = open(text, "r")
            text = f.read()
            split = text.split()
        except:
            print("File not found or not accessible")
    elif mode == "fileline":
        try:
            f = open(text, "r")
            text = f.read()
            split = text.split("\n")
        except:
            print("File not found")
    elif mode == "line":
        split = text.split()
    else:
        print("""
    Usage: plain2string [mode] [file|text]

    Print .txt, .py and other text filetypes from terminal

    positional arguments:   
        mode    file        Split text in file by ' '
                line        Split text by ' '
                fileline    Split text in file by '\\n'

        file    Source file (only works with 'file','fileline')
        text    String to split (only works with 'line')
    """)


    out = ""

    for item in split:
        out += "'" + item + "'" + ","

    return(out)

def download(target) -> None:
    from Void import DOWNLOAD
    d = Download(promptinstall=True, dictionarypath=DOWNLOAD, startifexeption=True, returnexeption=True)
    d.download(target=target)

def rng(_min: int, _max: int) -> int:
    "Returns random number between min and max. Min included, max excluded"
    random.seed(time.time())
    return random.randrange(_min, _max)

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MiB'
        1253656678 => '1.17GiB'
    """
    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_from_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MiB'
        1253656678 => '1.17GiB'
    """
    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes *= factor

def gpu() -> None:
    "Print GPU information"
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                    "temperature", "uuid")))

def cpu() -> None:
    "Print CPU information"

    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def sysinfo() -> None:
    "Print system information"

    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def bootinfo() -> None:
    "Print Boot Time information"

    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def memory() -> None:
    "Print memory information"

    # Memory Information
    print("="*40, "Memory Information", "="*40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

def disk() -> None:
    "Print disk information"

    # Disk Information
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

def network() -> None:
    "Print network information"

    # Network information
    print("="*40, "Network Information", "="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")



def decimal_to_binary(num: int) -> str:

    """
        Convert an Integer Decimal Number to a Binary Number as str.
        >>> decimal_to_binary(0)
        '0b0'
        >>> decimal_to_binary(2)
        '0b10'
        >>> decimal_to_binary(7)
        '0b111'
        >>> decimal_to_binary(35)
        '0b100011'
        >>> # negatives work too
        >>> decimal_to_binary(-2)
        '-0b10'
        >>> # other floats will error
        >>> decimal_to_binary(16.16) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'float' object cannot be interpreted as an integer
        >>> # strings will error as well
        >>> decimal_to_binary('0xfffff') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'str' object cannot be interpreted as an integer
    """

    if type(num) == float:
        raise TypeError("'float' object cannot be interpreted as an integer")
    if type(num) == str:
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)

def decimal_to_hexadecimal(decimal):
    """
        take integer decimal value, return hexadecimal representation as str beginning
        with 0x
        >>> decimal_to_hexadecimal(5)
        '0x5'
        >>> decimal_to_hexadecimal(15)
        '0xf'
        >>> decimal_to_hexadecimal(37)
        '0x25'
        >>> decimal_to_hexadecimal(255)
        '0xff'
        >>> decimal_to_hexadecimal(4096)
        '0x1000'
        >>> decimal_to_hexadecimal(999098)
        '0xf3eba'
        >>> # negatives work too
        >>> decimal_to_hexadecimal(-256)
        '-0x100'
        >>> # floats are acceptable if equivalent to an int
        >>> decimal_to_hexadecimal(17.0)
        '0x11'
        >>> # other floats will error
        >>> decimal_to_hexadecimal(16.16) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # strings will error as well
        >>> decimal_to_hexadecimal('0xfffff') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # results are the same when compared to Python's default hex function
        >>> decimal_to_hexadecimal(-256) == hex(-256)
        True
    """
    values = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }

    assert type(decimal) in (int, float) and decimal == int(decimal)
    hexadecimal = ""
    negative = False
    if decimal < 0:
        negative = True
        decimal *= -1
    while decimal > 0:
        decimal, remainder = divmod(decimal, 16)
        hexadecimal = values[remainder] + hexadecimal
    hexadecimal = "0x" + hexadecimal
    if negative:
        hexadecimal = "-" + hexadecimal
    return hexadecimal

def decimal_to_octal(num: int) -> str:
    """Convert a Decimal Number to an Octal Number.
    >>> all(decimal_to_octal(i) == oct(i) for i
    ...     in (0, 2, 8, 64, 65, 216, 255, 256, 512))
    True
    """
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.pow(10, counter))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        # This formatting removes trailing '.0' from `octal`.
    return f"0o{int(octal)}"

def roman_to_int(roman: str) -> int:
    """
    LeetCode No. 13 Roman to Integer
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(roman_to_int(key) == value for key, value in tests.items())
    True
    """
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    return total

def celsius_to_fahrenheit(celsius: float) -> float:
    return round((float(celsius) * 9 / 5) + 32)

def celsius_to_kelvin(celsius: float) -> float:
    return round(float(celsius) + 273.15)

def celsius_to_rankine(celsius: float) -> float:
    return round((float(celsius) * 9 / 5) + 491.67)

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return round((float(fahrenheit) - 32) * 5 / 9)

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.15)

def fahrenheit_to_rankine(fahrenheit: float) -> float:
    return round(float(fahrenheit) + 459.67)

def kelvin_to_celsius(kelvin: float) -> float:
    return round(float(kelvin) - 273.15)

def kelvin_to_fahrenheit(kelvin: float) -> float:
    return round(((float(kelvin) - 273.15) * 9 / 5) + 32)

def kelvin_to_rankine(kelvin: float) -> float:
    return round((float(kelvin) * 9 / 5))

def rankine_to_celsius(rankine: float) -> float:
    return round((float(rankine) - 491.67) * 5 / 9)

def rankine_to_fahrenheit(rankine: float) -> float:
    return round(float(rankine) - 459.67)

def rankine_to_kelvin(rankine: float) -> float:
    return round((float(rankine) * 5 / 9))

def convert(splitInput:str):
    if splitInput[1].lower() == "decimal":
        if splitInput[2].lower() == "binary":
            print(decimal_to_binary(int(splitInput[3])))
        if splitInput[2].lower() == "hexadecimal":
            print(decimal_to_hexadecimal(int(splitInput[3])))
        if splitInput[2].lower() == "octal":
            print(decimal_to_octal(int(splitInput[3])))
    elif splitInput[1].lower() == "roman":
        if splitInput[2].lower() == "int":
            print(roman_to_int(splitInput[3]))
    elif splitInput[1].lower() == "celsius":
        if splitInput[2].lower() == "fahrenheint":
            print(celsius_to_fahrenheit(float(splitInput[3])))
        if splitInput[2].lower() == "kelvin":
            print(celsius_to_kelvin(float(splitInput[3])))
        if splitInput[2].lower() == "rankine":
            print(celsius_to_rankine(float(splitInput[3])))
    elif splitInput[1].lower() == "fahrenheint":
        if splitInput[2].lower() == "celsius":
            print(fahrenheit_to_celsius(float(splitInput[3])))
        if splitInput[2].lower() == "kelvin":
            print(fahrenheit_to_kelvin(float(splitInput[3])))
        if splitInput[2].lower() == "rankine":
            print(fahrenheit_to_rankine(float(splitInput[3])))
    elif splitInput[1].lower() == "rankine":
        if splitInput[2].lower() == "celsius":
            print(rankine_to_celsius(float(splitInput[3])))
        if splitInput[2].lower() == "kelvin":
            print(rankine_to_kelvin(float(splitInput[3])))
        if splitInput[2].lower() == "fahrenheit":
            print(rankine_to_fahrenheit(float(splitInput[3])))
    elif splitInput[1].lower() == "color":
        if splitInput[2].lower() == "rgb":
            print(webcolors.name_to_rgb(splitInput[3]))
        if splitInput[2].lower() == "hex":
            print(webcolors.name_to_hex(splitInput[3]))
        if splitInput[2].lower() == "list":
            for key, value in webcolors.css3_names_to_hex.items(): 
                print("{:<30} {:<30}".format(key, value))
    else:
        print("Not Implement")

def prime_factors(n: int) -> list:
    """
    Returns prime factors of n as a list.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    import Void
    Void.main()