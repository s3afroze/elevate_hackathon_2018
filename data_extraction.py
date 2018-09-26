#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shahzeb Afroze

threading is needed to run the program smoother
need to record the music being played

"""


# from pprint import pprint
import pandas as pd
# import prepare_email
# import email_invoice
import time
import os
import random
import subprocess
from pygame import mixer



# --------------------------------------- Start Recording Time -------------------------------------- #

t0 = time.time()
pd.set_option('colheader_justify', 'center')
pd.options.mode.chained_assignment = None  # default='warn'

# path = os.getcwd()
# os.chdir("..")

# ------------------------------ Excel Data Extraction For Customer Invoices ------------------------ #

file = "monthly_invoice.xlsx"

X = pd.read_excel(file,index_col=False)
# ---------------------------------------- Variables Needed ---------------------------------------- #


# Column headers goes here
theme = 'TYPE'
song = 'SONG'
artist = 'ARTIST'
email_address = 'EMAIL'

n = 0

# temp database
features = [ theme, song, artist, email_address ]
raw = X[ features ]


# ---------------------------------- Grouping Dataframe  ------------------------------------------- #

theme_gb = X.groupby(theme)

# ------------------------------- Preparing Information For Email --------------------------------- #

def required(mood):

	# divide and conquer
	mood_songs = theme_gb.get_group(mood)
	list_of_songs = list(mood_songs[song])

	# extract the song list
	count = len(list_of_songs)
	n = random.randint(0, count-1)

	# play song
	file = list_of_songs[n] +".mp3"

	audio_file = os.path.join(os.getcwd(),"songs",file)
	print(audio_file)

	return_code = subprocess.call(["afplay", audio_file])
	#return_code.kill()

# 	list_of_songs = mood_songs[song]

# 	# static info
# 	info = database_dict[ client ]

# 	email = info.get(email_address)
# 	parent_company = info.get(company)

# 	# dynamic info
# 	grouped = customer_gb.get_group(client).sort_values(by = [ sales ])
# 	total_amount_owed = grouped[sales].sum()

# 	drop_columns = [ company, email_address, customer ]
# 	customer_summary = grouped.drop(drop_columns, axis=1)

# 	variables_for_pdf = customer_summary.to_dict('list')

# 	# ---------------------------- Table Variables ------------------------- #

# 	# customer_summary.set_index(invoice, inplace=True)

# 	# # Column headers in-line/note there is a new index = False so no idea
# 	# customer_summary.columns.name = customer_summary.index.name
# 	# customer_summary.index.name = None

# 	# # Conversion & CSS setup
# 	# customer_summary_html = customer_summary.to_html(classes='mystyle')



# 	n+=1

# 	html_body, attachment = prepare_email.magic(client, email, parent_company, variables_for_pdf, total_amount_owed)

# 	email_invoice.send_message(email, html_body, attachment)

# 	t1 = time.time()

# total = str(t1 - t0)
# number = str(n)
# print('{} emails sent in {}'.format(number,total))
# email_invoice.server.quit()
