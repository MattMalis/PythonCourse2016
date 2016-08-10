class School(object):
	def __init__ (self, name):
		self.name = name
		self.roster = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]} ## can create with keys, or empty and add on keys as needed
	def enroll(self, name, grade):
		self.roster[grade].append(name)
		print "Added %s to the grade %s roster" %(name, grade)
	def printRoster(self, grade):
		print '\n'.join(self.roster[grade])
	def __str__(self):
		school_str = ''
		for grade in self.roster.keys():
			#if len(self.roster[grade])>0:
			school_str+= "Grade %s: %s \n" % (str(grade), ' '.join(sorted(self.roster[grade])  ))
		return school_str	
	def __repr__(self):
		return self.__str__()
 
washu = School("WUSTL")
washu.enroll('jimmy',3)
washu.enroll('jill',2)
washu.enroll('jack',4)
washu.enroll('jane', 3)

print washu
washu
		