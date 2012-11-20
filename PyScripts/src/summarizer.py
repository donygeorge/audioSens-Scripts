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
    
    for infile in listing:
        f = open(os.getcwd()+"/data/"+infile+"/aggregate.csv", "r")
        outfile = open(os.getcwd()+"/derived/summary/"+infile+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
        first = 1
        last_year = -1
        last_month = -1
        last_day = -1
        last_hour = -1        
        last_count = 0
    
        print infile
        
        reader = csv.reader(f)
        header = reader.next()
        for row in reader:
            datetime=row[0]
            #print datetime
            [date,time]=datetime.split(" ")
            [year,month,day]=date.split("-")
            [hour,minute]=time.split(":")
            
            year_int = int(year)
            month_int = int(month)
            day_int = int(day)
            hour_int = int(hour)
            
            if hour_int >= 24:
                hour_int = 0
                if day_int >=31:
                    day_int =1
                    if month_int >= 12:
                        month_int = 1
                        year_int = year_int + 1
                    else:
                        month_int = month_int + 1
                else:
                    day_int = day_int + 1
            #end hour
            
            
            if first == 1:
                last_year = year_int
                last_month = month_int
                last_day = day_int
                last_hour = hour_int
                last_count = 1
                first = 0
                continue
            else:
                #skipping if next row less than previous
                if last_year >= year_int:
                    if last_month >= month_int:
                        if last_day >= day_int:
                            if last_hour > hour_int:
                                continue
            #end if
            
            if last_year == year_int and last_month == month_int and last_day == day_int and last_hour == hour_int:
                last_count = last_count + 1
                continue
            #end if 
            
            buffer_count = 0
            while  last_year != year_int or last_month != month_int or last_day != day_int or last_hour != hour_int:
                if buffer_count >500:
                    print "Buffer overflow"
                    exit()
                
                outrow = formatno(last_year,4)+"-"+formatno(last_month,2)+"-"+formatno(last_day,2)+"-"+formatno(last_hour,2)
                outrow = outrow + "," + str(last_count)
                print outrow
                
                wr.writerow(outrow.split(','))
                if last_hour >= 23:
                    last_hour = 0
                    if last_day >=31:
                        last_day =1
                        if last_month >= 12:
                            last_month = 1
                            last_year = last_year + 1
                        else:
                            last_month = last_month + 1
                    else:
                        last_day = last_day + 1
                else:
                    last_hour = last_hour + 1
                #end hour
                last_count = 0
                buffer_count = buffer_count + 1                
            #end while
            last_count = 1
            
        #end for
        
        if last_count > 0:
            outrow = formatno(last_year,4)+"-"+formatno(last_month,2)+"-"+formatno(last_day,2)+"-"+formatno(last_hour,2)
            outrow = outrow + "," + str(last_count)
            wr.writerow(outrow.split(','))
        #end if
        
        f.close()
    #end for different users                
#endif for main