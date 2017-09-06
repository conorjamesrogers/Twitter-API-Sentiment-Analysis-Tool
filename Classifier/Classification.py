import re, nltk, pickle, argparse
import markovify
from contextlib import redirect_stdout

def test():
    print("wow")

def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))

def get_text(review):
    return str(re.search(r'Text = "(.*)"', review).group(1))

def bin(count):
    return count if count < .008 else .5

def findValue(value, value_list):
    return True if value in value_list else False

def total_words(category_text_dict):
    total_words = []
    for category in category_text_dict:
        for text in category_text_dict[category]:
            total_words += get_words_tags(text, True)[0]
    print('total words list processed')
    return total_words


def binary_features(tokens, total_words, uni_tot, bi_tot, tri_tot):
    feature_vectors = {}
    #split up all lists into tokens
    # print(str(tokens))

    # print(str(total_words))
    uni = tokens
    bi = nltk.bigrams(tokens)
    tri = nltk.trigrams(tokens)

    # total_words = words_P + words_N
    
    # print(tri_tot[0])

    for token in uni_tot:
        feature_vectors["UNI_{0}".format(token)] = findValue(token, uni)
    for (b1, b2) in bi_tot:
        feature_vectors["BIGRAM_{0}_{1}".format(b1, b2)] = findValue((b1,b2),bi)
    for (b1, b2, b3) in  tri_tot:
        feature_vectors['TRIGRAM_{0}_{1}_{2}'.format(b1,b2,b3)] = findValue((b1,b2,b3),tri)

    return feature_vectors

def markov_chains(filename):
    with open(filename,'rb') as f:
        json_model = pickle.load(f)

    model = markovify.Text.from_json(json_model)
    #status in question
    return model.make_short_sentence(140, tries = 100)

def get_tweets(filepath):
    with open(filepath,'r') as f:
        tweet = f.read()
    return tweet.splitlines()

def get_reviews(num,is_training_mode):
    positive_texts = []
    negative_texts = []
    if(is_training_mode):
        # for x in range(num):
        positive_texts += [x for x in get_tweets('../text/tweets_love')]
        negative_texts += [x for x in get_tweets('../text/tweets_hate')]

    else:
        print('not training')
        for x in range(num):
            positive_texts.append(markov_chains('../tweet_model_love'))
            negative_texts.append(markov_chains('../tweet_model_hate'))

    # positive_texts = []
    # negative_texts = []
    # for review in re.split(r'\.\n', raw_data):
    #     overall_score = get_score(review)
    #     review_text = get_text(review)
    #     if overall_score > 3:
    #         positive_texts.append(review_text)
    #     elif overall_score < 3:
    #         negative_texts.append(review_text)
    #print(len(positive_texts))
    #print(len(negative_texts))
    return positive_texts, negative_texts

def process_reviews(classifier_fname, file_name, out_fname, feature_set, is_training_mode=False):
    # file = open(file_name, "rb")
    # raw_data = file.read().decode("latin1")
    # file.close()

    data_set = "training"
    if "testing" in file_name:
        data_set = "testing"
    elif "development" in file_name:
        data_set = "development"

    positive_texts, negative_texts = get_reviews(5000,is_training_mode)
    features_category_tuples, texts = get_features_category_tuples({"positive":positive_texts, "negative":negative_texts}, feature_set)
    write_features_category(features_category_tuples, feature_set)


    if is_training_mode == True:
        save_classifier(features_category_tuples, classifier_fname)
    else:
        classifier = get_classifier(classifier_fname)
        if classifier == None:
            return
        evaluate(classifier, features_category_tuples, texts, out_fname + '-' + data_set)

def get_features_category_tuples(category_text_dict, feature_set):
    features_category_tuples = []
    texts = []
    if feature_set == "competition":
        should_normalized  = True
    else:
        should_normalized  = True
    tot_words = []
    
    if feature_set == 'binary':
        tot_words = total_words(category_text_dict)
        uni_tot = tot_words
        bi_tot = nltk.bigrams(tot_words)
        tri_tot = nltk.trigrams(tot_words)
        # counter = 0
        print('processing data for binary features...')


    for category in category_text_dict:
        for text in category_text_dict[category]:
            tempL = get_words_tags(text, should_normalized)
            words = tempL[0]
            tags = tempL[1]
            # words, tags = get_words_tags(text, should_normalized)
            feature_vectors = {}
            if feature_set == "word_pos_features":
                feature_vectors.update(get_ngram_features(words, feature_set))
                feature_vectors.update(get_pos_features(tags))
            elif feature_set == "word_features":
                feature_vectors.update(get_ngram_features(words, feature_set))
            elif feature_set == "competition":
                feature_vectors.update(get_ngram_features(words, feature_set))
                feature_vectors.update(get_pos_features(tags))
                feature_vectors.update(get_liwc_features(u" ".join(words)))
            elif feature_set == 'absolute':
                feature_vectors.update(get_ngram_features(words, feature_set))
            elif feature_set == 'relative-improved':
                feature_vectors.update(get_ngram_features(words, feature_set))
            elif feature_set == 'binary':
                feature_vectors.update(binary_features(words, tot_words, uni_tot, bi_tot, tri_tot))
                # counter += 1




            features_category_tuples.append((feature_vectors, category))
            texts.append(text)
            # print(str(features_category_tuples))
            # print(counter)
    return features_category_tuples, texts

