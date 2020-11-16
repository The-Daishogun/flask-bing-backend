from flask import Flask, request, send_file
import os
import backgroundify as bg

app = Flask(__name__)

# can get pictures of previous days (up to 8 days bc of Bing restrictions). /?day={int}
@app.route("/")
def index():
    day = request.args.get("day", default=1, type=int)
    day = day if day <= 8 else 1
    response = (
        {"url": bg.get_img_url(day=day)}
        if request.content_type == "application/json"
        else bg.get_img_url(day=day)
    )
    return response


# can save pictures of previous days (up to 8 days bc of Bing restrictions). /?day={int}
@app.route("/save")
def save():
    file_path = os.getcwd() + "/static/pic/"
    day = request.args.get("day", default=1, type=int)
    day = day if day <= 8 else 1
    img_url = bg.get_img_url(day=day)
    filename = bg.get_filename(days=day - 1)
    if os.path.exists(file_path + filename):
        return send_file(file_path + filename, mimetype="image/jpg")
    else:
        return send_file(
            bg.save_file(img_url, file_path, filename), mimetype="image/jpg"
        )


if __name__ == "__main__":
    app.run(debug=True)
