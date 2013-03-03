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
    outfile = open(os.getcwd()+"/derived/power-table/power.csv", "wb")
    wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)

    maxMultiple = 600
    overhead = 2.3
    overhead_cost = 0.11
    normal_cost = 0.089
    silent_cost = 0.0057


    for period in range(1,maxMultiple+1):
        outrow = ''
        print "run" +str(period)
        for sample in range(1, period+1):
            cost = sample * normal_cost
            if (sample + overhead) >= period:
                cost = cost + (period - sample) * overhead_cost
            else:
                cost = cost + overhead * overhead_cost
                cost = cost + (period - sample - overhead) * silent_cost
                
            costPerSecond = cost /  period
            costPerSecond = costPerSecond - silent_cost
            costPerMinute = costPerSecond * 60
            
            if len(outrow) >= 1:
                outrow = outrow + "," + str(costPerMinute)
            else:
                outrow = str(costPerMinute)
            #break
        #end for multiple
        wr.writerow(outrow.split(','))
        #break
    #end for multiple ranges

#endif for main