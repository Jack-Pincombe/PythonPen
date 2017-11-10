'''
A function that will hash a password it is given
'''

import crypt

def hash(word):
    print("Your hash is --> " + crypt.crypt(word,'HIX'))

if __name__ == '__main__':
    hash(input('Enter you chosen password -->'))