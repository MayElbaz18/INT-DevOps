from flask import Flask
from flask import request
from flask import jsonify
from sys_info import SystemInfo
import logging


logging.basicConfig(
    filename= 'flask.systeminfo.log', # The Log File
    filemode= 'a', # Append To File
    format= '%(asctime)s - %(levelname)s - %(message)s', # %(Time) - %(Level) - %(LogMessage)
    level= logging.DEBUG # DEBUG To Handle All Logs Levels
)

class NoArgumentsException(Exception):
    pass

app = Flask(__name__)  # __name__ helps Flask locate resources and configurations

@app.route('/', methods=['GET'])
def home():
    logging.info('Home page retrived successfully.')
    return "Welcome to my Flask app!"

@app.route('/systeminfo', methods=['GET'])
def systeminfo():
        try: 
            metric = request.args.get('metric')
            system_info = SystemInfo()
            metrics = ["os_info", "cpu", "mem", "proc", "hd", "time", "all"]

            if metric == "os_info":
                os_info, hostname, user = system_info.get_os_info()
                logging.info("OS-info retrived successfully.")
                return f"Operating System: {os_info}, HostName: {hostname}, User: {user}"
            
            elif metric == "cpu":
                cpu_count, cpu_percent = system_info.get_cpu_info()
                logging.info("CPU-info retrived successfully.")
                return f"CPU Count: {cpu_count} GB, CPU Usage: {cpu_percent}%"
            
            elif metric == "mem":
                total_mem, used_mem, free_mem = system_info.get_memory_info()
                logging.info("MEMORY-info retrived successfully.")
                return f"Total Memory: {total_mem:.2f} GB, Used Memory: {used_mem:.2f} GB, Free Memory: {free_mem:.2f} GB"
            
            elif metric == "proc":
                process = system_info.get_process_info()
                logging.info("PROCESSES-info retrived successfully.")
                return f"Number of processes running: {len(process)}"
            
            elif metric == "hd":
                hd_info = system_info.get_hd_info()
                for hd in hd_info:
                    logging.info("HARD DISK-info retrived successfully.")  
                    return f"Hard Disk: Disk: {hd['device']}, Total: {hd['total']:.2f} GB, Used: {hd['used']:.2f} GB, Free: {hd['free']:.2f} GB, Usage: {hd['percent']}% "
                
            elif metric == "time":
                local_time, boot_time = system_info.get_time_info()
                logging.info("TIME-info retrived successfully.")  
                return f"Local Time: {local_time}, Boot Time: {boot_time}"
            
            elif metric == "all":
                os_info, hostname, user = system_info.get_os_info()
                cpu_count, cpu_percent = system_info.get_cpu_info()
                total_mem, used_mem, free_mem = system_info.get_memory_info()
                process = system_info.get_process_info()
                hd_info = system_info.get_hd_info()
                for hd in hd_info:
                    hd_result = f"Disk: {hd['device']}, Total: {hd['total']:.2f} GB, Used: {hd['used']:.2f} GB, Free: {hd['free']:.2f} GB, Usage: {hd['percent']}% "
                local_time, boot_time = system_info.get_time_info()
                logging.info("ALL-info retrived successfully.")  

                return f"'Os-info': Operating System: {os_info}, HostName: {hostname}, User: {user}//\
                         'Cpu-info': CPU Count: {cpu_count} GB, CPU Usage: {cpu_percent}%//\
                         'Memory-info': Total Memory: {total_mem:.2f} GB, Used Memory: {used_mem:.2f} GB, Free Memory: {free_mem:.2f} GB//\
                         'Process-info': Number of processes running: {len(process)}//\
                         'Hard-Disk': {hd_result}//\
                         'Time': Local Time: {local_time}, Boot Time: {boot_time}."
            
            elif metric not in metrics:
                 logging.error(f"Invalid Metric Provided. Input: {metric}")
                 raise NoArgumentsException("Error: Invalid Metric Provided. Please Provide Metric From The List > [os_info, cpu, mem, proc, hd, time, all]")

            return jsonify()   
     
        except NoArgumentsException as nae:
            return(f"NoArgumentsException: {str(nae)}"), 400
            

        finally:
            logging.info("Argument parsing completed.")


