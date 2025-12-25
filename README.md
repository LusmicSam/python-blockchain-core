# ⛓️ PyChain: Distributed Ledger & DeFi Prototype

PyChain is a **production-grade implementation of a Blockchain data structure in Python**.  
Unlike toy scripts, this project demonstrates a **full-stack distributed system** featuring:

- Peer-to-peer networking  
- Consensus algorithms (Longest Chain Rule)  
- Cryptographic wallets & transactions  
- Real-time visualization dashboard  
- CI/CD and DevOps automation  

---

## 📸 Project Screenshots

### Streamlit Dashboard
Real-time block visualization, wallet simulation, and mining interface.

![Dashboard](./screenshots/dashboard.png)

### P2P Network Simulation
Left: Node A Mining (Port 5000) | Right: Node B Syncing (Port 5001)

![P2P Sync](./screenshots/p2p_sync.png)

---

## 🏗️ System Architecture

The system is designed as a **distributed network of independent nodes**, each running a Flask API and maintaining a local copy of the ledger.

```mermaid
graph TD
    subgraph "Client Layer"
        User["👤 User"]
        Dash["📊 Streamlit Dashboard"]
        Wallet["🔑 Crypto Wallet"]
    end

    subgraph "Network Layer (Dockerized)"
        NodeA["🖥️ Node A (Port 5000)"]
        NodeB["🖥️ Node B (Port 5001)"]
        NodeC["🖥️ Node C (Port 5002)"]
    end

    subgraph "Core Logic"
        API["Flask API"]
        Consensus["⚔️ Consensus Algorithm"]
        PoW["⛏️ Proof of Work"]
        Chain["🔗 Immutable Ledger"]
    end

    User -->|Views Data| Dash
    User -->|Signs Tx| Wallet
    Wallet -->|POST /transactions/new| API
    Dash -->|Reads State| API
    
    NodeA <-->|P2P Sync| NodeB
    NodeB <-->|P2P Sync| NodeC
    
    API --> Consensus
    Consensus --> Chain
    PoW --> Chain
```

---

## 💸 Transaction Lifecycle

How a financial transaction flows from a wallet into the immutable ledger.

```mermaid
sequenceDiagram
    participant U as User (Wallet)
    participant N1 as Node A
    participant N2 as Node B
    participant BC as Blockchain

    U->>U: Sign Transaction (ECDSA)
    U->>N1: POST /transactions/new
    
    Note over N1: Verify Signature & Balance
    
    alt Valid Transaction
        N1->>BC: Add to Mempool
        N1-->>U: 201 Created
    else Invalid Transaction
        N1-->>U: 403 Forbidden
    end

    Note over N1: Miner Solves Proof of Work
    N1->>BC: Forge New Block
    
    N2->>N1: GET /chain
    N2->>N2: Replace Chain (If Longer)
```

---

## 🚀 Key Features

### P2P Consensus Engine
Implements the **Longest Chain Rule** to resolve conflicts between distributed nodes.

### Cryptographic Security
Uses **ECDSA (SECP256k1)** for wallet generation and transaction signing (same curve as Bitcoin).

### DevOps Pipeline
Fully automated **CI/CD** using **GitHub Actions** and **Docker containerization**.

### Interactive UI
Real-time visualization of blocks, transactions, and mining operations using **Streamlit**.

---

## 🛠️ Tech Stack

| Component  | Technology     | Description                       |
|------------|----------------|-----------------------------------|
| Core Logic | Python 3.10    | SHA-256 hashing, OOP architecture |
| API        | Flask          | RESTful P2P communication         |
| Frontend   | Streamlit      | Reactive web dashboard            |
| Security   | ECDSA          | Elliptic Curve Digital Signatures |
| DevOps     | Docker         | Containerized deployment          |
| Automation | GNU Make       | Task abstraction                  |
| CI/CD      | GitHub Actions | Automated linting & unit testing  |

---

## ⚙️ Installation & Usage

### Option A: Quick Start (Docker) — **Recommended**

Run the entire stack (API + Dashboard) using Docker.

```bash
docker-compose up --build
```

**Services:**

