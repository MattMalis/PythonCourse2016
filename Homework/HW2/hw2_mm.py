from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import unicodecsv as csv
import codecs

main_address = 'https://petitions.whitehouse.gov/'
main_page = urllib2.urlopen(main_address)
main_soup = BeautifulSoup(main_page.read(), 'html.parser')

all_h3 = main_soup.find_all('h3')
petition_titles_addresses = []
for hdr in all_h3[3:]:
	## all h3 headers after the first three consist only of petition titles with links
	title = hdr.get_text() ## get_text extracts only the titles
	## to get the url address:
	hdr_str = str(hdr)
	begin_address = hdr_str.find('href="/') + len('href="/')
	end_address = hdr_str[begin_address:].find('">')
	this_address = hdr_str[begin_address:begin_address+end_address]
	full_address = main_address + this_address
	l = [title, full_address]
	petition_titles_addresses.append(l)


## functions takes an address for a petition
## 		returns a list: [published_date, num_signatures, issues_text]
def get_petition_info(petition_address):
	pet_page = urllib2.urlopen(petition_address)
	pet_soup = BeautifulSoup(pet_page.read(), 'html.parser')
	all_p = pet_soup.find_all('p')
	## petition main text is always in the second <p> tag
	issue = all_p[1].get_text()
	
	all_spans = pet_soup.find_all('span')	
	sig_span = ""
	for span in all_spans:
		span_text = str(span)
		index = span_text.find('class="signatures-number') ## if text not found, .find() will return -1
		if index!=-1: 
			sig_span+=span_text
			break
	sig_index = sig_span.find('>')+1
	endex = sig_span[sig_index:].find('<')
	sig_str = sig_span[sig_index:sig_index+endex]
	sig_no_commas = sig_str.replace(',','')
	signatures = int(sig_no_commas)

	all_h4 = pet_soup.find_all('h4')
	## the first h4 header on each page takes the format: "Created by __ on [date]"
	created_by = all_h4[0].get_text()
	begindex = created_by.find(" on ")
	date = created_by[begindex+4:]

	return list([date, signatures, issue])
	
	
for p in petition_titles_addresses:
	## adding the date, signatures, and issue text to the lists already containing title and url
	p_info = get_petition_info(p[1])
	for slot in p_info:
		p.append(slot) 

c = open('petitions.csv','wb')
c_writer = csv.writer(c, encoding='utf-8') ## without the encoding, get an error (the subsection symbol does not translate to ascii)
c_writer.writerow(["Petition Title", "Date Published", "Number of Signatures", "Description"])

for p in petition_titles_addresses:
	try:
		c_writer.writerow([p[0], p[2], p[3], p[4]])
	except:
		print "ERROR: " + p[0] + '\n'
		pass

c.flush()
c.close()