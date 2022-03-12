#----------------
#   INSTRUÇÕES
#----------------
# -> Escolher site para Web Scrapping
# -> Pegar dados e adicionar ao Array
# -> Converter para JSON
# -> Criar rota (FLASK)
# -> Retorna JSON
# -> Query Parameters (?lang) | Suporte: pt/en

from bs4 import BeautifulSoup
import lxml
import json
from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='API')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False

from API.main import api

@app.get('/')
def Main():
  return render_template('docs.html')

#vai pra pasta API/main/api.py

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, use_reloader=False)

#https://BadWordAPI.uesleidev.repl.co

# Agora, vamos adicionar línguas.
# Vai ser complicado por conta de gírias