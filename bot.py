import aiml
kernel= aiml.Kernel()
kernel.bootstrap(brainFile = "/home/pi/chat_bot/bot_brain.brn")
kernel.setBotPredicate("hometown", "127.0.0.1")
kernel.setBotPredicate("name", "Tony")
kernel.setBotPredicate("master", "Sharmaji")
kernel.setBotPredicate("gender", "Male")
while True:
   print kernel.respond(raw_input("Enter your message >> "))
