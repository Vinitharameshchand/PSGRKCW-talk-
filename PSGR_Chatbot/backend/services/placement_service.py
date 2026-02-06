import json
import os

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "placements.json"
)

def get_placement_data():
    """
    Returns placement statistics data
    """
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return {
            "error": "Placement data not available",
            "details": str(e)
        }
