from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        # Call your transcription function here
        # Example: transcription_id = transcribe_podcast(upload_url)
        return 'File uploaded successfully'
    else:
        return 'No file uploaded'

# Define route to display transcriptions
@app.route('/transcriptions')
def transcriptions():
    # Load transcription metadata
    # Example: metadata = load_transcription_metadata()
    # Process metadata to display transcriptions
    return render_template('transcriptions.html', transcriptions=metadata)

if __name__ == '__main__':
    app.run(debug=True)
