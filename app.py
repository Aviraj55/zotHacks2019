from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def getId():
    id = request.args.get("id")
    return id

if __name__ == "__main__":
    app.run()