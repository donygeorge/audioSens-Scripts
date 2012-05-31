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
            
    f = open("values.csv", "r")
    reader = csv.reader(f)
    
    outfile = open("pastaggr.csv", "wb")
    wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)


    pastA=''
    pastB=''
    pastC=''
    pastD=''
    count=0
    totcount=0
    
    #output='sec -3,sec-2,sec -1,cur,count,tot, percent'
    #wr.writerow(output.split(','))
            

    L=[]
    for row in reader:
        A=row[0]
        B=row[1]
        C=row[2]
        D=row[3]
        
        if(pastA!=''):
            if(pastA==A and pastB ==B and pastC==C and pastD==D):
                count=count+1
                totcount=totcount+1
            else:
                outrow=pastA+','+pastB+','+pastC+','+pastD+','+str(count)
                
                if(pastA==A and pastB ==B and pastC==C):
                    totcount=totcount+1
                    L.append(outrow)
                else:
                    for item in L:
                        temp=item+','+str(totcount)
                        wr.writerow(temp.split(','))
                        L=[]
                    totcount=1
                count=1
                
        pastA=A
        pastB=B
        pastC=C
        pastD=D
    f.close()
                
#endif for main