import os, time
from pytube import YouTube as yt
from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory





app = Flask(__name__)
app.static_folder = "static"

#https://youtu.be/SWih3fGnQ7I?si=GtMlIOCy3nVrHH9W
@app.route("/", methods=["post", "get"])
def home():
    if request.method == "GET": return render_template("base.html")
    if request.method == "POST":
        form = request.form
        url = form["url"]
        vdo = yt(url)
        data = {
        "title": vdo.title,
        "author":vdo.author,
        "views" : vdo.views,
        "duration":vdo.length,
        "thumbnail":vdo.thumbnail_url,
        "channel_id":vdo.channel_url,   
        "audio": [x for x in vdo.streams if x.type=="audio"],
        "video":[x for x in vdo.streams if x.type=="video"]}
        return render_template("index.html", data=data, videos=data["video"], audios=data["audio"], int=int)



@app.route("/extract", methods=["POST"])
def extract():
    form = request.form
    url = form["url"]
    vdo = yt(url)
    data = {
    "title": vdo.title,
    "author":vdo.author,
    "views" : vdo.views,
    "duration":vdo.length,
    "thumbnail":vdo.thumbnail_url,
    "channel_id":vdo.channel_url,
    "audio": [x for x in vdo.streams if x.type=="audio"],
    "video":[x for x in vdo.streams if x.type=="video"]}
    return jsonify(data)



@app.route("/ytdl", methods=["POST", "GET"])
def download():
    form = request.form
    url = form["url"]
    obj = yt(url).streaming_data["formats"]
    if form["typ"] == "video": return redirect(obj[-1]["url"])
    else: return redirect(obj[0]["url"])

app.run(host="0.0.0.0", port=8080)
