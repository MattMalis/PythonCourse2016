import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
for line in text:
  if not keyword.search(line):
    print line 

# TODO: print lines that contain a word of any length starting with s and ending with e
  # pattern = re.compile(r'(\d*)\s(\w*)')# looks for digits, then whitespace, then characters
# pattern = re.compile(r'^b\w*',re.MULTILINE)

keyword = re.compile(r'\ss\w*e\s') #or:
keyword = re.compile(r'\bs\w*e\b')
  
date = raw_input("Please enter a date in the format MM.DD.YY: ")
pat = re.compile(r'(?P<MM>\d.)\.(?P<DD>\d.)\.(?P<YY>\d.)')
srchr = pat.search(date)
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY

date = raw_input("Please enter a date in the format MM.DD.YY: ")
pat = re.compile(r'(?P<Month>\d.)\.(?P<Day>\d.)\.(?P<Year>\d.)')
kywrd = re.compile(r'(\d\d?)\.(\d\d?)\.(\d\d))
srchrr = 
srchr = pat.search(date)
srchr.groupdict()

# TODO: Write a regular expression that finds html tags in example.html and print them.
file_html=open('Docket05-1.html','r')
text = file_html.readlines()
file_html.close()
tag = re.compile(r'<*>')
# TODO: Scrape a website and search for some things...