def get_words_tags(text, should_normalized):
    words = []
    tags = []
    # tokenization for each sentence
    for sent in nltk.sent_tokenize(text):           
        for word, pos in nltk.pos_tag(nltk.word_tokenize(sent)):
            checked_word = normalize(word, should_normalized)
            if checked_word is None:
                continue
            words.append(checked_word)
            tags.append(pos)
    return [words, tags]

def normalize(token, should_normalized=True):
    if not should_normalized:
        return token
    if token.lower() not in nltk.corpus.stopwords.words('english') and re.search(r'\w', token):
        return token.lower()
    return None

def get_ngram_features(tokens,feature_set):
    feature_vectors = {}
    uni_fdist = nltk.FreqDist(tokens)
    bi_fdist = nltk.FreqDist(nltk.bigrams(tokens))
    tri_fdist = nltk.FreqDist(nltk.trigrams(tokens))

    #1. absolute
    if feature_set == 'absolute':
        for token, freq in uni_fdist.items():
            feature_vectors["UNI_{0}".format(token)] = float(freq)
        for (b1, b2), freq in bi_fdist.items():
            feature_vectors["BIGRAM_{0}_{1}".format(b1, b2)] = float(freq)
        for (b1, b2, b3), freq in tri_fdist.items():
            feature_vectors['TRIGRAM_{0}_{1}_{2}'.format(b1,b2,b3)] = float(freq)
    #3. relative
    elif feature_set == 'relative-improved':
        for token, freq in uni_fdist.items():
            feature_vectors["UNI_{0}".format(token)] = bin(float(freq) / uni_fdist.N())
        for (b1, b2), freq in bi_fdist.items():
            feature_vectors["BIGRAM_{0}_{1}".format(b1, b2)] = bin(float(freq) / bi_fdist.N())
        for (b1, b2, b3), freq in tri_fdist.items():
            feature_vectors['TRIGRAM_{0}_{1}_{2}'.format(b1,b2,b3)] = bin(float(freq) / tri_fdist.N())
    else:
        for token, freq in uni_fdist.items():
            feature_vectors["UNI_{0}".format(token)] = float(freq) /uni_fdist.N()
        for (b1, b2), freq in bi_fdist.items():
            feature_vectors["BIGRAM_{0}_{1}".format(b1, b2)] = float(freq) / bi_fdist.N() 



    return feature_vectors

def get_pos_features(tags):
    feature_vectors = {}
    uni_fdist = nltk.FreqDist(tags)
    bi_fdist = nltk.FreqDist(nltk.bigrams(tags))
    for tag, freq in uni_fdist.items():
        feature_vectors["UNIPOS_{0}".format(tag)] = float(freq) / uni_fdist.N()
    for (b1, b2), freq in bi_fdist.items():
        feature_vectors["BIGPOS_{0}_{1}".format(b1, b2)] = float(freq) / bi_fdist.N()

    return feature_vectors

# Adds a simple LIWC derived feature
def get_liwc_features(text):
    feature_vectors = {}
    liwc_scores = word_category_counter.score_text(text)
    # All possible keys to the scores start on line 269
    # of the word_category_counter.py script
    negative_score = liwc_scores["Negative Emotion"]
    positive_score = liwc_scores["Positive Emotion"]
    feature_vectors["Negative Emotion"] = negative_score
    feature_vectors["Positive Emotion"] = positive_score
    if positive_score > negative_score:
        feature_vectors["liwc:positive"] = 1
    else:
        feature_vectors["liwc:negative"] = 1
    return feature_vectors

def write_features_category(features_category_tuples, output_file_name):
    output_file = open("features-training-word_features-{}.txt".format(output_file_name), "w", encoding="utf-8")
    for (features, category) in features_category_tuples:
        output_file.write("{0:<10s}\t{1}\n".format(category, features))
    output_file.close() 

def get_classifier(classifier_fname):
    classifier_file = open(classifier_fname,'rb')
    classifier = pickle.load(classifier_file)
    classifier_file.close()
    return classifier

def save_classifier(train_sets, classifier_fname):
    classifier = nltk.classify.NaiveBayesClassifier.train(train_sets)
    classifier_file = open(classifier_fname,'wb')
    pickle.dump(classifier, classifier_file)
    classifier_file.close()
    # print(classifier_fname)
    # info_file = open(classifier_fname.split(".")[0]+'-most-informative-features.txt','w', encoding="utf-8")
    # for feature, n in classifier.most_informative_features(20):
        # info_file.write("{0}\n".format(feature))
    # info_file.close()
    with open(classifier_fname.split(".")[0]+'-most-informative-features.txt','w', encoding="utf-8") as f:
        with redirect_stdout(f):
            classifier.show_most_informative_features(100)

    return classifier

