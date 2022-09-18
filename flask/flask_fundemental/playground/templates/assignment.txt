from flask import Flask, render_template

app = Flask(__name__)

# @app.route ("/play")
# def specific_boxes():
#     return render_template("index1.html")

# @app.route("/play/<int:x>")
# def many_boxes(x):
#     return render_template("index2.html", repeate=x)

# @app.route("/play/<int:x>/<color>")
# def many_colored_boxes(x,color):
#     return render_template("index3.html", repeate=x, color=color)

@app.route ("/play")
def specific_boxes(var = 1):
    return render_template("index4.html", var=var)

@app.route("/play/<int:x>")
def many_boxes(x, var = 2):
    return render_template("index4.html", repeate=x, var=var)

@app.route("/play/<int:x>/<color>")
def many_colored_boxes(x,color, var = 3):
    return render_template("index4.html", repeate=x, color=color, var=var)

if __name__ == "__main__":
    app.run(debug=True)