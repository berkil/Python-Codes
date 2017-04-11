#!/usr/bin/python

import feedparser, pprint, urllib
from bs4 import BeautifulSoup

rss = raw_input('Enter URL: ')
feed = feedparser.parse(rss)

print feed["feed"]["link"]
