# TwitterBot Sentiment Analysis
Status generation through markov chains of various corpa.

-----------------

##Overview

Uses Markov Chains to generate corpora based on tweets selected based on keywords (such as Love or Hate). Uses corpora in an attempt to construct a tweet-classification model to determine words and phrases associated with positive or negative connoations. 

Uses a naive bayes classification (number of times a specific word appears in a given corpora vs over number of words, then gives that word a value based on if it appears more in a negative context or positive context) but can also classify using Binary classification (strict positive or negative) and Absolute classification (just looking at how many times a specific word appears in specific negative or positive contexts). 

All of this, ofcourse, assumes that Love / Hate key words are good way to find positive (love) or negative (hate) tweets (sarcasm is ignored). 

------------------

##Explaination

I generate two large corpora from just tapping into a live feed of the twitter API, selecting only tweets with the specific keyword 'love' or 'hate'. This is knowingly very blunt and can create a lot of issues, especially when the machine learning algorithms used base the classification whole-heartedly on word frequency (i.e. every word 'love' would be exclusevly positive) -- This is where the Markov Chains come in.

I use a markov chain model of the tweets in a given corpus (see 'tweets_hate' or 'tweets_love' in /text to view these corpora). This enables me to have a fresh, 'randomized' tweet that is close-enough to a knowingly negative or positive nature based on very simple paradigms (such as one word can determine if a tweet is positive or negative). These ideas are flawed yet practical in the sense that it is very hard to find data to train your robot on what is negative or positive in the wild.

------------------

##Example

Already my naive bayse classifier has shown some interesting results. The top-twenty most informative features (i.e. if these words are used they most likely determine a negative or positive tweet) can be quite revealing:
```
           BIGRAM_love_u = 0.5            positi : negati =     51.6 : 1.0
         BIGRAM_n't_hate = 0.5            negati : positi =     46.1 : 1.0
                UNI_hate = 0.5            negati : positi =     39.6 : 1.0
               UNI_kills = 0.5            negati : positi =     35.3 : 1.0
               UNI_hated = 0.5            negati : positi =     34.5 : 1.0
             UNI_muslims = 0.5            negati : positi =     32.0 : 1.0
         UNI_seanhannity = 0.5            negati : positi =     32.0 : 1.0
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
   BIGRAM_happy_birthday = 0.5            positi : negati =     20.6 : 1.0
```
["UNI_..." represents a unigram (one 'word') and "BIGRAM_..." represents 2 words]

The one token I found surprising was the token 'jimin'. Upon a quick search on twitter I found that it is the name of a member of BTS (the Korean Pop group). This name being an informative feature in my sentiment analysis is probably due to the major flaw in how I collect the data, K-POP fans use the word 'love' in there tweets more than the average user I suppose.

------------------

#Uses:

markovify markov generation, nltk, twython, python twitter api and python3.5.

Example in use: twitter.com/Wethuselah

##Further Features

