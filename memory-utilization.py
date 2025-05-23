import psutil
from datetime import *
import os
# import sleep
import tarfile


LOG_FILE = "memory-utilization.log"
LOG_DIRECTORY = "memory-logs"
LOG_PATH = os.path.join(LOG_DIRECTORY, LOG_FILE)
TIMESTAMP = datetime.now().strftime("%d-%m-%Y,%H:%M:%S")
ARCH_DIR = "memory-archive"
ARCH_DIR_FORMAT = datetime.now().strftime("%d,%b%Y-%H-%M-%S")
TAR_FILE_NAME = f"{ARCH_DIR_FORMAT}.tar.gz"
TAR_FILE_PATH = os.path.join(ARCH_DIR,TAR_FILE_NAME)
INTERVAL = 1


def create_dir():
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
    os.makedirs(ARCH_DIR, exist_ok=True)

create_dir()

def memory():
    # while True:
    with open(LOG_PATH, "a") as file:
        mem_utils = psutil.virtual_memory() 
        log_entry = f"{TIMESTAMP}-Memory Usage:{mem_utils.percent}%\n"
        file.write(log_entry)
        # time.sleep(INTERVAL - 1)
memory()

def file_compress(): 
    if os.path.exists(LOG_PATH):
        with tarfile.open(TAR_FILE_PATH, "w:gz") as file_compress:
            file_compress.add(LOG_PATH, arcname=LOG_FILE)
    os.remove(LOG_PATH)
    print(f"Log file compress at : {TAR_FILE_PATH}")

file_compress()

def cleanup():
    while True: 
        if os.path.exists(TAR_FILE_PATH):
            cutoff_time = datetime.now() - timedelta(minutes=5)
            # print(f"cutoff time : {cutoff_time}")
            for archive_file in os.listdir(ARCH_DIR):
                archive_path = os.path.join(ARCH_DIR, archive_file)
                # print(f"archive path : {archive_path}")
                # print(f"archive file : {archive_file}")
                if os.path.isfile(archive_path): 
                    file_mod_time = datetime.fromtimestamp(os.path.getmtime(archive_path))
                    # print(f"file modified time : {file_mod_time}")
                    if file_mod_time < cutoff_time : 
                        os.remove(archive_path)
                        print(f"Deleted old archive file: {archive_path}")

cleanup()        
