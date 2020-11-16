from flask import Flask
import backgroundify as bg

app = Flask(__name__)


@app.route("/")
def index():
    return bg.get_img_url()


if __name__ == "__main__":
    app.run(debug=True)
