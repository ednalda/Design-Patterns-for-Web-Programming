#3 capturing Strings
first_name = "Ednalda"
last_name = "Fakira"
print first_name + last_name #print variables to show complete name


name = raw_input("Enter your last name")
print name
print "Hello ", name #print  message + variable that holds name

city = 'orlando'
state = 'Florida'
message = your city is {city} and your state is {state} #passing values city and state to variable  message 
message = message.format (**locals()) #to accept all locall format 
print message #print variable message


#array
books = ["The Giver", "Violet are Blue"]
books.append("Picking Cotton") #insert a new book to the end of the array
print books [0]#choose which book to print by the position on the array


# creatin a dictionary object for types of food
food = dict() 
food = {"fruit":"orange", "vegetable" : "spinach"}
print food["vegetable"]

#2 operation
#calculating how long to finish school
school_start = 2000 #variable that holds the start school year
current_year = 2014 #variable that holds the end school year
howLong = school_start - current_year #variable that holds the operation to calculate how long to finish school
print "How long to graduate  " + str(howLong) + "years" 

#calculating iventory
chair = 20
table = 5
diningTable = chair * table #variable that calculates how many dining room sets
print "Inventory result is  " + str(diningTable) #to print message + variable diningTable, strings "chair" and "table" need to be specified



#2 conditional
#checking how life is good!
grade = 100 #top grade in class
if  grade > 90: #if grade is more than 90, print variable college
    college = "nice"
    print "This" + college + "is coll!"
else: #if not the condition above, print "No cool."
	print "No cool."

	or
salary = 250 #top salary
if  salary > 200: #if salary is more than $200,000 print variable life
	life = "good"
	print "My life is" + life 

elif salary > 80 #if salary is more than $80,000 print "My lif is ok"
	print "My life is ok"
else: #if none the conditions above print "I need to go back to school."
	print "I need to go back to school."



#FUNCTION
x=4 # empty land
def calcArea(h,w):#function t calculate the area of a house
	area = h * w #hight * width
	return area + x #return total house area occupied 
	a = calcArea(50,40);#values of h and w
	print "My house is " + str(a) + "sqft"


#WHILE LOOP
a = 0 #Start variable a=0
while a<20: #count how many pages a user reads untill reach 19 pages. 
print "The count is", a
a = a+1 #add next page 
