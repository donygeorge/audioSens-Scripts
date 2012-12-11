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
    
    speech_threshold =20
    speech_length = 60
    
    for infile in listing:
        f = open(os.getcwd()+"/data/"+infile+"/aggregate.csv", "r")
        outfile = open(os.getcwd()+"/derived/silentlengths/"+str(speech_length)+"/"+infile+".csv", "wb")
        wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    
        reader = csv.reader(f)
        header = reader.next()
        
        current_count = 0
        prev_silence = 0
        prev_speech=0
        mode = "silent"
        distance=0
        first = 1
        prev_datetime=''
        
        for row in reader:
            datetime=row[0]
            print datetime
            for index in range(1,61):
                #print row[index]
                #print str(prev_silence)+','+str(prev_speech)+','+str(current_count)+','+str(distance)
                if mode == "silent":
                    #print "silent"
                    if float(row[index]) < speech_threshold:
                        #print "silent1"
                        current_count = current_count + 1
                        #print current_count
                    else:
                        #print "silent2"
                        if first != 1:
                            outrow = prev_datetime + "," + str(prev_silence) + "," + str(prev_speech) + "," + str(current_count)
                            wr.writerow(outrow.split(','))
                        else:
                            first = 0

                        prev_silence = current_count
                        current_count =1
                        mode = "speech"
                        distance = 0
                        prev_datetime = row[0]
                else:
                    #print "speech"
                    if float(row[index]) < speech_threshold:
                        distance = distance + 1
                        #print "speech1"
                        if distance > speech_length:
                            prev_speech = current_count
                            current_count = distance
                            distance = 0
                            mode ="silent"
                    else:
                        #print "speech2"
                        current_count = current_count + 1 + distance
                        #print current_count
                        distance = 0
            #end for
        #end for
        
        f.close()
    #end for different users                
#endif for main