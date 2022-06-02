from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>this  1111111is home page</h1>"

@app.route("/courses")
def courses():
    return "<h1>this is courses page</h1>"

@app.route("/<name>")
def name(name):
    return f"<h1>welcome {name}!</h1>"

@app.route("/admin")
def redi():
    return redirect(url_for("courses"))

if __name__=='__main__':
    app.run(debug=True)
