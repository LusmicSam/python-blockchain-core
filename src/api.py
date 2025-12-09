import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
import sys

# Import the Blockchain class
from blockchain import Blockchain

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

@app.route('/nodes/register', methods=['POST'])

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    return jsonify(response), 201

def consensus():
    # This asks neighboring nodes for their chains and replaces ours if theirs is longer
    if replaced:
        response = {
            'message': 'Our chain was replaced',
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

if __name__ == '__main__':
    # Allows running on different ports: python src/api.py 5001
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)    return jsonify(response), 200
            'new_chain': blockchain.chain
        }
    replaced = blockchain.resolve_conflicts()

@app.route('/nodes/resolve', methods=['GET'])
        'total_nodes': list(blockchain.nodes),
    }
    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
    values = request.get_json()
def register_nodes():
    }
    return jsonify(response), 200

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
        'length': len(blockchain.chain),
    response = {
        'chain': blockchain.chain,
    block = blockchain.new_block(proof, previous_hash)

def full_chain():
    response = {
@app.route('/chain', methods=['GET'])
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],

        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
        return jsonify({'message': 'Invalid Transaction (Signature Fail)'}), 403
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
    else:
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201
    # Create a new Transaction
    signature = values.get('signature') 
