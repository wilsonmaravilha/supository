# -*- coding: utf-8 -*-
import re

#
# Returns the slug of a string
#
def slugify(text_str):
	text_str = (text_str).lower()
	return re.sub(r'\W+','-',text_str)