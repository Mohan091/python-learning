import psutil
from datetime import *
import tarfile

timestamp = datetime.now().strftime("%d%m%Y,%H:%M:%S")
LOG_FILE = "cpu_usage.log"

def cpu_percentage(): 
    with open("cpu.txt", "w") as file: 
        cpu_details = psutil.cpu_times()
        log_write = f'{timestamp} - CPU Usage of system : {cpu_details}'
        file.write(log_write)
cpu_percentage()

# def compress_file():
#     compress_log_file = f"cpu-log-{timestamp}.tar.gz"
#     with tarfile.open(compress_log_file, "w:gz") as tar:
#         tar.add(archname=LOG_FILE)

# compress_file()
    

# with open("test.txt", "w") as file:
#     file.write("My name is Mohan")
#     print(file)