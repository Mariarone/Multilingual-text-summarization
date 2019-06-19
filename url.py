import requests
from bs4 import BeautifulSoup



#page = requests.get("https://www.healthline.com/nutrition/10-health-benefits-of-apples.html")

'''age = input("Enter the URL: ")

page = requests.get(age)
if page.status_code != 200:
    print('Web site does not exists')
else:
    soup = BeautifulSoup(page.content, 'html.parser')



    textContent = []
    for i in range(0, 10):
        paragraphs = soup.find_all("p")[i].text
        textContent.append(paragraphs)
    


    listToStr = ' '.join([str(elem) for elem in textContent]) 

    with open('new.txt', 'a') as f:
        f.write("%s" %listToStr)'''

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

f = open('new.txt', 'wb')
f.write(listToStr.encode("utf-8"))    
f.close()     
	        
import summarize1.py



