from sys import argv

script , first, second, third = argv

print("The script is called: ",script)
print("Your first variable is:",first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#python ex13.py first 2nd 3rd (is how you run this one precious)

#On line 1 we have what’s called an “import.” This is how you add features(Module/Libraries) to your script from the
#Python feature set. Rather than give you all the features at once, Python asks you to say what you
#plan to use. This keeps your programs small, but it also acts as documentation for other programmers who read your code later.
#The argv is the “argument variable,” a very standard name in programming that you will fi nd
#used in many other languages. This variable holds the arguments you pass to your Python script
#when you run it. In the exercises you will get to play with this more and see what happens.
#Line 3 “unpacks” argv so that, rather than holding all the arguments, it gets assigned to four
#variables you can work with: script, first, second, and third. This may look strange, but
#“unpack” is probably the best word to describe what it does. It just says, “Take whatever is in
#argv, unpack it, and assign it to all these variables on the left in order.”