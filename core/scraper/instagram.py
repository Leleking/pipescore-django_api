import instagram_explore as ie
from textblob import TextBlob

class InstagramAnalysis:
    def __init__(self, term):
        self.term = term
    
    def run(self):
        data, cursor = ie.tag(self.term)
        edges = data['edge_hashtag_to_media']['edges']  
        posts = []
        for post in edges:
            body = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
            text = TextBlob(body)
            sentiment = text.sentiment
            b = {
                "id":post['node']['id'],
                "body": body,
                "display_url": post['node']['display_url'],
                "caption": post['node']['accessibility_caption'],
                "sentiment": sentiment
                


            }
            posts.append(b)
        return posts


