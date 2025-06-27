from flask import Flask
from app.routes import init_routes

app = Flask(__name__)
app.secret_key = "H190nyt89011"

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
    