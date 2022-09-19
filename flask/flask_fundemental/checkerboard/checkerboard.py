from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def checkerboard1():
    return render_template("index.html", rows = 8, columns = 8, row_color = "red", column_color = "black")

@app.route("/<int:x>")
def checkerboard2(x):
    return render_template("index.html", rows = 8, columns = x, row_color = "red", column_color = "black")

@app.route("/<int:x>/<int:y>")
def checkerboard3(x,y):
    return render_template("index.html", rows = x, columns = y, row_color = "red", column_color = "black")

@app.route('/<int:x>/<int:y>/<color>/<color2>')          
def checkboard_with_many_color(x, y, color, color2):
    return render_template("index.html", rows=x, columns = y, column_color=color2, row_color=color )

if __name__ == "__main__":
    app.run(debug=True)
