from flask import Flask, render_template, request
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary = PyDictionary()

@app.route('/', methods=['GET', 'POST'])
def index():
    meaning = None
    synonyms = None
    antonyms = None
    word = None
    error = None

    if request.method == 'POST':
        word = request.form['word']
        try:
            meaning = dictionary.meaning(word)
            synonyms = dictionary.synonym(word)
            antonyms = dictionary.antonym(word)
            
            if not meaning:
                error = f"No results found for '{word}'"
        except Exception as e:
            error = str(e)

    return render_template('index.html', meaning=meaning, synonyms=synonyms, antonyms=antonyms, word=word, error=error)

if __name__ == '__main__':
    app.run(debug=True)
