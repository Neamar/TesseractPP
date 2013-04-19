"""
Remove multiple line consecutive line breaks.
Normalize for "\n" end line (no \r\n nonsense)
"""

import re

re_multiple_lines = re.compile("\n{2,}")
re_final_linebreak = re.compile("\n$")

def improver(text):
	text = text.replace("\r", '')
	text = re_multiple_lines.sub('\n', text)
	text = re_final_linebreak.sub('', text)

	return text