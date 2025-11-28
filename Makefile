# Makefile for Python Blockchain
# NOTE: Indentations below MUST be Tabs, not spaces!

.PHONY: run test clean

# Command: make run
# Description: Starts the blockchain node
run:
	python src/blockchain.py

# Command: make test
# Description: Runs the unit test suite
test:
	python tests/test_blockchain.py

# Command: make clean
# Description: Removes annoying __pycache__ folders
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
