from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot (name = 'PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation', 'chatterbox.logic.BestMatch'])
small_talk = ["Hi, there!",
"Hi!",
"How do you do?",
"How are you?",
"I'm cool",
"Fine, you?",
"Always cool",
"I'm OK",
"Glad to hear that!",
"I'm fine.",
'I feel fine',
"I feel awesome",
"Excellent, great to hear that",
"Not so good",
"Sorry, to hear that",
"What's your name?",
"I'm PyBot. Ask me a maths question, please"
]
math_talk_1 = ['Pythagorean theorem', 'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines', 'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2): list_trainer.train(item)

print(my_bot.get_response("Hi!"))#How do you do?
print(my_bot.get_response("I feel awesome today!"))#Excellent, glad to hear that.
print(my_bot.get_response("What's your name?"))#I/'m PyBot.Ask me a maths question, please.
print(my_bot.get_response("Show me pythagorean theorem"))#a squared plus b squared equals c squared.
print(my_not.get_response("Do you know the law of cosines?"))#**2 = a**2 + b**2 -2 * a * b * cos(gamma)





