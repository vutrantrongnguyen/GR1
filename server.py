from flask import Flask, render_template
from flask import jsonify
from flask import request
import speech_recognition
# from scipy.io.wavfile import read as wavread
# from scipy.io.wavfile import write as wavwrite
# import numpy as np
# import wave
# import cgi
# import contextlib
# import base64
# import soundfile as sf
# from flask_cors import CORS, cross_origin
# import subprocess

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
# @cross_origin()
def post():
    # with open("file.wav", "wb") as vid:
    #     vid.write(request.data)

    # proc = subprocess.Popen(
    #     "deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio file.wav",
    #     # "deepspeech --models models/deepspeech-0.7.0-models.pbmm --scorer models/deepspeech-0.7.0-models.scorer --audio file.wav",
    #     shell=True, stdout=subprocess.PIPE, )
    # print(proc)
    # output = proc.communicate()[0]
    # print(output)

    # return jsonify(
    #     username=output
    # )

recognizer = speech_recognition.Recognizer()
if (1==1):
  with speech_recognition.WavFile("audio.wav") as source:
    _data = recognizer.record(source)  # read the entire WAV file
    print(_data)
    print(type(_data))
    # recognize speech using Google Speech Recognition
  try:
    text = recognizer.recognize_google(_data)
      # print recognizer.recognize_google(_data, show_all=True)
  except speech_recognition.UnknownValueError:
      # print(" | error: could not understand audio (empty input?)")
    print_debug('asr | (empty)\n')
    text = ''
print(text.decode("utf-8"))

return jsonify(
    data=text
    )


# @app.route('/file', methods=['POST'])
# @cross_origin()
# def post1():
#     with open("file.wav", "wb") as vid:
#         vid.write(request.data)

#     proc = subprocess.Popen(
#         "deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio file.wav",
#         shell=True, stdout=subprocess.PIPE, )
#     output = proc.communicate()[0]
#     print(output)

#     return jsonify(
# 	username=output
#     )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
