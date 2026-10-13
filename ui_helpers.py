# ui_helpers.py - shared layout used by EVERY page (Leads own this file)
# Python meaning: small functions we call from each page.
# Engineering meaning: every lab looks the same, so the app feels like one environment.
import streamlit as st

# === EDIT HERE ===
PROJECT_NAME = "MAT-VERSE"
TAGLINE = "From Material Design to Failure - One Digital Materials Engineering Environment."
STAGES = ["phaselab", "heatlab", "corrolab", "autopsy", "ecolab"]  # Journey stages
NAVY = "#0B2545"        # dark colour (sidebar, banners)
BLUE = "#2E86DE"        # accent colour

# CSS = the "paint" of the web page. Juniors can safely change colours here.
STYLE = """
<style>
#MainMenu, footer {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 1150px;}
[data-testid="stSidebar"] {background: linear-gradient(180deg, #0B2545 0%, #13315C 100%);}
[data-testid="stSidebar"] * {color: #EAF2FB !important;}
.hero {background: linear-gradient(135deg, #0B2545 0%, #1B4F8A 60%, #2E86DE 100%);
       color: white; padding: 2.2rem 2.4rem; border-radius: 18px; margin-bottom: 1.2rem;
       box-shadow: 0 8px 24px rgba(11,37,69,0.25);}
.hero h1 {color: white; margin: 0; font-size: 2.6rem; letter-spacing: 1px;}
.hero h3 {color: #CFE3F8; font-weight: 400; margin: 0.3rem 0 0.6rem 0;}
.hero p {color: #E3EEF9; margin: 0;}
.banner {background: linear-gradient(135deg, #0B2545 0%, #1B4F8A 100%); color: white;
         padding: 1.2rem 1.6rem; border-radius: 14px; margin-bottom: 1rem;}
.banner h1 {color: white; margin: 0; font-size: 2rem;}
.banner p {color: #CFE3F8; margin: 0.2rem 0 0 0;}
.card {background: white; border-radius: 16px; padding: 1.3rem 1.4rem; margin-bottom: 1rem;
       border: 1px solid #D5E3F2; border-top: 5px solid #2E86DE; min-height: 170px;
       box-shadow: 0 2px 8px rgba(11,37,69,0.08); transition: all 0.2s;}
.card:hover {transform: translateY(-5px); box-shadow: 0 10px 22px rgba(46,134,222,0.25);}
.card .icon {font-size: 2.2rem;}
.card h4 {margin: 0.3rem 0; color: #0B2545;}
.card p {color: #4A6078; margin: 0; font-size: 0.93rem;}
.tag {display:inline-block; background:#E3EEF9; color:#1B4F8A; border-radius:20px;
      padding:2px 12px; font-size:0.78rem; margin-top:0.6rem;}
.stTabs [data-baseweb="tab"] {font-weight: 600;}
div[data-testid="stMetric"] {background: white; border-radius: 12px; padding: 12px 16px;
       border: 1px solid #D5E3F2; box-shadow: 0 2px 6px rgba(11,37,69,0.06);}
.stButton > button {background: #2E86DE; color: white; border-radius: 10px; border: none;
       padding: 0.5rem 1.4rem; font-weight: 600;}
.stButton > button:hover {background: #1B4F8A; color: white;}
</style>
"""


def init_journey():
    # Python: create the shared 'journey' dictionary once per session.
    # Engineering: stores each lab's result so the Journey page can summarise them.
    if "journey" not in st.session_state:
        st.session_state["journey"] = {}


def show_sidebar():
    # Python: apply the style, then draw project name and progress in the sidebar.
    # Engineering: shows how many labs the user has run on this material.
    st.markdown(STYLE, unsafe_allow_html=True)
    init_journey()
    st.sidebar.markdown("## ⚙️ " + PROJECT_NAME)
    st.sidebar.caption("Materials Engineering Virtual Intelligence & Simulation Environment")
    done = 0
    for stage in STAGES:
        if stage in st.session_state["journey"]:
            done = done + 1
    st.sidebar.progress(done / len(STAGES))
    st.sidebar.caption("Journey progress: " + str(done) + " of " + str(len(STAGES)) + " labs run")


def module_page(title, icon, description):
    # Python: set page config, show header banner + notice, return two columns.
    # Engineering: inputs (with units) go LEFT, plots/results go RIGHT.
    st.set_page_config(page_title=title + " | " + PROJECT_NAME, page_icon=icon, layout="wide")
    show_sidebar()
    st.markdown("<div class='banner'><h1>" + icon + " " + title + "</h1><p>"
                + description + "</p></div>", unsafe_allow_html=True)
    st.warning("Estimate only: outputs are screening support, not lab results or industrial diagnosis.", icon="⚠️")
    left, right = st.columns([1, 2], gap="large")
    return left, right


def show_tabs(equations, assumptions, references):
    # Python: three tabs, each showing the text we pass in.
    # Engineering: every result must show its equations, assumptions and references.
    tab1, tab2, tab3 = st.tabs(["📐 Equations used", "📋 Assumptions", "📚 References"])
    with tab1:
        st.markdown(equations)
    with tab2:
        st.markdown(assumptions)
    with tab3:
        st.markdown(references)
