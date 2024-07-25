#!/usr/bin/python3
#!/usr/bin/python3
"""A script that starts a Flask web application
Your web application must be listening on 0.0.0.0,
port 5000

outes: 
    /: display “Hello HBNB!”
You must use the option strict_slashes=False
in your route definition
"""
from flask import Flask

# An instance of flask
app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def display():
    """Displays “Hello HBNB! """
    return 'Hello HBNB!'

@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def display_two():
    """ / hbnb: display HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)