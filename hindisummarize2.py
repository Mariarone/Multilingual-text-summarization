from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import math
from nltk.tag import tnt
from nltk.corpus import indian
from googletrans import Translator
import nltk
import re
import codecs
from numpy import unicode



def summarizer():

    def sentence_similarity(sent1, sent2):
        
    
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]
    
        all_words = list(set(sent1 + sent2))
    
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
    
        # build the vector for the first sentence
        for w in sent1:
            vector1[all_words.index(w)] += 1
    
            
        
        # build the vector for the second sentence
        for w in sent2:
            vector2[all_words.index(w)] += 1
    
        
        
        return euclid(np.array(vector1),np.array(vector2))
    
    def build_similarity_matrix(sentences):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2: #ignore if both are same sentences
                    continue 
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2])

        
        
        return similarity_matrix




    def euclid(vec1,vec2):
        if all((vec1 is not None, vec2 is not None)):
            return np.linalg.norm(vec1-vec2) 

        



    
    #def read_article(text):
    file = open('tokenized2.txt', "r",encoding='utf-8')
    for line in file:
        sentences = line.split(u"।")
        while '' in sentences:
            sentences.remove('')
        #print(sentences)



    sentence_similarity_martix = build_similarity_matrix(sentences)
    #print(sentence_similarity_martix)

    def clean1_text(text):
        text = text.replace('\n', '')
        return(text)

    summarize_text = []
    nx_graph =nx.from_numpy_array(sentence_similarity_martix)
    scores=nx.pagerank(nx_graph)
    print(scores)
    f1=open('input1.txt',"r",encoding='utf-8')
    text = f1.read()
    text1=clean1_text(text)
    for line in text1:
        sentences1=text1.split(u"।")
        while '' in sentences1:
            sentences1.remove('')
        
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences1)), reverse=True)
    #print(ranked_sentence)
    for i in range(5):
        summarize_text.append("".join(ranked_sentence[i][1]))
        listToStr = '।'.join([str(elem) for elem in summarize_text])
    return(listToStr)
   

        