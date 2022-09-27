x = "There are %d types of people." % 10 # the very first string!!!
binary = "binary" #string
do_not = "don't" #another one 
y = "Those who know %s and those who %s." % (binary, do_not) # more string

print(x)
print(y)

print("I said : %r." % x)
print("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke funny?!! %r" # And here we find a string

print(joke_evaluation % hilarious)

w = "This is the left side of ..." # we meet again string
e = " a string with right side." # oh, you too

print ( w + e) # a bigger string is printed here 