from twitter import *
import markovify
import pickle


# tester = {}
# execfile("markovTest.py",tester)
# with open(os.path.join(os.path.dirname('__file__'), 'paradise_model'))as g:
# 	paradise_model = g.read()

# print paradise_model
with open('paradise_model') as f:
	paradise_model = pickle.load(f)

model = markovify.Text.from_json(paradise_model)
# #status in question
# testStatus = model.make_short_sentence(140, tries = 100)

# # get token bits into a dict
# config = {}
# execfile("config.py",config)

# # # twitter API object creation
# twitterObj = Twitter(auth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))

# # # Posting new status
# result = twitterObj.statuses.update(status = testStatus)

for x in range(0, 10):
	print model.make_short_sentence(140, tries = 100)

# print "should have updated status as: %s" % testStatus



