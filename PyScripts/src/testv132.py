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

def print16time(last_hour,last_minute,i):
    last_second=i*16
    #print(last_minute);
    last_minute = last_minute + last_second/60000
    last_hour = last_hour + last_minute/60
    return formatno(last_hour,2)+":"+formatno(last_minute%60,2)+":"+formatno(last_second%60000,5)
#enddef
    

#the main function
if __name__ == "__main__":
    os.chdir("F:/Study2/data2-vibrant")
    listing = os.listdir(os.getcwd())
    listing.sort();
    
    #versionno="-1";
    
    feature_nop=[]
    feature_pv=[]
    feature_rse=[]
    last_minute=-1
    last_hour=-1
    last_day=-1
    last_month=-1
    last_year=-1;
    last_date=-1;
    last_timestamp="";
        
    count=0
            
    
    for infile in listing:
        if(infile.endswith('.txt')):
            print infile
            curfile = open(infile, "r")
            curfile.readline()
            #fetaure_
            for line in curfile:
                strarr = line.split(', ',7)
                #print strarr          
                arr = json.loads(strarr[7])
                feature = arr["feature"]
                data=arr["data"]
                data=data[1:-1]
                #print data
                dataarr=data.split(",")
                timestamp = arr["timestamp"]
                datetime=arr["date"]
                part=arr["part"]
                count_orig=arr["count"]
                [date,time]=datetime.split(" ")
                [year,month,day]=date.split("-")
                [hour,minute,second]=time.split(":")
                
                if(last_hour==-1):
                    last_minute=minute
                    last_hour=hour
                    last_year=year
                    last_month=month
                    last_day=day
                    last_date=date
                    last_timestamp = timestamp
                #endif
                    
                
                if(part==0):
                    if(len(feature_nop)>0 and len(feature_rse)>0 and len(feature_pv)>0):
                        opfilename = "o"+last_date+"-"+last_hour+""+last_minute
                        outfile = open(opfilename+".csv", "w")
                        temp_second=0
                        
                        min = len(feature_nop)
                        if(min>len(feature_rse)):
                            min = len(feature_rse)
                        if(min>len(feature_pv)):
                            min = len(feature_pv)
                        
                        for i in range(0,min):
                            opstr=""
                            opstr=last_date+' '+print16time(int(last_hour),int(last_minute),i)+","+str(last_timestamp)+",";
                            opstr+=str(feature_pv[i])+","+str(feature_nop[i])+","+str(feature_rse[i])+"\n"
                            outfile.write(opstr)
                            #temp_second+=16
                        #endfor
                        outfile.close()
                        print "file created:"+opfilename
                    #endif
        
                    feature_nop=[]
                    feature_rse=[]
                    feature_pv=[]
                #endif
                    
                if(feature=="no_correlation_peak"):
                    count=count+1
                    feature_nop+=dataarr
                elif(feature=="relative_spectral_entropy"):
                    feature_rse+=dataarr
                elif(feature=="max_correlation_peak_value"):
                    feature_pv+=dataarr
                #endif  
                
                last_minute=minute
                last_hour=hour
                last_year=year
                last_month=month
                last_day=day
                last_date=date
                last_timestamp = timestamp                    
                #print decoded_arr
                #print arr["data"]
            #endfor
            
            print "count:"+str(count)
        #endif
    #endfor
    
    if(len(feature_nop)>0 and len(feature_rse)>0 and len(feature_pv)>0):
        opfilename = "o"+date+"-"+last_hour+""+last_minute
        outfile = open(opfilename+".csv", "w")
        temp_second=0
        print("OVERFLOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:"+opfilename)
                
        min = len(feature_nop)
        if(min>len(feature_rse)):
            min = len(feature_rse)
        if(min>len(feature_pv)):
            min = len(feature_pv)

        for i in range(0,min):
            opstr=""
            opstr=str(last_year)+'-'+str(month)+'-'+str(day)+' '+print16time(int(last_hour),int(last_minute),i)+","+str(last_timestamp)+",";
            opstr+=str(feature_pv[i])+","+str(feature_nop[i])+","+str(feature_rse[i])+"\n"
            outfile.write(opstr)
            #temp_second+=16
        #endfor 
        outfile.close()
        print "file created:"+opfilename
    #endif
    
#endif

