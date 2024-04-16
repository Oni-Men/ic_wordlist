# -*- coding: utf-8 -*-

__author__ = "Onimen"
__date__ = "2024/04/16"
__version__ = "0.0.1"

from urllib import request
from urllib.request import Request
from .word import Word

class WordListScraper:

  def __init__(self, wordlist_url) -> None:
    self.url = wordlist_url
    pass

  def execute(self):
    req = Request(self.url)
    res = request.urlopen(req)
    csv = res.read().decode('utf8')
    rows = str.split(csv, "\n")[1:] # Ignore first line because it's a heading line.

    wordlist = []

    for row in rows:
      word = Word(row)
      if word.has_description():
        wordlist.append(word)

    return wordlist 