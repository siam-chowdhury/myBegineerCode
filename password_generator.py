import random


class Password:

    randWords = ''
    randLetters = []


    # add random word in randLetters list 
    def letters(self):
        for num in range(33, 123):
            self.randLetters.append(chr(num))
        


    # ask password len and output random words between [a-z] [A-Z] [0-9] and [symbol]
    def password(self):

        self.letters()

        lenght = int(input("Password Length : "))
        for plen in range(lenght):
            self.randWords += random.choice(self.randLetters)
        
        return self.randWords



    
pswd = Password()
print(pswd.password())