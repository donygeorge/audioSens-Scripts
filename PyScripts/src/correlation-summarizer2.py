import csv
import math
import os
import json
from scipy import stats

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
    
    maxPeriod = 300

    for infile in listing:
        outfile = open(os.getcwd()+"/derived/correlation-summarizer/"+infile+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        for period in range(1,maxPeriod+1):
            outrow = ''
            print infile +str(period)

            mainList = list()
            currentTotal = [0] * (period+1)

            for sample in range(0,period+1):
                mainList.append(list())

            f = open(os.getcwd()+"/data/"+infile+"/aggregate.csv", "r")    
            reader = csv.reader(f)
            header = reader.next()
            
            current_count = 0
            prev_datetime=''
            
            totalList = list()
            
            totalcount = 0
            total = 0
            
            for row in reader:
                datetime=row[0]
                for index in range(1,61):
                    if totalcount >= period:
                        totalList.append(total/period)
                        for sample in range(1,period+1):
                            mainList[sample].append(currentTotal[sample]/sample)

                        totalcount = 0
                        total = 0
                        for sample in range(1,period+1):  
                            currentTotal[sample] = 0

                    total = total + float(row[index])
                    
                    for sample in range(1,period+1):
                        if totalcount < sample:
                            currentTotal[sample] = currentTotal[sample] + float(row[index])
                    totalcount = totalcount + 1 
                #end for
            #end for
            
            for sample in range(1,period+1):            
                temp = stats.pearsonr(totalList, mainList[sample])
                #print temp
                corr = temp[0]
                if len(outrow) >= 1:
                    outrow = outrow + "," + str(corr)
                else:
                    outrow = str(corr)
            
            f.close()
            print outrow
            wr.writerow(outrow.split(','))
            #break

        #end multiple
        #
        #break
    #end for different users                
#endif for main