@app.route('/systeminfo/json', methods= ['GET'])
def systeminfojson():
        try:
            metric = request.args.get('metric')
            system_info = SystemInfo()
            system= {}

            if metric == "os_info":
                os_info, hostname, user = system_info.get_os_info()
                system['Operating System'] = os_info
                system['HostName'] = hostname
                system['User'] = user
                logging.info("OS-info retrived successfully.")
                return jsonify(system)

            elif metric == "cpu":
                cpu_count, cpu_percent = system_info.get_cpu_info()
                system['CPU Count'] = (f"{cpu_count} GB" )
                system['CPU Usage'] = (f"{cpu_percent}%") 
                logging.info("CPU-info retrived successfully.")
                return jsonify(system)

            elif metric == "mem":
                total_mem, used_mem, free_mem = system_info.get_memory_info() 
                system['Total Memory'] = (f"{total_mem:.2f} GB")
                system['Used Memory'] = (f"{used_mem:.2f} GB")
                system['Free Memory'] = (f"{free_mem:.2f} GB") 
                logging.info("MEMORY-info retrived successfully.")
                return jsonify(system)     

            elif metric == "proc":
                processes = system_info.get_process_info()
                system['Number of processes running'] = len(processes)
                logging.info("PROCESSES-info retrived successfully.")
                return jsonify(system)

            elif metric == "hd":
                hd_info = system_info.get_hd_info()
                for hd in hd_info:
                    system['Hard Disk'] = (f"Disk: {hd['device']}, Total: {hd['total']:.2f} GB, Used: {hd['used']:.2f} GB, Free: {hd['free']:.2f} GB, Usage: {hd['percent']}%")
                logging.info("HARD DISK-info retrived successfully.") 
                return jsonify(system)

            elif metric == "time":
                local_time, boot_time = system_info.get_time_info()
                system['Local Time'] = local_time
                system['Boot Time'] = boot_time
                logging.info("TIME-info retrived successfully.")
                return jsonify(system)

            elif metric == "all":
                os_info, hostname, user = system_info.get_os_info()
                cpu_count, cpu_percent = system_info.get_cpu_info()
                total_mem, used_mem, free_mem = system_info.get_memory_info()
                processes = system_info.get_process_info()
                hd_info = system_info.get_hd_info() 
                for hd in hd_info:
                    hd_result = (f"Disk: {hd['device']}, Total: {hd['total']:.2f} GB, Used: {hd['used']:.2f} GB, Free: {hd['free']:.2f} GB, Usage: {hd['percent']}%") 
                local_time, boot_time = system_info.get_time_info()

                system['all'] ={
                    'Os-info': f"Operating System: {os_info}, HostName: {hostname}, User: {user}",
                    'Cpu-info': f"CPU Count: {cpu_count} GB, CPU Usage: {cpu_percent}%",
                    'Memory-info': f"Total Memory: {total_mem:.2f} GB, Used Memory: {used_mem:.2f} GB, Free Memory: {free_mem:.2f} GB",
                    'Process-info': f"Number of processes running: {len(processes)}",
                    'Hard-Disk': f"{hd_result}",
                    'Time': f"Local Time: {local_time}, Boot Time: {boot_time}"
                }
                logging.info("ALL-info retrived successfully.")
                return jsonify(system)
            
            else:
                logging.error(f"Invalid Metric Provided. Input: {metric}")
                raise NoArgumentsException("Error: Invalid Metric Provided. Please Provide Metric From The List > [os_info, cpu, mem, proc, hd, time, all]")

        except NoArgumentsException as nae:
            logging.error(f"NoArgumentsException: {nae}")
            return jsonify({'error': str(nae)}), 400

        finally:
            logging.info("Argument parsing - JSON - completed.")
            


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
