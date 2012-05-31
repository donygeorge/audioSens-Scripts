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
    os.chdir("F:/Study2/") 
    fileStart="data3-hossein-complete/past/"
    os.chdir("F:/Study2/"+fileStart)
            
    f = open("pastaggr.csv", "r")
    reader = csv.reader(f)
    
    outfile = open("pastaggr1.csv", "wb")
    wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)


    pastA=''
    pastB=''
    pastC=''
    pasttot=0
    max=0
    count=0
    totcount=0
    
    output='sec -3,sec-2,sec -1,tot,highest percent'
    wr.writerow(output.split(','))
            

    L=[]
    for row in reader:
        A=row[0]
        B=row[1]
        C=row[2]
        tot=row[5]
        D=row[6]
        
        if(pastA!=''):
            if(pastA==A and pastB ==B and pastC==C):
                if(D>max):
                    max=D
            else:
                outrow=pastA+','+pastB+','+pastC+','+str(pasttot)+','+str(max)
                wr.writerow(outrow.split(','))
                max=D
                
        else:
            max=D
        pastA=A
        pastB=B
        pastC=C
        pasttot=tot
    f.close()
                
#endif for main