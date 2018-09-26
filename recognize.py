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
import threading
import speech_recognition as sr


#++++++++++++++++++++++++++Next Thread +++++++
class Listen(object):


    def __init__(self, feeling,interval=1,):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.feeling = feeling

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        output = ""
        while not "stop" in output:
           harvard = sr.Recognizer()

           with sr.Microphone() as source:
              print("Rec")
              audio = harvard.listen(source)
              print("audio recording")
           try:
               output = speech.recognize_google(audio)
           except sr.UnknownValueError:
               print("Google Speech Recognition could not understand audio")
           print(output)
           if "next" in output:
           	  print("next")
           	  data_extraction.required(self.feeling)
           if "mute" in output:
              print(2)
           speech_content = {"text": output }


#++++++++++++++++++++++++++++++++++++++++++++++

# --------------------------------- Needed to make changes if you want to play -----------------------------------
# import pyaudio

# CHUNK = 1024
# FORMAT = pyaudio.paInt16 #paInt8
# CHANNELS = 2
# RATE = 44100 #sample rate
# RECORD_SECONDS = 4
# WAVE_OUTPUT_FILENAME = "output11.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK) #buffer

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data) # 2 bytes(16 bits) per channel

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

# loading json and creating model

# ------------------------------------------- ENDS -------------------------------------------------------

file = 'output10.wav'

# UNCOMMENT & ASK
file = raw_input("Which data set would you like to use?")

# It is to be noted that both of the file is being currently used with IBM API and


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
#score = loaded_model.evaluate(x_testcnn, y_test, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
data, sampling_rate = librosa.load(file)
#livedf= pd.DataFrame(columns=['feature'])
X, sample_rate = librosa.load(file, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
sample_rate = np.array(sample_rate)
mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
featurelive = mfccs
livedf2 = featurelive
livedf2= pd.DataFrame(data=livedf2)
livedf2 = livedf2.stack().to_frame().T
livedf2
twodim= np.expand_dims(livedf2, axis=2)
livepreds = loaded_model.predict(twodim,
						 batch_size=32,
						 verbose=1)
livepreds1=livepreds.argmax(axis=1)
liveabc = livepreds1.astype(int).flatten()

# classification of the the person.
feeling = ["female_angry","female_calm","female_fearful","female_happy","female_sad","male_angry","male_calm","male_fearful","male_happy","male_sad"]
print(liveabc[0])
print("\nAnalysis: " + feeling[liveabc[0]] + "\n")
print(type(feeling[liveabc[0]]))
#liste = Listen(feeling[liveabc[0]])
data_extraction.required(feeling[liveabc[0]])



# ------------------------------------------- ENDS -----------------------------------------



# GARBAGE
#livepredictions = (lb.inverse_transform((liveabc)))
#livepredictions
