from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Rendu"

if __name__ == "__main__":
<<<<<<< HEAD
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True,host='0.0.0.0',port=port)
=======
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
creating a new commit
creating a second commit tag
>>>>>>> testing
