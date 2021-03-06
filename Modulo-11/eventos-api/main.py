from flask import Flask, jsonify, abort, make_response, request, json
from evento import Evento
from evento_online import EventoOnline

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

@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    # Parsing
    data = json.loads(request.data)  
    nome = data.get("nome")
    local = data.get("local")

    # Validação
    if not nome:
        abort(400, "'nome' precisa ser informado!")

    # Criando Evento
    if local:
        evento = Evento(nome=nome, local=local)
    else:
        evento = EventoOnline(nome=nome)
    eventos.append(evento)
    # json.dumps dict => json
    # json.loads(json) = > dict
    return {
        "id": evento.id,
        "url": f"/api/eventos/{evento.id}/"
    }

@app.errorhandler(400)
def nao_encontrado(erro):
    # data = {"erro": str(erro)}
    return (jsonify(erro=str(erro)), 400)

@app.errorhandler(404)
def nao_encontrado(erro):
    # data = {"erro": str(erro)}
    return (jsonify(erro=str(erro)), 404)

def get_evento_or_404(id):
    for ev in eventos:
        if ev.id == id:
            return ev
    abort("404", "Evento não encontrado")


@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    ev = get_evento_or_404(id)
    return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
    ev = get_evento_or_404(id)
    eventos.remove(ev)
    return jsonify(id=id)

@app.route("/api/eventos/<int:id>/", methods=["PUT"])
def editar_evento(id):
    
    # Parsing
    data = request.get_json()  
    nome = data.get("nome")
    local = data.get("local")

    # Validação
    if not nome:
        abort(400, "'nome' precisa ser informado!")
    if not local:
        abort(400, "'local' precisa ser informado!")

    ev = get_evento_or_404(id)
    ev.nome = nome
    ev.local = local
        
    return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/", methods=["PATCH"])
def editar_evento_parcial(id):

    # Parsing
    data = request.get_json()  
    
    ev = get_evento_or_404(id)
    # Validação
    if "nome" in data.keys():
        nome = data.get("nome")
        if not nome:
            abort(400, "'nome' precisa ser informado!")
        ev.nome = nome
    if "local" in data.keys():
        local = data.get("local")
        if not local:
            abort(400, "'local' precisa ser informado!")
        ev.local = local
        
    return jsonify(ev.__dict__)

    # abort(404, "Evento não encontrado")
    # data = {"erro": f"Não encontrei o evento com id: {id}"}
    # return make_response(jsonify(data), 404)

