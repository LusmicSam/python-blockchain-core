import streamlit as st
import pandas as pd
from time import time
from blockchain import Blockchain

# Page Configuration
st.set_page_config(
    page_title="PyChain Network",
    page_icon="⛓️",
    layout="wide"
)

# --- SESSION STATE MANAGEMENT ---
# This ensures the blockchain persists between clicks
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

bc = st.session_state.blockchain

# --- SIDEBAR (Wallet Simulation) ---
st.sidebar.title("💰 Wallet Simulator")
sender = st.sidebar.text_input("Sender Address", "Alice_0x1")
receiver = st.sidebar.text_input("Receiver Address", "Bob_0x2")
amount = st.sidebar.number_input("Amount", min_value=1, value=50)

if st.sidebar.button("Broadcast Transaction"):
    index = bc.new_transaction(sender, receiver, amount)
    st.sidebar.success(f"Transaction added to Block #{index}")

# --- MAIN DASHBOARD ---
st.title("⛓️ PyChain Block Explorer")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Current Block Height", value=len(bc.chain))
with col2:
    st.metric(label="Pending Transactions", value=len(bc.pending_transactions))
with col3:
    st.metric(label="Difficulty Level", value=4) # Static for now

# --- ACTION CENTER ---
st.divider()
c1, c2 = st.columns([1, 4])

with c1:
    if st.button("⛏️ MINE BLOCK", type="primary", use_container_width=True):
        with st.spinner('Mining Proof of Work...'):
            # Run the PoW algorithm
            last_block = bc.last_block
            proof = bc.proof_of_work(last_block['proof'])
            previous_hash = bc.hash(last_block)
            block = bc.new_block(proof, previous_hash)
            st.toast(f"Block #{block['index']} Mined Successfully!")

# --- LEDGER VISUALIZATION ---
st.subheader("📜 Blockchain Ledger")

# Convert chain to DataFrame for a professional table view
chain_data = []
for block in bc.chain:
    chain_data.append({
        "Index": block['index'],
        "Timestamp": block['timestamp'],
        "Proof": block['proof'],
        "Prev Hash": block['previous_hash'][:10] + "...", # Truncate for UI
        "Transactions": len(block['transactions'])
    })

df = pd.DataFrame(chain_data)
st.dataframe(df, use_container_width=True)

# --- BLOCK INSPECTOR ---
st.subheader("🔍 Block Inspector")
selected_block = st.selectbox("Select Block to Inspect", [b['index'] for b in bc.chain])
block_view = bc.chain[selected_block - 1]
st.json(block_view)
