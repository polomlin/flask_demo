# -*- coding:utf8 -*-

'''
Created on Jun 15, 2016

@author: sam

sudo apt-get install libssl-dev
sudo apt-get install libffi-dev
sudo pip install pyopenssl
sudo pip install --upgrade pyopenssl
sudo pip install cryptography
'''


from flask import Flask
from flask import jsonify
from firebase import firebase
from flask import request
from flask import make_response
from OpenSSL import SSL

app = Flask(__name__)

__VERSION = 'v0.1'
__RESTFUL_VERSION = '/fevolution/api/'+ __VERSION +'/'

message = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

"""
    Following function only for single by single
"""
@app.route(__RESTFUL_VERSION + 'get_message', methods=['GET'])
def get_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'put_message', methods=['PUT'])
def put_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'post_message', methods=['POST'])
def post_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'delete_message', methods=['DELETE'])
def delete_message():
    return jsonify({'message': message})

"""
    Following function only for room by room
"""
@app.route(__RESTFUL_VERSION + 'get_room_message', methods=['GET'])
def get_room_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'put_room_message', methods=['PUT'])
def put_room_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'post_room_message', methods=['POST'])
def post_room_message():
    return jsonify({'message': message})

@app.route(__RESTFUL_VERSION + 'delete_room_message', methods=['DELETE'])
def delete_room_message():
    return jsonify({'message': message})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, % s!</h1>' % name



if __name__ == '__main__':
    #context = SSL.Context(SSL.TLSv1_2_METHOD)
    #context.use_privatekey_file('/home/sam/Documents/ssl_key/ca.key')
    #context.use_certificate_file('/home/sam/Documents/ssl_key/ca.crt')
    context = ('/home/sam/Documents/ssl_key/ca.crt', '/home/sam/Documents/ssl_key/ca.key')
    app.run(host='127.0.0.1', port=8080, ssl_context=context, debug=True)
