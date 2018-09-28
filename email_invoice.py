#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shahzeb Afroze
https://myaccount.google.com/lesssecureapps?pli=1

This script will email with all the information created by "prepare email code"

"""
import smtplib
import random
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email_invoice

# ---------------------------------- Variables introduced here ---------------------------------- #

# Login information
user_email = 'EMAIL'
user_password = "PASSWORD"

# ---------------------------------- Making connection with server ---------------------------------- #

# Current smtp for gmail
print("Signing in")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user_email, user_password)

# ---------------------------------------------------------------------------------------------------- #
   
def send_message(email, html_body):
	
	msg = MIMEMultipart()

	msg['From'] = user_email
	msg['To'] = email
	msg['Subject'] = "List of songs"

	# ------------------------------- Email body fitted in ------------------------------- #

	msg.attach(MIMEText(html_body, 'html'))

	# ------------------------ Conversion and sent to SMTP -------------------------- #

	text = msg.as_string()

	server.sendmail(user_email, email, text)
	print('Message Sent')
	print()




