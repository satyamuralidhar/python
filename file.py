
import os
path = "D:\\python\\test\\"
with open( path + 'Ram.txt' , 'w') as f:
    pass
    f.write('Hi this is satya')    
    #over write this file
    f.seek(0)
    f.write('Hi this is muralidhar')
    f.seek(1)
    f.write('ey ')
os.rename(path + 'Ram.txt' , path +'Sam.txt') 
