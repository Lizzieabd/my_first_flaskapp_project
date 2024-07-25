from flask import Flask, render_template

app = Flask(__name__)


@app.route('/welcome/')
def welcome():
    return "<p>Hello lizzie</p>"


if __name__ == '__main__':
    app.run(debug=True)
