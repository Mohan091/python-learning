import psutil 
import compress


def cpu_log():
    cpu = psutil.cpu_percent()
    file_format = f"CPU percenatge is: {cpu}"
    with open('cpu_log.txt','w') as logfile:
        logfile.write(file_format)

cpu_log()

compress.file_compress()

