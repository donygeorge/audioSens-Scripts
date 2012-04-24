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
    os.chdir("F:/Study2/data-emm")
    listing = os.listdir(os.getcwd())
    listing.sort();
    outfile = open("aggregate.csv", "wb")
    wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
    outfile2 = open("aggregate2.csv", "wb")
    wr2 = csv.writer(outfile2, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
            
    output='datetime'
    for i in xrange(55):
        output = output +',s'+formatno(i+1,2)
    wr.writerow(output.split(','))
                
    output='datetime'
    for i in xrange(110):
        output = output +',s'+formatno(i+1,2)
    wr2.writerow(output.split(','))
    
    count2_arr = [0] * 120
    total2_arr = [0] * 120
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
            count_arr = [0] * 60
            total_arr = [0] * 60

            if(rowcount%2==1):
                count2_arr = [0] * 120
                total2_arr = [0] * 120
            #endif
            
            for row in reader:
                datetime=row[0]
                inf=row[1]
                [date,time]=datetime.split(" ")
                [year,month,day]=date.split("-")
                [hour,minute,msecond]=time.split(":")
                second= int(msecond) / 1000
                ms=int(msecond) % 1000;
                
                if second<60:
                    if float(inf) == 1.0:
                        count_arr[second] = count_arr[second] + 1
                        if(rowcount%2==0):
                            count2_arr[55+second] = count2_arr[55+second] + 1
                        else:
                            count2_arr[second] = count2_arr[second] + 1
                        
                        
                    #endif
                    total_arr[second] = total_arr[second] + 1
                    if(rowcount%2==0):
                        total2_arr[55+second] = total2_arr[55+second] + 1
                    else:
                        total2_arr[second] = total2_arr[second] + 1

                #endif
            #endfor
            
            outrow = datetime[:-6]
            for i in xrange(55):
                if total_arr[i]>0:
                    temp_float = (float(count_arr[i])*100)/total_arr[i]
                    outrow = outrow + ','+ str(temp_float)
                else:
                    break
            #endfor
            wr.writerow(outrow.split(','))
            
            if(rowcount%2==0):
                outrow2 = datetime[:-6]
                for i in xrange(110):
                    if total2_arr[i]>0:
                        temp_float = (float(count2_arr[i])*100)/total2_arr[i]
                        outrow2 = outrow2 + ','+ str(temp_float)
                    else:
                        break
                #endfor
                wr2.writerow(outrow2.split(','))
            #endif
            
            f.close()
        #endif to check file type
    #endfor 
                
#endif for main