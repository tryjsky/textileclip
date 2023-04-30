#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# Copyright 2023 Y., Ryota <tryjsky@gmail.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Clipboard, TextDataFormat
from HTMLParser import HTMLParser
import re


class HtmlTableParser(HTMLParser):
	def __init__(self):
        	HTMLParser.__init__(self)
		self.table = ""
		self.table_depth = 0
		self.td_depth = 0
		self.row = []
		self.use_header = True
		self.is_header = False

	def handle_starttag(self, tag, attrs):
		if tag == "table":
			self.table_depth += 1
			if self.table_depth != 1:
				return
			self.table += "table{background-color: #FFFFFF; color: #333333}.\n{background-color: #CCCCCC}. "
			self.is_header = self.use_header
		elif tag == "tr":
			if self.row:
				self.table += "|" + "|".join(self.row) + "|\n"
				self.row = []
				self.is_header = False
		elif (tag == "th" or tag == "td"):
			self.td_depth += 1
			if self.row:
				self.row.append("")
			dictattrs = dict(attrs)
			attr = ""
			if self.is_header:
				attr += "_"
			if "colspan" in dictattrs:
				attr += "\\" + dictattrs["colspan"]
			if "rowspan" in dictattrs:
				attr += "/" + dictattrs["rowspan"]
			if "align" in dictattrs and dictattrs["align"] == "left":
				attr += "<"
			if "align" in dictattrs and dictattrs["align"] == "right":
				attr += ">"
			if "align" in dictattrs and dictattrs["align"] == "center":
				attr += "="
			if attr:
				attr += ". "
			else:
				attr = " "
			if self.row:
				self.row[-1] += attr
			else:
				self.row.append(attr)

	def handle_endtag(self, tag):
		if tag == "table":
			self.table_depth -= 1
			if self.table_depth != 0:
				return
			if self.row:
				self.table += "|" + "|".join(self.row) + "|\n"
				self.row = []
				self.is_header = False
		elif tag == "tr":
			pass
		elif (tag == "th" or tag == "td"):
			self.td_depth -= 1

	def handle_data(self, data):
		if self.table_depth != 1:
			return
		if self.td_depth == 1:
			if self.row:
				self.row[-1] += re.sub(r"^\n\s+", r"\n", data)
			else:
				self.row.append(data)
		

def get_html():
	cliplines = Clipboard.GetText(TextDataFormat.Html).splitlines()
	line = 0
	for clip in cliplines:
		if (clip.startswith("Version:")
				or clip.startswith("StartHTML:")
				or clip.startswith("EndHTML:")
				or clip.startswith("StartFragment:")
				or clip.startswith("EndFragment:")
				or clip.startswith("SourceURL:")
				or clip == ""):
			# header part
			line = line + 1
		else:
			# body part
			return "\n".join(cliplines[line:])
	# empty body
	return ""


def set_text(text):
	if text:
		Clipboard.SetText(text)


def main():
	if Clipboard.ContainsText(TextDataFormat.Html):
		html = get_html()
		#sys.stdout.write(html)
		parser = HtmlTableParser()
		parser.feed(html)
		sys.stdout.write(parser.table)
		set_text(parser.table)


main()