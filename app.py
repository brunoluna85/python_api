from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
characters = [
    {
        'id': 1,
        'name': 'Ana',
        'role': 'Support',
        'counter': ['reaper']
    },
    {
        'id': 2,
        'name': 'Baptiste',
        'role': 'Support',
        'counter': ['brigitte']
    },
    {
        'id': 3,
        'name': 'Brigitte',
        'role': 'Support',
        'counter': ['genji']
    }
]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Overwatch 2 API"

@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(characters)

@app.route('/characters/<name>', methods=['GET'])
def get_characters_by_name(name):
    for char in characters:
        if char.get('name').lower() == name.lower():
            return jsonify(char)

@app.route('/characters/<int:id>', methods=['GET'])
def get_characters_by_id(id):
    for char in characters:
        if char.get('id') == id:
            return jsonify(char)

@app.route('/characters/<name>/counter', methods=['GET'])
def get_character_counter_by_name(name):
    for char in characters:
        if char.get('name').lower() == name.lower():
            return jsonify(char.get('counter'))

@app.route('/characters/<int:id>/counter', methods=['GET'])
def get_character_counter_by_id(id):
    for char in characters:
        if char.get('id') == id:
            return jsonify(char.get('counter'))

app.run(port=5001, host='localhost', debug=True)