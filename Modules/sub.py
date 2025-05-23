import subprocess 


p1=subprocess.run('cat output.txt | grep -n os.py',capture_output=True,text=True,shell=True)

# p2=subprocess.run(['grep','-n','os.py'],capture_output=True,input=p1.stdout,text=True,)
print(p1.stdout)