#!/usr/bin/env python
import Image
import importlib

improvers = (
	'improvers.remove_garbage_words',
	'improvers.remove_garbage_lines',
	'improvers.improve_charset',
	'improvers.clean_line_breaks',
	'improvers.clean_spaces',
)

_improvers = [importlib.import_module(improver_module).improver for improver_module in improvers]


def tesseract(path):
	from lib.tesseract import image_to_string
	return image_to_string(Image.open(path), lang='fra')

def tesseractpp(path):
	text = tesseract(sample)

	for improver in improvers:
		text = improver(text)

	return text