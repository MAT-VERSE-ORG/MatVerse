# pages/1_PhaseLab.py - placeholder page (replaced when the module is built)
import streamlit as st
from ui_helpers import module_page, show_tabs

left, right = module_page("PhaseLab", "🧪", "Fe-C phase diagram: region, phase fractions and microstructure.")
with left:
    st.subheader("Inputs")
    st.caption("Inputs with units will appear here.")
with right:
    st.subheader("Results")
    st.info("Coming in Week 1.")
show_tabs("Equations will be added from the Advisor's sheet.",
          "Assumptions will be listed here.",
          "References will be listed here.")
