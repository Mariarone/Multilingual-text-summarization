import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
import validators
from collections import OrderedDict
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import numpy as np
import networkx as nx


def pos_tagging():
	punctuations = '''!()[]{};:'"\,-<>/?@#$%^&*_~'''

	porter = PorterStemmer()
	stop_words = set(stopwords.words('english'))





	with open('new.txt', 'r') as myfile:
		data = myfile.read()

	print(data)



	dig="0123456789"

	print(sent_tokenize(data))
	print("\n")

	for s in sent_tokenize(data):
		tokens=[]
		nltk_tokens = nltk.word_tokenize(s.lower())
		
		for w in nltk_tokens:
			#print("\n","\t",w,len(w))
			k=w.split('.')
			if(int(len(w.split('.'))>1) and k[1]=='' ):
				tokens.append(k[0])
				tokens.append('.')
			else:
				tokens.append(k[0])
		print(tokens)
		
		filtered_sentence = [] 
		
		for w in tokens: 
			if w.lower() not in stop_words: 
				filtered_sentence.append(w) 
		
		#print(nltk_tokens) 

		#print("\n Filtered sentence is: ")
		#print(filtered_sentence) 
		#print("\n\n\n")

		no_punct = []

		for char in filtered_sentence:
			if char not in punctuations:
				no_punct.append(char)

			
		

		#print("\n Punctuation removed: ")
		#print(no_punct)




		#print("\n\n\n")

		tagged = nltk.pos_tag(no_punct)
		#print("\n POS Tagged tokens: ")
		#print(tagged)

		tagged=OrderedDict(tagged)

		#print (tagged)
		
		key=list(tagged.keys())
		#print("\n\n\n")
		#print (key)

		print("\n\n")

		last=[]

		lemmatizer = WordNetLemmatizer()
		ps=PorterStemmer()
		f=open('startup.txt','r')
		for i in key:
			flag=0
			f1=open('startup3.txt','r')
			for line in f1:
				#print(line.strip())
				if(i==line.strip()):
					last.append(i)
					flag=1
			if flag==1:
				continue

			if tagged[i]=='NN' or tagged[i]=='NNP' :
				#print("\n",i)
				last.append(i)
		
			elif tagged[i]=='NNS'or tagged[i]=='NNPS':
				#print("\n",i)		
				last.append(lemmatizer.lemmatize(i))	
		
		
			elif tagged[i]=='VBD' or tagged[i]=='VBN':
				c1=0
				f=open('startup.txt','r')
				for line in f:
					if(i==line.strip()):
						#print(line)
						last.append((ps.stem(i))+'e')
						c1=1
					
				f.close()


				f=open('startup2.txt','r')
				for line in f:
					if(i==line.strip()):
						#print(line)
						last.append((ps.stem(i))+'ate')
						c1=1
					
				f.close()

				
				if(c1==0):
					last.append(ps.stem(i))


		
			elif tagged[i]=='VBG':
				c2=0
				#print("verb is",i,lemmatizer.lemmatize(i))
				f=open('startup.txt','r')
				for line in f:
					if(i==line.strip()):
						last.append((ps.stem(i))+'e')
						c2=1
				f.close()
				f=open('startup2.txt','r')
				for line in f:
					if(i==line.strip()):
						#print(line)
						last.append((ps.stem(i))+'ate')
						c2=1
					
				f.close()
				if(c2==0):
					last.append(ps.stem(i))

			elif tagged[i]=='JJ':
				c3=0
				#print("verb is",i,lemmatizer.lemmatize(i))
				f=open('startup.txt','r')
				for line in f:
					if(i==line.strip()):
						#print(line)
						last.append((ps.stem(i))+'e')
						c3=1
				f.close()
				if(c3==0):
					last.append(ps.stem(i))


			else:
				last.append(lemmatizer.lemmatize(i))		

		print(last)
		listToStr = ' '.join([str(elem) for elem in last]) 

		with open('comparison.txt', 'a') as f:
				f.write("%s" %listToStr)
				return()
			

		
		
		
			
			


			
				
			

			
		