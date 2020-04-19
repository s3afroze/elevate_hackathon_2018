#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shahzeb Afroze

This uses the excel file as a quering database.

Have to make a list of songs being played and use jinja to make a list
Need to change the name of the music so that they appear properly in email.
Either we can make a new list and go on to join them later in the code
or we can go on to change the name of the files

we can integrate the invoice code snippet and send a much neater email


"""

import pandas as pd
import time
import os
import random
import subprocess
from pygame import mixer
# import email_invoice # remove comment once login information has been entered
import prepare_email

# --------------------------------------- Start Recording Time -------------------------------------- #

t0 = time.time()
pd.set_option('colheader_justify', 'center')
pd.options.mode.chained_assignment = None  # default='warn'

# ------------------------------ Excel Data Extraction For Customer Invoices ------------------------ #

file = "Music_list & customer_info.xlsx"

X = pd.read_excel(file,index_col=False)

# ---------------------------------------- Variables Needed ---------------------------------------- #

# Column headers goes here
theme = 'TYPE'
song = 'SONG'

n = 0

# temp database
features = [ theme, song ]

raw = X[ features ]

# ---------------------------------- Grouping Dataframe  ------------------------------------------- #

theme_gb = X.groupby(theme)

# ------------------------------- Preparing Information For Email --------------------------------- #

songs_played = []

def required(mood):

	# divide and conquer
	mood_songs = theme_gb.get_group(mood)
	list_of_songs = list(mood_songs[song])

	# extract the song list
	count = len(list_of_songs)
	n = random.randint(0, count-1)

	# play song
	file = list_of_songs[n] + ".mp3"

	audio_file = os.path.join(os.getcwd(),"songs",file)
	print(audio_file)

	songs_played.append(file)

	# return_code = subprocess.call(["afplay", audio_file])
	mixer.init()
	mixer.music.load(audio_file)
	mixer.music.play()

	# ---------------------------- Table Variables ------------------------- #

def prep():

	client = "xyz"
	email = "xyz@gmail.com"

	html_body = prepare_email.magic(client,songs_played)

	email_invoice.send_message(email, html_body)

t1 = time.time()
total = str(t1 - t0)
number = str(n)
print('{} emails sent in {}'.format(number,total))
