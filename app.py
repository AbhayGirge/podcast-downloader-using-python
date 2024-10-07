# app.py

from flask import Flask, render_template, request
from download_podcasts import download_podcasts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_podcasts', methods=['POST'])
def download_podcasts_route():
    podcast_name = request.form['podcast_name']
    limit = int(request.form['limit'])
    download_podcasts(podcast_name, limit)
    return 'Podcasts downloaded successfully!'

@app.route('/transcribe_podcasts', methods=['POST'])
def transcribe_podcasts():
    # Access form data submitted by the user
    podcast_name = request.form['podcast_name']
    start_time = int(request.form['start_time'])
    end_time = int(request.form['end_time'])

    # Perform the transcription action
    # Example: transcribe_podcasts(podcast_name, start_time, end_time)
    
    return 'Podcasts transcribed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
