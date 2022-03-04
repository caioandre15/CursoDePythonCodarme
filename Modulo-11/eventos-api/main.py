from flask import Flask, jsonify, abort, make_response
from evento import Evento
from evento_online import EventoOnline
import json

app = Flask(__name__)

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Rio de Janeiro")
eventos = [ev2_online, ev2_online, ev, ev_online, ev2_online]

@app.route("/") # Mapeamento de rotas
def index():
    return "<h1>Flask configurado com sucesso!!!!</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)

@app.errorhandler(404)
def nao_encontrado(erro):
    # data = {"erro": str(erro)}
    return (jsonify(erro=str(erro)), 404)

@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    for ev in eventos:
        if ev.id == id:
            return jsonify(ev.__dict__)
    abort(404, f"Não encontrei o evento com id: {id}")
    # abort(404, "Evento não encontrado")
    # data = {"erro": f"Não encontrei o evento com id: {id}"}
    # return make_response(jsonify(data), 404)

