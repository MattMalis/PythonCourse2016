from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv

main_address = 'https://petitions.whitehouse.gov/'
main_page = urllib2.urlopen(main_address)
main_soup = BeautifulSoup(main_page.read(), 'html.parser')

all_h3 = main_soup.find_all('h3')

non_header_sibs = []

for header in all_h3:
	for sibling in header.next_sibling:
		if sibling in all_h3:
			break
		else:
			non_header_sibs.append(sibling)