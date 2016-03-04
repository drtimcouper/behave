from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mine():
    return render_template('mine.html')

if __name__ == "__main__":
    app.run()
