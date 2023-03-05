from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
personagens = [
    {
        'id': 1,
        'nome': 'Ana',
        'funcao': 'Suporte',
        'counter': ['reaper']
    },
    {
        'id': 2,
        'nome': 'Baptiste',
        'funcao': 'Suporte',
        'counter': ['brigitte']
    },
    {
        'id': 3,
        'nome': 'Brigitte',
        'funcao': 'Suporte',
        'counter': ['genji']
    }
]

@app.route('/', methods=['GET'])
def home():
    return "Bem vindo a API Overwatch 2"

@app.route('/personagens', methods=['GET'])
def obter_personagens():
    return jsonify(personagens)

@app.route('/personagens/<nome>', methods=['GET'])
def obter_personagens_por_nome(nome):
    for personagem in personagens:
        if personagem.get('nome').lower() == nome.lower():
            return jsonify(personagem)

@app.route('/personagens/<int:id>', methods=['GET'])
def obter_personagens_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem)

@app.route('/personagens/<nome>/counter', methods=['GET'])
def obter_counter_do_personagem_por_nome(nome):
    for personagem in personagens:
        if personagem.get('nome').lower() == nome.lower():
            return jsonify(personagem.get('counter'))

@app.route('/personagens/<int:id>/counter', methods=['GET'])
def obter_counter_do_personagen_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem.get('counter'))

app.run(port=5001, host='localhost', debug=True)