import cookielib, urllib2, socket, urllib, re, os, csv, math
from optparse import OptionParser

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

path="c:/study3/data4"
#argument parser

if (os.path.isdir(path) == 0):
    os.makedirs(path)
os.chdir(path)


for index in range(1,15):
    
    sday=index
    smonth='Jun'
    syear=2012
    reqlevel='Any'
    
    smonth_no = 0
      
    
    tag_control='AcousticAppControl'
    tag_data='AcousticAppData'
    
    eday=sday
    emonth=smonth
    eyear=syear
    shour = '00'
    sminute ='00'
    ehour='23'
    eminute='59'
    imei = '355213041577065'
    name='hossein'
    
    if (smonth is 'Jun'):
        smonth_no = 6
    elif (smonth is 'May'):
        smonth_no = 5
    elif (smonth is 'Jul'):
        smonth_no = 7
        
    f = open('imei.csv', "r")
    logfile = open('log-'+str(sday)+'-'+smonth+'-'+str(syear)+'.csv', 'wb')
    log = csv.writer(logfile, quoting=csv.QUOTE_MINIMAL)
    reader = csv.reader(f)
    for row in reader:
        imei=row[0]
        name=row[1]
    
        if (os.path.isdir(path+'/'+name) == 0):
            os.makedirs(path+'/'+name)
        
        opfilename=name+'/'+name+'-'+formatno(syear,4)+'-'+formatno(smonth_no,2)+'-'+formatno(sday,2)+'.txt'
        outfile = open(opfilename, "w")
        
        print("Getting data for "+name+"...")
        
        #get url opener
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #default timeout in seconds
        #socket.setdefaulttimeout(1800)
        #get fist page
        firstPage = opener.open("http://systemlog.ohmage.org/systemlog/logs/login/").read()
        #get secret no set by Hossein
        secret = re.search("value='([^']{32})'", firstPage).group(1)
        #login with secret and Dony's password
        loginParams = urllib.urlencode({'username': 'dony', 'password': 'George', 'login': 1, 'next':'/systemlog/logs/', 'csrfmiddlewaretoken': secret})
        opener.open("http://systemlog.ohmage.org/systemlog/logs/login/", loginParams).read()
        
        dumpParams = urllib.urlencode({'reqlevel': reqlevel, 'dump': 'Dump', 
                                       'reqimei':  imei,
                                       'reqtag': tag_data,
                                       'shour': shour, 'sminute': sminute, 'smonth': smonth, 'sday': sday, 'syear': syear,
                                       'ehour': ehour, 'eminute': eminute, 'emonth': emonth, 'eday': eday, 'eyear': eyear})
        outfile.write(opener.open("http://systemlog.ohmage.org/systemlog/logs/", dumpParams).read())
        outfile.flush()
        outfile.close()
        no_of_bytes = os.path.getsize(opfilename)
        no_of_bytes = no_of_bytes/1000
        
        outrow = [row[0]]
        outrow.extend([row[1]])
        outrow.extend([str(no_of_bytes)])
        log.writerow(outrow)
        print("Received "+str(no_of_bytes)+" KB of data for "+name+".")
    #end imei for
    print("\n Compeleted successfully for day "+str(sday))
#end day for
print("\n Compeleted successfully")
f.close()
logfile.close()
