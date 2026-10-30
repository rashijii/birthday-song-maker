
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()[:40]
        gender = request.form.get("gender", "").strip().lower()

        if name and gender in ["boy", "girl"]:
            return render_template(
                "result.html",
                name=name,
                gender=gender
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
