import tarfile 
import os 
import shutil
import pathlib
from datetime import *

timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
log_dir_name = "CPU"
log_file_name = "cpu_log.txt"
log_dir = os.makedirs(log_dir_name, exist_ok=True)
copied_file_path = shutil.copy(log_file_name, log_dir_name)
compression_path = f"{log_dir_name}/cpu-{timestamp}.tar.gz"

def file_compress():
    print("compression started")
    with tarfile.open(compression_path,'w:gz') as tar:
        tar.add(name=copied_file_path,arcname=f"cpu-{timestamp}.tar.gz")
        print("compression completed")
        
if __name__ == "__main__":
    file_compress()
