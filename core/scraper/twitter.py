from twitterscraper import query_tweets
import twitterscraper
from bs4 import BeautifulSoup
import random
import requests
import datetime as dt
HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]
twitterscraper.query.HEADER = {'User-Agent': random.choice(HEADERS_LIST), 'X-Requested-With': 'XMLHttpRequest'}

class TwitterAnalysis:
    def __init__(self, term):
        self.term = term
        self.url = 'https://twitter.com/search?q={}'.format(self.term)
    
    def run(self):
        begin_date = dt.date(2019,4,15)
        end_date = dt.date(2020,2,12)
        limit = 100
        lang = 'english'
        list_of_tweets = query_tweets(self.term, begindate=begin_date, enddate=end_date,limit=limit, lang = lang)
        for tweet in list_of_tweets:
            print(tweet+ "\n")

        #print the retrieved tweets to the screen:
        """  for tweet in query_tweets("Trump OR Clinton", 10):
            print(tweet) """

        #Or save the retrieved tweets to file:
    
    def run_soup(self):
        result = requests.get(self.url)
        result = requests.get(self.url)
        soup = BeautifulSoup(result.text, 'html5lib')
        print(soup)
