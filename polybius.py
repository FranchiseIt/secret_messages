from ciphers import Cipher


class Polybius(Cipher):
    '''Child class of Cipher; applies Polybius cipher to user text.'''

    def __init__(self):
        '''Outlines attributes for Polybius class;
        Places alphabet in 5x5 grid;
        Assigns unique coordinates to each character.
        '''
        self.alphabet = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
        self.coordinates = []
        for y in range(1, 6):
            for x in range(1, 6):
                self.coordinates.append(str(y) + str(x))

    def encrypt(self, text):
        '''Encrypt function takes user text;
        Replaces I with J;
        Locates and returns coordinates for each character.
        '''
        output = []
        adjusted_text = text.upper().replace('I', 'J')
        text = adjusted_text.upper()
        for char in text:
            try:
                alpha_index = self.alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.coordinates[alpha_index])
        return ' '.join(output)

    def decrypt(self, text):
        '''Decrypt function takes user text;
        Pulls coordinates for grid out of user text by indexing;
        Locates and returns character for each set of coordinates.
        '''
        output = []
        text = text.replace(' ', '')
        for i in range(0, len(text), 2):
            try:
                cipher_coord = text[i] + text[i + 1]
                coord_index = self.coordinates.index(cipher_coord)
            except ValueError:
                output.append(text[i])
            else:
                output.append(self.alphabet[coord_index])
        return ''.join(output)
