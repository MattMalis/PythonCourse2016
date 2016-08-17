
def name_webpage_subfield(sib_a, fac_dict, sub):
	cur = str(sib_a)
	page_begin = cur.find('href="') + 6  ## 6=len('href="')
	page_end = cur[page_begin:].find('"')
	## find the closing " for the url
	personal_url = cur[page_begin:page_begin+page_end]
	full_personal_url = base_url + personal_url
	name_begin = page_begin+page_end+2
	name_end = cur[name_begin:].find("</a>")
	name = cur[name_begin:name_begin+name_end]
	subfield = sub
	subfield_url = tuple([subfield, full_personal_url])
	fac_dict[name] = subfield_url
	
	
subfields = soup.find_all('h3')

ticker = 1
print "\n\n\n\n\n"

for subfield in subfields:

	subfield_text = subfield.get_text()
	for sibling in subfield.next_siblings:
		if sibling in subfields:
			break
		else: 
			try: ## some of the siblings will not be the right type of object
				## skip over those
				## but if it's the right type, find the a
				sib_a = sibling.find_all('a')
				name_webpage_subfield(sib_a, fac_name_url_dict, subfield_text)
				#print "ticker: " + str(ticker) + '\n'
				#ticker+=1
			except:
				pass
				