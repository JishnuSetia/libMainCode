import random
if lexile <= 400:
    books = ["Magic Tree House Series" , "Magic School Bus by Joanna Cole" , "Amulet Series", "Asterix" , "Graphic Adventures"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 645:
    books = ["The Cat in the Hat" , "The Princess in Black" , "Smile" , "Henry and Mudge" , "Sugar and Spice" , "Midnight on the Moon" , "Nancy Clancy, Super Sleuth" , "Judy Moody and the Bad Luck Charm" , "The Girl who Drank the Moon" , "A to Z Mysteries" , "Star war series" , "Amelia Bedelia Series"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 745:
    books = ["BFG", "Adventure Series" , "Holes" , "Scarlet and Ivy" , "The 1000 Year Old Boy" , "Artemis Fowl" , "The one and only Ivan" , "The kid who came from Space" , "The blue umbrella" , "Land of stories series" , "Famous Five Series" , "Mariella Mystery Investigates" , "Hardy Boys" , "Nancy Drew"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 890:
    books = ["Wonder" , "Alex Rider Series" , "Narnia Series" , "Matilda" , "Inside Out and Back Again" , "Wish" , "The Boy who harnessed the wind", "An eagle in the snow"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 1200:
    books = ["The Jungle Books", "How to train your dragon" , "The Wind in the Willows", "Journey to the Center of the Earth" , "The Swiss Family Robinson", "A Series of Unfortuneate Events"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
else:
    books = ["Little Women", "The Legend of Sleepy Hollow", "Ivanhoe", "Huck Finn"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)