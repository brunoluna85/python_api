from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# Abre o arquivo JSON para leitura
with open('./entire_json.json', 'r') as json_file:
    all_data = json.load(json_file)
with open('./location.json', 'r') as json_file:
    one_location = json.load(json_file)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Overwatch 2 API"

@app.route('/locations', methods=['GET'])
def get_entire_json():
    return all_data

@app.route('/locations/first_location', methods=['GET'])
def get_specific_location():
    return one_location
    

app.run(port=5001, host='localhost', debug=True)