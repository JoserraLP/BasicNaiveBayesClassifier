import csv, nltk

# Process training tweets from the csv file

tweets = []

with open("tweets.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    if header != None:
        for row in reader:
            words_filtered = [word.lower() for word in row[0].split() if len(word) >= 3]
            tweets.append((words_filtered, row[1].replace('\"', '')))

# Process test tweets from the csv file

test_tweets = []

with open("tweets_test.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    if header != None:
        for row in reader:
            words_filtered = [word.lower() for word in row[0].split() if len(word) >= 3]
            test_tweets.append((words_filtered, row[1].replace('\"', '')))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, _type) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    sortedwordlist = sorted(wordlist.items(), key=lambda item : item[1], reverse=True)
    word_features = []
    for word in sortedwordlist:
        word_features.append(word[0])
    return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

for test_tweet in test_tweets:
    print("Predicted: " + classifier.classify(extract_features(test_tweet[0])) + ' --> Type: ' + test_tweet[1])


try:
    while True:
        tweet = input("Insert your tweet: ")
        print("The type predicted is: " + classifier.classify(extract_features(word.lower() for word in tweet.split())))
except KeyboardInterrupt:
    pass