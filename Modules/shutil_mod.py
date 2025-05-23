import shutil 
import os 
# shutil.copy("shutil_mod.py", "main.py")
# os.remove("main.py")

# shutil.copy2("shutil_mod.py","main.py")

# shutil.copytree("test","mohan")
# shutil.rmtree("test")
# print(shutil.disk_usage("/dev/sdb"))

# shutil.move("os.py","../")

num = 1
file_name = "test.txt"
dir_name = f"mohan-{num}"
dir_path = f"{dir_name}/{file_name}"
file_msg = "this is test message in file"


def create_dir():
    os.makedirs(dir_name,exist_ok=True)
    with open(dir_path,'w') as file:
        file.write(file_msg)
    for num in range(2,11):
        shutil.copytree(dir_name,f"mohan-{num}")
create_dir()


# def rm_dir():
#     for num in range(1,11):
#         shutil.rmtree(f"mohan-{num}")
# rm_dir()        