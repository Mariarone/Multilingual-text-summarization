import codecs
import re

from numpy import unicode


class Tokenizer():
    '''class for tokenizer'''

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
        text = re.sub(r'(\d+)', r'', text)
        text = text.replace('\n', '')
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
            print(self.tokens)
            # remove words containing spaces
            self.remove_only_space_words()
            # remove hyphenated words
            self.hyphenated_tokens()
            t.generate_stem_dict()
            t.remove_stop_words()
            t.formSentence()
    def print_tokens(self, print_list=None):
        '''done'''
        if print_list is None:
            for i in self.tokens:
                print(i)
        else:
            for i in print_list:
                print(i)

    def formSentence(self):
        finalSentence=""
        for word in self.final_tokens:
            finalSentence +=word+" "
         
        self.final_Sentences.append(finalSentence)
        print(self.final_Sentences)
    def print_finalSentence(self, x):
        fileName = "tokenized.txt"
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


    def generate_stem_words(self, word):
        suffixes = {
           # 1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],  
            2: ["तृ","ान","ैत","ने","ाऊ","ाव","कर", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती",
                "ता", "ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा","ित","ीन","लु","यत","वट","लू"],     
            3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक",
                "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन",
                "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार",
                "गार", "दान","खोर"],     
            4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", 
                "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां",
                "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
            5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
        }
        for L in  5,4, 3, 2, :
            if len(word) > L + 1:
                for suf in suffixes[L]:
                    # print type(suf),type(word),word,suf
                    if word.endswith(suf):
                        # print 'h'
                        return word[:-L]
        return word

    def generate_stem_dict(self):
    

        stem_word = {}
        self.stemmed_word = []
        # if not self.tokens:
        #     self.tokenize()
        for each_token in self.tokens:
            # print type(each_token)
            temp = self.generate_stem_words(each_token)
            # print temp
            stem_word[each_token] = temp
            
            self.stemmed_word.append(temp)
        
        return stem_word

    def remove_stop_words(self):
        f = codecs.open("stopwords.txt", encoding='utf-8')
        self.final_tokens=[]
        # if not self.stemmed_word:
        #     self.generate_stem_dict()
        stopwords = [x.strip() for x in f.readlines()]
        # stopwords = []
        tokens = [i for i in self.stemmed_word if unicode(i) not in stopwords]
        self.final_tokens = tokens
        return tokens


if __name__ == "__main__":
    for x in range(1):
        str=[]
        t = Tokenizer()
        
        fileName = "input1.txt"

        t.read_from_file(fileName)
        str=t.generate_sentences()
        print(str)
        t.tokenize()
        # t.print_tokens(t.final_tokens)
t.print_finalSentence(x)