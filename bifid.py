
from ciphers import Cipher


class Bifid(Cipher):
    '''Child class of Cipher; applies Bifid cipher to user text.'''

    def __init__(self):
        '''Outlines attributes for Bifid class;
        Self.mixed represents 25 alphabet characters unordered;
        Coordinates are found by placing alphabet into 5x5 grid.
        '''
        self.mixed = 'DEFKLMQUVXAZBTRCYWGHSPOJN'
        self.coordinates = []
        self.y_coord = []
        self.x_coord = []
        self.cipher_coord = (str(self.y_coord) + str(self.x_coord))
        for y in range(1, 6):
            for x in range(1, 6):
                self.y_coord.append(str(y))
                self.x_coord.append(str(x))
                self.coordinates.append(str(y) + str(x))

    def encrypt(self, text):
        '''Encrypt function takes user text;
        Replaces I with J;
        Locates coordinates in 5x5 grid for respective characters;
        Strings y coordinates together, followed by x coordinates;
        Iterates through new string to find new coordinates;
        Returns the respective alphabet character for new coordinates.
        '''
        y_coord_out = []
        x_coord_out = []
        alpha_output = []
        text = text.upper().replace('I', 'J')
        for char in text:
            try:
                alpha_index = self.mixed.index(char)
            except ValueError:
                y_coord_out.append(char)
                x_coord_out.append(char)
            else:
                y_coord_out.append(self.y_coord[alpha_index])
                x_coord_out.append(self.x_coord[alpha_index])
        output = ''.join(y_coord_out) + ''.join(x_coord_out)
        output = output.replace(' ', '')
        for i in range(0, len(output), 2):
            try:
                cipher_coord = output[i] + output[i + 1]
                coord_index = self.coordinates.index(cipher_coord)
            except ValueError:
                alpha_output.append(output[i])
            else:
                alpha_output.append(self.mixed[coord_index])
        return ''.join(alpha_output)

    def decrypt(self, text):
        '''Decrypt function takes user text;
        Replaces I with J;
        Strings together the coordinates of each respective character;
        Finds new coordinates by taking iterating through string
        Based on length of characters in user text;
        Returns respective alphabet character for new coordinates.
        '''
        coord_output = []
        alpha_output = []
        text = text.upper().replace('I', 'J')
        for char in text:
            try:
                alpha_index = self.mixed.index(char)
            except ValueError:
                coord_output.append(char)
            else:
                coord_output.append(self.coordinates[alpha_index])
        output = ''.join(coord_output)
        output = output.replace(' ', '')
        for i in range(0, int(len(output)/2)):
            try:
                cipher_coord = output[i] + output[i + int(len(output)/2)]
                coord_index = self.coordinates.index(cipher_coord)
            except ValueError:
                alpha_output.append(output[i])
            else:
                alpha_output.append(self.mixed[coord_index])
        return ''.join(alpha_output)
