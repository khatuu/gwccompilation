import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

pv = []

for tweet in tweetData:
    tt = tweet["text"]
    tb = TextBlob(tt)
    print("{}: {}".format(tt, tb.polarity))
    pv.append(tb.polarity)
# Continue your program below!

# Textblob sample:
# while True:
#     phrase = input("Enter a phrase: ")
#     tb = TextBlob(phrase)
#     print(tb.polarity)

plt.hist(pv)
plt.title("Tweets Polarity")
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.grid()
plt.show()
