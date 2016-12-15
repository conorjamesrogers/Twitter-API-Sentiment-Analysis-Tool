import markovify
import sys, os
import operator
import nltk
import re


class POSifiedText(markovify.Text):
	def word_split(self,sentence):
		words = re.split(self.word_split_pattern,sentence)
		words = [ "::".join(tag) for tag in nltk.pos_tag(words)]
		print words
		return words

	def word_join(self, words):
		sentence = " ".join(word.split("::")[0] for word in words)
		return sentence

with open(os.path.join(os.path.dirname('__file__'), "Paradise_Lost.txt")) as f:
	p = f.read()

#with open(os.path.join(os.path.dirname('__file__'), "Britney.txt")) as g:
#	b = g.read()

text_modelP = markovify.Text(p)
#text_modelB = POSifiedText(b)

#combo = markovify.combine([text_modelB, text_modelP],[1,.5])

TEST = text_modelP.make_short_sentence(140, tries = 100)





