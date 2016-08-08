from sys import argv

#script, first, second, third = argv

#print "script:" , script,
#print ", first:", first,
#print ", second:", second, 
#print ", third:", third

#print("merp" + """ merp, continued
#onto
#another line""")
#for i in range(1,10):
#	print i

#print "Give me a number: ",
#n = raw_input()
#print "and one more",
#m = raw_input()
#print "You told me %r, but you also said %r." % (n, m)
a = 5
b=10
c=20
d=100

#f = "5 + %r"
#g = (f % 20)
#print g
#print "add up %r and %d and %r and %d to get %r." % (a, b, c, d, a+b+c+d)

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
