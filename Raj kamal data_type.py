# string data type
import math
# literal assignment
first = "Raj"
last = "Kamal"

#print(type(first))
#print(type(first) = str)
#print(isinstance(first, str))

# constructer function
# pizza = str("pepperoni")
# print(type(pizza)) = str)
# print(isinstance(pizza, str))
# print(isinstance(pizza, str))

# concatenation
Rajkamal = first + "  " + last
print(Rajkamal)

Rajkamal += " ! "
print(Rajkamal)

#casting a number to a string
decade = str(2003)
print(decade)
print(decade)

statement = " I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = " "
"Hey", "how" "are" "you"

"I" "was" "just" "checking in"
"All" "good"

" " 
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nwhere\ "s this at\\located?'
print(sentence)

# string methods

print(first)
print(first.lower)
print(first.upper)
print(first)

print(multiline.title)
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += ''
multiline = ''
print(len(multiline))

print(len(multiline.strip))
print(len(multiline.strip))
print(len(multiline.strip))

print(" ")

# build a menu
title = "menu".upper()
print(title.centre(20, "="))
print("coffee".ljust(16, ".")) + "$1".rjust(4)
print("muffin".ljust(16, ".")) + "$" .rjust(4)
print("cheesecake". ljust(16, ".")) + "$4" .rjust(4)

print(" ")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("d"))
print(first.endswith("z"))


#boolean data type
myvalue = "true"
x= bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numneric data types

#interger type
price = 100
# best price = int(80)
print(type(price))
print(isinstance("best_price", int))

#float type
gpa = 3,28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value)
print(comp_value.img)

# Built-in function for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print(round(gpa, 1))


print(math).pi
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attemt to cast incorrect data
zip_value = int("new york")