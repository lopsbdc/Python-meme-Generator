from flask import Flask, render_template
import requests
import json

app = Flask(__name__) #informando que tudo que é necessário, ja está aqui, sem pastas adicionais

#função para usar a api pronta de memes do reddit
def buscar_meme():
    url = "https://meme-api.com/gimme" #link atualizado da API
    response = json.loads(requests.request("GET", url).text) 
    meme = response["preview"][-2] 
    reddit = response["subreddit"] #trazer a fonte do subreddit
    return meme, reddit

#trazendo isso para a Homepage (vulgo "/")
@app.route("/")
def index():
    meme_img,reddit = buscar_meme()
    return render_template("meme_index.html", meme_img=meme_img, reddit=reddit)


app.run(host="0.0.0.0", port=5000)