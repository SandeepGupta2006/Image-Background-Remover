from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from dotenv import load_dotenv
from os import getenv
from PIL import Image, UnidentifiedImageError
from rembg import remove
from uuid import uuid4
from io import BytesIO


load_dotenv()
UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB


def remove_bg(input_stream):
    try:
        output_image = remove(Image.open(input_stream))

        output_stream = BytesIO()

        output_image.save(output_stream, format="PNG")

        output_stream.seek(0)

        return output_stream

    except Exception:
        return False


def validImage(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'tiff'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files.get("file")

        if not file or file.filename == "":
            flash("No file uploaded")
            return redirect(url_for("home"))

        if not validImage(file.filename):
            flash("File type not supported")
            return redirect(url_for("home"))

        try:
            Image.open(file.stream).verify()
            file.stream.seek(0)
        except UnidentifiedImageError:
            flash("Invalid image file")
            return redirect(url_for("home"))

        output_stream = remove_bg(file.stream)

        if not output_stream:
            flash("Error while removing background.")
            return redirect(url_for("home"))

        return send_file(output_stream, mimetype="image/png", download_name=f"{uuid4().hex}.png")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
