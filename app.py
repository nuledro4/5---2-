from flask import Flask, request, render_template
from flask import redirect, url_for
from flask import render_template_string
from User_class import User
from flask import session
from Exceptions import SearchExeption

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return registration()
    else:
        return render_template("main.html")


@app.route("/reg", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form["username"]
        mail = request.form["mail"]
        password = request.form["password"]
        user = User(name, password, mail)
        code = user.send_code()
        user = user.to_SET()
        session["user"] = user
        session["code"] = code
        if code:
            return redirect("/check")
        else:
            return f"что-то пошло не так {code}"
    else:
        return render_template("register.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        if "code" in session:
            if int(request.form["code"]) == int(session["code"]):
                session.pop("code", None)
                user = User(
                    session["user"]["name"],
                    session["user"]["password"],
                    session["user"]["mail"],
                )
                try:
                    session.pop("user", None)
                    if user.user_registration():
                        return redirect("/")
                    else:
                        return "Пользователь с такой почтой или именем уже есть."
                except:
                    session.pop("user", None)
                    return f"При добавлении пользователя произошла ошибка"
            else:
                session.pop("code", None)
                session.pop("user", None)
                return "Not Ok"
    else:
        return render_template("check.html")


@app.route("/log", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["login"]
        password = request.form["password"]
        user = User(name, password, name)
        try:
            res = user.login()
            if res != SearchExeption and res:
                return redirect("/")
            elif user.login() == SearchExeption:
                return "Произошла ошибка"
            else:
                return "Неверный логин или пароль"
        except:
            return "Произошла ошибка"
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.secret_key = b"9245a0065e066c7b07198c8e762ffda1278ead01b47adfc605eeb159fc9e9602"
    app.run(debug=True)
