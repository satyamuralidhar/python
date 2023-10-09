import os 
import json 
import subprocess as sub

filename="containers.json"
with open(filename) as file:
    file=json.load(file)
try:
    for containers in file["containers"]["Name"]:
        print(containers)
except:
    print(f"[Error] containers bames are not found",{e})
    exit(1)
for i in containers:
     sub.run("docker ps | grep -i i",stderr=sub.STDOUT,shell=True)



