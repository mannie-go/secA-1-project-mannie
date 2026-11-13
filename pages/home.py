"""Home page — UI only (static content)."""
from pathlib import Path

import streamlit as st

PAGES_DIR = Path(__file__).parent

APPS = [
    ("statistics.py", "📈", "Statistics", "Mean, Median, Mode, SD, Variance", "Descriptive statistics"),
    ("bayes.py", "🎲", "Bayes' Theorem", "Compute posterior P(A|B)", "Conditional probability"),
    ("markov.py", "🔗", "Markov Text Prediction", "Predict the next word / sentence", "Markov chain"),
    ("display_data.py", "🗂️", "Display Data", "Browse raw data from data/", "Data viewer"),
    ("custom_app.py", "🚀", "Custom App", "Our applied innovation", "Matrices / Vectors"),
    ("members.py", "👥", "Members", "Team members & responsibilities", "—"),
]

st.title("📊 Statistics, Probability & Applied Math Toolkit")
st.caption("Streamlit mono-repo · UI in `pages/` · logic in `services/`")

st.markdown(
    "A web application for computing **descriptive statistics**, **Bayesian probability**, "
    "**Markov-chain text prediction**, and an **applied math** custom app. "
    "Choose an app below or from the sidebar."
)

st.divider()
st.subheader("Applications")

cols = st.columns(3)
for i, (file, icon, title, desc, _) in enumerate(APPS):
    with cols[i % 3]:
        with st.container(border=True, height=170):
            st.markdown(f"#### {icon} {title}")
            st.write(desc)
            if (PAGES_DIR / file).exists():
                st.page_link(f"pages/{file}", label=f"Open {title}", icon="➡️")
            else:
                st.caption("🚧 Coming soon")

st.divider()
st.subheader("Overview")
st.table(
    {
        "App": [f"{icon} {title}" for _, icon, title, _, _ in APPS],
        "Description": [desc for _, _, _, desc, _ in APPS],
        "Math topic": [topic for *_, topic in APPS],
    }
)
