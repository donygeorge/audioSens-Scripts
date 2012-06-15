import csv
import math
import os
import json
import sys
import testv132
import voiceClassifier132
import aggregatorv132
import aggregatormulti132

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
    folder_name ='c:/study3/data-aggr/hossein/'
    os.chdir(folder_name) 
    listing0 = os.listdir(os.getcwd())
    listing0.sort();
    
    for infile0 in listing0:
        #infile0 = 'note' #temp
        if (os.path.isdir(infile0) !=0):
            print("reading: " + folder_name+infile0)
            #testv132.test_main_function(folder_name+infile0) 
            #voiceClassifier132.vc_main_function(folder_name+infile0) 
            aggregatorv132.aggr_main_function(folder_name+infile0)
            aggregatormulti132.aggr2_main_function(folder_name+infile0)
            os.chdir(folder_name)  
        #endif folder
        #break #temp
    #end for  folder 
#endif for main