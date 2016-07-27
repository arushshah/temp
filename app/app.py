from flask import Flask, request, render_template, make_response, redirect
import sys
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

app.run()