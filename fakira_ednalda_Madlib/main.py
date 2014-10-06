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

