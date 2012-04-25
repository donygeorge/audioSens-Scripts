import csv
import math
import os
import json

def formatno(no,length):
    i=0
    if(no != 0):
        while(no<math.pow(10,length-i-1)):
            i=i+1
    else:
        i=length-1
    #endif
        
    out=""
    for j in range(0,i):
        out+=str(0);
    #endfor    
    return out+str(no)
#enddef

#the main function
if __name__ == "__main__":
    filename="F:/Study2/battery/battery2.txt"
    curfile = open(filename, "r")
    curfile.readline()
    
    opfilename = "F:/Study2/battery/obattery2.csv"
    outfile = open(opfilename, "w")
        

    offset=-1

    #fetaure_
    for line in curfile:
        strarr = line.split(', ' )
        [value0,value1] = strarr[7].split(":")
        [value,value0] = value1.split("/")
        ts = strarr[1]

        if(offset==-1):
            offset=ts
            
        temp_second=0
        
        opstr=""
        opstr="{x:"+str((long(ts)-long(offset))/60000)+",y:"+str(value)+"},\n"
                    
        outfile.write(opstr)
    #endfor
    outfile.close()
    print "file created:"+opfilename
#endif

