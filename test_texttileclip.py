#!/usr/bin/env ipy
# -*- coding: utf-8 -*- #

import unittest
import textileclip

class TestTextileClip(unittest.TestCase):
    def setUp(self):
        self.parser = textileclip.HtmlTableParser()

    def test_one_cell(self):
        html = r"""<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link id=Main-File rel=Main-File
href="file:///C:/Users/User/AppData/Local/Temp/msohtmlclip1/01/clip.htm">
<link rel=File-List
href="file:///C:/Users/User/AppData/Local/Temp/msohtmlclip1/01/clip_filelist.xml">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
x\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]-->
<style>
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .71in .75in .71in;
	mso-header-margin:.31in;
	mso-footer-margin:.31in;
	mso-page-orientation:landscape;}
.font5
	{color:black;
	font-size:9.0pt;
	font-weight:700;
	font-style:normal;
	text-decoration:none;
	font-family:"ＭＳ Ｐゴシック", monospace;
	mso-font-charset:128;}
.font6
	{color:black;
	font-size:9.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:"ＭＳ Ｐゴシック", monospace;
	mso-font-charset:128;}
tr
	{mso-height-source:auto;
	mso-ruby-visibility:none;}
col
	{mso-width-source:auto;
	mso-ruby-visibility:none;}
br
	{mso-data-placement:same-cell;}
td
	{padding:0px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:游ゴシック, monospace;
	mso-font-charset:128;
	mso-number-format:General;
	text-align:general;
	vertical-align:middle;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl65
	{font-size:8.0pt;}
.xl66
	{font-size:8.0pt;
	mso-number-format:"0_\)\;\[Red\]\\\(0\\\)\;\0022\0022\;\0022\0022";}
ruby
	{ruby-align:left;}
rt
	{color:windowtext;
	font-size:6.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:游ゴシック, monospace;
	mso-font-charset:128;
	mso-char-type:katakana;
	display:none;}
-->
</style>
</head>

<body link="#0563C1" vlink="#954F72">

<table border=0 cellpadding=0 cellspacing=0 width=18 style='border-collapse:
 collapse;width:14pt'>
 <col width=18 style='mso-width-source:userset;mso-width-alt:576;width:14pt'>
 <tr height=25 style='height:18.75pt'>
<!--StartFragment-->
  <td height=25 class=xl66 align=right width=18 style='height:18.75pt;
  width:14pt;font-size:8.0pt;color:black;font-weight:400;text-decoration:none;
  text-underline-style:none;text-line-through:none;font-family:游ゴシック, sans-serif;
  mso-font-charset:128;background:#92D050;mso-pattern:black none'>3 </td>
<!--EndFragment-->
 </tr>
</table>

</body>

</html>
"""
        expected = """table{background-color: #FFFFFF; color: #333333}.
{background-color: #CCCCCC}. |_>. 3 |
"""
        self.parser.feed(html)
        self.assertEqual(self.parser.table, expected)

if __name__ == "__main__":
    unittest.main()
