def make_ordinal(i):
	if (isinstance(i, float)):
		raise TypeError, "input value must be int, not float"
	if (isinstance(i, str)):
		raise TypeError, "input value must be int, not string"
	if (isinstance(i, int)):
		if (i<0):
			raise Exception, "can't ordinalize a negative number"
		suffixes = {1:"st", 2:"nd", 3:"rd", 4:"th"}
		teens = ( (i%100) >10 and (i%100 <20) )
		if (teens):
			suf = suffixes[4]
		else: 
			digit = i%10;
			if not digit in {1, 2, 3}:
				digit = 4
			suf = suffixes[digit]
		return str(i)+suf

#print make_ordinal(42.35)
#print make_ordinal("a word")