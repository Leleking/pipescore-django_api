import requests
from bs4 import BeautifulSoup
from facebook_scraper import get_posts


class FacebookAnalysis:
    def __init__(self, term):
        self.term = term
        

    def run(self):
        print(self.term)
        posts = get_posts(self.term, pages=1)
        results = []
       

        return posts
    
