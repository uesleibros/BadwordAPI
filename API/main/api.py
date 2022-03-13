from __main__ import app
from utils.censor import censor
from flask import jsonify, request
from bs4 import BeautifulSoup
import requests

@app.route('/badwords')
def xingamentos():

  badwords = [] # <- Lista de palavrões.
  bwJson = [] # <- Armazena o JSON.
  
  lang = request.args.get("lang", default="pt-br")

  if lang == "pt-br":
    url = 'https://aprenderpalavras.com/lista-de-palavroes-xingamentos-e-girias/'
    r = requests.Session().get(url)
    soup = BeautifulSoup(
        r.content, 'lxml'
    )  # <- O parser (LXML) é mais rápido que o (html.parser ou http.parser).
    
    for bw in soup.find_all("ul")[7].find_all("li"): # <- Pegamos todos os <li> da página.
        if bw.string == 'Ot-ria':
          badwords.append('Otária')
        elif bw.string == 'Ot-rio':
          badwords.append('Otário')
        else:
          badwords.append(bw.string)
    
    for lis in badwords:
      bwJson.append({"word": lis.lower(), "bypasses": []})

    for index, u in enumerate(bwJson):
      for i in censor(u["word"]):
          bwJson[index]["bypasses"].append(i)
        #bwJson[index]["bypasses"].append(ix)
	
    return jsonify(bwJson)

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
      bwJson.append({"word": lis, "bypasses": []})

    for index, u in enumerate(bwJson):
      for i in censor(u["word"]):
        if i != "no":
          bwJson[index]["bypasses"].append(i)

    return jsonify(bwJson)