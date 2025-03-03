import hashlib
import json
import time
from database import store_block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block(transaction="Genesis Block", previous_hash="0")
        self.chain.append(genesis_block)
        store_block(genesis_block)

    def create_block(self, transaction, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transaction': transaction,
            'previous_hash': previous_hash,
            'hash': self.compute_hash(transaction, previous_hash)
        }
        return block

    def compute_hash(self, transaction, previous_hash):
        block_string = json.dumps({"transaction": transaction, "previous_hash": previous_hash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, transaction):
        previous_block = self.chain[-1]
        new_block = self.create_block(transaction, previous_block['hash'])
        self.chain.append(new_block)
        store_block(new_block)

# Create blockchain instance
bc = Blockchain()
