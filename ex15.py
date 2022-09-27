#we call a function from the system specifically argv in this case
from sys import argv
#assignment of our argv
script, filename = argv
#calling the open() module
txt = open (filename)
#printing and asking for input in order to open the file, and thenn open the file\read it
print("Here's your file %r : " % filename)
print(txt.read())

#same as above
print("Type the file name again:")
file_again = input(">")
#opening the file again
txt_again = open(file_again)
#printing the contents of said file
print( txt_again.read())

#We did the study drills p56 is where we left off