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
    os.chdir("F:/Study2/data")
    listing = os.listdir(os.getcwd())
    listing.sort();
    
    seccount=55
    for index in xrange(1,61):
        outfile = open("aggregate"+str(index)+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        
        
        output='datetime'
        for i in xrange(0,55):
            output = output +',s'+formatno(i+1,3)
        wr.writerow(output.split(','))
                    
        count2_arr = [0] * seccount #(index)#*seccount + 1)
        total2_arr = [0] * seccount #(index)#*seccount + 1)
        rowcount=0
    
    
        for infile in listing:
            if(infile.endswith('.csv') and infile.startswith('p')):
                
                #print("1ind"+str(rowcount%index))
                print "\nRead file:"+infile
                f = open(infile, "r")
                reader = csv.reader(f)
                last_second=0;
    
                #print("rowcount:"+str(rowcount)+",seccount:"+str(seccount))
                #print("c:"+str(count2_arr))
                #print("ind"+str(rowcount%index))
                if(rowcount%index==0):
                    #print("index1:"+str(index))
                    count2_arr = [0] * seccount #(index)#*seccount)
                    total2_arr = [0] * seccount #(index)#*seccount)
                #endif
                #print("sc:"+str(count2_arr))
                
                rowcount=rowcount+1
                
                
                for row in reader:
                    datetime=row[0]
                    inf=row[1]
                    [date,time]=datetime.split(" ")
                    [year,month,day]=date.split("-")
                    [hour,minute,msecond]=time.split(":")
                    second= int(msecond) / 1000
                    ms=int(msecond) % 1000;
                    
                    #print("index:"+str(index))
                    #print("act:"+str(((rowcount-1)%index)*seccount+second))
                    if second<seccount:
                        if float(inf) == 1.0:
                            count2_arr[(((rowcount-1)%index)*seccount+second)/index] = count2_arr[(((rowcount-1)%index)*seccount+second)/index] + 1
                        #endif
                        #print("total:"+str((((rowcount-1)%index)*seccount+second)/index))
                        total2_arr[(((rowcount-1)%index)*seccount+second)/index] = total2_arr[(((rowcount-1)%index)*seccount+second)/index] + 1
                        #print("total:"+str(((rowcount-1)%index)*seccount+second))
                    #endif
                #endfor
                
                if(rowcount%index==0):
                    outrow = datetime[:-6]
                    for i in xrange(0,seccount):
                        if total2_arr[i]>0:
                            temp_float = (float(count2_arr[i])*100)/total2_arr[i]
                            outrow = outrow + ','+ str(temp_float)
                        else:
                            break
                    #endfor
                    wr.writerow(outrow.split(','))
                #endif
                
                f.close()
            #endif to check file type
        #endfor 
    #endfor
                
#endif for main