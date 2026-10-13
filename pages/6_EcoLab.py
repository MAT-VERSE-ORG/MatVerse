# pages/6_EcoLab.py - placeholder page (replaced when the module is built)
import streamlit as st
from ui_helpers import module_page, show_tabs

left, right = module_page("EcoLab", "♻️", "Recycling analysis.")
with left:
    st.subheader("Inputs")
    st.caption("Inputs with units will appear here.")
with right:
    st.subheader("Results")
    st.info("Coming in Week 3.")
show_tabs("Equations will be added from the Advisor's sheet.",
          "Assumptions will be listed here.",
          "References will be listed here.")
