from flask import Flask

app = Flask(__name__)

@app.route("/") # Mapeamento de rotas
def index():
    return "<h1>Flask configurado com sucesso!</h1>"