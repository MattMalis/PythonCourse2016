def make_ordinal(i):
	if (isinstance(i, float)):
		raise TypeError, "input value must be int, not float"
	i = int(i)
	if (isinstance(i, int)):
		suffixes = {1:"st", 2:"nd", 3:"rd", 4:"th"}
		digit = i%10;
		if not digit in {1, 2, 3}:
			digit = 4
		suf = suffixes[digit]
		return str(i)+suf

#print make_ordinal(42.35)
#print make_ordinal("a word")