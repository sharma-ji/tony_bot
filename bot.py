#importing the aiml module
import aiml
kernel= aiml.Kernel() #initiating the Kernel
kernel.bootstrap(brainFile = "bot_brain.brn") #since I have already optimised the files for you so now you need to only include the brain file
'''set predicates for your bot name, hometown, gender and so on.............
 alo you can set the user predicted by using 
 kernel.setBotPredicate()
 And you can set the sessionID for custom chat behaviour'''

kernel.setBotPredicate("hometown", "127.0.0.1") 
kernel.setBotPredicate("name", "Tony")
kernel.setBotPredicate("master", "Sharmaji")
kernel.setBotPredicate("gender", "Male")
while True:
   print kernel.respond(raw_input("Enter your message >> "))
