#flask=2.0.0
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ip_download = "null"
ip_upload = "null"
file_path = "./"

download_path = './'

ALLOWED_EXTENSIONS = []

@app.route("/", methods=["GET"])
def main():
    if (request.remote_addr == ip_download):
        return send_file(file_path)
    else:
        return "Access denied "+request.remote_addr

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if (request.remote_addr == ip_upload):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return "Error 400"
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(download_path, filename))
                return "Saved"
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.run(host="0.0.0.0")
