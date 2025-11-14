from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World from Flask and Elasticbeanstalk!"

if __name__ == "__main__":
    app.run(debug=True)
