
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/premium", methods=["GET", "POST"])
def premium():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        sender = request.form.get("sender", "").strip()
        message = request.form.get("message", "").strip()
        theme = request.form.get("theme", "pink")

        if name and sender and message:
            return render_template(
                "premium.html",
                name=name,
                sender=sender,
                message=message,
                theme=theme
            )

    return render_template("premium.html")

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
