from flask import Flask

app = Flask(__name__)

#http://IP: PORT/

@app.route("/welcome")
def welcome():
    return "Welcome to my python flask page"

#launch development server

app.run(port=4002)