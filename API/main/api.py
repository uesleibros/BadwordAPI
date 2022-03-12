from __main__ import app
from flask import jsonify, request
from bs4 import BeautifulSoup
import requests

@app.route('/badwords')
def xingamentos():

  lang = request.args.get("lang", default="pt-br")

  if lang == "pt-br":
    url = 'https://aprenderpalavras.com/lista-de-palavroes-xingamentos-e-girias/'
    r = requests.Session().get(url)
    soup = BeautifulSoup(
        r.content, 'lxml'
    )  # <- O parser (LXML) é mais rápido que o (html.parser ou http.parser)
    
    badwords = []
    bwJson = []
    
    for bw in soup.find_all("ul")[7].find_all("li"):
        if bw.string == 'Ot-ria':
            badwords.append('Otária')
    
        elif bw.string == 'Ot-rio':
            badwords.append('Otário')
    		
        else:
            badwords.append(bw.string)
    
    for lis in badwords:
        bwJson.append({"badword": lis})

  if lang == "en":
    url = "https://www.joe.co.uk/life/a-definitive-ranking-of-every-swear-word-from-worst-to-best-122544"
    r = requests.Session().get(url)
    soup = BeautifulSoup(
        r.content, 'lxml'
    )  # <- O parser (LXML) é mais rápido que o (html.parser ou http.parser)
    badwords = []
    bwJson = []
    for bw in soup.find_all("strong"):
      if "Search" not in bw.string:
        if "Oh fuck off." not in bw.string:
          badwords.append(bw.string.split(".", 1)[1].strip())
          
    for lis in badwords:
        bwJson.append({"badword": lis})

  return jsonify(bwJson)