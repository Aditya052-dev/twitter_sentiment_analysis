#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tweepy 
import pandas as pd
from textblob import TextBlob
import re 
from IPython.display import display
import matplotlib.pyplot as plt


# In[2]:


CONSUMER_KEY    = 'your_key'
CONSUMER_SECRET = 'your_key'

ACCESS_TOKEN  = 'your_key'
ACCESS_SECRET = 'yourkey'


# In[3]:


# API's setup:
def twitter_setup():
# Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Return API with authentication:
    api = tweepy.API(auth)
    return api
extractor = twitter_setup()


# In[4]:


user_name = input("enter twitter username ")
print(user_name)


# In[5]:


tweets = extractor.user_timeline(screen_name=user_name, count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))


# In[6]:


# We print the most recent 10 tweets:
print("10 recent tweets:\n")
for tweet in tweets[:10]:
    print(tweet.text)
    print()	


# In[7]:


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
display(data.head(10))


# In[8]:


print("Latest Tweet:")
print(tweets[0].text)
print("Time Created:",tweets[0].created_at)
print("Source:",tweets[0].source)
print("Likes count:",tweets[0].favorite_count)
print("Retweet Count",tweets[0].retweet_count)
print(tweets[0].entities)
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
display(data.head(10))


# In[9]:


mean = np.mean(data['len'])

print("The length's average in tweets: {}".format(mean))
fav_max = np.max(data['Likes'])
rt_max  = np.max(data['RTs'])

fav = data[data.Likes == fav_max].index[0]
rt  = data[data.RTs == rt_max].index[0]

# Max Favourites:
print("The tweet with most likes is: \n{}".format(data['Tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))
# Max RTs:
print("The tweet with most retweets is: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))


# In[10]:


#GRAPH for average length of tweets
tlen = pd.Series(data=data['len'].values, index=data['Date'])
tlen.plot(figsize=(16,4),label="Length", legend=True,color="r")
plt.show()


# In[11]:


#GRAPH for average Favourites of tweets
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tfav.plot(figsize=(16,4), label="Likes", legend=True,color="g")
plt.show()


# In[12]:


#GRAPH for average Retweets of tweets
tret = pd.Series(data=data['RTs'].values, index=data['Date'])
tret.plot(figsize=(16,4), label="Retweets", legend=True,color="b")
plt.show()


# In[13]:


#Analysis of Sources
sources = []
for source in data['Source']:
    if source not in sources:
        sources.append(source)
print("Creation of content sources:")
for source in sources:
    print("* {}".format(source))
    percent = np.zeros(len(sources))

for source in data['Source']:
    for index in range(len(sources)):
        if source == sources[index]:
            percent[index] += 1
            pass       


# In[14]:


percent /= 100
pie_chart1 = pd.Series(percent, index=sources, name='Sources')
pie_chart1.plot.pie(fontsize=10, autopct='%.2f', figsize=(6, 6))

plt.show()


# In[15]:


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])
display(data.head(10))


# In[16]:


pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]
sa=[len(pos_tweets),len(neu_tweets),len(neg_tweets)]
s=["Positive","Neutral","Negative"]
pie_chart2 = pd.Series(sa,index=s, name='Sentiment Analysis')
pie_chart2.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6))
plt.show()


# In[ ]:




