from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/templates', methods=['POST'])
def original_text_form():
    title = "Summarizer"
    text = request.form['input_text'] #Get text from html
    f = open('input1.txt', 'wb')
    f.write(text.encode('utf-8'))    
    f.close()

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

if __name__ =='__main__':
    app.run(debug = True)
    