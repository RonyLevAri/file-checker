import urllib2
from hashlib import sha1


class UrlHash:
    def __init__(self, url_path):
        self.url_path = url_path
        self.hash = self.hash_content()

    def retrieve_url_content(self):
        response = urllib2.urlopen(self.url_path)
        html = response.read()
        return html

    def hash_content(self):
        encrypt = str(self.retrieve_url_content())
        m = sha1(encrypt).hexdigest()
        return m
