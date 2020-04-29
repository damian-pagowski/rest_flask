from flask import Flask, jsonify, request

from flask_cors import CORS

# init Flask
app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)
CORS(app)


@app.route('/hello')
def get_greeting():
    return jsonify({'message': 'Hello, World!'})


@app.route('/hi', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        return jsonify({'message': 'Hello CREATED'})
    else:
        return jsonify({'message': 'Hello!'})

# path params usage
# method argument + <> in route path
@app.route('/books/<int:book_id>')
def retrieve_book(book_id):
    return jsonify({'message': 'Book %d' % book_id })

# query parem usage
@app.route('/query', methods=['GET'])
def get_entrees():
    page = request.args.get('page', 1, type=int)
    return jsonify({'message': 'Page %d' % page })
