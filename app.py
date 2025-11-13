from flask import Flask, render_template
from pathlib import Path
import os
import ast
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)

@app.route("/")

def index():
    coordinate_str = os.getenv("EIU_COORDINATE", "[11.052738, 106.666281]")
    lat, lng = ast.literal_eval(coordinate_str)

    zoom = int(os.getenv("ZOOM", 8))

    tile_url = os.getenv(
        "TILE_LAYER_URL_TEMPLATE",
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    )

    return render_template("map.html", lat=lat, lng=lng, zoom=zoom, tile_url=tile_url)

if __name__ == "__main__":
    app.run(debug=True)
