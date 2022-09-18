from flask import Flask
app = Flask(__name__)
@app.route ("/")
def hello():
    return "hello World!!"

@app.route ("/dojo")
def dojo():
    return "Hello Dojo!"

@app.route ("/say/<name>")
def say_flask(name):
    return "Hi " + name

@app.route("/repeat/<int:n1>/<greeting>")
def introduce(n1,greeting):
    return (greeting+ " ")* n1


if __name__ == "__main__":
    app.run(debug=True)