#Libraries needed
import pandas as pd
import snscrape.modules.twitter as sntwitter
#nltk. download('stopwords*) #run once and comment it out to avoid it downloading multiple times
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

#comment it out once you have gathered your data
# to avoid running out of the wait time gather the data per month
query = "(#klimakleber OR #letztegeneration OR #lastgeneration) until:2022-12-18 since:2022-12-12"
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i>20000:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content,tweet.likeCount, tweet.retweetCount])
df = pd.DataFrame (tweets, columns = ['Date', 'ID', 'url', 'username', 'source', 'location', 'tweet', 'num of likes', 'num of retweets'])
df.to_csv('scraping.csv')