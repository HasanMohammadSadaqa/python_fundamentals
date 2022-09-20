
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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

@app.route('/result')
def show():
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)