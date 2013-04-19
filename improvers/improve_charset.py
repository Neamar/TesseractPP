# -*- coding: utf-8 -*-
"""
Remove lines containing only garbages, e.g. "Ë? È Ë  ï :".
They don't carry any informations, and are mostly errors occuring while reading manuscript text.
"""

import re

re_pipe_i = re.compile("([A-Z])\\|([A-Z])")
re_pipe_l_apostrophe = re.compile("\\|'", re.UNICODE)

def improver(text):
	# Use plain apostrophe, instead of typographic apostrophe
	text = text.replace("’", "'")
	
	text = re_pipe_i.sub('\\1I\\2', text)
	text = re_pipe_l_apostrophe.sub("l'", text)

	return text