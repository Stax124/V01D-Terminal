import psutil
import GPUtil
import platform
import threading
from datetime import datetime

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Processor
cpu_count_physical = psutil.cpu_count(logical=False)
cpu_count_threads = psutil.cpu_count(logical=True)
cpu_frequency = psutil.cpu_freq()
cpu_frequency_min = cpu_frequency.min
cpu_frequency_max = cpu_frequency.max
cpu_frequency_current = cpu_frequency.current
cpu_percent = psutil.cpu_percent()
cpu_percent_all = psutil.cpu_percent(percpu=True)
cpu_stats = psutil.cpu_stats()

# GPUs
__gpus = GPUtil.getGPUs()
gpus = []
for gpu in __gpus:
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
    gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))

# System
uname = platform.uname()
system = uname.system
node_name = uname.node
release = uname.release
version = uname.version
machine = uname.machine
processor = uname.processor

# Boot time
__boot_time_timestamp = psutil.boot_time()
__bt = datetime.fromtimestamp(__boot_time_timestamp)
boot_time = (f"Boot Time: {__bt.year}/{__bt.month}/{__bt.day} {__bt.hour}:{__bt.minute}:{__bt.second}")

# Memory
svmem = psutil.virtual_memory()
memory_total = get_size(svmem.total)
memory_available = get_size(svmem.available)
memory_used = get_size(svmem.used)
memory_percent = svmem.percent

# Swap or Pagefile
swap = psutil.swap_memory()
swap_total = get_size(swap.total)
swap_free = get_size(swap.free)
swap_used = get_size(swap.used)
swap_percentage = swap.percent

# Disks
partitions = psutil.disk_partitions()

# Network
network = []
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        if str(address.family) == 'AddressFamily.AF_INET'or str(address.family) == 'AddressFamily.AF_PACKET':
            network.append((interface_name,address.address,address.netmask,address.broadcast))

# Threads
threadcount = threading.enumerate()