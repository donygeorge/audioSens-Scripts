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
    os.chdir("F:/Study2") 
    fileStart="data3"
    listing0 = os.listdir(os.getcwd())
    listing0.sort();
    
    for infile0 in listing0:
        if(infile0.startswith(fileStart)):
            print "in data set :" +infile0
            os.chdir("F:/Study2/"+infile0)
            listing = os.listdir(os.getcwd())
            listing.sort();
            outfile = open("aggregate.csv", "wb")
            wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            
            output='datetime'
            for i in xrange(60):
                output = output +',s'+formatno(i+1,2)
            wr.writerow(output.split(','))
                            
            rowcount=0
        
            for infile in listing:
                if(infile.endswith('.csv') and infile.startswith('p')):
                    rowcount=rowcount+1
                    print "\nRead file:"+infile
                    f = open(infile, "r")
                    reader = csv.reader(f)
                    last_second=0;
                    cur_count=0;
                    cur_total=0;
                    last_datetime=-1;
                    count_arr = [0] * 60
                    total_arr = [0] * 60
        
                    for row in reader:
                        datetime=row[0]
                        inf=row[1]
                        [date,time]=datetime.split(" ")
                        [year,month,day]=date.split("-")
                        [hour,minute,msecond]=time.split(":")
                        second= int(msecond) / 1000
                        ms=int(msecond) % 1000;
                        
                        if(second==0  and total_arr[1]>0):
                            outrow = last_datetime[:-6]
                            for i in xrange(60):
                                if total_arr[i]>0:
                                    temp_float = (float(count_arr[i])*100)/total_arr[i]
                                    outrow = outrow + ','+ str(temp_float)
                                else:
                                    break
                            #endfor
                            wr.writerow(outrow.split(','))
                            count_arr = [0] * 60
                            total_arr = [0] * 60
                        #endif to output
                        
                        
                        if second<60:
                            if float(inf) == 1.0:
                                count_arr[second] = count_arr[second] + 1              
                            #endif
                            total_arr[second] = total_arr[second] + 1
                        
                        #endif for file type open
                        last_datetime=datetime
                    #endfor reader row
                    
                    if(total_arr[59]>0):
                        outrow = last_datetime[:-6]
                        for i in xrange(60):
                            if total_arr[i]>0:
                                temp_float = (float(count_arr[i])*100)/total_arr[i]
                                outrow = outrow + ','+ str(temp_float)
                            else:
                                break
                        #endfor
                        wr.writerow(outrow.split(','))
                        count_arr = [0] * 60
                        total_arr = [0] * 60
                    #endif to output
                        
                    
                    f.close()
                #endif to check file type
            #endfor 
        #endif folder
    #end for  folder
                
#endif for main