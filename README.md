# TwitterBot Language Analysis
Status generation through markov chains of various corpa.

Uses Markov Chains to generate corpora based on tweets selected based on keywords (such as Love or Hate). Uses corpora in an attempt to construct a tweet-classification model to determine words and phrases associated with positive or negative connoations. 

Uses a naive bayes classification (number of times a specific word appears in a given corpora vs over number of words, then gives that word a value based on if it appears more in a negative context or positive context) but can also classify using Binary classification (strict positive or negative) and Absolute classification (just looking at how many times a specific word appears in specific negative or positive contexts). 

All of this, ofcourse, assumes that Love / Hate key words are good way to find positive (love) or negative (hate) tweets (sarcasm is ignored). 

I generate two large corpora from just tapping into a live feed of the twitter API, selecting only tweets with the specific keyword 'love' or 'hate'. This is knowingly very blunt and can create a lot of issues, especially when the machine learning algorithms used base the classification whole-heartedly on word frequency (i.e. every word 'love' would be exclusevly positive) -- This is where the Markov Chains come in.

I use a markov chain model of the tweets in a given corpus (see 'tweets_hate' or 'tweets_love' in /text to view these corpora). This enables me to have a fresh, 'randomized' tweet that is close-enough to a knowingly negative or positive nature based on very simple paradigms (such as one word can determine if a tweet is positive or negative). These ideas are flawed yet practical in the sense that it is very hard to find data to train your robot on what is negative or positive in the wild.

Already my naive bayse classifier has shown some interesting results. The top-twenty most informative features (i.e. if these words are used they most likely determine a negative or positive tweet) can be quite revealing:

           BIGRAM_love_u = 0.5            positi : negati =     51.6 : 1.0
         BIGRAM_n't_hate = 0.5            negati : positi =     46.1 : 1.0
                UNI_hate = 0.5            negati : positi =     39.6 : 1.0
               UNI_kills = 0.5            negati : positi =     35.3 : 1.0
               UNI_hated = 0.5            negati : positi =     34.5 : 1.0
         UNI_seanhannity = 0.5            negati : positi =     32.0 : 1.0
             UNI_muslims = 0.5            negati : positi =     32.0 : 1.0
           BIGRAM_hate_u = 0.5            negati : positi =     28.7 : 1.0
           UNI_happening = 0.5            negati : positi =     28.7 : 1.0
               UNI_jimin = 0.5            positi : negati =     28.6 : 1.0
               UNI_white = 0.5            negati : positi =     27.9 : 1.0
      BIGRAM_people_hate = 0.5            negati : positi =     27.9 : 1.0
        BIGRAM_hate_love = 0.5            negati : positi =     27.0 : 1.0
                UNI_dick = 0.5            negati : positi =     27.0 : 1.0
              UNI_killed = 0.5            negati : positi =     25.4 : 1.0
            UNI_violence = 0.5            negati : positi =     24.5 : 1.0
        BIGRAM_love_much = 0.5            positi : negati =     23.8 : 1.0
         UNI_republicans = 0.5            negati : positi =     22.9 : 1.0
             UNI_liberal = 0.5            negati : positi =     22.7 : 1.0
         UNI_performance = 0.5            negati : positi =     22.0 : 1.0

["UNI_..." represents a unigram (one 'word') and "BIGRAM_..." represents 2 words]

The one token I found surprising was the token 'jimin'. Upon a quick search on twitter I found that it is the name of a member of BTS (the Korean Pop group). This name being an informative feature in my sentiment analysis is probably due to the major flaw in how I collect the data, K-POP fans use the word 'love' in there tweets more than the average user I suppose.

Uses the markovify markov generation, nltk, twython, python twitter api and python3.5.

Example in use: twitter.com/Wethuselah
