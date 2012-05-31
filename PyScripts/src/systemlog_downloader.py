import cookielib, urllib2, socket, urllib, re, os, csv
from optparse import OptionParser


path="f:/study2/data4"
#argument parser

if (os.path.isdir(path) == 0):
    os.makedirs(path)
os.chdir(path)

sday='30'
smonth='May'
syear='2012'
reqlevel='Any'

tag='AcousticAppControl'

eday=sday
emonth=smonth
eyear=syear
shour = '00'
sminute ='00'
ehour='23'
eminute='59'
imei = '355213041577065'
name='hossein'

f = open('imei.csv', "r")
logfile = open('log-'+sday+'-'+smonth+'-'+syear+'.csv', 'wb')
log = csv.writer(logfile, quoting=csv.QUOTE_MINIMAL)
reader = csv.reader(f)
for row in reader:
    imei=row[0]
    name=row[1]

    if (os.path.isdir(path+'/'+name) == 0):
        os.makedirs(path+'/'+name)
    
    opfilename=name+'/'+name+'-'+sday+'-'+smonth+'-'+syear+'.txt'
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
                                   'reqtag': tag,
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
f.close()
logfile.close()
