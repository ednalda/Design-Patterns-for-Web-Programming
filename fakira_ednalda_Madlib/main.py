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


