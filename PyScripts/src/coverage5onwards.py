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
    os.chdir("F:/Study3")
    listing = os.listdir(os.getcwd()+"/data")
    listing.sort();
    
    interval = 10
    maxMultiple = 60

    speech_length = 5
    
    for infile in listing:
        f = open(os.getcwd()+"/derived/silentlengths/"+str(speech_length)+"/"+infile+".csv", "r")
        outfile = open(os.getcwd()+"/derived/coverage5onwards/"+str(speech_length)+"/"+infile+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
        reader = csv.reader(f)
        myList = list(reader)
        print infile
        for multiple in range(1,maxMultiple+1):
            outrow = ''
            print infile +str(multiple)
            for sample in range(1,interval+1):
                count = 0
                secondCount = 0
                period = interval * multiple
                duration = sample * multiple
                totalcount = 0
                for element in myList:
                    secondCount = secondCount + int(element[1])
                    
                    if int(element[2]) < 5:
                        secondCount = secondCount + int(element[2])
                        continue
                    
                    totalcount = totalcount + 1
                    
                    #already recording
                    if ((secondCount) % period) < duration:
                        count = count + 1
                        #print "case1"
                        secondCount = secondCount + int(element[2])
                        continue
                    
                    start = secondCount / period
                    end = (secondCount + int(element[2]) - 1) / period
                    
                    if end > start:
                        count = count + 1
                        #print "case2"
                        secondCount = secondCount + int(element[2])
                        continue
                    secondCount = secondCount + int(element[2])
                    #print "case3"
                #end one number
                percent = count * 100 / totalcount
                if len(outrow) >= 1:
                    outrow = outrow + "," + str(percent)
                else:
                    outrow = str(percent)
                #break
            #end for multiple
            wr.writerow(outrow.split(','))
            #break
        #end for multiple ranges
        f.close()
        #break
    #end for different users                
#endif for main