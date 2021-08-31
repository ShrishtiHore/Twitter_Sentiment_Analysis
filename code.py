import tweepy
from textblob import TextBlob
def percentage(part: object, whole: object) -> object:
    return 100*float(part)/float(whole)

consumer_key= '_______________________________'
consumer_secret= '_____________________________________'

access_token='____________________________________________________'
access_token_secret='_________________________________________________'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
searchTerm=input("enter keyword/hashtag to search about:")
date="2019-01-01"
noOfSearchTerms=int(input("enter how many tweets to analyze:"))
tweets=tweepy.Cursor(api.search,q=searchTerm,lang="en").items(noOfSearchTerms)
positive =0
negative =0
neutral =0
polarity =0
def clean_tweets(text):
    text=re.sub("RT @[\w]*:","",text)
    text=re.sub("@[\w]*","",text)
    text=re.sub("https?://[A-Za-z0-9./]*","",text)
    text=re.sub("\n","",text)
    text=re.sub("#","",text)
    return text

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

     if(analysis.sentiment.polarity == 0):
         neutral += 1
     elif(analysis.sentiment.polarity <0.00):
        negative +=1
     elif(analysis.sentiment.polarity >0.00):
        positive +=1
positive=percentage(positive,noOfSearchTerms)
neutral=percentage(neutral,noOfSearchTerms)
negative=percentage(negative,noOfSearchTerms)

positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negative=format(negative,'.2f')
print("how many people are reacting on" +searchTerm+ "by analyzing" + str(noOfSearchTerms)+ "Tweets.")

if(polarity == 0):
    print("neutral")
elif(polarity<0):
    print("negative")
elif(polarity>0):
     print("positive")
labels = ['positive['+str(positive)+'%]','negative['+str(negative)+'%]','neutral['+str(neutral)+'%]']
sizes =[positive,negative,neutral]
colors=['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title('how people are reacting on ' + searchTerm+' by analyzing '+str(noOfSearchTerms)+'Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
    
