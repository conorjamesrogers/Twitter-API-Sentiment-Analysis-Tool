import markovify
import sys, os
import operator
import nltk
import re
import pickle
import nltk
from nltk.twitter import Twitter
from Classifier import Classification
from contextlib import redirect_stdout


class POSifiedText(markovify.Text):
	def word_split(self,sentence):
		words = re.split(self.word_split_pattern,sentence)
		words = [ "::".join(tag) for tag in nltk.pos_tag(words)]
		return words

	def word_join(self, words):
		sentence = " ".join(word.split("::")[0] for word in words)
		return sentence

def createTweetModel(keyword):
    tw = Twitter()
    # store_stdout = sys.stdout
    with open('text/tweets_'+keyword,'a') as f:
        with redirect_stdout(f):
            tw.tweets(keywords=keyword)

    # sys.stdout = f
    # sys.stdout = store_stdout
    f.close()



def createModel(keyword):
    # nltk.corpus.gutenberg.fileids()

    # with open("text/Paradise_Lost.txt") as f:
    # 	paradise_LostTxt = f.read()

    # with open('text/austen-emma.txt')as g:
    # 	austen_emmaTxt = g.read()

    # with open('text/Dongers.txt') as f2:
    # 	macbeth = f2.read()

    # with open('text/carroll-alice.txt') as f3:
    # 	Alice = f3.read()


    with open("text/tweets_"+keyword,'r') as f:
        tweet = f.read()

    tweet = tweet.replace("Written 100 Tweets",'')

    # with open("text/tweets_"+keyword,'w') as f:
    #     f.write(tweet)

    #with open(os.path.join(os.path.dirname('__file__'), "Britney.txt")) as g:
    #	b = g.read()

    # text_modelP = markovify.Text(paradise_LostTxt)
    # text_modelA = markovify.Text(austen_emmaTxt)
    # text_modelM = markovify.Text(macbeth)
    # text_modelC = markovify.Text(Alice)
    tweet_model = markovify.Text(tweet)

    #text_modelB = POSifiedText(b)

    # combo_texts = markovify.combine([text_modelP, text_modelA, text_modelM, text_modelC,tweet_model],[.2,.2,.2,.2,1])
    # combo_texts = markovify.combine([text_modelC,tweet_model])

    # pos= POSifiedText() combo_texts
    tweet_model_markov = tweet_model.to_json()


    # print mac_Bible_ParadiseToFile

    # f = open('paradise_model', 'w')
    # f.write(mac_Bible_ParadiseToFile)
    # f.close()

    with open('tweet_model_'+keyword,'wb') as outfile:
    	pickle.dump(tweet_model_markov, outfile)

    TEST = tweet_model.make_short_sentence(140, tries = 100)
    print(TEST)
    return tweet_model

if __name__ == '__main__':
    # createTweetModel('hate')
    # createTweetModel('love')
    print("creating hate model")
    tweet_model_hate = createModel('hate')
    print("creating love model")
    tweet_model_love = createModel('love')

    print('combo')
    combo_texts = markovify.combine([tweet_model_hate, tweet_model_love])
    TEST = combo_texts.make_short_sentence(140, tries = 100)
    print(TEST)
    Classification.test()









