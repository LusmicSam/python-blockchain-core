import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

# OPTIMIZATION EXPERIMENT: PENDING REVIEW
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.nodes = set()
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount, signature=None):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount to send
        :param signature: (Optional) <str> Digital signature of the transaction
        :return: <int> Index of the block this transaction will be added to
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
        if signature:
            transaction['signature'] = signature
        
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - p is the previous proof, and p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest valid chain in the network.
        :return: <bool> True if our chain was replaced, False if not
        """
        longest_chain = None
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in self.nodes:
            try:
                response = requests.get(f'http://{node}/chain')
                if response.status_code == 200:
                    length = response.json()['length']
                    chain = response.json()['chain']
                    
                    # Check if the length is longer and the chain is valid
                    if length > max_length and self.valid_chain(chain):
                        max_length = length
                        longest_chain = chain
            except:
                continue

        # Replace our chain if we discovered a valid chain longer than ours
        if longest_chain:
            self.chain = longest_chain
            return True

        return False

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            # Check that the previous hash matches
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1

        return True

# Main execution for demonstration
if __name__ == "__main__":
    print("--- Blockchain Initialized ---")
    blockchain = Blockchain()
    
    print("Mining a block...")
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    
    blockchain.new_transaction(sender="Alice", recipient="Bob", amount=50)
    
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    
    print(f"Chain Data: {json.dumps(blockchain.chain, indent=2)}")
