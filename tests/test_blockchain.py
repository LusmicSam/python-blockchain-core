import unittest
import sys
import os

# Add src to path so we can import blockchain
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain()

    def test_genesis_block(self):
        # Ensure the chain starts with 1 block (Genesis)
        self.assertEqual(len(self.bc.chain), 1)

    def test_new_transaction(self):
        # Test adding a transaction
        index = self.bc.new_transaction("UserA", "UserB", 100)
        self.assertEqual(len(self.bc.pending_transactions), 1)
        self.assertEqual(self.bc.pending_transactions[0]['amount'], 100)

    def test_hashing_integrity(self):
        # Ensure hashing returns a string
        block = self.bc.last_block
        block_hash = self.bc.hash(block)
        self.assertTrue(isinstance(block_hash, str))
        self.assertEqual(len(block_hash), 64) # SHA256 is 64 chars

if __name__ == '__main__':
    unittest.main()
