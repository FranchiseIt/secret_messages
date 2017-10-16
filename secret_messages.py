import os

from atbash import Atbash
from bifid import Bifid
from polybius import Polybius


def clear():
    '''Function to clear screen in console when called'''
    os.system('cls')
    os.system('clear')

clear()


def secret_messages():
    '''Main function for Secret Messages;
    Offers user option to Encrypt/Decrypt;
    Offers user option between Atbash, Bifid, and Polybius ciphers;
    Asks user input for text to be encrypted/decrypted;
    Returns encrypted/decrypted text to user.
    '''
    cipher_choices = {'ATBASH': 'Atbash',
                      'BIFID': 'Bifid',
                      'POLYBIUS': 'Polybius'
                     }
    encryption_paths = {'ENCRYPT': 'encrypt', 'DECRYPT': 'decrypt'}
    print("\nWelcome to the Secret Messasges project!\n\n"
          "Would you like to do with your text? Encrypt or Decrypt?\n"
          "You may also enter 'Q' to QUIT.")
    text_path = input('\n>').lower()
    if text_path == 'q':
        quit()
    for value in encryption_paths.values():
        while True:
            if text_path.lower() in encryption_paths.values():
                break
            try:
                opted_two = encryption_paths[text_path]
                break
            except KeyError:
                text_path = input('\nInvalid entry\n'
                                  'Enter ENCRYPT or DECRYPT.\n>').lower()
    clear()
    print("\nPlease choose one of the following ciphers\n\n"
          "Or enter 'Q' to QUIT\n")
    for key in cipher_choices:
        print(key)
    cipher_opted = input('\n>').title()
    if cipher_opted == 'Q':
        quit()
    for value in cipher_choices.values():
        while True:
            if cipher_opted.title() in cipher_choices.values():
                break
            try:
                opted = cipher_choices[cipher_opted]
                break
            except KeyError:
                cipher_opted = input('\nInvalid entry\n'
                                     'Please enter a cipher '
                                     'from the list.\n>').title()
    clear()
    print("\nEnter text below to {} your message.".format(text_path.lower()))
    text = input('\n>')
    if cipher_opted.title() == 'Atbash' and text_path.lower() == 'encrypt':
        print(Atbash().encrypt(text))
    if cipher_opted.title() == 'Atbash' and text_path.lower() == 'decrypt':
        print(Atbash().decrypt(text))
    if cipher_opted.title() == 'Polybius' and text_path.lower() == 'encrypt':
        print(Polybius().encrypt(text))
    if cipher_opted.title() == 'Polybius' and text_path.lower() == 'decrypt':
        print(Polybius().decrypt(text))
    if cipher_opted.title() == 'Bifid' and text_path.lower() == 'encrypt':
        print(Bifid().encrypt(text))
    if cipher_opted.title() == 'Bifid' and text_path.lower() == 'decrypt':
        print(Bifid().decrypt(text))

if __name__ == "__main__":
    secret_messages()
