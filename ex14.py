from sys import argv

script, user_name, TheScript = argv #argv means putting the input on the command line while running the script
prompt ='>' #prompt here is given as >, we can change it to anything.It's a String
script
print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s" % user_name)
lives = input(prompt)

print("What kind of a computer do you have?")
computer = input(prompt)



print ( """
Alright, so you said %r about liking me.
You live  in %r. Not sure where that is.
And you have an %r computer. Nice!
""" % (likes, lives, computer))
print("This is MY script :  ", TheScript)