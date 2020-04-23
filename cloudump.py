#!/usr/bin/python
#
####################################################################################
#[S] SCRIP : Cloudump                                                              #
#[J]   JOB : identifying real IP of CloudFlare protected website.                  #
#[A]Codedby: ghosthub (b@b@y)                                                      #
####################################################################################
##
##Modlues
import sys,os,re,socket
from time import sleep
try:
	import requests
except ImportError:
	print("\n[!] Error: requests module is missed Please install it use command: pip install requests")
	exit(1)
try:
	import json
except ImportError:
	print("\n[!] Error: JSON module is missed Please install it use command: pip install simplejson")
	exit(1)	
os.system("cls||clear")
####=COLORS=########
wi = '\033[1;37m' ##>>White
rd = '\033[1;31m' ##>Red
gr = '\033[1;32m' ##>Green
yl = '\033[1;33m' ##>Yallow
####################
def cnet():
	try:
		ip =  socket.gethostbyname("www.google.com")
		con = socket.create_connection((ip,80), 2)
		return True
	except socket.error:
		pass
	return False

def getINFO(IP):
	try:
                response = requests.get("http://ip-api.com/json/"+IP).text
		labs = json.loads(response.decode("utf-8"))
		info = [
		labs['query'].encode('ascii','replace'),
		labs['status'].encode('ascii','replace'),
		labs['regionName'].encode('ascii','replace'),
		labs['country'].encode('ascii','replace'),
		labs['city'].encode('ascii','replace'),
		labs['isp'].encode('ascii','replace'),
		str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'),
		labs['zip'].encode('ascii','replace'),
		labs['timezone'].encode('ascii','replace'),
		labs['as'].encode('ascii','replace')]
                sleep(0.10)
                print(gr + "\t\t IP: " +wi+info[0])
                sleep(0.10)
                print(gr+ "\t\t Status: " +wi+info[1])
                sleep(0.10)
                print(gr+ "\t\t Region: " +wi+ info[2])
                sleep(0.10)
                print(gr + "\t\t Country: " +wi+ info[3])
                sleep(0.10)
                print(gr + "\t\t City: " +wi+ info[4])
                sleep(0.10)
                print(gr + "\t\t ISP: "+wi + info[5])
                sleep(0.10)
                print(gr + "\t\t Lat,Lon: "+wi+ info[6])
                sleep(0.10)
                print(gr + "\t\t ZIPCODE: "+wi + info[7])
                sleep(0.10)
                print(gr + "\t\t TimeZone: " +wi+ info[8])
                sleep(0.10)
                print(gr + "\t\t AS: " +wi+ info[9])
                sleep(0.10)
	except(KeyboardInterrupt,EOFError):
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
                sleep(1.5)
                exit(1)
        except Exception:
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Something Went Wrong"+rd+" !!!"+wi)
                print(wi+"\n["+yl+"!"+wi+"]"+yl+" You Can Show The GeoIP OF Target In [ "+wi+"https://whatismyipaddress.com/ip/"+str(ip)+yl+" ]"+wi)
                exit(1)
def cloudump(URL,noinfo=None):
	if cnet() !=True:
		print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Please Check Your Internet Connection "+rd+"!!!"+wi)
		exit(1)
	domain = re.sub(r'(.*://)?([^/?]+).*', '\g<2>', URL)
	try:
		fakeIP = socket.gethostbyname(domain)
	except socket.error:
		print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: "+rd+"404"+yl+" - Server Not Found "+rd+"!!!"+wi)
		exit(1)
	try:
		print(yl+"\n["+wi+"~"+yl+"]"+gr+" Analysis "+yl+"Website[ "+wi+URL+yl+" ]"+rd+"..."+wi)
		DATA = {"cfS":domain}
		headers = {"User-agent":"FireFox"}
		data = requests.post("http://www.crimeflare.org:82/cgi-bin/cfsearch.cgi",headers=headers,data=DATA).text
		print(wi+"======================"+"="*len(URL)+"=====")
                if "No working nameservers are registered." in data:
                        print(rd+"  ["+yl+"!"+rd+"]"+yl+" ERRORCode["+rd+"404"+yl+"]: Server Not Found!"+wi)
                        print(rd+"  ["+yl+"!"+rd+"]"+wi+" Please Check Your URL !")
                if "these are not CloudFlare-user nameservers" in data and "No working nameservers are registered." not in data:
                        print(rd+"  ["+yl+"!"+rd+"]"+yl+" CloudFlare "+wi+"STATUS: "+rd+" Disabled"+yl+"!"+wi)
                        print(rd+"  ["+yl+"!"+rd+"]"+yl+" This Website Not Using "+rd+"CloudFlare"+yl+" Security"+rd+" !!!"+wi)
                        print(wi+"====================================================")
                        print(gr+"["+wi+"+"+gr+"]"+wi+" IP: "+gr+fakeIP+wi)
                        if noinfo==None:
                                print(gr+"["+wi+"+"+gr+"]"+wi+" [ GEOIP INFO ]:"+gr+"======"+wi)
                                getINFO(fakeIP)
                if "Sorry, but the domain name must contain one or two dots." in data:
                        print(rd+"  ["+yl+"!"+rd+"] "+yl+"Sorry,"+wi+" but the domain name must contain one or two dots."+rd+" !!!"+wi)
                if "A direct-connect IP address was found:" in data:
                        ips =  re.findall( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",data)
                        print(wi+"  ["+gr+">"+wi+"]"+yl+" CloudFlare "+wi+" STATUS:"+gr+" Enabled"+wi)
                        print(wi+"  ["+gr+">"+wi+"]"+gr+" CloudFlare IP Is: "+wi+fakeIP)
                        print(yl+"  ======================"+"="*len(fakeIP))
                        print(gr+"  ["+wi+"+"+gr+"]"+wi+" Real IP Is: "+gr+ips[0])
                        print(yl+"  ================"+"="*len(ips[0])+wi)
                        if noinfo==None:
                                print(gr+"  ["+wi+"+"+gr+"]"+wi+" [ GEOIP INFO ]:"+gr+"======"+wi)
                                getINFO(ips[0])
                if "No direct-connect IP address was found for this domain." in data:
                        print(rd+"  ["+yl+"!"+rd+"] "+yl+"Sorry,"+wi+" I Can't Find The Real IP Address Of This Website"+yl+"!"+rd+" :("+wi)
	except(KeyboardInterrupt,EOFError):
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
                sleep(1.5)
                exit(1)
        except Exception as e:
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: "+rd+str(e)+wi)
                exit(1)               
def usage():
	print("Usage: python2 cloudump.py <Website URL>\n\nExample: python2 cloudump.py 16honey.com\n         python2 cloudump.py 16honey.com noinfo")
	exit(1)

if len(sys.argv) <2:
	print(usage())

if len(sys.argv) ==2:
        URL = sys.argv[1]
        if URL in ("-h","-H","-hh","-HH","--help","--HELP","/?"):
                print(usage())
        cloudump(URL)
        
if len(sys.argv) ==3:
        URL = sys.argv[1]
        if URL in ("-h","-H","-hh","-HH","--help","--HELP","/?"):
                print(usage())
        if sys.argv[2] in ("no","NO","nofo","NOINFO","noinfo","n","N"):
                cloudump(URL,noinfo=True)
        else:
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Unknown Option : "+rd+sys.argv[2]+wi)
                cloudump(URL)

    
