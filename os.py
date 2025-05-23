import os 

# cd=os.getcwd()
# print(cd)

# list = os.listdir()
# print(list)

# print(os.chdir('../'))
# print(os.listdir())

# env = os.getenv('test')
# print(env)

# umask = os.umask(18)
# print(umask)

# uname = os.uname()
# print(uname)

# directory=os.makedirs('test.py',mode=755,exist_ok=True)
# print(f'Directory name is {directory}')


file = os.open('file.py',os.O_CREAT)
print(file)
os.write(file,b'test')
os.close(file)
