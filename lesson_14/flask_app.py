from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return request.form.to_dict()
    return request.args.to_dict()


if __name__ == "__main__":
    app.run()
