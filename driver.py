import time
import datetime

while True:
	print "executing at...{0}".format(datetime.datetime.now())
	execfile('status.py')
	time.sleep(90)