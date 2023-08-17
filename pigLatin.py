#!python3
import sys

VOWELS=('a','e','i','o','u','y')

def latinize(text):
    text_list = text.split()
    for i in range(len(text_list)):
        suffix_consonant = ''
        word = ''
        if str(text_list[i].lower()).startswith(VOWELS):
            text_list[i] += 'yay'
        else:
            while len(text_list[i]) > 0:
                suffix_consonant
                word  
                
    return text_list
            


if __name__ == '__main__':
    
        print(latinize('Czekolada jest fajna a erupcje są eksplodujące'))