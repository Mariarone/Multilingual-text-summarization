from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx



def summarizer():
    stop_words = stopwords.words('english')   
    def clean1_text(text):
        text = text.replace('\n', '')
        return(text)
    def sentence_similarity(sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []

        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1

        return euclid(np.array(vector1),np.array(vector2))

    def build_similarity_matrix(sentences, stop_words):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2: #ignore if both are same sentences
                    continue 
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        
        
        return similarity_matrix




    def euclid(vec1,vec2):
        #print(vec1,vec2)
        if all((vec1 is not None, vec2 is not None)):
            return np.linalg.norm(vec1-vec2) 




    #def read_article(text):
    file = open('comparison.txt', "r")
    for line in file:
        sentences = line.split(".")
        while '' in sentences:
            sentences.remove('')

        
    #print(sentences)



    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    print(sentence_similarity_martix)


    #graph
    #import networkx as nx
    summarize_text = []
    nx_graph =nx.from_numpy_array(sentence_similarity_martix)
    scores=nx.pagerank(nx_graph)
    print(scores)

    f1=open('new.txt',"r")
    text = f1.read()
    text1=clean1_text(text)
    for line in text1:
        sentences1=text1.split(".")
        while("" in sentences1): 
            sentences1.remove("") 


        

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences1)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    
    for i in range(5):
        summarize_text.append("".join(ranked_sentence[i][1]))
        listToStr = '.'.join([str(elem) for elem in summarize_text])
    return(listToStr)
            
