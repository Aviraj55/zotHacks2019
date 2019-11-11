from flask import Flask
from flask import request
import main

app = Flask(__name__)

@app.route("/")
def getId():
    id = request.args.get("id")
    print(id)
    main.main(id)
    return "Hello World"

if __name__ == "__main__":
    app.run()