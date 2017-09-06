import time
import datetime
import status

def run():
	print("executing at...{0}".format(datetime.datetime.now()))
	status.writeStatus('paradise_model')
	time.sleep(90)

if __name__ == '__main__':
	run()