
```python
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conectar-se ao MongoDB
uri = 'mongodb://root:mongo@localhost:27017/'
client = MongoClient(uri)
database = client['AulaDemo']
collection = database['Estudantes']

@app.route('/inserir', methods=['POST'])
def inserir():
    data = request.json
    try:
        collection.insert_one(data)
        return jsonify({"message": "Registro inserido com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ler', methods=['GET'])
def ler():
    try:
        resultados = list(collection.find())
        return jsonify(resultados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/buscar', methods=['GET'])
def buscar():
    field = request.args.get('field')
    op = request.args.get('op')
    value = request.args.get('value')
    try:
        resultados = list(collection.find({field: {op: value}}))
        return jsonify(resultados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/atualizar', methods=['PUT'])
def atualizar():
    try:
        collection.update_many({'idade': 18}, {'$set': {'idade': 'dezoito'}})
        return jsonify({"message": "Registros atualizados com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deletar', methods=['DELETE'])
def deletar():
    try:
        collection.delete_many({'idade': {'$lt': 18}})
        return jsonify({"message": "Registros excluídos com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```