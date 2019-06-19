import nltk
import re
from nltk.tag import tnt
from nltk.corpus import indian
from googletrans import Translator

def pos_tagging():
    translator = Translator()
    sentence_id = 0

    file1 = open("simple1.txt", "r",encoding='utf-8')
    text =" ".join(file1.readlines())

    model_path = "hindi.pos" #Copy hindi.pos from NLTK corpus

    def train_hindi_model(model_path):
        train_data = indian.tagged_sents(model_path)
        tnt_pos_tagger = tnt.TnT()
        tnt_pos_tagger.train(train_data)
        return tnt_pos_tagger


    def get_sentId(model_path):
        ids = re.compile('<Sentence\sid=\d+>')
        with open(model_path, "r+",encoding='utf-8') as temp_f:
            content = temp_f.readlines()
            for i in content:
                id_found = (ids.findall(i))
                if id_found:
                    id_found = str(id_found).replace("['<Sentence id=", "").replace(">']", "")
                    id = int(id_found)
        id = id + 1
        return id


    def tag_words(model,text):
        tagged = (model.tag(nltk.word_tokenize(text)))
        return tagged


    def handle_UNK(tagged_words, model_path, sentence_id):
        with open(model_path, "r+",encoding='utf-8') as f1:
            result_list = []
            for nep_word, tag in tagged_words:
                if tag == "Unk":
                    x = translator.translate(nep_word)
                    if x is not None:
                        str1 = str(x)
                        new_str = str1.split()
                        for j in new_str:
                            if re.search('^text=', j, re.I):
                                word = j.replace("text=", ",").replace(",", "")
                                word = str(word)
                                # pos=nltk.pos_tag(word)
                                pos = nltk.tag.pos_tag([word])
                                # print (i, pos)
                                for en_word, tag in pos:
                                    result = nep_word + "_" + (tag) + " "
                                    result_list.append(result)

                else:
                    result = nep_word + "_" + (tag) + " "
                    result_list.append(result)

            writing_word = str("\n<Sentence id=") + str(sentence_id) + ">\n"
            output = writing_word + "".join(result_list) + "\n</Sentence>\n</Corpora>"
            for line in f1.readlines():
                f1.write(line.replace("</Corpora>", ""))
            f1.write(output)
            return(result_list)


    sentence_id = (get_sentId(model_path))
    #print (sentence_id)

    model = train_hindi_model(model_path)
    tagged_words = tag_words(model,text)

    #print ("=================================Tagged words=================================\n",tagged_words,"\n")

    r_list=handle_UNK(tagged_words,model_path,sentence_id)
    #print(r_list)

    #retrain the model
    model = train_hindi_model(model_path)
    new_tagged_words =  tag_words(model,text)
    #print ("=================================New Tagged words=================================\n",new_tagged_words,"\n")

    with open("output.txt","a",encoding='utf-8') as output_file:
        output_file.write(str(r_list))

    r_list1=[]
    for i in r_list:
        r_list1.append(i.split('_'))
    #print(r_list1)
    #print("\n")
    no_punct=[]
    for i in r_list1:
        if i[1]=='PUNC':
            continue
        else:
            no_punct.append(i)


    suffixes = { 
                1: ["ो", "े", "ू", "ु", "ी", "ि", "ा","ता"],  
                2: ["ल","ड","न","कर","एं","स","में","क","तृ","ान","ैत","ने","ाऊ","ाव", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती","गी",
                    "ता","गा","ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा","ित","ीन","लु","यत","वट","लू"],     
                3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक",
                    "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन",
                    "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं","एं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार",
                    "गार", "दान","खोर"],     
                4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", 
                    "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां",
                    "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
                5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
            }

    final=[]
    for nep_word, tag in no_punct:
        if tag.startswith('R'):
            for L in 5,4,3,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 

        elif tag.startswith("PRP"):
            for L in 1,3:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 

        elif tag.startswith("JJ"):
            for L in 5,3,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L])                       

        elif tag.startswith("VA") or tag.startswith("VF"):
            for L in 5,4,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 
    
        elif (tag=='VB' or tag=='VBG'):
            final.append(nep_word)

        elif tag.startswith('VBN'):
            for L in 5,4,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 
        
        elif tag.startswith('VJ'):
            for L in 5,4,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 
    
        elif tag.startswith('VNN'):
            for L in 2,3:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 
    

        elif tag.startswith("NNS") or tag.startswith("NNPS"):
            for L in 5,4,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 

        elif tag.startswith('MD'):
            for L in 5,4,3,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 

        elif tag.startswith('VRB'):
            for L in 5,4,3,2:
                if len(nep_word) > L + 1:
                    for suf in suffixes[L]:
                        if nep_word.endswith(suf):
                            final.append(nep_word[:-L]) 
                    

        elif tag.startswith('PREP'):
            final.append(nep_word)

        else:
            final.append(nep_word)
                            
    listToStr = ' '.join([str(elem) for elem in final])  


            

    with open('tokenized2.txt', 'a',encoding='utf-8') as f:
                f.write("%s" %listToStr)           
                
                    
                    

    with open("tokenized1.txt","a",encoding='utf-8') as output_file:
        
        
        output_file.write(str(final)) 
        return()
