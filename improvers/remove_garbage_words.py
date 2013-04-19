# -*- coding: utf-8 -*-
"""
Remove words containing only garbages, e.g. "Ë?ÈËï:".
They don't carry any informations, and are mostly errors occuring while reading manuscript text.
"""

import re

#Only special characters
re_garbage_word = re.compile("(^|\s)([^A-Za-z0-9à/]+)(\s|$)")

def improver(text):
	text = re_garbage_word.sub('\\1\\3', text)

	return text