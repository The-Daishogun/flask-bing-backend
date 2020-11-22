from flask import Flask, request, send_file, url_for
from flask_cors import CORS
from backgroundify import Backgroundify
import os

app = Flask(__name__)
cors = CORS(app)

# can get pictures of previous days (up to 8 days bc of Bing restrictions).
@app.route("/<int:days>")
def index(days):
    bg = Backgroundify(days=days)
    response = (
        bg.get_imgs()
        if request.content_type == "application/json"
        else str(bg.get_imgs())
    )
    return response


# can save pictures of previous days (up to 8 days bc of Bing restrictions). saves all the files up to that day but only serves the latest pic
@app.route("/save/<int:days>")
def save(days):
    bg = Backgroundify(days=days)
    bg.get_imgs()
    bg.save_files()
    file_path = os.getcwd() + "/static/pic/"
    filename = bg.imgs[0]["filename"]
    return send_file(file_path + filename, mimetype="image/jpg")


@app.route("/api/<int:days>")
def api(days):
    response = {}
    bg = Backgroundify(days=days)
    bg.get_imgs()
    bg.save_files()
    for i in range(days):
        response[i] = {
            "url": "http://localhost:5000"
            + url_for("static", filename="pic/" + bg.imgs[i]["filename"]),
            "title": bg.imgs[i]["title"],
            "copyright": bg.imgs[i]["copyright"],
        }
    return response


@app.route("/static/pic/<filename>")
def serve(filename):
    return send_file("static/pic/" + filename + ".jpg")


if __name__ == "__main__":
    app.run(debug=True)
