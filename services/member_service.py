"""Member photos — backend logic for pages/members.py."""
import base64
from pathlib import Path

IMG_DIR = Path(__file__).parent.parent / "data" / "imgs"
PLACEHOLDER = "placeholder.jpg"


def photo_src(filename):
    """Read a photo from data/imgs and return it as a data URI (placeholder if missing)."""
    path = IMG_DIR / filename
    if not path.exists():
        path = IMG_DIR / PLACEHOLDER
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()
