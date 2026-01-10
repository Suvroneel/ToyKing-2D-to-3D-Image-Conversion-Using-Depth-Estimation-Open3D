from flask import Flask, render_template, request
import numpy as np
import cv2
from processing.pipeline import image_to_pseudo_3d
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    if "image" not in request.files:
        return render_template("index.html", error="No image uploaded")

    file = request.files["image"]
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return render_template("index.html", error="Invalid image file")

    # Convert to RGB for model
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    try:
        output_image_base64 = image_to_pseudo_3d(img_rgb, invert=True)
    except Exception as e:
        return render_template("index.html", error=f"Processing failed: {str(e)}")

    return render_template("index.html",
                           output_image=output_image_base64,
                           original_image_base64=base64.b64encode(cv2.imencode(".png", img)[1]).decode("utf-8"))

if __name__ == "__main__":
    app.run(debug=True)
