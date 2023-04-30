# textileclip
Copying tables in Textile style

## Overview

This script converts the table (Excel, HTML) in the clipboard to a table in Redmine (Textile) format.
It supports IronPython 2.

## Usage

Copy the table to the clipboard and run the script. It will overwrite the clipboard with a table in Textile style.

## Implementation

The script uses Python to extract the HTML table from the clipboard. It uses IronPython's CLR integration.
It extracts the table tag from the HTML using HTMLParser and converts it to a table format with Textile tags.
It reproduces the merged cells.
It adds a special tag for the header row.
It overwrites the clipboard with a table in Textile format.
It supports Unicode encoding.

## Future plans

- color
- class, style
- merged header row
- reverse conversion