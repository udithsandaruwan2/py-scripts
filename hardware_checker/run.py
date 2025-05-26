import platform
import psutil
import cpuinfo
import GPUtil
import os

def get_system_info():
    print("==== System Info ====")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()}")

    print("\n==== CPU Info ====")
    cpu = cpuinfo.get_cpu_info()
    print(f"Brand: {cpu['brand_raw']}")
    print(f"Cores (physical): {psutil.cpu_count(logical=False)}")
    print(f"Cores (total): {psutil.cpu_count(logical=True)}")
    print(f"Max Frequency: {psutil.cpu_freq().max:.2f} MHz")

    print("\n==== RAM Info ====")
    svmem = psutil.virtual_memory()
    print(f"Total RAM: {svmem.total / (1024**3):.2f} GB")
    print(f"Available RAM: {svmem.available / (1024**3):.2f} GB")

    print("\n==== Disk Info ====")
    partitions = psutil.disk_partitions()
    for p in partitions:
        print(f"Device: {p.device}, Mountpoint: {p.mountpoint}, File System: {p.fstype}")
        usage = psutil.disk_usage(p.mountpoint)
        print(f"  Total: {usage.total / (1024**3):.2f} GB, Used: {usage.used / (1024**3):.2f} GB")

    print("\n==== GPU Info ====")
    gpus = GPUtil.getGPUs()
    if not gpus:
        print("No GPU found (or not supported by GPUtil).")
    for gpu in gpus:
        print(f"GPU Name: {gpu.name}")
        print(f"Memory Total: {gpu.memoryTotal}MB")
        print(f"Memory Free: {gpu.memoryFree}MB")
        print(f"Driver: {gpu.driver}")

    print("\n==== Battery Info ====")
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery percent: {battery.percent}%")
        print(f"Plugged in: {'Yes' if battery.power_plugged else 'No'}")
    else:
        print("Battery status not available.")

get_system_info()
