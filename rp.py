import requests
from requests.auth import HTTPBasicAuth
import time


lamp = 0
for i in range(6):
	if lamp == 0:
		r = requests.get('http://10.0.1.13:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/on', auth=HTTPBasicAuth('admin', 'WelcometoCX01'))
	else:
		r = requests.get('http://10.0.1.13:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/off', auth=HTTPBasicAuth('admin', 'WelcometoCX01'))
	lamp = not lamp
	print(lamp)
	time.sleep(1)





#print(r.text)