- 📊 Dashboard: [http://localhost:8501](http://localhost:8501)
- 🔗 API Node: [http://localhost:5000](http://localhost:5000)

---

### Option B: Manual Setup (Local)

#### Prerequisites

- Python **3.10+**
- pip package manager

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Flask API

```bash
python src/api.py 5000
```

#### Launch Dashboard

```bash
streamlit run src/dashboard.py
```

---

## 🌿 Gitflow Strategy

This repository follows **strict Gitflow conventions**, showcasing feature isolation, structured merges, and release tagging.

---

## 📸 Git Workflow & Troubleshooting Log

This log documents the Git operations performed during the project's development, illustrating the workflow from initialization to deployment and detailing how merge conflicts were resolved.

### 1. Project Initialization
We started by initializing the repository in Git Bash and making the initial commit to set up the project foundation.
![Initialization](./screenshots/initialize.png)

### 2. Feature Branching & Merging
To work on new features in isolation, we created separate branches. Once the features were ready, we successfully merged them back into the `main` branch.
![Simple Merge](./screenshots/mergedsimple.png)

### 3. Handling & Resolving Merge Conflicts
**The Problem:** A merge conflict occurred when trying to merge a branch that had competing changes in the same file as `main`. Git Bash alerted us to the conflict.
![Conflict Warning](./screenshots/conflict.png)

**Investigation:** We checked the status and examined the conflicting file to identify the specific lines causing the issue.
![Conflict Details](./screenshots/conflictsshow.png)

**The Resolution:** We manually resolved the conflict by editing the code to keep the desired changes and removing the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then committed the resolved file.
![Conflict Fixed](./screenshots/conflictfixed.png)

### 4. CI/CD Verification
After pushing the resolved changes, GitHub Actions automatically ran our CI/CD pipeline to verify that the build and tests passed.
![GitHub Actions](./screenshots/actions.png)

### 5. Docker Deployment
With the code verified, we used Docker Compose to build and launch the application containers.
![Docker Run](./screenshots/docker.png)

### 📜 Git Commands Used

The following commands were used to manage the project workflow:

```bash
# 1. Initialization
git init
git add .
git commit -m "Initial commit"

# 2. Inspecting Status & History
git status                     # Check the state of changes
git log                        # Show commit history
git log --oneline              # Show simplified history
git log --graph --oneline --decorate --all  # Visualize branch topology

# 3. Working with Branches
git checkout -b <branch-name>  # Create and switch to a new branch
git branch                     # List local branches
git checkout main              # Switch back to the main branch

# 4. Merging, Tagging & Syncing
git merge <branch-name>        # Merge a branch into the current branch
git tag -a v1.0.0 -m "v1.0"    # Create a version tag
git push origin main           # Push changes to remote
git push --tags                # Push tags to remote

# 5. Resolving Conflicts
# After a merge conflict occurs:
git status                     # Identify conflicted files
# ... manual edit to fix files ...
git add <file>                 # Stage the resolved file
git commit                     # Commit the resolution
```

---

## 📡 API Endpoints

| Method | Endpoint            | Description                           |
|--------|---------------------|---------------------------------------|
| GET    | `/mine`             | Calculates PoW and forges a new block |
| POST   | `/transactions/new` | Submits a signed transaction          |
| GET    | `/chain`            | Returns the full blockchain           |
| POST   | `/nodes/register`   | Registers a new node                  |
| GET    | `/nodes/resolve`    | Triggers the consensus algorithm      |

---

## 📂 Project Structure

```
.github/
    └── workflows/
        └── python-app.yml
screenshots/
    ├── dashboard.png
    └── p2p_sync.png
src/
    ├── __pycache__/
    ├── api.py
    ├── blockchain.py
    ├── dashboard.py
    └── wallet.py
tests/
    └── test_blockchain.py
.gitignore
config.py
docker-compose.yml
Dockerfile
Makefile
README.md
requirements.txt
```

---

## 🧪 Testing

Run the test suite to verify core functionality:

```bash
# Run all tests
make test

# Run with coverage report
pytest --cov=src tests/
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feat/amazing-feature
   ```
3. Commit your changes
   ```bash
   git commit -m "feat: add amazing feature"
   ```
4. Push to branch
   ```bash
   git push origin feat/amazing-feature
   ```
5. Open a Pull Request

Please ensure your code passes all tests and follows the project's coding style.

---

## 📄 License

Distributed under the **MIT License**.  
See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- Inspired by Satoshi Nakamoto's Bitcoin whitepaper
- Built with modern Python best practices
- Special thanks to the open-source community

---

**⭐ Star this repo if you find it useful!**
