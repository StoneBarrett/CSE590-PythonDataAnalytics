# Stone Barrett
# CSE 590: Python Data Analytics
# Homework 2

# Importing libraries
from operator import index
from mysqlx import Row
import pandas as pd

# Testing
# import os
# os.getcwd()

'''(b) Load the words of this structure in sequential order of appearance 
into a one-dimensional Python list (i.e. the first word should be the first element in the list, 
while the last word should be the last element) that is **case insensitive**.  
It's up to you how to deal with special chacters -- you can remove them manually, 
ignore them during the loading process, or even count them as words, for example.  
**Make sure you have this list clearly assigned to a variable, so we can evaluate it during grading.**'''

# Opening text file containing the script
file = open("./HW2/BARRETT_STONE_2/rots_script.txt", mode="r")
# Assigning entire script to a variable
rotsFile = file.read()
# Closing file
file.close()

# .strip() didn't work for some reason
# rotsStrip1 = rotsPreStrip.strip(":;,.?/!@#$%^&*()")
# .replace() works, so replacing all problematic characters
rotsReplace1 = rotsFile.replace("\n", " ")
rotsReplace2 = rotsReplace1.replace(".", " ")
rotsReplace3 = rotsReplace2.replace(",", " ")
rotsReplace4 = rotsReplace3.replace(":", " ")
rotsReplace5 = rotsReplace4.replace(";", " ")
rotsReplace6 = rotsReplace5.replace("(", " ")
rotsReplace7 = rotsReplace6.replace(")", " ")
rotsReplace8 = rotsReplace7.replace("!", " ")
rotsReplace9 = rotsReplace8.replace("?", " ")
rotsReplace10 = rotsReplace9.replace("'", " ")
rotsReplace11 = rotsReplace10.replace('"', " ")
rotsReplace12 = rotsReplace11.replace("_", " ")
rotsReplace13 = rotsReplace12.replace("\t", " ")
rotsReplace14 = rotsReplace13.replace("<", " ")
rotsReplace15 = rotsReplace14.replace(">", " ")
rotsReplace16 = rotsReplace15.replace("~", " ")
rotsReplace17 = rotsReplace16.replace("`", " ")
rotsReplace18 = rotsReplace17.replace("&", " ")
rotsReplace19 = rotsReplace18.replace("#", " ")
# Final replace, assigning to variable to be split
rots = rotsReplace19.replace("^", " ")
# .split() based on spaces
# This is the final list of words to be evaluated in grading
rotsList = rots.split(" ")

# Testing
# for i in range(len(rotsList)):
#     print(rotsList[i])


'''(c) Use your list to create **and print** a two-column pandas data-frame with the following properties: <br>
i. The first column for each index should represent the word in question at that index <br>
ii. The second column should represent the number of times that particular word appears in the text. <br>
iii. The rows of the data-frame should be ordered according to the **first** occurrence of each word. <br>
iv. It's up to you whether or not your data-frame will include an index per row.  
<br>**Make sure you have this data-frame clearly assigned to a variable, so we can evaluate it during grading.**'''

# New variable to hold words in order they appear and only once
rots2 = []
# New variable to hold appearance count for each word
rotsFreq = []
# Loop and list comprehension to hold words in order that they appear and only once
for i in rotsList:
    if i not in rots2:
        rots2.append(i)
# Counting number of times each word appears
for i in range(len(rots2)):
    rotsFreq.append(rotsList.count(rots2[i]))

# Dataframe with word and frequency columns that zips the two lists together
rotsFrame = pd.DataFrame(list(zip(rots2, rotsFreq)), columns=["Word", "Frequency"])
# Dropping whitespace row (not sure why it's still there anyway)
rotsFrame.drop(labels=[4], axis=0, inplace=True)
# Resetting indecies after drop
rotsFrame.reset_index(drop=True, inplace=True)
# rotsFrame is now the final variable to be evaluated for grading

# Testing
# outFile = open('./HW2/BARRETT_STONE_2/out.txt', 'w')
# print(rotsFrame.to_string(), file = outFile)
# outFile.close()

