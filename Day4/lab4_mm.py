#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read(),"html.parser")

base_url = 'https://polisci.wustl.edu'

fac_name_url_dict = {}


def name_webpage_subfield(sib_div, fac_dict, sub):
	cur = str(sib_div)
	page_begin = cur.find('href="') + 6  ## 6=len('href="')
	page_end = cur[page_begin:].find('"')
	personal_url = cur[page_begin:page_begin+page_end]
	full_personal_url = base_url + personal_url
	name_begin = page_begin+page_end+2
	name_end = cur[name_begin:].find("</a>")
	name = cur[name_begin:name_begin+name_end]
	job_begin = cur.find("</strong>") + 24 ### counted it out manually
	job_end = cur[job_begin:].find("    </div>")
	job = cur[job_begin:job_begin+job_end]

	subfield = sub
	if full_personal_url != base_url:
		subfield_url = [subfield, full_personal_url, job]
		fac_dict[name] = subfield_url
	

subs = soup.find_all('h3')

ticker = 1
print "\n\n\n\n\n"

for subfield in subs:
	subfield_text = subfield.get_text()
	for sibling in subfield.next_siblings:
		if sibling in subs:
			break
		else: 
			try: ## some of the siblings will not be the right type of object
				## skip over those
				## but if it's the right type, find the a
				
				name_webpage_subfield(str(sibling), fac_name_url_dict, subfield_text)

			except:
				pass
				
#####################
	
print "len(fac_nam_url_dict): " + str(len(fac_name_url_dict)) + '\n'
keys = fac_name_url_dict.keys()

def get_email(full_page_str):
	f = full_page_str
	email_start = f.find("mailto:")+len("mailto:")
	email_end = f[email_start:].find('">')
	email = f[email_start:email_start+email_end]
	return email

def get_website(full_page_str):
	f = full_page_str
	web_pre = f.find("website")
	if web_pre==-1: ## if 'website' is not found on the page (ie there is no link to a different personal web page)
		return '0'
	web_start = f[web_pre:].find('href="')
	web_real_start = web_pre+web_start+len('href="')
	web_end = f[web_real_start:].find('"')
	web = f[web_real_start:web_real_start+web_end]
	return web

for key in keys:
	address = fac_name_url_dict[key][1]
	page = urllib2.urlopen(address)
	fac_soup = BeautifulSoup(page.read(), 'html.parser')
	fac_text = str(fac_soup)
	email = get_email(fac_text)
	fac_name_url_dict[key].append(email)
	web = get_website(fac_text)
	if web=='0':## if another website was not found (in the get_website method)
		fac_name_url_dict[key].append(fac_name_url_dict[key][1]) ## use the original page for that faculty member
	else:
		fac_name_url_dict[key].append(web)

fac_dict = fac_name_url_dict
	
for key in keys:
 	print str(key) + ": " + fac_dict[key][0]+ ", " + fac_dict[key][1]  + ", " + fac_dict[key][2] + ", " + fac_dict[key][3] +", " + fac_dict[key][4] +'\n'


c = open('faculty.csv', 'wb')
c_writer = csv.writer(c)
c_writer.writerow(["Name", "Title", "Subfield", "Website", "E-mail"])

for key in keys:
	c_writer.writerow([key, fac_dict[key][2], fac_dict[key][0], fac_dict[key][4], fac_dict[key][3]])

c.flush()
c.close()
