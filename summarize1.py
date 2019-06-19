import codecs
import re
from nltk.corpus import stopwords 
from numpy import unicode
from flask import Flask, render_template, request #Used to render .html templates



#------------Flask Application---------------#

app = Flask(__name__)
@app.route('/english', methods=['POST'])
def original_text_form():
    title = "Summarizer"
    text = request.form['input_text'] #Get text from html
    f = open('new.txt', 'wb')
    f.write(text.encode('utf-8'))    
    f.close()
    

    
    import che1
    che1.pos_tagging()

    import similarity
    summarize_text=similarity.summarizer()
    


    return render_template("index1.html", title = title, original_text = text, output_summary = summarize_text)
@app.route('/')
def homepage():
	title = "Text Summarizer"
	return render_template("index1.html", title = title)
	
if __name__ == "__main__":
	app.debug = True
	app.run()