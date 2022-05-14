from app import app
from flask import request, render_template, flash
from services import nlp_service
import sys


@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")


@app.route("/", methods=["POST"])
def crypt():
    if request.form.get("encrypt"):
        encrypt = request.form["encrypt"]
        decrypted_text = nlp_service.encrypt(encrypt)
        print(decrypted_text, file=sys.stderr)
        flash("Succesfully encrypted!", "success")
        return render_template("main.html", result=decrypted_text, text="Encryption")
    else:
        decrypt = request.form["decrypt"]
        encrypted_text = ""
        try:
            encrypted_text = nlp_service.decrypt(decrypt)
            flash("Succesfully decrypted!", "success")
        except:
            flash("Something went wrong! Have you encrypted the text before?", "danger")
        print(encrypted_text, file=sys.stderr)
        return render_template("main.html", result=encrypted_text, text="Decryption")

@app.errorhandler(Exception)
def server_error(err):
    return render_template('error.html'), 500
