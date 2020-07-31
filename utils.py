from datetime import datetime
import platform
if platform.system() == "Windows":
    import psutil
    import GPUtil
    from tabulate import tabulate
import requests
import sys
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

def PlainToString(text, mode) -> str:
    "Returns list of strings from plain text file (hello world -> 'hello','world')"

    split = ""
    
    if mode == "file":
        try:
            f = open(text, "r")
            text = f.read()
            split = text.split()
        except:
            print("File not found")
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


if __name__ == "__main__":
    import Void
    Void.main()

if platform.system() == "Windows":
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
