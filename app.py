# app.py - MAT-VERSE home page (Leads own this file)
# Run with:  python -m streamlit run app.py
import streamlit as st
from ui_helpers import show_sidebar, PROJECT_NAME, TAGLINE

# === EDIT HERE === (module name, icon, one-line description, week)
MODULES = [
    ("PhaseLab", "🧪", "Fe-C phase diagram: region, phase fractions (lever rule) and microstructure.", "Week 1"),
    ("HeatLab", "🔥", "Heat treatment: austenitizing range, expected microstructure, Ms estimate.", "Week 2"),
    ("CorroLab", "🧲", "Corrosion rate from weight loss or current density, plus galvanic risk.", "Week 2"),
    ("MicroLab", "🔬", "Area-fraction measurement from a micrograph (future extension).", "Stretch"),
    ("Autopsy", "🩺", "Ranked possible failure mechanisms with a WHY explanation.", "Week 3"),
    ("EcoLab", "♻️", "Recycling: contained, recovered and lost metal for scrap scenarios.", "Week 3"),
]

st.set_page_config(page_title=PROJECT_NAME, page_icon="⚙️", layout="wide")
show_sidebar()

# Hero banner (Python: one HTML block; Engineering: the project's first impression)
st.markdown(
    "<div class='hero'><h1>⚙️ " + PROJECT_NAME + "</h1>"
    "<h3>Materials Engineering Virtual Intelligence &amp; Simulation Environment</h3>"
    "<p>" + TAGLINE + "</p></div>", unsafe_allow_html=True)

# Quick facts row
c1, c2, c3 = st.columns(3)
c1.metric("Labs", "6 modules")
c2.metric("Course", "CSC-214")
c3.metric("Focus", "Design to Failure")

st.markdown("### Explore the labs")
columns = st.columns(3, gap="medium")
index = 0
for name, icon, text, week in MODULES:
    with columns[index % 3]:
        st.markdown(
            "<div class='card'><div class='icon'>" + icon + "</div><h4>" + name + "</h4><p>"
            + text + "</p><span class='tag'>" + week + "</span></div>", unsafe_allow_html=True)
    index = index + 1

st.caption("B.Sc. Metallurgy & Materials Engineering, University of the Punjab. "
           "Outputs are estimates and decision support, not a replacement for laboratory testing.")
