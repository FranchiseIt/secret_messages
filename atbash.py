import string

from ciphers import Cipher


class Atbash(Cipher):
    '''Child class of Cipher; applies Atbash cipher to user text.'''

    def __init__(self):
        '''Outlines attributes for Atbash class.'''
        self.alphabet = string.ascii_uppercase
        self.reverse = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        '''Encrypt function takes user text;
        Finds the index for each alphabet character;
        Applies each index to self.reverse;
        Returns the alphabet character in the respective index.
        '''
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.reverse[index])
        return ''.join(output)

    def decrypt(self, text):
        '''Decrypt function takes user text;
        Finds the index for each alphabet character in self.reverse;
        Applies each index to self.alphabet;
        Returns the alphabet character in the respective index.
        '''
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.reverse.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alphabet[index])
        return ''.join(output)
