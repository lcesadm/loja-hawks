from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def init():
    session["email"] = ""
    session["password"] = ""
    session["cart"] = ""
    return redirect("/index")

@app.route("/index", methods=['GET', "POST"])
def indexpage():
    if request.method == "POST":
        if request.form.get("registrar") == "registrar":
            session["email"] = request.form.get("email")
            session["password"] = request.form.get("password")
            if session["email"] and session["password"] and session["email"] == request.form.get("email") and session["password"] == request.form.get("password"):
                return render_template("index.html", alarm="Registro realizado!")
            else:
                return render_template("index.html", alarm="Campos inválidos!")
        if session["email"] and session["password"] and session["email"] == request.form.get("email") and session["password"] == request.form.get("password"):
            return redirect("/home")
        else:
            return render_template("index.html", alarm="Campos inválidos!")
    if session["email"] and session["password"]:
        return redirect("/home")
    return render_template("index.html")


@app.route("/home", methods=["GET", "POST"])
def homepage():
    user = {
        "email": session.get("email"),
        "password": session.get("password"),
        "cart": session.get("cart")
    }
    if user["email"] and user["password"]:
        return render_template("home.html")
    else:
        return redirect("/")
    

@app.route("/<string:nome>", methods=["GET", "POST"])
def error(nome):
    if request.method == "POST":
        return redirect("/index")
    return render_template("error.html", nome=nome)


if __name__ == "__main__":
    app.run(debug=True)
