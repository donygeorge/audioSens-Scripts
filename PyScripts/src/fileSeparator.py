import csv
import math
import os
import json
import sys
import shutil

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


def filesep_main_function(folder_name):
    #if (os.path.isdir(folder_name+"/data") ==0):
    #    return
    #os.chdir(folder_name+'/data')
    os.chdir(folder_name)#temp
   
    if not os.path.exists("multi"):
        #print("creating")
        os.makedirs("multi")
    
    listing = os.listdir(os.getcwd()+"/data")
    listing.sort();
    #outfile = open("aggregate.csv", "wb")
    #wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
    daycount = 0
    lastdate=''                
    rowcount=0
   

    for infile in listing:
        print infile
        if(infile.endswith('.csv') and infile.startswith('p')):
            print "\nin day: " + str(daycount)
            print "\nRead file:"+infile

            [year,month,day,time]=infile.split("-")
            currentdate = year+month+day
            
            print "current" + currentdate
            print "last" + lastdate
            
            if currentdate != lastdate:
                daycount = daycount + 1
                if not os.path.exists("multi/"+str(daycount)):
                    print("creating: "+"multi/"+str(daycount))
                    os.makedirs("multi/"+str(daycount))
            
            shutil.copy ("data/"+infile, "multi/"+str(daycount)+"/"+infile)                
            lastdate=currentdate
        #endif to check file type
    #endfor 
#enddef

#the main function
if __name__ == "__main__":
    folder_name = "f:/data5/andy"
    
    if (len(sys.argv) > 1):
        folder_name = sys.argv[1]
    filesep_main_function(folder_name)       
#endif for main