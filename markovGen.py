import markovify
import sys, os
import operator
import nltk
import re
import pickle

class POSifiedText(markovify.Text):
	def word_split(self,sentence):
		words = re.split(self.word_split_pattern,sentence)
		words = [ "::".join(tag) for tag in nltk.pos_tag(words)]
		return words

	def word_join(self, words):
		sentence = " ".join(word.split("::")[0] for word in words)
		return sentence

nltk.corpus.gutenberg.fileids()

with open(os.path.join(os.path.dirname('__file__'), "text/Paradise_Lost.txt")) as f:
	paradise_LostTxt = f.read()

with open(os.path.join(os.path.dirname('__file__'), 'text/austen-emma.txt'))as g:
	austen_emmaTxt = g.read()

with open(os.path.join(os.path.dirname('__file__'), 'text/shakespeare-macbeth.txt')) as f2:
	macbeth = f2.read()

with open(os.path.join(os.path.dirname('__file__'), 'text/carroll-alice.txt')) as f3:
	Alice = f3.read()

with open(os.path.join(os.path.dirname('__file__'), "text/Britney.txt")) as f4:
	Britney = f4.read()

#with open(os.path.join(os.path.dirname('__file__'), "Britney.txt")) as g:
#	b = g.read()

text_modelP = markovify.Text(paradise_LostTxt)
text_modelA = markovify.Text(austen_emmaTxt)
text_modelM = markovify.Text(macbeth)
text_modelC = markovify.Text(Alice)
text_modelBrit = markovify.Text(Britney)

#text_modelB = POSifiedText(b)

combo_texts = markovify.combine([text_modelP, text_modelA, text_modelM, text_modelC,text_modelBrit],[.2,.2,.2,1,0])

mac_Bible_ParadiseToFile = combo_texts.to_json()


# print mac_Bible_ParadiseToFile

# f = open('paradise_model', 'w')
# f.write(mac_Bible_ParadiseToFile)
# f.close()

with open('paradise_model','w') as outfile:
	pickle.dump(mac_Bible_ParadiseToFile, outfile)

# TEST = text_modelP.make_short_sentence(140, tries = 100)





