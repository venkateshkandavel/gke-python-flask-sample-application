from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Rendu"

if __name__ == "__main__":
    # Choose the port based on your preference
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
