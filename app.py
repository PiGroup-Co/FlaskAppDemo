from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

def handle(file):
	return file.filename


@app.route("/", methods=["POST"])
def uploader():
	if request.method == "POST" :
		file = request.files["file"]
		
		result = handle(file)
		return result

	return "404 NOT FOUND"

if __name__ == "__main__":
    app.run(debug = True)