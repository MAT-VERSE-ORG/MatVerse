# pages/7_Journey.py - combined summary of all labs (Week 3: full version)
import json
import streamlit as st
from ui_helpers import show_sidebar, init_journey

st.set_page_config(page_title="Journey | MAT-VERSE", page_icon="🧭", layout="wide")
show_sidebar()
init_journey()
st.markdown("<div class='banner'><h1>🧭 Journey</h1><p>Combined summary of every lab you have run.</p></div>", unsafe_allow_html=True)
for stage in ["phaselab", "heatlab", "corrolab", "autopsy", "ecolab"]:
    if stage in st.session_state["journey"]:
        st.success(stage + " done")
        st.json(st.session_state["journey"][stage])
    else:
        st.info(stage + ": not run yet.")
st.download_button("Download summary (JSON)",
                   json.dumps(st.session_state["journey"], indent=2, default=str),
                   file_name="matverse_journey.json")
