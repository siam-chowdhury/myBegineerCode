

class ChiperDecrypt():

    ciper = ''
    cnt = 0

    def __init__(self, text):
        self.text = text
        


    def decryption(self):

        for word in self.text:

           keys = 1
           if word == ' ':
               self.ciper += ' '
            
           elif word.isupper():
               self.ciper = self.ciper + chr((ord(word)-keys-65)%26+65)
           
           else:
               self.ciper = self.ciper + chr((ord(word)-keys-97)%26+97)
           
           keys += 1
           print(f'{self.ciper}\n ')



txt = input('text : ')
# key = int(input("keys : "))
text = ChiperDecrypt(txt)
print(text.decryption())




