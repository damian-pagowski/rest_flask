from flask import Flask, jsonify, request

from flask_cors import CORS


# Organize API Endpoints
# Handle Cross-Origin Resource Sharing (CORS)
# Parse the request path and body
# Use POST, PATCH, and DELETE requests in Flask
# Handle errors


# REST Principles
# Should be intuitive
# Organize by resource
# Use nouns in the path, not verbs (!!!)
# The method used will determine the operation taken
# GOOD:
# https://example.com/posts
# BAD:
# https://example.com/get_posts
# Keep a consistent scheme
# Plural nouns for collections
# Use parameters to specify a specific item
# GOOD:
# https://example.com/entrees
# https://example.com/entrees/5
# BAD:
# https://example.com/entree
# https://example.com/entree_five
# Don’t make them too complex or lengthy
# No longer than collection/item/collection
# GOOD:
# https://example.com/entrees/5/reviews
# BAD:
# https://example.com/entrees/5/customers/4/reviews

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
    return jsonify({'message': 'Book %d' % book_id})

# query parem usage
@app.route('/query', methods=['GET'])
def get_entrees():
    page = request.args.get('page', 1, type=int)
    return jsonify({'message': 'Page %d' % page})


# in decorator, there is status code argument
#   error code should be also returned to response
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404
