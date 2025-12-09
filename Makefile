# Makefile for Python Blockchain
# NOTE: Indentations below MUST be Tabs, not spaces!

.PHONY: run test clean node1 node2 dashboard

# Command: make run
# Description: Starts the blockchain node on default port
run:
	python src/api.py 5000

# Command: make node1
# Description: Starts Node 1 (Port 5000)
node1:
	python src/api.py 5000

# Command: make node2
# Description: Starts Node 2 (Port 5001) - The Peer Node
node2:
	python src/api.py 5001

# Command: make test
# Description: Runs the unit test suite
test:
	python tests/test_blockchain.py

# Command: make dashboard
# Description: Launches the Web UI
dashboard:
	streamlit run src/dashboard.py

# Command: make clean
# Description: Removes annoying __pycache__ folders
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
