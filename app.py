from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "123456"

# Usuario de prueba (puedes luego usar base de datos)
usuario_demo = {
    "correo": "admin@gmail.com",
    "password": generate_password_hash("1234")
}

@app.route("/")
def inicio():
    if "correo" in session:
        return render_template("index.html")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]

        if correo == usuario_demo["correo"] and check_password_hash(usuario_demo["password"], password):
            session["correo"] = correo
            return redirect("/")
        else:
            flash("Correo o contraseña incorrectos")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("correo", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)