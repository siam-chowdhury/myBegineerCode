


class Chiper():

    ciper = ''

    def __init__(self, text, keys):
        self.text = text
        self.keys = keys

    
    def encryption(self):
        
        for word in self.text:
           if word == ' ':
               self.ciper += ' '
            
           elif word.isupper():
               self.ciper = self.ciper + chr((ord(word)+self.keys-65)%26+65)
           
           else:
               self.ciper = self.ciper + chr((ord(word)+self.keys-97)%26+97)

        return self.ciper



txt = input('Text : ')
key = int(input('Keys : '))

text = Chiper(txt, key)
print(text.encryption())
