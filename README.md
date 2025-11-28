Python Blockchain Ledger Prototype

Project Overview

This project is a functional implementation of a Blockchain data structure in Python. It demonstrates core decentralized concepts including SHA-256 Hashing, Proof-of-Work (PoW) consensus, and Immutable Ledger construction.

This repository was created to demonstrate advanced Version Control Systems (VCS) workflows using Git and GitHub.

Technical Architecture

The system utilizes a linked-list structure where every block contains the cryptographic hash of the previous block, ensuring integrity.

Key Features

Genesis Block Creation: Automatic initialization of the ledger.

Proof of Work: CPU-intensive mining algorithm to validate blocks.

Transaction Buffer: Staging area for pending transfers before mining.

Unit Testing: Included unittest suite for validation.

Git Workflow & Branching Strategy

This project follows the Gitflow Workflow to simulate a professional development environment:

Main: Stable production code.

feat/core-logic: Implementation of the Blockchain class and hashing methods.

test/unit-tests: Implementation of automated testing logic.

fix/difficulty-adjust: Hotfix branch used to demonstrate merge conflict resolution on config.py.

Conflict Resolution Case Study

A merge conflict was intentionally engineered on config.py:

Main Branch set MINING_DIFFICULTY = 5.

Fix Branch set MINING_DIFFICULTY = 2.

Resolution: Manual intervention selected MINING_DIFFICULTY = 4 as the optimal value.

Installation & Usage

Clone the repository

git clone [https://github.com/LusmicSam/python-blockchain-core.git](https://github.com/LusmicSam/python-blockchain-core.git)
cd python-blockchain-core


Run the Blockchain

python src/blockchain.py


Run Tests

python tests/test_blockchain.py


Conclusion

This project demonstrates proficiency in Python programming and advanced Git operations, including branching, merging, and complex conflict resolution.
