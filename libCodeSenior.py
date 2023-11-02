import random
if lexile <= 400:
    self.tts.say("Your lexile is low. Please read a few Graphic Novels to improve your lexile.")
elif lexile <= 645:
    books = ["Smile by Raina Telgemeier", "Midnight on the Moon by Osborne, Mary Pope",
                     "Nancy Clancy, Super Sleuth by Jane O'Connor", "Judy Moody and the Bad Luck Charm by Megan McDonald",
                     "When Stars Are Scattered by Victoria Jamieson", "The Girl Who Drank the Moon by Kelly Barnhill"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 745:
    books = ["Scarlet and Ivy by Sophie Cleverly", "The 1000-Year-Old Boy by Ross Welford",
                     "Artemis Fowl by Eoin Colfer", "Holes by Louis Sachar", "The One and Only Ivan by Katherine Applegate",
                     "Number the Stars by Lois Lowry", "The Kid Who Came from Space by Ross Welford",
                     "A Long Walk to Water by Linda Sue Park", "Dust On The Mountain by Ruskin Bond"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 890:
    books = ["Wonder by R J Palacio", "Alex Rider series by Anthony Horovitz", "Inside Out & Back Again by Thanhha Lai",
                     "Wish by Barbara O'Connor", "The 1,000-Year-Old Boy by Ross Welford",
                     "The Boy Who Harnessed the Wind by William Kamkwamba", "An Eagle in the Snow by Michael Morpurgo",
                     "I, Robot by Isaac Asimov", "The House of Dies Drear by Virginia Hamilton"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 1200:
    books = ["The Hobbit by J R R Tolkien", "A Tale of Two Cities by Charles Dickens",
                     "Threatened by Eliot Schrefer", "How to Train Your Dragon by Cressida Cowell",
                     "The Wind in the Willows by Kenneth Grahame", "Journey to the Center of the Earth by Jules Verne",
                     "The Swiss Family Robinson by Johann David Wyss", "A Series of Unfortunate Events by Lemony Snickett",
                     "Brain by Robin Cook", "Hard Times by Charles Dickens", "To the Lighthouse by Virginia Woolf"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 1500:
    books = ["Little Women by Louisa May Alcott", "One Hundred Years of Solitude by Gabriel Garcia Marquez",
                     "The Legend of Sleepy Hollow by Washington Irving", "The Tales of Beedle the Bard by J.K. Rowling",
                     "The Last of the Mohicans by James Fenimore Cooper", "Metamorphosis by Franz Kafka",
                     "Ivanhoe by Sir Walter Scott", "Huck Finn by Mark Twain"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
else:
    books = ["Rule of the Bone by Russell Banks", "How I Live Now by Meg Rosoff"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)