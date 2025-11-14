import os
import platform
import psutil

def get_os_version():
    return platform.version()

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total // (1024 * 1024),
        'available': mem.available // (1024 * 1024),
        'percent': mem.percent,
    }

def get_cpu_info():
    return psutil.cpu_count(logical=True)

def get_computer_name():
    return os.environ['COMPUTERNAME']

def get_user_name():
    return os.getlogin()

def get_architecture():
    return platform.architecture()[0]

def get_pagefile_info():
    pagefile = psutil.virtual_memory().total - psutil.virtual_memory().available
    return {
        'used': pagefile // (1024 * 1024),
        'total': psutil.virtual_memory().total // (1024 * 1024),
    }

def get_drives_info_as_dicts():
    drives_data = []
    
    partitions = psutil.disk_partitions(all=True)
    
    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            
            if p.mountpoint.endswith(':\\') and p.fstype:
                free_mb = round(usage.free / (1024**2))
                total_mb = round(usage.total / (1024**2))
                
                drive_info = {
                    'device': p.mountpoint,
                    'fstype': p.fstype,
                    'free': free_mb,
                    'total': total_mb
                }
                drives_data.append(drive_info)
            
        except OSError:
            continue
        except Exception as e:
            continue
            
    return drives_data

print(f"OS Version: {get_os_version()}")
print(f"Computer Name: {get_computer_name()}")
print(f"User: {get_user_name()}")
print(f"Architecture: {get_architecture()}")
    
mem_info = get_memory_info()
print(f"RAM: {mem_info['available']}MB / {mem_info['total']}MB")
    
virtual_mem = get_pagefile_info()
print(f"Virtual Memory: {virtual_mem['total']}MB")
    
print(f"Memory Load: {mem_info['percent']}%")
    
print(f"Pagefile: {virtual_mem['used']}MB / {virtual_mem['total']}MB")
    
cpu_count = get_cpu_info()
print(f"Processors: {cpu_count}")
    
print("Drives:")
        
drives = get_drives_info_as_dicts() 
        
for drive in drives:
    print(f"  - {drive['device']}  ({drive['fstype']}): {drive['free']} MB free / {drive['total']} MB total")
