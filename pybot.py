from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot (name = 'PyBot', read_only=True, logic_adapters= ['chatterbot.logic.MathematicalEvaluation', 'chatterbox.logic.BestMatch'])
small_talk = ['Hi, there!',
              'Hi!',
              'How do you do?',
              'How are you?',
              'I\'m cool',
              'Fine, you?',
              'Always cool.',
              "I'm OK",
              "Glad to hear that!",
              "I'm fine."
              'I feel awesome!',
              'Excellent,glad to hear that',
              "Not so good",
              'sorry to hear that',
              "What's your name?",
              "I'm PyBot. Ask me a maths question, please"
              ]
             math_talk_1 =['Pythagorean theorem','a squared plus b squared equals c squared.']
             
             math_talk_2 = ['law of cosines',
                            'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']
              
              #We can create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings:
              #THIS PART TRAINS THE BOT!
              list_trainer = ListTrainer(my_bot)
              
              for item in (small_talk, math_talk_1, math_talk_2): list_trainer.train(item)
              
              #You can communicate with your bot using its method .get_response().
              
             
             >>> print(my_bot.get_response("Hi!"))How do you do?
              
              
              
              >>> print(my_bot.get_response("i feel awesome today"))
excellent, glad to hear that.
 >>> print(my_bot.get_response("what's your name?"))
i'm pybot. ask me a math question, please.
>>> print(my_bot.get_response("show me the pythagorean theorem"))
a squared plus b squared equals c squared.
>>> print(my_bot.get_response("do you know the law of cosines?"))
c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)
              
              