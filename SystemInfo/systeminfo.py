import platform
import socket
import os
import psutil
import time
import argparse
import json
import sys
import logging

"""
This script collects and displays detailed system information, including:
- Determine the operating system.
- Get hostname and user info.
- Get CPU usage info.
- Get memory usage info
- Get the number of running/idle processes.
- Get hard drive info.
- Get local time and boot time.
- Display all the information as Text or Json.
"""


logging.basicConfig(
    filename= 'SystemInfo/systeminfo.log', # The Log File
    filemode= 'a', # Append To File
    format= '%(asctime)s - %(levelname)s - %(message)s', # %(Time) - %(Level) - %(LogMessage)
    level= logging.DEBUG # DEBUG To Handle All Logs Levels
)


class NoArgumentsException(Exception):
    pass

try:
  logging.info("Starting argument parsing.")
  parser = argparse.ArgumentParser(description="Get Info About System")
  parser.add_argument("-o", "--os-info", action="store_true", required=False, help="Getting operating system info.")
  parser.add_argument("-c", "--cpu-info", action="store_true", required=False, help="Getting CPU info.")
  parser.add_argument("-m", "--memory-info", action="store_true", required=False, help="Getting memory info.")
  parser.add_argument("-p", "--process-info", action="store_true", required=False, help="Getting process info.")
  parser.add_argument("-a", "--all", action="store_true", required=False, help="Getting all info.")
  parser.add_argument("-f" ,"--format", choices=["text", "json"], default="text", required=False, help="Choose the output format: text (default) or json.")
  parser.add_argument("--output", type=str, required=False, help="Choose Your JSON file name")
  args = parser.parse_args()

  if not (args.os_info or args.cpu_info or args.memory_info or args.process_info or args.all):
      logging.error("No arguments provided.")
      raise NoArgumentsException("Error: No Arguments Provided. Use -h/--help For Help!")
  
  
except NoArgumentsException as nae:
    print(f"NoArgumentsException: {nae}")
    sys.exit(1)


finally:
    logging.info("Argument parsing completed.")
    


class SystemInfo():
 def __init__(self):
    logging.debug("SystemInfo Instence Created.")


 # Determine the operating system
 def get_os_info(self):
      os_info = platform.system()
      hostname = socket.gethostname()
      user = os.getlogin()
      logging.info("OS-info retrived successfully.")
      return os_info, hostname, user


 # Get CPU usage info
 def get_cpu_info(self):
      cpu_count = psutil.cpu_count(logical=True)
      cpu_percent = psutil.cpu_percent(interval=1)
      logging.info("CPU-info retrived successfully.")
      return cpu_count, cpu_percent


 # Get memory usage info
 def get_memory_info(self):
      mem = psutil.virtual_memory()
      total_memory = mem.total / (1024 ** 3)  # Convert from bytes to GB
      used_memory = mem.used / (1024 ** 3)    
      free_memory = mem.free / (1024 ** 3)
      logging.info("MEMORY-info retrived successfully.")    
      return total_memory, used_memory, free_memory


 # Get running/idle processes
 def get_process_info(self):
      processes = []
      for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
          processes.append(proc.info)
      logging.info("PROCESS-info retrived successfully.")    
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
      logging.info("Hard Disk-info retrived successfully.")    
      return hd_info


 # Get local time and boot time
 def get_time_info(self):
      local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      boot_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time()))
      logging.info("TIME-info retrived successfully.")
      return local_time, boot_time
  

 # Print all information to the terminal as plain text
 def display_as_text(self, system_info):
          for key, value in system_info.items():
            print(f"{key}: {value}")
          logging.info("System information displayed as text in Terminal.")     


 # Save the information to a JSON file
 def save_as_json(self, system_info):
        output_file = args.output or "system_info.json"
        with open(output_file, 'w') as f:
            json.dump(system_info, f, indent=4)
            print(f"System information saved to {output_file}")
        logging.info(f"System information saved as JSON in {output_file}.")


 # Main function to display all information
 try:
  def display_system_info(self):
          logging.info("Retrieving system information.")
          system_info = {}

          if args.os_info or args.all:
            os_info, hostname, user = self.get_os_info()
            system_info['Operating System'] = os_info
            system_info['HostName'] = hostname
            system_info['User'] = user      

          if args.cpu_info or args.all:
            cpu_count, cpu_percent = self.get_cpu_info()
            system_info['CPU Count'] = (f"{cpu_count} GB" )
            system_info['CPU Usage'] = (f"{cpu_percent}%")

          if args.memory_info or args.all:
            total_mem, used_mem, free_mem = self.get_memory_info()
            system_info['Total Memory'] = (f"{total_mem:.2f} GB")
            system_info['Used Memory'] = (f"{used_mem:.2f} GB")
            system_info['Free Memory'] = (f"{free_mem:.2f} GB")
          
          if args.process_info or args.all:
            processes = self.get_process_info()
            system_info['Number of processes running'] = len(processes)
          
          if args.all:
            hd_info = self.get_hd_info()
            for hd in hd_info:
              system_info['Hard Disk'] = (f"Disk: {hd['device']}, Total: {hd['total']:.2f} GB, Used: {hd['used']:.2f} GB, Free: {hd['free']:.2f} GB, Usage: {hd['percent']}%") 
            
          if args.all:
            local_time, boot_time = self.get_time_info()
            system_info['Local Time'] = local_time
            system_info['Boot Time'] = boot_time
            
      # Output in the format selected by the user
          if args.format == "text":
              self.display_as_text(system_info)

          elif args.format == "json":
              self.save_as_json(system_info)
              print(system_info)

 except Exception as e:
     logging.exception(f"An error occurred while displaying system information: {e}")
     print(f"An error occurred: {e}")

 finally:
     logging.info("System info retrieval completed.")
        

if __name__ == "__main__":
    system_info = SystemInfo()
    system_info.display_system_info()