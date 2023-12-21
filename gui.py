from tkinter import *
import numpy as np
import tweepy 
import pandas as pd
from textblob import TextBlob
import re 
from IPython.display import display
import matplotlib.pyplot as plt

root = Tk()
root.title('Posi Tweets') #Title


width=600
hight=400

root.geometry(f"{width}x{hight}")
root.minsize(width,hight) # minimum size
root.maxsize(width,hight)


#================Banner Part Begin =================#
banner = Frame(root,padx=15,pady=14, bg="green")
banner.pack()

heding = Label(banner, text="Posi Tweets", font="comicsansms 20 bold")
heding.pack()

#================Banner Part End ===================#

#================User Input Part Begin ===================#
input_frame = Frame(root,padx=0,pady=30)
input_frame.pack(anchor="w")

input_frame1 = Frame(root,padx=0,pady=0, bg="yellow")
input_frame1.pack()

username = Label(input_frame, text="Enter UserID without @ :- ",justify=LEFT,font="comicsansms 10 bold", padx=30)
username.grid(row=2, column=1)

user_value = StringVar()

userinput = Entry(input_frame, textvariable=user_value)
userinput.grid(row=2, column=2)
def click():  
    user_name = user_value.get()
    # Twitter App Keys

    CONSUMER_KEY    = 'weL8lMDJ4MrxgIJAYnzpqqSnS'
    CONSUMER_SECRET = 'yPHTZSWOFx1tM6ee0cmFSAVkyltO13l3OQlf9I2ZAYhhtgYRUd'

    ACCESS_TOKEN  = '810904421148278785-CeJTxd3JdTfyO8YjNvDG60P32Wrl5is'
    ACCESS_SECRET = 'brumdrRZnTTd2CNNyXYXZqWxCehshro7pb5rShkAwGPJ9'




# API's setup:
    def twitter_setup():
    # Authentication and access using keys:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
        api = tweepy.API(auth)
        return api
    extractor = twitter_setup()



#Tweet List
    tweets = extractor.user_timeline(screen_name=user_name, count=200,lang="UTF-8")
    print("Number of tweets extracted: {}.\n".format(len(tweets)))


# We print the most recent 10 tweets:
    print("10 recent tweets:\n")
    for tweet in tweets[:10]:
        print(tweet.text)
        print()	




    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
    display(data.head(10))




#print(dir(tweets[0]))
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




    #GRAPH for average length of tweets with months
    tlen = pd.Series(data=data['len'].values, index=data['Date'])
    tlen.plot(figsize=(16,4),label="Length", legend=True,color="r")
    plt.show()




    #GRAPH for average Favourites of tweets with months
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tfav.plot(figsize=(16,4), label="Likes", legend=True,color="g")
    plt.show()




    #GRAPH for average Retweets of tweets with months
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])
    tret.plot(figsize=(16,4), label="Retweets", legend=True,color="b")
    plt.show()





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

    percent /= 100
    pie_chart1 = pd.Series(percent, index=sources, name='Sources')
    pie_chart1.plot.pie(fontsize=10, autopct='%.2f', figsize=(6, 6))

    plt.show()



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




    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]
    sa=[len(pos_tweets),len(neu_tweets),len(neg_tweets)]
    s=["Positive","Neutral","Negative"]
    pie_chart2 = pd.Series(sa,index=s, name='Sentiment Analysis')
    pie_chart2.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6))
    plt.show()








#================User Input Part End ===================#


number=0
button = Button(input_frame1,text="Get Analysis", command=click, fg="blue",height = 1, width = 15)
button.grid(row=1, column=1)

root.mainloop()