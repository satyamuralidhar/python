import os


dir(os)
help(os)
os.system("ls -l") # list the file 
#it can store listed vavles in below x varible reulst as been Zero to over this we can use subprocess module
x=os.system("ls -l")
print(x)
'''
total 4
-rw-r--r-- 1 satya satya 207 Oct  9 20:17 basic.py
0
'''
os.system("pwd")
os.getcwd()

'''task3:
------'''
os.chdir("../")
os.system("pwd")
'''
/home/satya/python
'''
os.chdir("../../")
os.listdir()

for i in os.listdir():
    print(i)

os.listdir("/etc")
os.mkdir("demo")


#os.makedirs("demo/demo1")
#os.environ
# os.getuid()
# os.getgid()
#os.rmdir("demo") # it works only for empty dir
os.removedirs("demo/demo1")

os.rename()# to rename the file

dir(os.path)
os.path.exists('/etc/hosts') #True
os.path.isfile('/etc/hostss') # False
os.path.isdir('/etc/hostss')#False
os.path.islink("/etc/rc0.d")#True
os.path.basename("/etc/hosts") #'hosts'
os.path.dirname("/etc/hosts") #'/etc'
os.path.join('/home','testfile') #/home/testfile



