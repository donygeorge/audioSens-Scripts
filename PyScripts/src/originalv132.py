import csv
import math
import os
import json
import sys

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


def orig_main_function(folder_name):
#    if (os.path.isdir(folder_name+"/data") ==0):
#        print("skipping!!!!!!!!!!!!!!!!!!"+folder_name)
#        return
    os.chdir(folder_name)
    
    outfile1 = open("orig.csv", "wb")
    outfile2 = open("hour.csv", "wb")

    wr = csv.writer(outfile1, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    wr2 = csv.writer(outfile2, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    f = open("aggregate.csv", "r")
    reader = csv.reader(f)
    
    hour_index = [0]* 25
    hour_count = [0] * 25
    rowcount = 0
    
    for row in reader:
        if rowcount==0:
            rowcount =1
            continue
        datetime=row[0]
        inf=row[1]
        print(datetime)
        [date,time]=datetime.split(" ")
        [year,month,day]=date.split("-")
        [hour,minute]=time.split(":")
        
        total=0
        for i in range(1,61):
            total = total + float(row[i])
        outrow = datetime + ','+ str(total/60)
        wr.writerow(outrow.split(','))
        
        hour_index[int(hour)] = hour_index[int(hour)] + total/60
        hour_count[int(hour)]=hour_count[int(hour)] + 1
        
        #endif for file type open
        last_datetime=datetime
    #endfor reader row
    
    for i in range(0,24):
        if hour_count[i]>0:
            outrow = str(i) + ','+ str(hour_index[i]/hour_count[i])
        else:
            outrow = str(i) + ','+ str(0)

        wr2.writerow(outrow.split(','))
        
    f.close()
#enddef

#the main function
if __name__ == "__main__":
    folder_name = "f:/data5/note"
    
    if (len(sys.argv) > 1):
        folder_name = sys.argv[1]
    orig_main_function(folder_name)       
#endif for main