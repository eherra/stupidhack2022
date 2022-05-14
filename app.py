from os import getenv

from flask import Flask

app = Flask(__name__)
app.config["FLASK_ENV"] = getenv("FLASK_ENV")
app.secret_key = getenv("SECRET_KEY")

import routes