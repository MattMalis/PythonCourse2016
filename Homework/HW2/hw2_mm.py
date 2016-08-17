#!/usr/bin/python
# -* coding: utf-8 -*-

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
	title = hdr.get_text()
	hdr_str = str(hdr)
	#hdr_str = hdr.encode('utf-8')
	begin_address = hdr_str.find('href="/') + len('href="/')
	end_address = hdr_str[begin_address:].find('">')
	address = hdr_str[begin_address:begin_address+end_address]
	l = [title, address]
	petition_titles_addresses.append(l)

for p in petition_titles_addresses:
	p[1] = main_address+ p[1]
	
	
## functions takes an address for a petition
## 		returns a list: [published_date, num_signatures, issues_text]
def get_petition_info(petition_address):
	pet_page = urllib2.urlopen(petition_address)
	pet_soup = BeautifulSoup(pet_page.read(), 'html.parser')
	all_p = pet_soup.find_all('p')
	issue = all_p[1].get_text()
	#print "petition:  " + petition_address + "\n"
	#print issue + "\n"
	all_spans = pet_soup.find_all('span')	
	sig_span = ""
	for span in all_spans:
		span_text = str(span)
		#span_text = span.encode('utf-8')
		index = span_text.find('class="signatures-number')
		if index!=-1:
			sig_span+=span_text
			break
	sig_index = sig_span.find('>')+1
	endex = sig_span[sig_index:].find('<')
	sig_str = sig_span[sig_index:sig_index+endex]
	sig_no_commas = sig_str.replace(',','')
	signatures = int(sig_no_commas)
	#print "signatures: " + str(signatures) + '\n'
	all_h4 = pet_soup.find_all('h4')
	created_by = all_h4[0].get_text()
	begindex = created_by.find(" on ")
	date = created_by[begindex+4:]
	#print "date: " + date + '\n\n'
	return list([date, signatures, issue])
	
#count = 0
for p in petition_titles_addresses:
	#print "count: " + str(count) + '\n'
	#count +=1
	p_info = get_petition_info(p[1])
	for slot in p_info:
		p.append(slot) 


#c = codecs.open('petitions.csv', 'wb', encoding='UTF-8')
c = open('petitions.csv','wb')
#c_writer = codecs.csv.writer(c, encoding='UTF-8')
c_writer = csv.writer(c, encoding='utf-8')
c_writer.writerow(["Petition Title", "Date Published", "Number of Signatures", "Description"])

for p in petition_titles_addresses:
	#try:
	c_writer.writerow([p[0], p[2], p[3], p[4]])
	#except:
		#print p[0]
		#pass

c.flush()
c.close()