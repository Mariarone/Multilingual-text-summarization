import requests
from bs4 import BeautifulSoup
import codecs
import re

from numpy import unicode

print("Enter/Paste your content:")
contents = []    
line=input()
contents.append(line)
print(contents)

listToStr = ' '.join([str(elem) for elem in contents]) 

#with open('input.txt', 'a') as f:

f = open('input1.txt', 'wb')
f.write(listToStr.encode("utf-8"))    
f.close()

import example.py