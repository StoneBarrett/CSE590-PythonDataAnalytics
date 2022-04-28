# Stone Barrett
# CSE 590: Python Data Analytics
# Final Exam

# Importing libraries
from audioop import cross
import json
from platform import machine
import preprocessor as p
from sklearn.model_selection import cross_val_score
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold import TSNE
import warnings

# Issue with Problem 5, explained in ReadMe
warnings.filterwarnings("ignore")

# Problem 1
def Part1():
    # Loading all files
    f = open('savedtweets_americalatina.json')
    americanlatina = json.load(f)
    f.close()

    f = open('savedtweets_machinelearning.json')
    machinelearning = json.load(f)
    f.close()

    f = open('savedtweets_superleague.json')
    superleague = json.load(f)
    f.close()

    f = open('savedtweets_weibo.json')
    weibo = json.load(f)
    f.close()

    # Getting rid of tweets without lat/long
    alltweets = [americanlatina, machinelearning, superleague, weibo]
    lat_AL = []
    lat_ML = []
    lat_SL = []
    lat_WE = []
    i = -1
    for list in alltweets:
        i += 1
        for dict in list:
            if 'latitude' in dict:
                if i == 0:
                    lat_AL.append(dict)
                elif i == 1:
                    lat_ML.append(dict)
                elif i == 2:
                    lat_SL.append(dict)
                else:
                    lat_WE.append(dict)
            else:
                continue

    # Testing
    # x = 0
    # for i in lat_WE:
    #     print(x)
    #     x += 1
    # print(lat_AL[1])
    lattweets = [lat_AL, lat_ML, lat_SL, lat_WE]

    # Cleaning tweets
    for list in lattweets:
        for dict in list:
            dict["text"] = p.clean(dict["text"])
    
    # Testing
    # print(lat_AL[1])

    # Saving to json
    i = 0
    for list in lattweets:
        jsonString = json.dumps(list, indent=2)
        jsonFile = open("prep_tweets_class{}.json".format(i), "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        i += 1
    
# Problem 2
def Part2():
    # Loading all files
    f = open('prep_tweets_class0.json')
    americanlatina = json.load(f)
    f.close()

    f = open('prep_tweets_class1.json')
    machinelearning = json.load(f)
    f.close()

    f = open('prep_tweets_class2.json')
    superleague = json.load(f)
    f.close()

    f = open('prep_tweets_class3.json')
    weibo = json.load(f)
    f.close()

    files = [americanlatina, machinelearning, superleague, weibo]
    
    # Counting
    pos0 = 0
    neg0 = 0
    neu0 = 0
    pos1 = 0
    neg1 = 0
    neu1 = 0
    pos2 = 0
    neg2 = 0
    neu2 = 0
    pos3 = 0
    neg3 = 0
    neu3 = 0
    
    for tweet in americanlatina:
        blob = TextBlob(tweet["text"])
        if blob.sentiment.polarity < 0:
            neg0 += 1
        elif blob.sentiment.polarity == 0:
            neu0 += 1
        elif blob.sentiment.polarity > 0:
            pos0 += 1
    for tweet in machinelearning:
        blob = TextBlob(tweet["text"])
        if blob.sentiment.polarity < 0:
            neg1 += 1
        elif blob.sentiment.polarity == 0:
            neu1 += 1
        elif blob.sentiment.polarity > 0:
            pos1 += 1
    for tweet in superleague:
        blob = TextBlob(tweet["text"])
        if blob.sentiment.polarity < 0:
            neg2 += 1
        elif blob.sentiment.polarity == 0:
            neu2 += 1
        elif blob.sentiment.polarity > 0:
            pos2 += 1
    for tweet in weibo:
        blob = TextBlob(tweet["text"])
        if blob.sentiment.polarity < 0:
            neg3 += 1
        elif blob.sentiment.polarity == 0:
            neu3 += 1
        elif blob.sentiment.polarity > 0:
            pos3 += 1
    
    # Testing
    # print("Pos count: ", pos0)
    # print("Neu count: ", neu0)
    # print("Neg count: ", neg0)
    # print("Pos count: ", pos1)
    # print("Neu count: ", neu1)
    # print("Neg count: ", neg1)
    # print("Pos count: ", pos2)
    # print("Neu count: ", neu2)
    # print("Neg count: ", neg2)
    # print("Pos count: ", pos3)
    # print("Neu count: ", neu3)
    # print("Neg count: ", neg3)

    countAL = {'positive': 2, 'neutral': 42, 'negative': 0}
    countML = {'positive': 35, 'neutral': 32, 'negative': 9}
    countSL = {'positive': 39, 'neutral': 3, 'negative': 9}
    countWE = {'positive': 5, 'neutral': 13, 'negative': 7}

    # Graphing
    x0 = list(countAL.keys())
    y0 = list(countAL.values())
    x1 = list(countML.keys())
    y1 = list(countML.values())
    x2 = list(countSL.keys())
    y2 = list(countSL.values())
    x3 = list(countWE.keys())
    y3 = list(countWE.values())

    # America Latina graph
    #plt.bar(x0, y0)
    # Machine Learning graph
    #plt.bar(x1, y1)
    # Super League graph
    #plt.bar(x2, y2)
    # Weibo graph
    plt.bar(x3, y3)

    plt.xlabel("Sentiment Polarity")
    plt.ylabel("Number of Tweets")
    plt.show()

# Problem 3
def Part3():
    # Loading all files
    f = open('prep_tweets_class0.json')
    americanlatina = json.load(f)
    f.close()

    f = open('prep_tweets_class1.json')
    machinelearning = json.load(f)
    f.close()

    f = open('prep_tweets_class2.json')
    superleague = json.load(f)
    f.close()

    f = open('prep_tweets_class3.json')
    weibo = json.load(f)
    f.close()

    # List of all tweets
    alltweets = americanlatina + machinelearning + superleague + weibo
    # Making list of class number
    tweetclasses = []
    # Testing
    #listlengths = [len(americanlatina), len(machinelearning), len(superleague), len(weibo)]
    #print(listlengths)
    for i in range(1,197):
        if i < 45:
            tweetclasses.append(0)
        elif 44 < i < 121:
            tweetclasses.append(1)
        elif 120 < i < 172:
            tweetclasses.append(2)
        elif i > 171:
            tweetclasses.append(3)
    
    # Testing
    # print(len(tweetclasses))
    # print(len(alltweets))

    # Returning tuple
    return (alltweets, tweetclasses)

# Problem 4
def Part4(alltweets, tweetclasses):
    # Making array
    allfeatures = []

    # Appending information
    for tweet in alltweets:
        text = len(str(tweet["text"]))
        rtcount = tweet["retweet_count"]
        lat = tweet["latitude"]
        long = tweet["longitude"]
        if tweet["lang"] == "en":
            lang = 0
        else:
            lang = 100
        features = [text, rtcount, lat, long, lang]
        allfeatures.append(features)

    featuresnp = np.array(allfeatures)

    # Testing
    #print(allfeatures)
    #print(featuresnp)

    return featuresnp

# Problem 5
def Part5(featuresnp, tweetclasses):
    # Setting up x and y
    x = featuresnp
    y = np.array(tweetclasses)

    # Setting up classifier instances
    knn = KNeighborsClassifier()
    rf = RandomForestClassifier()
    lsvm = LinearSVC()

    # Scoring
    knnscores = cross_val_score(knn, x, y, cv=10)
    rfscores = cross_val_score(rf, x, y, cv=10)
    lsvmscores = cross_val_score(lsvm, x, y, cv=10)

    # Printing scores
    print("K Nearest Neighbor Cross-Val Average: {:.2f}".format(knnscores.mean()))
    print("Random Forest Cross-Val Average: {:.2f}".format(rfscores.mean()))
    print("Linear Support Vector Machine Cross-Val Average: {:.2f}".format(lsvmscores.mean()))

# Problem 6
def Part6(featuresnp, tweetclasses):
    featuresnp = featuresnp
    tsne = TSNE(n_components=2, random_state=11)
    reduced_data = tsne.fit_transform(featuresnp)
    figure = plt.figure(figsize=(5,5))
    dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=tweetclasses, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
    colorbar = plt.colorbar(dots)
    plt.show()


# Testing
Part1()
Part2()
alltweets, tweetclasses = Part3()
featuresnp = Part4(alltweets, tweetclasses)
Part5(featuresnp, tweetclasses)
Part6(featuresnp, tweetclasses)