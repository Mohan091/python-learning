with open("file.txt", 'w') as file:
    file.write("hello, World!")
    data=file.truncate(5)
    print(data)




# with open("file.txt",'r') as f:
#     f.seek(5)
#     print(f.tell())
#     data = f.read(7)    
#     print(data)
   