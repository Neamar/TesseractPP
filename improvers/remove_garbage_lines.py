# -*- coding: utf-8 -*-
"""
Remove lines containing only garbages, e.g. "Ë? È Ë  ï :".
They don't carry any informations, and are mostly errors occuring while reading manuscript text.
"""

import re

# Only special characters
re_garbage_lines = re.compile("^[^A-Za-z0-9]+$", re.MULTILINE)
# Only a few characters
re_short_lines = re.compile("^.{1,3}$", re.MULTILINE)

def improver(text):
	text = re_garbage_lines.sub('', text)
	text = re_short_lines.sub('', text)

	return text