# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os
import json
import pyttsx3
import speech_recognition
import wave

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
	recognizer = speech_recognition.Recognizer()
	file = request.files['file']
	filename = file.filename
	file.save(os.getcwd() + r"\storage" + r'\\' + filename)
	with speech_recognition.WavFile(os.getcwd() + r"\storage" + r'\\' + filename) as source:
		data = recognizer.record(source)
		text = recognizer.recognize_google(data, language='vi-VN')
		unicodeStr = u""+text
	return (unicodeStr)
if __name__ == '__main__':
	app.run(debug=True)
