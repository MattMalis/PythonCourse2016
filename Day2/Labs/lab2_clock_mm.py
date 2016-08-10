class Clock(object):
    def __init__(self, hour, minutes):
        hour+= int(minutes)/60
        minutes = minutes%60
        if (hour>=0):
	        hour = hour%24
        self.minutes = minutes
        self.hour = hour

		
    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
    	if (self.hour<0 or self.minutes<0):
			return("Warning: hours and minutes must be >=0")
    	am = True;
    	clock_string = ''
    	if (self.hour==0):
    		clock_string+='12'
    	elif (self.hour>12):
    		hour12 = self.hour-12;
    		clock_string += str(hour12)
    		am = False;
    	else:
    		clock_string+= str(self.hour)
    	if (am):
    		am_str = 'AM'
    	else:
    		am_str = 'PM'
    	min_str = str(self.minutes)
    	if (self.minutes <=10):
    		min_str = '0'+min_str
    	clock_string+= ":%s %s" %(min_str, am_str)
    	return clock_string
    	
    def __add__(self,minutes):
    	#if minutes<0:
    #		return self.__sub__(-minutes)
    	self.minutes+=minutes
    	if self.minutes >=60:
    		self.hour += int(self.minutes)/60
    		self.minutes = self.minutes%60
    	elif self.minutes <0:
    		self.hour += int(self.minutes)/60
    		self.minutes = self.minutes%60
    	self.hour = self.hour%24
    	return self
    	
    def __sub__(self,minutes):
    	return self.__add__(-minutes)
    	
    def __eq__(self, other):
    	return (self.hour==other.hour and self.minutes == other.minutes)
    def __ne__(self, other):
		return not(self.__eq__(other))
		
c1 = Clock(13,63)
print "Clock(13,63): ", c1
c2 = Clock(100, 5)
print "Clock(100, 5): ", c2
c3 = Clock(-4, 20)
print "Clock(-4, 20): " , c3
c4 = Clock(17,0)
print "Clock(17,0): " , c4
c4.__add__(75)
print "c4.__add__(75): ", c4
c1.__sub__(30)
print "c1.__sub__(30): " , c1
print "c2.__eq__(Clock(4,65)): " , c2.__eq__(Clock(4,65))
print "c2.__eq__(c3): " , c2.__eq__(c3)
print "c2.__ne__(c3): " , c2.__ne__(c3)

print "c4+30: " , c4+30
print "c4+800: ", c4+800