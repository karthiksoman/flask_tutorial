# This code shows how to restrict a webpage to accept a specific http request
# such as GET, POST, PUT, DELETE

from flask import Flask

app = Flask(__name__)

# Here, POST method is given to the home page. Now, we cannot get the message given in the
# hello function in the brower since GET request is restricted in this page.
@app.route('/', methods=['POST'])
def hello():
    return 'Hello. This website only accepts GET request'

if __name__ == "__main__":
    app.run(debug=True)