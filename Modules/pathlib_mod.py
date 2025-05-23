import pathlib

file_name = pathlib.Path("test.txt")

# if not file_name.exists():
#     file_name.touch()
#     print(f"{file_name} created")
# else:
#     print(f"{file_name} already created")


if file_name.exists():
    print("file exists")
else: 
    print("file does not exists")    