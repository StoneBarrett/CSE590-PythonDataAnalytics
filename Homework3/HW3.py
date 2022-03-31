# Stone Barrett
# CSE 590: Python Data Analytics
# Homework 3

# Importing libraries
from pathlib import Path
import re
from collections import Counter
import nltk
import wordcloud
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
import imageio
import textatistic
import spacy
import pandas as pd
import matplotlib.pyplot as plt

# Testing
# import os
# os.getcwd()

# Opening files and assigning them to vars
file = open("./HW3/1984.txt", mode="r")
raw1984 = file.read()
file.close()

file = open("./HW3/POIS3E23.txt", mode="r")
rawPOI = file.read()
file.close()

file = open("./HW3/WelcometotheMachine.txt", mode="r")
rawFLOYD = file.read()
file.close()

'''This assignment deals with using `textblob` and other open-source libraries to perform NLP-based 
analysis on documents using Python.  **All parts should use the same three documents (as outlined in Part 1 below).  
In addition to your .ipynb and/or .py files, you must submit a report document (in .doc or .pdf format) that 
answers various questions below.** 

**Part 1:**<br> Select and download three texts of your choosing that represent different media or writing 
formats (for example, you could choose i. a novel, movie script, and play script or ii. a short story, poem, and novel, etc.)
**Make sure you briefly descibe your documents and explain the difference between them in a paragraph.** 
'''
'''
**Part 2:**<br>
(a) Compute word counts for each of your documents after excluding English stop words (and optionally, performing lemmatization).<br>
(b) Create and display a bar plot for each document that include word counts for the 25 most frequent 
words (after the above processing).<br>
(c) Create and display a word cloud for each document (using a mask image of your choice) that includes 
only the 100 most frequent words.  Note that you'll likely want to use the approach outlined in Session 25 
that utilizes the `fitwords` method, since you will want data consistent with those for part (b).<br>
(d) Do you see any notable difference between the documents wrt (b) and/or (c) above?  Try to explain why or why not, 
and whether you would expect such a difference.<br>
'''
def Part2():
    # 2a
    # Removing punctuation and special characters
    strippedPOI = re.sub('[!@#$.,?:()\'/;“”-]', '', rawPOI)
    stripped1984 = re.sub('[!@#$.,?:()\'/;“”-]', '', raw1984)
    strippedFLOYD = re.sub('[!@#$.,?:()\'/;“”-]', '', rawFLOYD)

    # Stop words list
    #stop_words = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "A", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "after", "afterwards", "ag", "again", "against", "ah", "ain", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appreciate", "approximately", "ar", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "B", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "been", "before", "beforehand", "beginnings", "behind", "below", "beside", "besides", "best", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "C", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "ci", "cit", "cj", "cl", "clearly", "cm", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "could", "couldn", "couldnt", "course", "cp", "cq", "cr", "cry", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d", "D", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "dj", "dk", "dl", "do", "does", "doesn", "doing", "don", "done", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "E", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "F", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "G", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "H", "h2", "h3", "had", "hadn", "happens", "hardly", "has", "hasn", "hasnt", "have", "haven", "having", "he", "hed", "hello", "help", "hence", "here", "his","her","him","she","they","them","hereafter", "hereby", "herein", "heres", "hereupon", "hes", "hh", "hi", "hid", "hither", "hj", "ho", "hopefully", "how", "howbeit", "however", "hr", "hs", "http", "hu", "hundred", "hy", "i2", "i3", "i4", "i6", "i7", "i8", "i","ia", "ib", "ibid", "ic", "id", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "im", "immediately", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "inward", "io", "ip", "iq", "ir", "is", "isn", "it", "itd", "its", "iv", "ix", "iy", "iz", "j", "J", "jj", "jr", "js", "jt", "ju", "just", "k", "K", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "ko", "l", "L", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "M", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "my", "n", "N", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "neither", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "O", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "otherwise", "ou", "ought", "our", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "P", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "pp", "pq", "pr", "predominantly", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "Q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "R", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "S", "s2", "sa", "said", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "seem", "seemed", "seeming", "seems", "seen", "sent", "seven", "several", "sf", "shall", "shan", "shed", "shes", "show", "showed", "shown", "showns", "shows", "si", "side", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somehow", "somethan", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "sz", "t", "T", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they", "theyd", "theyre", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "U", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "used", "useful", "usefully", "usefulness", "using", "usually", "ut", "v", "V", "va", "various", "vd", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "W", "wa", "was", "wasn", "wasnt", "way", "we", "wed", "welcome", "well", "well-b", "went", "were", "weren", "werent", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "wi", "widely", "with", "within", "without", "wo", "won", "wonder", "wont", "would", "wouldn", "wouldnt", "www", "x", "X", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "Y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "your", "youre", "yours", "yr", "ys", "yt", "z", "Z", "zero", "zi", "zz"]
    stop_words = stopwords.words('english')

    # Removing stop words
    splitPOI = strippedPOI.split(' ')
    split1984 = stripped1984.split(' ')
    splitFLOYD = strippedFLOYD.split(' ')

    resultPOI = [word for word in splitPOI if word.lower() not in stop_words]
    result1984 = [word for word in split1984 if word.lower() not in stop_words]
    resultFLOYD = [word for word in splitFLOYD if word.lower() not in stop_words]

    finalPOI = ' '.join(resultPOI)
    final1984 = ' '.join(result1984)
    finalFLOYD = ' '.join(resultFLOYD)

    # Getting word counts
    countPOI = len(resultPOI)
    count1984 = len(result1984)
    countFLOYD = len(resultFLOYD)

    print("Number of words in Deus Ex Machina: ", countPOI)
    print("Number of words in 1984: ", count1984)
    print("Number of words in Welcome to the Machine: ", countFLOYD)

    # 2b
    # Getting 25 most frequent words and their counts
    poi25 = Counter(resultPOI).most_common(25)
    ne425 = Counter(result1984).most_common(25)
    floyd25 = Counter(resultFLOYD).most_common(25)

    # Splitting into two lists for graphing
    wordsPOI = ['know', 'dont', 'Northern', 'need', 'didnt', 'will', 'people', 'time', 'machine', 'nothing', 'want', 'worried', 'good', 'hell', 'see', 'American', 'thing', 'someone', 'never', 'government', 'long', 'theyll', 'fair', 'safe', '5th']
    countsPOI = [15, 12, 9, 8, 6, 6, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3]

    words1984 = ['Winston', 'Party','time','will','face','other','never','moment','thought','OBrien','man','know','eyes','war','words','same','long','knew','thing','years','round','himself','word','because','voice']
    counts1984 = [276, 219, 167, 156, 155, 145, 143, 131, 122, 119, 114, 105, 104, 98, 97, 96, 95, 93, 93, 93, 91, 89, 86, 86, 85]

    wordsFLOYD = ['son\nWelcome','alright','know','machine\nWhere','been\nIts','youve','been\nYouve','pipeline\nFilling','time\nProvided','toys','scouting','boys\nYou','brought','guitar','punish','ma\nAnd','didnt','school\nAnd','nobodys','fool\nSo','machine\nWelcome','machine\nWhat','dream\nIts','told','dream\nYou']
    countsFLOYD = [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Making bar graph for each
    # plt.bar(range(len(wordsPOI)), countsPOI, tick_label=wordsPOI)
    # plt.bar(range(len(words1984)), counts1984, tick_label=words1984)
    # plt.bar(range(len(wordsFLOYD)), countsFLOYD, tick_label=wordsFLOYD)
    
    # plt.xticks(rotation=90)
    # plt.show()

    # 2c
    # Making wordclouds
    maskimagePOI = imageio.imread('./HW3/computer.png')
    wordcloudPOI = WordCloud(colormap='prism', mask=maskimagePOI, background_color='white')
    textPOI = Path('./HW3/POIS3E23.txt').read_text()
    wordcloudPOI = wordcloudPOI.generate(textPOI)
    wordcloudPOI = wordcloudPOI.to_file('./HW3/wordcloudPOI.png')

    maskimage1984 = imageio.imread('./HW3/horse.png')
    wordcloud1984 = WordCloud(colormap='prism', mask=maskimage1984, background_color='white')
    text1984 = Path('./HW3/1984.txt').read_text()
    wordcloud1984 = wordcloud1984.generate(text1984)
    wordcloud1984 = wordcloud1984.to_file('./HW3/wordcloud1984.png')

    maskimageFLOYD = imageio.imread('./HW3/guitar.png')
    wordcloudFLOYD = WordCloud(colormap='prism', mask=maskimageFLOYD, background_color='white')
    textFLOYD = Path('./HW3/WelcometotheMachine.txt').read_text()
    wordcloudFLOYD = wordcloudFLOYD.generate(textFLOYD)
    wordcloudFLOYD = wordcloudFLOYD.to_file('./HW3/wordcloudFLOYD.png')


'''
**Part 3:**<br>
(a) Use **Textatistic** to compute the _average_ of the Flesch–Kincaid, Gunning Fog, SMOG, and Dale–Chall scores for each document.   
(b) Are there noticeable differences among your documents's readability scores, 
and do you suspect any difference is present (or _should be_ present)?
'''
def Part3():
    fkscore1984 = textatistic.fleschkincaid_score(raw1984)
    gfscore1984 = textatistic.gunningfog_score(raw1984)
    smog1984 = textatistic.smog_score(raw1984)
    dcscore1984 = textatistic.dalechall_score(raw1984)
    avg1984 = (fkscore1984 + gfscore1984 + smog1984 + dcscore1984) / 4
    print("Average reading scores for 1984: ", avg1984)

    fkscorePOI = textatistic.fleschkincaid_score(rawPOI)
    gfscorePOI = textatistic.gunningfog_score(rawPOI)
    smogPOI = textatistic.smog_score(rawPOI)
    dcscorePOI = textatistic.dalechall_score(rawPOI)
    avgPOI = (fkscorePOI + gfscorePOI + smogPOI + dcscorePOI) / 4
    print("Average reading scores for Deus Ex Machina: ", avgPOI)

    fkscoreFLOYD = textatistic.fleschkincaid_score(rawFLOYD)
    gfscoreFLOYD = textatistic.gunningfog_score(rawFLOYD)
    smogFLOYD = textatistic.smog_score(rawFLOYD)
    dcscoreFLOYD = textatistic.dalechall_score(rawFLOYD)
    avgFLOYD = (fkscoreFLOYD + gfscoreFLOYD + smogFLOYD + dcscoreFLOYD) / 4
    print("Average reading scores for Welcome to the Machine: ", avgFLOYD)

'''**Part 4:**<br> 
(a) Use spaCy to compute the pairwise similarity between your documents (i.e. doc. 1 to doc. 2, doc. 1 to doc. 3, doc. 2 to doc. 3).<br>
(b) Do any of these similarity scores seem higher or lower than you would expect?  Explain your response.
'''
def Part4():
    nlp = spacy.load('en_core_web_lg')
    print("Similarity score between 1984 and Deus Ex Machina: ", nlp(raw1984).similarity(nlp(rawPOI)))
    print("Similarity score between 1984 and Welcome to the Machine: ", nlp(raw1984).similarity(nlp(rawFLOYD)))
    print("Similarity score between Deus Ex Machina and Welcome to the Machine: ", nlp(rawPOI).similarity(nlp(rawFLOYD)))

'''
**Part 5:**<br>
(a) Use spaCy to find the named entities in your documents.<br>
(b) Produce a bar plot for each document that includes the count for the 20 most common named entities (by name).<br>
(c) Produce a second bar plot per document based on the counts of every named entity type (PERSON, ORG, etc.)<br>
(d) Do you notice any meaningful differences (or similarities) among the documents wrt to these plots?  If so, explain what they are.
'''
def Part5():
    # 5a
    # Loading NLP model
    nlp = spacy.load("en_core_web_sm")

    # Creating NLP docs from each raw document
    nlpPOI = nlp(rawPOI)
    nlp1984 = nlp(raw1984)
    nlpFLOYD = nlp(rawFLOYD)

    # Lists to hold named entities and their types
    namedPOInames = []
    namedPOItypes = []

    named1984names = []
    named1984types = []

    namedFLOYDnames = []
    namedFLOYDtypes = []

    # Printing out the named entities, their types and appending them to respective lists
    print("Named entities in Deus Ex Machina:")
    for entity in nlpPOI.ents:
        print(f'{entity.text}: {entity.label_}')
        namedPOInames.append(entity.text)
        namedPOItypes.append(entity.label_)
    
    print("Named entities in 1984:")
    for entity in nlp1984.ents:
        print(f'{entity.text}: {entity.label_}')
        named1984names.append(entity.text)
        named1984types.append(entity.label_)
    
    print("Named entities in Welcome to the Machine:")
    for entity in nlpFLOYD.ents:
        print(f'{entity.text}: {entity.label_}')
        namedFLOYDnames.append(entity.text)
        namedFLOYDtypes.append(entity.label_)
    
    # Creating dataframes from the lists
    namedPOIframe = pd.DataFrame(list(zip(namedPOInames, namedPOItypes)), columns=['Name', 'Type'])
    named1984frame = pd.DataFrame(list(zip(named1984names, named1984types)), columns=['Name', 'Type'])
    namedFLOYDframe = pd.DataFrame(list(zip(namedFLOYDnames, namedFLOYDtypes)), columns=['Name', 'Type'])

    # 5b
    # Creating lists of top 20 occuring names and their counts
    # Creating bar graphs for them
    n = 20

    most20namesPOI = namedPOIframe['Name'].value_counts()[:n].index.tolist()
    most20POI = namedPOIframe['Name'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20namesPOI)), most20POI, tick_label=most20namesPOI)

    most20names1984 = named1984frame['Name'].value_counts()[:n].index.tolist()
    most201984 = named1984frame['Name'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20names1984)), most201984, tick_label=most20names1984)

    most20namesFLOYD = namedFLOYDframe['Name'].value_counts()[:n].index.tolist()
    most20FLOYD = namedFLOYDframe['Name'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20namesFLOYD)), most20FLOYD, tick_label=most20namesFLOYD)

    # plt.xticks(rotation=90)
    # plt.show()

    # 5c
    # Creating lists of top 20 occuring types and their counts
    most20typesPOI = namedPOIframe['Type'].value_counts()[:n].index.tolist()
    most20POI2 = namedPOIframe['Type'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20typesPOI)), most20POI2, tick_label=most20typesPOI)

    most20types1984 = named1984frame['Type'].value_counts()[:n].index.tolist()
    most2019842 = named1984frame['Type'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20types1984)), most2019842, tick_label=most20types1984)

    most20typesFLOYD = namedFLOYDframe['Type'].value_counts()[:n].index.tolist()
    most20FLOYD2 = namedFLOYDframe['Type'].value_counts()[:n].tolist()
    #plt.bar(range(len(most20typesFLOYD)), most20FLOYD2, tick_label=most20typesFLOYD)

    # plt.xticks(rotation=90)
    # plt.show()
    

# Testing
# Part2()
# Part3()
# Part4()
# Part5()