# More testing
# rotsFrame.to_csv(r'./HW2/BARRETT_STONE_2/testCSV.txt', header=None, index=None, sep=' ', mode='a')
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# for i in rotsFrame.index:
#     print(rotsFrame['Word'][i], rotsFrame['Frequency'][i])


'''(d) **Stop-words** are commonly used words in a given language that often fail to communicate useful 
summative information about its content.  The attached stop_words.py file has a simple list of common stop words 
assigned to a variable.  For this part of the assigment, you are to create a modified copy of the data-frame 
from (c) with the following modifications: _i. all stop words have been removed from the data-frame_ and _ii. 
the data frame rows have been sorted in decreasing order of frequency counts_.  
**Again, make sure you have this data-frame clearly assigned to a variable, so we can evaluate it during grading.** '''

# Stop words list
stop_words = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "A", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "after", "afterwards", "ag", "again", "against", "ah", "ain", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appreciate", "approximately", "ar", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "B", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "been", "before", "beforehand", "beginnings", "behind", "below", "beside", "besides", "best", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "C", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "ci", "cit", "cj", "cl", "clearly", "cm", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "could", "couldn", "couldnt", "course", "cp", "cq", "cr", "cry", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d", "D", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "dj", "dk", "dl", "do", "does", "doesn", "doing", "don", "done", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "E", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "F", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "G", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "H", "h2", "h3", "had", "hadn", "happens", "hardly", "has", "hasn", "hasnt", "have", "haven", "having", "he", "hed", "hello", "help", "hence", "here", "his","her","him","she","they","them","hereafter", "hereby", "herein", "heres", "hereupon", "hes", "hh", "hi", "hid", "hither", "hj", "ho", "hopefully", "how", "howbeit", "however", "hr", "hs", "http", "hu", "hundred", "hy", "i2", "i3", "i4", "i6", "i7", "i8", "i","ia", "ib", "ibid", "ic", "id", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "im", "immediately", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "inward", "io", "ip", "iq", "ir", "is", "isn", "it", "itd", "its", "iv", "ix", "iy", "iz", "j", "J", "jj", "jr", "js", "jt", "ju", "just", "k", "K", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "ko", "l", "L", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "M", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "my", "n", "N", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "neither", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "O", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "otherwise", "ou", "ought", "our", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "P", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "pp", "pq", "pr", "predominantly", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "Q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "R", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "S", "s2", "sa", "said", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "seem", "seemed", "seeming", "seems", "seen", "sent", "seven", "several", "sf", "shall", "shan", "shed", "shes", "show", "showed", "shown", "showns", "shows", "si", "side", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somehow", "somethan", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "sz", "t", "T", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they", "theyd", "theyre", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "U", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "used", "useful", "usefully", "usefulness", "using", "usually", "ut", "v", "V", "va", "various", "vd", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "W", "wa", "was", "wasn", "wasnt", "way", "we", "wed", "welcome", "well", "well-b", "went", "were", "weren", "werent", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "wi", "widely", "with", "within", "without", "wo", "won", "wonder", "wont", "would", "wouldn", "wouldnt", "www", "x", "X", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "Y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "your", "youre", "yours", "yr", "ys", "yt", "z", "Z", "zero", "zi", "zz"]
# New dataframe dropping all stop_words from Word column
rotsFrameD = rotsFrame[~rotsFrame.Word.isin(stop_words)]
# Sorting by word count in descending order
rotsFrameD.sort_values(by=['Frequency'], axis=0, ascending=False, inplace=True)
# Resetting indecies after drop
rotsFrameD.reset_index(drop=True, inplace=True)
# rotsFrameD is now the final variable to be evaluated for grading

# Potentially another method of doing so
# # Dropping all rows where "Word" contains any stop_words entry
# for i in range(len(stop_words)):
#     rotsFrameD[rotsFrameD["Word"].str.contains(stop_words[i])==False]

# Testing
# outFile = open('./HW2/BARRETT_STONE_2/outD.txt', 'w')
# print(rotsFrameD.to_string(), file = outFile)
# outFile.close()


