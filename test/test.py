from twitter import *


tester = {}
execfile("markovTest.py",tester)
#status in question
testStatus = tester["TEST"]

#get token bits into a dict
config = {}
execfile("config.py",config)

#twitter API object creation
#twitterObj = Twitter(auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

#Posting new status
#result = twitterObj.statuses.update(status = testStatus)

print "should have updated status as: %s" % testStatus



