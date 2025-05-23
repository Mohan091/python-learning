import os 
import shutil
from pathlib import Path 


if not os.path.exists("test"):
    os.mkdir("test")

listdir = os.listdir("test")    

# for i in range(1,11):
#     os.mkdir(f"test/mohan-{i}") 

for i in listdir:
    shutil.rmtree(f"test/{i}")

# for i in listdir:
#     # print(os.listdir(f"test/{i}"))
#     os.removedirs(f"test/{i}")

    