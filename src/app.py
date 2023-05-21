from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("sobremim.html")


@app.route("/sobremim")
def sobremim():
    return render_template("sobremim.html")


@app.route("/projetos")
def projetos():
    return render_template("projetos.html")


@app.route("/capacidades")
def capacidades():
    return render_template("capacidades.html")


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


if __name__ == "__main__":
    app.run(debug=True)
