# app.py
import streamlit as st
from main import run_swarm
import json

st.set_page_config(page_title="Phantom Protocol — Simulated Swarm", layout="wide")
st.title("🛡️ Phantom Protocol — Simulated Cybersecurity Swarm (Stage 1)")

st.markdown("""
This demo runs a simulated observation → prediction → attack → defense → archive workflow.
**Note:** All scanning and exploits are simulated for demo purposes.
""")

target = st.text_input("Target (domain / IP / name)", value="demo.example.com")
run = st.button("Run Swarm")

if run and target:
    with st.spinner("Running agent swarm..."):
        try:
            out = run_swarm(target)
            st.success("Simulation complete — results archived")
            st.subheader("Archive Summary")
            # Pretty-print archive summary
            st.json(out)
        except Exception as e:
            st.error(f"Error running swarm: {e}")
            raise
else:
    st.info("Enter a target and click Run Swarm to begin.")
