import codecs
import re
from numpy import unicode
from flask import Flask, render_template, request #Used to render .html templates
from langdetect import detect
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

class Tokenizer():
    

    def __init__(self, text=None):
        if text is not None:
            self.text = text
            self.clean_text()
        else:
            self.text = None
        self.sentences = []
        self.tokens = []
        self.stemmed_word = []
        self.final_list = []
        self.final_Sentences=[]
    # self.final_tokens=[]


    def read_from_file(self, filename):
        f = codecs.open(filename, encoding='utf-8')
        self.text = f.read()
        self.clean_text()

    def generate_sentences(self):
        '''generates a list of sentences'''
        text = self.text
        text = text.replace(u'?', u'।')
        self.sentences = text.split(u"।")
        while '' in self.sentences:
            self.sentences.remove('')
        return(self.sentences)

    def print_sentences(self, sentences=None):
        print("COUNT: ", len(self.sentences))
        if sentences:
            for i in sentences:
                print(i)
        else:
            for i in self.sentences:
                print(i)

    def clean_text(self):

        text = self.text
        
        text = text.replace(u'\n', '')
        text = text.replace(u',', '')
        text = text.replace(u'"', '')
        text = text.replace(u'(', '')
        text = text.replace(u')', '')
        text = text.replace(u'"', '')
        text = text.replace(u':', '')
        text = text.replace(u"'", '')
        text = text.replace(u"’", '')
        text = text.replace(u"‘", '')
        text = text.replace(u"‘‘", '')
        text = text.replace(u"’’", '')
        text = text.replace(u"''", '')
        text = text.replace(u".", '')
        self.text = text

    def remove_only_space_words(self):
        tokens = filter(lambda tok: tok.strip(), self.tokens)
        tokens = [tok for tok in self.tokens if tok.strip()]
        self.tokens = tokens

    def hyphenated_tokens(self):

        for i,each in enumerate(self.tokens):
            if '-' in each:
                tok = each.split('-')
                self.tokens.remove(each)
                self.tokens.insert(i,tok[0])
                self.tokens.insert(i+1,tok[1])

    def tokenize(self):
        '''done'''
        if not self.sentences:
            self.generate_sentences()

        sentences_list = self.sentences

        for each in sentences_list:
            tokens = []
            word_list = each.split(' ')
            tokens = tokens + word_list
            self.tokens = tokens
            #print(self.tokens)
            # remove words containing spaces
            self.remove_only_space_words()
            # remove hyphenated words
            self.hyphenated_tokens()
            self.remove_stop_words()
            self.formSentence()
    """def print_tokens(self, print_list=None):
        '''done'''
        if print_list is None:
            for i in self.tokens:
                #print(i)
        else:
            for i in print_list:
                #print(i)"""

    def formSentence(self):
        finalSentence=""
        for word in self.final_tokens:
            finalSentence +=word+" "
         
        self.final_Sentences.append(finalSentence)
        #print(self.final_Sentences)
    def print_finalSentence(self, x):
        fileName = "simple1.txt"
        f = open(fileName, "w+", encoding="utf8")
     
        for sentence in self.final_Sentences:
           if(len(sentence.strip())>0):
               
                   f.write(sentence.strip()+" " + u"\u0964" + " ")


    def tokens_count(self):
        '''done'''
        return len(self.tokens)

    def sentence_count(self):
        '''done'''
        return len(self.sentences)

    def len_text(self):
        '''done'''
        return len(self.text)


    

    def remove_stop_words(self):
        f = codecs.open("stopwords.txt", encoding='utf-8')
        self.final_tokens=[]
        
        stopwords = [x.strip() for x in f.readlines()]
        
        tokens = [i for i in self.tokens if unicode(i) not in stopwords]
        self.final_tokens = tokens
        return tokens

@app.route('/english', methods=['POST'])
def original_text_form_english():
    title = "Summarizer"
    text = request.form['input_text'] #Get text from html
    
    f = open('new.txt', 'wb')
    f.write(text.encode('utf-8'))    
    f.close()
    import lang
    s1=lang.validate(text)
    if s1=="en":    

        
        import che1
        che1.pos_tagging()

        import similarity
        summarize_text=similarity.summarizer()
        


        return render_template("index1.html", title = title, original_text = text, output_summary = summarize_text)
    else:
        return render_template("hello1.html")

#------------Flask Application---------------#

@app.route('/hindi', methods=['POST'])
def original_text_form():
    title = "Summarizer"
    text = request.form['input_text'] #Get text from html
    f = open('input1.txt', 'wb')
    f.write(text.encode('utf-8'))    
    f.close()
    import lang
    s=lang.validate(text)
    if s=="hi":


        for x in range(1):
            str=[]
            t = Tokenizer()
            fileName = "input1.txt"
            t.read_from_file(fileName)
            str=t.generate_sentences()
            #print(str)
            t.tokenize()
                # t.print_tokens(t.final_tokens)
            t.print_finalSentence(x) 

        import hindi_pos_tag_handling_UNK
        hindi_pos_tag_handling_UNK.pos_tagging()

        import hindisummarize2
        summarize_text = hindisummarize2.summarizer()
        


        return render_template("index.html", title = title, original_text = text, output_summary = summarize_text)
    else:
        return render_template("hello.html")
    # @app.route('/')
    # def homepage():
    # 	title = "Text Summarizer"
    # 	return render_template("index.html", title = title)

@app.route('/')
def homepage():
	title = "Text Summarizer"
	return render_template("home.html", title = title)
	
if __name__ == "__main__":
	app.debug = True
	app.run()