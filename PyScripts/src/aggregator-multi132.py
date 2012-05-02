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
    os.chdir("F:/Study2/data3-hossein-date1")
    listing = os.listdir(os.getcwd())
    listing.sort();
    
    if not os.path.exists("aggr"):
        print("creating")
        os.makedirs("aggr")
    
    myList=[1,2,3,5,10,20,30,60]
    
    seccount=60
    for index in myList:
        print("Run........................................................................"+str(index))
        outfile = open("aggr/aggregate"+str(index)+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        
        
        output='datetime'
        for i in xrange(0,60):
            output = output +',s'+formatno(i+1,2)
        wr.writerow(output.split(','))
                    
        count2_arr = [0] * seccount
        total2_arr = [0] * seccount
        
        rowcount=0
        
    
        for infile in listing:
            if(infile.endswith('.csv') and infile.startswith('p')):
                
                #rint("1ind"+str(rowcount%index))
                print "\nRead file:"+infile
                f = open(infile, "r")
                reader = csv.reader(f)
                last_second=0;
                rowcount=0
                last_datetime=-1;
    
    
                #print("rowcount:"+str(rowcount)+",seccount:"+str(seccount))
                #print("c:"+str(count2_arr))
                #print("ind"+str(rowcount%index))
                count2_arr = [0] * seccount
                total2_arr = [0] * seccount
                #print("sc:"+str(count2_arr))
                
                
                for row in reader:
                    #print("b")
                    datetime=row[0]
                    inf=row[1]
                    [date,time]=datetime.split(" ")
                    [year,month,day]=date.split("-")
                    [hour,minute,msecond]=time.split(":")
                    second= int(msecond) / 1000
                    ms=int(msecond) % 1000;
                    
                    #print("sec"+str(second)+"tot"+str(total2_arr[1]))
                    
                    if(second==0 and last_second>0):
                        rowcount=rowcount+1
                        #print("ne wrowc:"+str(rowcount))
                        #print(last_datetime)
                        if(rowcount%index==0):
                            #print("writing")
                            outrow = last_datetime[:-6]
                            for i in xrange(0,seccount):
                                if total2_arr[i]>0:
                                    temp_float = (float(count2_arr[i])*100)/total2_arr[i]
                                    outrow = outrow + ','+ str(temp_float)
                                else:
                                    break
                            #endfor
                            count2_arr = [0] * seccount
                            total2_arr = [0] * seccount
                            wr.writerow(outrow.split(','))
                        #endif
                    #endif
                    
                    #print("index:"+str(index))
                    #print("act:"+str(((rowcount-1)%index)*seccount+second))
                    if second<seccount:
                        if float(inf) == 1.0:
                            count2_arr[(((rowcount)%index)*seccount+second)/index] = count2_arr[(((rowcount)%index)*seccount+second)/index] + 1
                        #endif
                        
                        #print("rowcount:"+str(rowcount))
                        #print("index"+str((((rowcount)%index)*seccount+second)/index)+"  total1:"+str((total2_arr[(((rowcount)%index)*seccount+second)/index])))
                        total2_arr[(((rowcount)%index)*seccount+second)/index] = total2_arr[(((rowcount)%index)*seccount+second)/index] + 1
                        #print("total2:"+str((total2_arr[(((rowcount-1)%index)*seccount+second)/index])))
                    #endif
                    last_datetime=datetime
                    last_second=second
                #endfor
                
                if(last_second>0 and total2_arr[59]>0):
                    rowcount=rowcount+1

                    if(rowcount%index==0):
                        outrow = last_datetime[:-6]
                        for i in xrange(0,seccount):
                            if total2_arr[i]>0:
                                temp_float = (float(count2_arr[i])*100)/total2_arr[i]
                                outrow = outrow + ','+ str(temp_float)
                            else:
                                break
                        #endfor
                        count2_arr = [0] * seccount
                        total2_arr = [0] * seccount
                        wr.writerow(outrow.split(','))
                    #endif
                #endif
                    
                
                f.close()
            #endif to check file type
        #endfor 
    #endfor
                
#endif for main