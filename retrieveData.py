import time
import os
import subprocess
import OSC
import requests
import json
from pprint import pprint

#subprocess.call("pd master.pd &", shell=True)
client = OSC.OSCClient()
client.connect(('127.0.0.1', 9000))

def sendToPureData(no):
	print "sending to patch"
	print no
	no = str(no)
	no = no[5:]
	no = float(no)
	client.send(OSC.OSCMessage("/myPatch", no)) 	

while True:
	#replace this with whatever URL you want to get your data from, the one below is for books
	#myJSON = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699')
	myJSON = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	myJSON = json.loads(myJSON.text)
	data = myJSON['bpi']["EUR"]["rate_float"]
	
	sendToPureData(data)
	time.sleep(3)				#arbitrary time to refresh load, every 3 seconds
    	print myJSON['bpi']["EUR"]["rate_float"]
    

