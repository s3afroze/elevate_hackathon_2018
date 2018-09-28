#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Shahzeb Afroze

"""
import sys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import random
import datetime
from pprint import pprint

# Introducing a new environment for Jinja2
env = Environment(loader=FileSystemLoader('.'))

# --------------------------------- Preparing Email Template  ----------------------------------- #
def magic(name,songs_played):

	# Introduce your files here
	temp_email = "songs_played.html"

	name_title = name.title()
	name_caps = name.upper()
	name_lower = name.lower()

	length = len(songs_played)

	email_body = env.get_template(temp_email)

	template_vars_email = {"name" : name_title,
							"length": length,
							"songs_played":songs_played}

	# Rendering the template from the environment
	html_body = email_body.render(template_vars_email)

	# ------------------------------- Debugging ------------------------------------- #

	# with open("email_in_html.html", "w") as fh:
	# 	fh.write(html_body)

	# ------------------------------------------------------------------------------- #

	return html_body
