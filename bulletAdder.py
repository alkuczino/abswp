#!python3
# mclip.py - A multi-clipboard program
import sys
import pyperclip

pre = pyperclip.paste()

wordlist = pre.split('\n')

new_wordlist = ['* ' + word for word in wordlist]

text = '\n'.join(new_wordlist)
pyperclip.copy(text)
print(new_wordlist)