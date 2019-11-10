from flask import Flask
from flask import request
import main

app = Flask(__name__)

id = ""

@app.route("/")
def getId():
    id = request.args.get("id")
    main.main()
    return id

if __name__ == "__main__":
    app.run()