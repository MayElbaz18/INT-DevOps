import platform
import socket
import os
import psutil
import time


class SystemInfo():
 def __init__(self):
    pass


 # Determine the operating system
 def get_os_info(self):
      os_info = platform.system()
      hostname = socket.gethostname()
      user = os.getlogin()
      
      return os_info, hostname, user


 # Get CPU usage info
 def get_cpu_info(self):
      cpu_count = psutil.cpu_count(logical=True)
      cpu_percent = psutil.cpu_percent(interval=1)
      
      return cpu_count, cpu_percent


 # Get memory usage info
 def get_memory_info(self):
      mem = psutil.virtual_memory()
      total_memory = mem.total / (1024 ** 3)  # Convert from bytes to GB
      used_memory = mem.used / (1024 ** 3)    
      free_memory = mem.free / (1024 ** 3)
          
      return total_memory, used_memory, free_memory


 # Get running/idle processes
 def get_process_info(self):
      processes = []
      for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
          processes.append(proc.info)
         
      return processes


 # Get hard drive info
 def get_hd_info(self):
      partitions = psutil.disk_partitions()
      hd_info = []
      for part in partitions:
          usage = psutil.disk_usage(part.mountpoint)
          hd_info.append({
              'device': part.device,
              'mountpoint': part.mountpoint,
              'fstype': part.fstype,
              'total': usage.total / (1024 ** 3),  # Convert from bytes to GB
              'used': usage.used / (1024 ** 3),
              'free': usage.free / (1024 ** 3),
              'percent': usage.percent
          })
        
      return hd_info


 # Get local time and boot time
 def get_time_info(self):
      local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      boot_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time()))
      
      return local_time, boot_time
 
     
 
