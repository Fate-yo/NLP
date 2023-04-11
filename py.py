# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
import nltk
from zhtools import langconv, zh_wiki
from zhtools.langconv import Converter

from urllib.request import urlopen

url = r'https://gutenberg.org/cache/epub/23962/pg23962.html'

html = urlopen(url).read()
text = html.decode('utf-8')

patten = '[\W \d a-zA-Z]'
print(re.sub(patten, '', text))