def evaluate(classifier, features_category_tuples, reference_text, data_set_name):
    name_string ='dev'
    if 'dev' in data_set_name:
        name_string = 'dev'
    elif 'test' in data_set_name:
        name_string = 'test'

    all_results_file = open('all-results.txt','a',encoding='utf-8')
    accuracy_results_file = open("out-{0}-word_features-{1}.txt".format(name_string, data_set_name.split("-")[0]), 'w', encoding='utf-8')
    accuracy_results_file.write('Results of {}:\n\n'.format(data_set_name))
    all_results_file.write('Results of {}:\n\n'.format(data_set_name))
    # test on the data
    accuracy = nltk.classify.accuracy(classifier, features_category_tuples)
    print("The accuracy of {0} is ".format(data_set_name))
    print(accuracy)
        
    accuracy_results_file.write("{0:10s} {1:8.5f}\n\n".format("Accuracy", accuracy))
    all_results_file.write("{0:10s} {1:8.5f}\n\n".format("Accuracy", accuracy))
    
    features_only = []
    reference_labels = []
    for feature_vectors, category in features_category_tuples:
        features_only.append(feature_vectors)
        reference_labels.append(category)
        
    predicted_labels = classifier.classify_many(features_only)
    
    confusion_matrix = nltk.ConfusionMatrix(reference_labels, predicted_labels)

    accuracy_results_file.write(str(confusion_matrix))
    accuracy_results_file.write('\n\n')
    accuracy_results_file.close()

    all_results_file.write(str(confusion_matrix))
    all_results_file.write('\n\n')
    all_results_file.close()

    predict_results_file = open("{}_output.txt".format(data_set_name), 'w', encoding='utf-8')
    for reference, predicted, text in zip(
                                          reference_labels,
                                          predicted_labels,
                                          reference_text
                                          ):
        if reference != predicted:
            predict_results_file.write("{0} {1}\n{2}\n\n".format(reference, predicted, text))
    predict_results_file.close()

if __name__ == '__main__':

    #HOW TO RUN:

    #Absolute:
    #train:
    #python3 restaurant-word-features-P3.py --train -d restaurant-training.data -f absolute 
    #run test:
    #python3 restaurant-word-features-P3.py -f absolute -r absolute
    #run dev:
    #python3 restaurant-word-features-P3.py -f absolute -r absolute -d restaurant-development.data

    #Binary:
    #train:
    #python3 restaurant-word-features-P3.py --train -d restaurant-training.data -f binary
    #run test:
    #python3 restaurant-word-features-P3.py -f binary -r binary
    #run dev:
    #python3 restaurant-word-features-P3.py -f binary -r binary -d restaurant-development.data


    #Relative Improved:
    #train:
    #python3 restaurant-word-features-P3.py --train -d restaurant-training.data -f relative-improved 
    #run test:
    #python3 restaurant-word-features-P3.py -f relative-improved -r relative-improved
    #run dev:
    #python3 restaurant-word-features-P3.py -f relative-improved -r relative-improved -d restaurant-development.data



    parser = argparse.ArgumentParser()
    parser.add_argument('--train', dest="is_training_mode", action="store_true", help='Is it a training mode or testing mode?')
    parser.add_argument('-c', dest="classifier_fname", default="word_features-classifier.pickle",  help='File name of the classifier pickle.')
    parser.add_argument('-d', dest="data_fname", default="restaurant-testing.data",  help='File name of the testing data.')
    parser.add_argument('-r', dest="result_fname", default="word_features-testing",  help='Output file name without extensions.')
    parser.add_argument('-f', dest="feature_set", default="word_features",  help='Feature set: word_features, word_pos_features, competition (includes LIWC).')
    

    args = parser.parse_args()
    is_training_mode = args.is_training_mode
    classifier_fname = args.classifier_fname
    data_fname = args.data_fname
    result_fname = args.result_fname
    feature_set = args.feature_set

    if feature_set == 'absolute':
        classifier_fname = 'nb-word_features-absolute-model-P3.pickle'
    elif feature_set == 'relative-improved':
        classifier_fname = 'nb-word_features-relative-improved-model-P3.pickle'
    elif feature_set == 'binary':
        classifier_fname = 'nb-word_features-binary-model-P3.pickle'
        print('binary chosen')


    if is_training_mode:
        process_reviews(classifier_fname, data_fname, None, feature_set, is_training_mode)
    else:
        process_reviews(classifier_fname, data_fname, result_fname, feature_set)
    


    #print(get_features_category_tuples({"negative":["Horrible!!!"], "positive":["Yamy!!"]}))
    #is_baseline=True
    #process_reviews(train_file, "training", is_baseline)
    #process_reviews(dev_file, "development", is_baseline)
    #process_reviews(test_file, "testing", is_baseline)
