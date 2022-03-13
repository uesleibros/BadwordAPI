#----------------
#   INSTRUÇÕES (CRIAR A API)
#----------------
# -> Escolher site para Web Scrapping
# -> Pegar dados e adicionar ao Array
# -> Converter para JSON
# -> Criar rota (FLASK)
# -> Retorna JSON
# -> Query Parameters (?lang) | Suporte: pt/en

from flask import Flask, render_template, url_for
from werkzeug.serving import run_simple
import threading

app = Flask(__name__, template_folder='public')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
app.static_folder = 'static'

from API.main import api

@app.get('/')
def Main():
  return render_template('docs.html') # <- Renderiza o arquivo docs.html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, threaded=True)
    run_simple("localhost", 2222, app, use_reloader=True)