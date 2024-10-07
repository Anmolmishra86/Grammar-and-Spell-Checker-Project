from flask import Flask, request, render_template
from models import SpellChecker

app = Flask(__name__)
spell_checker = SpellChecker()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/spell', methods=['POST'])
def spell_check():
    text = request.form['text']
    corrected_text = spell_checker.correct_spell(text)
    corrected_grammar = spell_checker.correct_grammar(text, corrected_text)
    return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)


@app.route('/grammar', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return render_template('index.html', corrected_file_text='', corrected_file_grammar=[])

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', corrected_file_text='', corrected_file_grammar=[])

    text = file.read().decode('utf-8')
    corrected_text = spell_checker.correct_spell(text)
    corrected_grammar = spell_checker.correct_grammar(text, corrected_text)

    return render_template('index.html', corrected_file_text=corrected_text, corrected_file_grammar=corrected_grammar)


if __name__ == '__main__':
    app.run(debug=True)
