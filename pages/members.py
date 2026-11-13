"""Members page — UI only (static member data)."""
import html

import streamlit as st

from services.member_service import photo_src

MEMBERS = [
    {
        "name": "Worapol Siriburi",
        "id": "1680703131",
        "img": "worapol.jpg",
        "role": "Routing (main.py), Home page, Statistics, Members page",
    },
    {
        "name": "Atthaporn Napinthorn",
        "id": "1680706072",
        "img": "atthaporn.jpg",
        "role": "Markov Chain text prediction (markov.py)",
    },
    {
        "name": "Pratchimaporn Poolcharoen",
        "id": "1670706702",
        "img": "pratchimaporn.jpeg",
        "role": "Bayes' Theorem calculator (bayes.py)",
    },
    {
        "name": "Padol Kaewpia",
        "id": "1670704202",
        "img": "padol.jpg",
        "role": "Data viewer (display_data.py)",
    },
    {
        "name": "Chinnawat Rakpuang",
        "id": "1680703434",
        "img": "chinnawat.jpg",
        "role": "Custom application (custom_app.py)",
    },
]

st.title("👥 Team Members")
st.caption("Group secA-1 · names, student IDs and responsibilities")
st.divider()

CARD_CSS = """
<style>
.member-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    align-items: stretch;          /* every card gets the same height */
}
.member-card {
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(128, 128, 128, 0.3);
    border-radius: 12px;
    overflow: hidden;
    font-family: "Source Sans Pro", sans-serif;
}
.member-photo {
    width: 100%;
    aspect-ratio: 3 / 4;           /* identical photo frame for everyone */
    object-fit: cover;
    display: block;
}
.member-body { padding: 0.75rem 0.9rem 1rem; flex: 1; }
.member-name { font-weight: 700; font-size: 1.05rem; margin: 0 0 0.25rem; }
.member-id { opacity: 0.65; font-size: 0.85rem; margin: 0 0 0.5rem; }
.member-role { font-size: 0.9rem; margin: 0; }
</style>
"""


cards = "".join(
    f"""
    <div class="member-card">
        <img class="member-photo" src="{photo_src(m['img'])}" alt="{html.escape(m['name'])}">
        <div class="member-body">
            <p class="member-name">{html.escape(m['name'])}</p>
            <p class="member-id">Student ID: {html.escape(m['id'])}</p>
            <p class="member-role"><b>Role:</b> {html.escape(m['role'])}</p>
        </div>
    </div>"""
    for m in MEMBERS
)

st.html(CARD_CSS + f'<div class="member-grid">{cards}</div>')
