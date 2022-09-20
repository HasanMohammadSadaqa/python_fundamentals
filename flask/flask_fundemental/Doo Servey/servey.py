
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# app.secret_key = 'keep it secret, keep it safe' 

@app.route("/")
def hasan():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def creat_user():
    firstname_from_form = request.form["first_name"]
    lastname_from_form = request.form["last_name"]
    department_from_form = request.form["department"]
    username_from_form = request.form["user_name"]
    password_from_form = request.form['user_password']
    email_from_form = request.form["email"]
    number_from_form = request.form["contact_no"]
    return render_template("show.html", first_name =firstname_from_form, last_name = lastname_from_form, department = department_from_form,
            username =username_from_form, password = password_from_form, email = email_from_form, num = number_from_form)

# @app.route('/result', methods=['POST'])
# def create_user():
#     session["first_name"] = request.form["first_name"]
#     session["last_name"] = request.form["last_name"]
#     session["department"] = request.form["department"]
#     session["user_name"] = request.form["user_name"]
#     session["user_password"] = request.form["user_password"]
#     session["email"] = request.form["email"]
#     session["contact_no"] = request.form["contact_no"]
#     return redirect("/show")

# @app.route("/show")
# def show_user():
#     return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)