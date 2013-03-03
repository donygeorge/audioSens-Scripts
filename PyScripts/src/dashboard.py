import csv
import os 

coverage=80
corr=0.9
minRange=30
user = "keshav"
os.chdir("F:/Study3/derived")

powerCSV=csv.reader(open(os.getcwd()+"/power-table/power.csv","rb"),delimiter=',')
corrCSV=csv.reader(open(os.getcwd()+"/correlation-summarizer/"+user+".csv","rb"),delimiter=',')
coverageCSV=csv.reader(open(os.getcwd()+"/coverage5onwards-summary/"+user+".csv","rb"),delimiter=',')

powerTable=[ [float(q) for q in p] for p in list(powerCSV) ]
corrTable=[ [float(q) for q in p] for p in list(corrCSV) ]
coverageTable=[ [float(q) for q in p] for p in list(coverageCSV) ]

opList = []
for i in xrange(minRange,len(corrTable)):
    for j in xrange(0,len(corrTable[i])):

        if coverageTable[i][j] > coverage and corrTable[i][j] > corr:
            opList.append((powerTable[i][j], 4.98*17/powerTable[i][j] ,j+1, i+1, coverageTable[i][j], corrTable[i][j]))
    

opList = sorted(opList, key=lambda element: element[0])
    
print("length:"+str(len(opList)))
print(opList)