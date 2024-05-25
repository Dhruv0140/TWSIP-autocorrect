from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST'])
def spell():
    text = request.form['text']
    corrected_text = spell_checker_module.correct_text(text)
    return render_template('index.html', corrected_text=corrected_text, input_text=text)

# python main
if __name__ == "__main__":
    app.run(debug=True)

# helo i am studeent of engeniering