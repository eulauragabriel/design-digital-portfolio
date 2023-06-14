from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    title = "Sobre mim"
    return render_template("sobremim.html", title=title)


@app.route("/sobremim")
def sobremim():
    title = "Sobre mim"
    return render_template("sobremim.html", title=title)


@app.route("/projetos")
def projetos():
    title = "Projetos"
    return render_template("projetos.html", title=title)


@app.route("/capacidades")
def capacidades():
    title = "Capacidades"
    return render_template("capacidades.html", title=title)


@app.route("/hobbies")
def hobbies():
    title = "Hobbies"
    return render_template("hobbies.html", title=title)


if __name__ == "__main__":
    app.run(debug=True)
