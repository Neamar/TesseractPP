"""
Remove multiple consecutive spaces
"""

import re

re_multiple_spaces = re.compile("\\s{2,}")

def improver(text):
	text = re_multiple_spaces.sub(' ', text)

	return text