Top 100 Informative Features in my sentiment analysis:
```
           BIGRAM_love_u = 0.5            positi : negati =     51.6 : 1.0
         BIGRAM_n't_hate = 0.5            negati : positi =     46.1 : 1.0
                UNI_hate = 0.5            negati : positi =     39.6 : 1.0
               UNI_kills = 0.5            negati : positi =     35.3 : 1.0
               UNI_hated = 0.5            negati : positi =     34.5 : 1.0
             UNI_muslims = 0.5            negati : positi =     32.0 : 1.0
         UNI_seanhannity = 0.5            negati : positi =     32.0 : 1.0
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
   BIGRAM_happy_birthday = 0.5            positi : negati =     20.6 : 1.0
               UNI_actor = 0.5            negati : positi =     20.4 : 1.0
              UNI_robert = 0.5            negati : positi =     20.4 : 1.0
        BIGRAM_much_love = 0.5            positi : negati =     19.0 : 1.0
        UNI_rabiasquared = 0.5            negati : positi =     18.7 : 1.0
       BIGRAM_still_love = 0.5            positi : negati =     17.9 : 1.0
              UNI_easily = 0.5            negati : positi =     17.9 : 1.0
        UNI_jackposobiec = 0.5            negati : positi =     17.9 : 1.0
             UNI_bitches = 0.5            negati : positi =     17.9 : 1.0
               UNI_idiot = 0.5            negati : positi =     17.9 : 1.0
            UNI_baseball = 0.5            negati : positi =     17.0 : 1.0
      UNI_poeticallyiost = 0.5            negati : positi =     16.2 : 1.0
BIGRAM_rt_poeticallyiost = 0.5            negati : positi =     16.2 : 1.0
                UNI_kill = 0.5            negati : positi =     16.2 : 1.0
          BIGRAM_hate_'m = 0.5            negati : positi =     15.4 : 1.0
              UNI_absurd = 0.5            negati : positi =     15.4 : 1.0
               UNI_treat = 0.5            positi : negati =     14.7 : 1.0
               UNI_obama = 0.5            negati : positi =     14.6 : 1.0
             UNI_country = 0.5            negati : positi =     13.7 : 1.0
               UNI_final = 0.5            negati : positi =     13.2 : 1.0
           UNI_literally = 0.5            negati : positi =     13.2 : 1.0
            UNI_thoughts = 0.5            positi : negati =     13.1 : 1.0
              UNI_saying = 0.5            negati : positi =     12.9 : 1.0
      BIGRAM_new_twitter = 0.5            negati : positi =     12.9 : 1.0
                 UNI_th… = 0.5            negati : positi =     12.7 : 1.0
              UNI_donald = 0.5            negati : positi =     12.1 : 1.0
                  UNI_e… = 0.5            positi : negati =     11.5 : 1.0
               UNI_media = 0.5            negati : positi =     11.2 : 1.0
                UNI_love = 0.5            positi : negati =     10.8 : 1.0
       BIGRAM_love_https = 0.5            positi : negati =     10.7 : 1.0
       BIGRAM_lmao_https = 0.5            positi : negati =     10.4 : 1.0
         BIGRAM_n't_ever = 0.5            positi : negati =     10.4 : 1.0
               UNI_match = 0.5            negati : positi =     10.4 : 1.0
            UNI_starting = 0.5            negati : positi =     10.4 : 1.0
          UNI_regardless = 0.5            negati : positi =     10.2 : 1.0
                UNI_date = 0.5            positi : negati =      9.8 : 1.0
        BIGRAM_hate_hate = 0.5            negati : positi =      9.6 : 1.0
        BIGRAM_ever_find = 0.5            positi : negati =      9.4 : 1.0
          BIGRAM_'s_love = 0.5            positi : negati =      8.8 : 1.0
                UNI_shut = 0.5            negati : positi =      8.7 : 1.0
            UNI_bringing = 0.5            negati : positi =      8.7 : 1.0
   BIGRAM_twitter_update = 0.5            negati : positi =      8.7 : 1.0
       BIGRAM_hate_trump = 0.5            negati : positi =      8.7 : 1.0
                  UNI_ta = 0.5            positi : negati =      8.5 : 1.0
           BIGRAM_got_ta = 0.5            positi : negati =      8.5 : 1.0
               UNI_great = 0.5            positi : negati =      8.4 : 1.0
       BIGRAM_game_https = 0.5            negati : positi =      8.2 : 1.0
        BIGRAM_never_let = 0.5            negati : positi =      7.9 : 1.0
              UNI_update = 0.5            negati : positi =      7.9 : 1.0
     BIGRAM_hate_getting = 0.5            negati : positi =      7.9 : 1.0
                UNI_ugly = 0.5            negati : positi =      7.9 : 1.0
                 UNI_cnn = 0.5            negati : positi =      7.9 : 1.0
           UNI_listening = 0.5            positi : negati =      7.9 : 1.0
      BIGRAM_love_always = 0.5            positi : negati =      7.9 : 1.0
               UNI_child = 0.5            negati : positi =      7.6 : 1.0
           UNI_motivated = 0.5            negati : positi =      7.2 : 1.0
                  UNI_lt = 0.5            positi : negati =      7.2 : 1.0
          BIGRAM_love_'s = 0.5            positi : negati =      7.2 : 1.0
            UNI_peaceful = 0.5            positi : negati =      7.2 : 1.0
               UNI_blame = 0.5            negati : positi =      7.1 : 1.0
               UNI_punch = 0.5            negati : positi =      7.1 : 1.0
                UNI_sick = 0.5            negati : positi =      7.1 : 1.0
               UNI_carry = 0.5            negati : positi =      7.1 : 1.0
         BIGRAM_'ve_ever = 0.5            negati : positi =      7.1 : 1.0
     BIGRAM_hate_someone = 0.5            negati : positi =      7.1 : 1.0
             UNI_exactly = 0.5            negati : positi =      7.1 : 1.0
         BIGRAM_n't_find = 0.5            negati : positi =      7.1 : 1.0
          BIGRAM_hate_us = 0.5            negati : positi =      7.1 : 1.0
             UNI_hillary = 0.5            negati : positi =      7.1 : 1.0
           UNI_community = 0.5            negati : positi =      7.1 : 1.0
        BIGRAM_love_love = 0.5            positi : negati =      6.9 : 1.0
         BIGRAM_fans_n't = 0.5            positi : negati =      6.9 : 1.0
BIGRAM_everything_starts = 0.5            positi : negati =      6.9 : 1.0
             UNI_driving = 0.5            negati : positi =      6.7 : 1.0
        BIGRAM_much_hate = 0.5            negati : positi =      6.7 : 1.0
                 UNI_men = 0.5            negati : positi =      6.7 : 1.0
                UNI_says = 0.5            negati : positi =      6.7 : 1.0
                 UNI_mic = 0.5            positi : negati =      6.7 : 1.0
              UNI_pissed = 0.5            positi : negati =      6.7 : 1.0
                UNI_must = 0.5            negati : positi =      6.5 : 1.0
```
