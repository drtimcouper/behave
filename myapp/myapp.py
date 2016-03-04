from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def mine():
    return render_template('mine.html')


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


if __name__ == "__main__":
   app.run()
