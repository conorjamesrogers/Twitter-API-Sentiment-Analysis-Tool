from twitter import *
import markovify
import pickle
import config


# tester = {}
# execfile("markovTest.py",tester)
# with open(os.path.join(os.path.dirname('__file__'), 'paradise_model'))as g:
# 	paradise_model = g.read()

# print paradise_model

def writeStatus(file):

    with open(file,'rb') as f:
        paradise_model = pickle.load(f)

    model = markovify.Text.from_json(paradise_model)
    #status in question
    testStatus = model.make_short_sentence(140, tries = 100)

    config_dict = config.access()
    print(config_dict)
    # # twitter API object creation
    # twitterObj = Twitter(auth = OAuth(config_dict["access_token"], config_dict["access_secret"], config_dict["consumer_key"], config_dict["consumer_secret"]))

    # # Posting new status
    # result = twitterObj.statuses.update(status = testStatus)

    # for x in range(0, 10):
    # 	print model.make_short_sentence(140, tries = 100)

    print("should have updated status as: {0}".format(testStatus))

