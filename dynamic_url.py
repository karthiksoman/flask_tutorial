## How to make URL dynamic, i.e the url chanes its names based on which users use that.
#This can be considered as FB style URL. For my FB page the url is
# https://www.facebook.com/karthik.soman.35
# This means that for a different user, his FB URL will be different.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world. This is the home page"

@app.route('/users/<string:name>')
def dynamic_url(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run(debug=True)