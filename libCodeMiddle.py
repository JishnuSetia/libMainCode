import random
if lexile <= 400:
    self.tts.say("Your lexile is low. Please read a few Graphic Novels to improve your lexile.")
elif lexile <= 645:
    books = ["The Princess in Black by Shannon Hale", "Smile by Raina Telgemeier", "Midnight on the Moon by Osborne, Mary Pope", "Nancy Clancy, Super Sleuth by Jane O'Connor", "Judy Moody and the Bad Luck Charm by Megan McDonald", "When stars are scattered by Victoria Jamieson", "The Girl Who Drank the Moon by Kelly Barnhill", "A to Z Mysteries", "Amelia Bedelia series"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 745:
    books = ["Middle School Series by James Patterson","Holes by Louis Sachar","Scarlet and Ivy by Sophie Cleverly","The 1000-Year-old Boy by Ross Welford","Artemis Fowl by Eoin Colfer","Holes by Louis Sachar","Number the stars by Lois Lowry","The Kid Who Came from Space by Ross Welford","A Long Walk to Water by Linda Sue Park","The Blue Umbrella by Ruskin Bond","Land of Stories series by Chris Colfer","Famous Five series by Enid Blyton","Mariella Mystery investigates","Hardy boys series","Nancy Drew series"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 890:
    books = ["Wonder by R J Palacio","Alex Rider series by Anthony Horovitz","Narnia series by C S Lewis","Inside Out & Back Again by Thanhha Lai","Wish by Barbara O'Connor","The 1,000-Year-old Boy by Ross Welford","The boy who harnessed the wind by William Kamkwa","An eagle in the snow by Michael Morpurgo","The House of Dies Drear by Virginia Hamilton"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 1200:
    books = ["The Jungle Books by Rudyard Kipling","The Hobbit by J R R Tolkien","A Tale of Two Cities by Charles Dickens","Threatened by Eliot Schrefer","How to train your dragon by Cressida Cowell","The Wind in the Willows by Kenneth Grahame","Journey to the Center of the Earth by Jules Verne","The Swiss Family Robinson by Johann David Wyss","A Series of Unfortunate Events by lemony Snickett","Hard Times by Charles Dickens"]
    recommended_books = random.sample(books, 2)
    self.tts.say("Here are 2 books which I recommend to read to improve your lexile:")
    for book in recommended_books:
        self.tts.say(book)
elif lexile <= 1500:
    books = ["Little Women by Louisa May Alcott","The legend of sleepy hollow by Washington Irving","The Tales of Beedle the Bard by J.K. Rowling","The Last of the Mohicans by James Fenimore Cooper","Ivanhoe by Sir Walter Scott","Huck Finn by Mark Twain"]
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