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
            
            
    for index in xrange(1,10):
        f = open("values"+str(index)+".csv", "r")
        reader = csv.reader(f)
        
        outfile = open("aggr"+str(index)+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
    
        pastA=''
        pastB=''
        count=0
        totcount=0
        
        #output='sec -3,sec-2,sec -1,cur,count,tot, percent'
        #wr.writerow(output.split(','))
                
    
        L=[]
        Lno=[]
        for row in reader:
            A=row[0]
            B=row[1]
            
            if(pastA!=''):
                if(pastA==A and pastB ==B):
                    count=count+1
                    totcount=totcount+1
                else:
                    outrow=pastA+','+pastB+','+str(count)
                    
                    if(pastA==A):
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
        f.close()
                
#endif for main