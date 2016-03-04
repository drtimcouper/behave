import logging

from flask import Flask, render_template

logger = logging.getLogger()

app = Flask(__name__)
user = 'Fred'

@app.route("/")
def mine():
    return render_template('mine.html', user=user)


if __name__ == "__main__":
    logging.basicConfig()
    app.run()
