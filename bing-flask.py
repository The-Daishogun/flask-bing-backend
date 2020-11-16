from flask import Flask, request
import backgroundify as bg

app = Flask(__name__)

# can get pictures of previous days (up to 8 days bc of Bing restrictions). /?day={int}
@app.route("/")
def index():
    day = request.args.get("day", default=1, type=int)
    day = day if day <= 8 else 1
    return bg.get_img_url(day=day)


if __name__ == "__main__":
    app.run(debug=True)
