from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    englishText = request.args.get('textToTranslate')
    frenchText = translator.english_to_french(englishText)
    return "French Translated Text: "+frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    frenchText = request.args.get('textToTranslate')
    englishText = translator.french_to_english(frenchText)
    return "English Translated Text: "+englishText

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
