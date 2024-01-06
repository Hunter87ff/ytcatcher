import os, time
from pytube import YouTube as yt
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.static_folder = "static"

#https://youtu.be/SWih3fGnQ7I?si=GtMlIOCy3nVrHH9W
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ytdl", methods=["POST"])
def download():
    form = request.form
    url = form["url"]
    obj = yt(url).streaming_data["formats"]
    if form["typ"] == "video": return redirect(obj[-1]["url"])
    else: return redirect(obj[0]["url"])

app.run(host="0.0.0.0", port=8080)