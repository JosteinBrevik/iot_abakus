import sys
import threading
from Naked.toolshed.shell import muterun_js

import sys
from twython import Twython

import requests
from requests.auth import HTTPBasicAuth
import time


CONSUMER_KEY = '0NPPS5ox4Fj9huir7M5LmcZFm'
CONSUMER_SECRET = 'bL50LFzCfWou7xAmkbsvOkcUbl9hIktb26pcwdCiCIFA2ffazv'
ACCESS_KEY = '398979418-2fUZrfhN6McruTxhJd59YOkv7xg2mI1Fkb8lN3Bc'
ACCESS_SECRET = '6PJnq4tXQXK1lwHHazRVqU1Z3B9TcurLm11aVY2g6BOWP'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 





class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
    	response = muterun_js('example2.js')


def blink(n):
	lamp = 0
	for i in range(n):
		if lamp == 0:
			r = requests.get('http://10.0.1.13:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/on', auth=HTTPBasicAuth('admin', 'WelcometoCX01'))
		else:
			r = requests.get('http://10.0.1.13:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/off', auth=HTTPBasicAuth('admin', 'WelcometoCX01'))
		lamp = not lamp
		#print(lamp)
		time.sleep(1)


thread1 = myThread(1, "Thread-2", 1)
thread1.start()

best = 0.0
while True:
	with open("input.txt", "r") as f:
		for line in f:
			new = line.strip()
			new = float(new)
			new = "{0:.2f}".format(new)

	new = float(new)
	if new > best:
		print(best)
		best = new
		with open("input3.txt", "a") as f0:
			f0.write(str(best) + "\n")
		api.update_status(status="Noen kastet pikaball raskere enn lynet! Den nye rekorden er " + str(new) + " m/s")
		blink(2)

"""
best = 0
while True:
	with open("input.txt", "r") as f:
		for line in f:
			new = line.strip()

	new = int(new)
	if new > best:
		best = new
		api.update_status(status="Noen kastet pikaball raskere enn lynet! Den nye rekorden er " + str(new))
		blink(2)
"""
