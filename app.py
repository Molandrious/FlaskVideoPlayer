# docker run -p 5000:5000 -v D:/Downloads/sys/videos:/app/videos my-flask-app
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Constants for absolute path to video folder and supported video formats
VIDEO_PATH = "D:/videos"
SUPPORTED_FORMATS = [".mp4", ".avi", ".mkv"]


def get_video_files():
    video_files = [f for f in os.listdir(VIDEO_PATH) if f.lower().endswith(tuple(SUPPORTED_FORMATS))]
    return video_files


@app.route('/')
def index():
    video_files = get_video_files()
    current_video = request.args.get('video')
    if current_video is None:
        current_video = video_files[0]
    return render_template('index.html', video_files=video_files, current_video=current_video)


@app.route('/videos/<filename>')
def videos(filename):
    return send_from_directory(VIDEO_PATH, filename)


if __name__ == "__main__":
    app.run()
