class RPGInfo():
    author = "name"
    
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made in Python 3.9 using the FutureLearn OOJ course")
        
    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
