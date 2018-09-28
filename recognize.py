#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shahzeb Afroze
@author: Islam Azeddine Mennouchi

External Github Projects used: MITESHPUTHRANNEU/Speech-Emotion-Analyzer

This script will classify the current input to select an appropriate song.
If you have a recorded file, comment out the Live Demo and change the name for "file" variable.

Todo list:
Songs API
Train Song and classify for emotion
Create a relational database 
How to set up a different microphone(eatphones) so that song played doesnt mess it up.
Link it with how it would relate to the song being played
Currently assuming one customer in mind.

It might be a good idea to break the features

"""
import librosa
import librosa.display
import numpy as np
import matplotlib as mpl
import subprocess
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.pyplot import specgram
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Input, Flatten, Dropout, Activation
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import wave
from keras.models import model_from_json
import data_extraction
import speech_recognition as sr
import time 

t0 = time.time()

# ----------------------------------------------- LIVE DEMO ------------------------------------------ 

import pyaudio


CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 44100 #sample rate
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "output11.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
                
                

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:

	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))

# ----------------------------------------- SENTIMENTAL ANALYSIS ------------------------------------

# Live Demo
file = "output11.wav"

# File Demo
# file = input("Which data set would you like to use?")

subprocess.call(["afplay", file])

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
lb = LabelEncoder()

# load weights into new model
loaded_model.load_weights("saved_models/Emotion_Voice_Detection_Model.h5")
print("Loaded model from disk")
opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)

# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

data, sampling_rate = librosa.load(file)
X, sample_rate = librosa.load(file, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
sample_rate = np.array(sample_rate)
mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
featurelive = mfccs
livedf2 = featurelive
livedf2= pd.DataFrame(data=livedf2)
livedf2 = livedf2.stack().to_frame().T

twodim= np.expand_dims(livedf2, axis=2)
livepreds = loaded_model.predict(twodim,
						 batch_size=32,
						 verbose=1)

livepreds1=livepreds.argmax(axis=1)
liveabc = livepreds1.astype(int).flatten()

# classification of the the person.
feeling_list = ["female_angry","female_calm",
			"female_fearful","female_happy",
			"female_sad","male_angry",
			"male_calm","male_fearful",
			"male_happy","male_sad"]

feeling = feeling_list[liveabc[0]]

print("\nAnalysis: " + feeling + "\n")

# Use the excel sheet as a relational database to select a song
data_extraction.required(feeling)

# ----------------------------------------- VOICE FEATURES ------------------------------------

output = ""

while not "stop" or not "mute" in output:

	 harvard = sr.Recognizer()

	 with sr.Microphone() as source:
		
			harvard.adjust_for_ambient_noise(source)
			print("Voice Command")
			audio = harvard.listen(source)
			print("analyzing...")

	 try:
			 output = harvard.recognize_google(audio)

	 except sr.UnknownValueError:
			 print("Google Speech Recognition could not understand audio")

	 except WaitTimeoutError:
			print("Say something")

	 print("You said: " + output)

	 if "next song" in output:
			print("Your wish is my command!")
			print()
			data_extraction.required(feeling)
			print()

	 if "download" in output:
	 	print("Check you email in a few seconds. Enjoy!!")
	 	data_extraction.prep()
	 	
	 speech_content = {"text": output }

t1 = time.time()
total = str(t1 - t0)
print(total)
email_invoice.server.quit()



# ------------------------------------------- ENDS -----------------------------------------
