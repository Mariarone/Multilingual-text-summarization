from langdetect import detect
from nltk.tokenize import sent_tokenize


def validate(data):


    nltk_sent=sent_tokenize(data)
    print(nltk_sent)
    for line in nltk_sent:
        s=detect(line)
    return(s)    
		