'''(e) While total word counts can provide a useful measure of the content of a document, 
they cannot reveal much about its underlying trends.  In the context of document analysis, 
the term _trend_ implies a direction (in terms of theme, mood, etc.) in which the content changes 
throughout the narrative.  For example, some works of fiction begin with a comedic tone, 
and take on a more serious tone in later stages, or vice versa.  For the last part of your assignment, 
you are going to modify the approach taken in part (d) to address individual segments of the document. 
More specifically, you are to divide the raw document into partitions according to the chapters, 
acts, etc. that are present, and then produce a _list of data-frames_, where **each list element is a 
single data-frame containing word frequencies for a single segment** with the same format as the data-frame 
from part (d) outlined above.  You are free to use whatever means you prefer in splitting the text into chapters 
and constructing the list of data-frames, but one option is to use regular expressions with the raw document.  
**Once again, you must insure your list is readily accessible to us in the form of a variable.**'''

# Splitting list from B into 5 lists
intro = rotsList[0:145]
act1 = rotsList[154:11894]
act2 = rotsList[11895:26462]
act3 = rotsList[26464:39405]
ending = rotsList[39407:40167]

# Method for repeating C and D on new lists
def pandatize(someList):
    # New variable to hold words in order they appear and only once
    rotsInFunc = []
    # New variable to hold appearance count for each word
    rotsFreqInFunc = []
    # Loop and list comprehension to hold words in order that they appear and only once
    for i in someList:
        if i not in rotsInFunc:
            rotsInFunc.append(i)
    # Counting number of times each word appears
    for i in range(len(rotsInFunc)):
        rotsFreqInFunc.append(someList.count(rotsInFunc[i]))

    # Dataframe with word and frequency columns that zips the two lists together
    rotsFrameInFunc = pd.DataFrame(list(zip(rotsInFunc, rotsFreqInFunc)), columns=["Word", "Frequency"])
    # Dropping whitespace row (not sure why it's still there anyway)
    rotsFrameInFunc.drop(labels=[4], axis=0, inplace=True)
    # Resetting indecies after drop
    rotsFrameInFunc.reset_index(drop=True, inplace=True)
    # New dataframe dropping all stop_words from Word column
    rotsFrameInFuncD = rotsFrameInFunc[~rotsFrameInFunc.Word.isin(stop_words)]
    # Sorting by word count in descending order
    rotsFrameInFuncD.sort_values(by=['Frequency'], axis=0, ascending=False, inplace=True)
    # Resetting indecies after drop
    rotsFrameInFuncD.reset_index(drop=True, inplace=True)
    # rotsFrameInFuncD is now the final variable to be returned for adding to list of dataframes
    return rotsFrameInFuncD

# Repeating C and D for Intro
introFrame = pandatize(intro)
# Repeating C and D for Act 1
act1Frame = pandatize(act1)
# Repeating C and D for Act 2
act2Frame = pandatize(act2)
# Repeating C and D for Act 3
act3Frame = pandatize(act3)
# Repeating C and D for Ending
endingFrame = pandatize(ending)

# Dropping whitespace row for each
# introFrame.drop(labels=[0], axis=0, inplace=True)
act1Frame.drop(labels=[0], axis=0, inplace=True)
act2Frame.drop(labels=[0], axis=0, inplace=True)
act3Frame.drop(labels=[0], axis=0, inplace=True)
endingFrame.drop(labels=[0], axis=0, inplace=True)

# Resetting index for each after whitespace drop
# introFrame.reset_index(drop=True, inplace=True)
act1Frame.reset_index(drop=True, inplace=True)
act2Frame.reset_index(drop=True, inplace=True)
act3Frame.reset_index(drop=True, inplace=True)
endingFrame.reset_index(drop=True, inplace=True)

# Testing
# outFile = open('./HW2/BARRETT_STONE_2/outFuncTest.txt', 'w')
# print(act2Frame.to_string(), file = outFile)
# outFile.close()

# Making final list of frames
listOfFrames = [introFrame, act1Frame, act2Frame, act3Frame, endingFrame]