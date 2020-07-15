import pyttsx3
import speech_recognition
import wave
from flask import Flask, flash, render_template, jsonify, request
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['JSON_AS_ASCII'] = False
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/hello', methods=['GET'])
def hello():
  return render_template('index.html')

  # wave_file = wave.open(audio.wav, 'r')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    recognizer = speech_recognition.Recognizer()
    if (1==1):
      with speech_recognition.WavFile(filename) as source:
        _data = recognizer.record(source)  # read the entire WAV file
        print(_data)
        print(type(_data))
    # recognize speech using Google Speech Recognition
      try:
        text = recognizer.recognize_google(_data, language='vi-VN')
      # print recognizer.recognize_google(_data, show_all=True)
      except speech_recognition.UnknownValueError:
      # print(" | error: could not understand audio (empty input?)")
        print_debug('asr | (empty)\n')
        text = ''
      print(text)

      return jsonify(
        data=text
        )
    # return send_from_directory(app.config['UPLOAD_FOLDER'],
    #                            filename)

@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# def post():
#   recognizer = speech_recognition.Recognizer()
#   if (1==1):
#     with speech_recognition.WavFile("audio.wav") as source:
#       _data = recognizer.record(source)  # read the entire WAV file
#       print(_data)
#       print(type(_data))
#     # recognize speech using Google Speech Recognition
#     try:
#       text = recognizer.recognize_google(_data)
#       # print recognizer.recognize_google(_data, show_all=True)
#     except speech_recognition.UnknownValueError:
#       # print(" | error: could not understand audio (empty input?)")
#       print_debug('asr | (empty)\n')
#       text = ''
#     print(text)

#     return jsonify(
#       data=text
#       )
  
# recognizer = speech_recognition.Recognizer()
# if (1==1):
#   with speech_recognition.WavFile("audio.wav") as source:
#     _data = recognizer.record(source)  # read the entire WAV file
#     print(_data)
#     print(type(_data))
#     # recognize speech using Google Speech Recognition
#   try:
#     text = recognizer.recognize_google(_data)
#       # print recognizer.recognize_google(_data, show_all=True)
#   except speech_recognition.UnknownValueError:
#       # print(" | error: could not understand audio (empty input?)")
#     print_debug('asr | (empty)\n')
#     text = ''


if __name__ == '__main__':
    app.run(host='192.168.0.121', port=8000,debug=True)


# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()