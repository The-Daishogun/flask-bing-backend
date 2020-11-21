from flask import Flask, request, send_file
from backgroundify import Backgroundify
import os

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
