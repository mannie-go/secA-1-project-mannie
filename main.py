"""Main entry point — routing only."""
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "pages"

st.set_page_config(page_title="Stat & Math Toolkit", page_icon="📊", layout="wide")

# (file, title, icon) — in spec order
PAGE_SPECS = [
    ("home.py", "Home", "🏠"),
    ("statistics.py", "Statistics", "📈"),
    ("bayes.py", "Bayes' Theorem", "🎲"),
    ("markov.py", "Markov Text Prediction", "🔗"),
    ("display_data.py", "Display Data", "🗂️"),
    ("custom_app.py", "Custom App", "🚀"),
    ("members.py", "Members", "👥"),
]

# Register only pages that exist, so the app runs while teammates are still building theirs.
pages = [
    st.Page(str(PAGES_DIR / f), title=title, icon=icon, default=(f == "home.py"))
    for f, title, icon in PAGE_SPECS
    if (PAGES_DIR / f).exists()
]

pg = st.navigation(pages)
pg.run()
