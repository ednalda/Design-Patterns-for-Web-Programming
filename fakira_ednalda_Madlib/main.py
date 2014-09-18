#3 Strings
first_name="Ednalda"
last_name="Fakira"
print last_name

name=raw_input("Enter your last name")
print name
print "Hello ", name

#array
books=["The Giver", "Violet are Blue"]
books.append("Picking Cotton")
print books [0]


#dictionary 
food = dict() 
food = {"fruit":"orange", "vegetable" : "spinach"}
print food["vegetable"]

#2 operation
'''
school_start = 2000
current_year = 2014
howLong= school_start - current_year
print "How long to graduate "+ str(howLong) + "years" 

chair = 20
table = 5
diningTable= chair * table
print "Inventory result is "+ str(diningTable)

'''

#2 conditional
'''
grade = 200
if grade > 90:
	college="nice"
	print "This" + college + "is coll!"
else:
	   print "No cool."
or
	salary= 200
if salary > 200:
	   life="good"
	print "My life is" + life 
elif salary > 80
	   print "My life is ok"
else:
	   print "I need to go back to school."

	'''

	#FUNCTION
    def calcArea(h,w):
	    area = h * w
	    return area
	    a = calcArea(50,40);
	    print "My house is " + str(a) + "sqft"

	#1 loop
	a = 0
    while a<20:
	    print "The count is", a
	    a = a+1
