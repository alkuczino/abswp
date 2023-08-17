#!python3
import sys
import pyperclip
import re

# REGEXES:

phone_number_regex = re.compile(r'\+{0,1}\d+[-.\d]+\d')
#email_regex = re.compile(r'''[a-zA-Z0-9]                # first char must be a letter or a digit
#                         [a-zA-Z0-9!#$%&'*+-/=?^_`{|]* # sequence of allowed chars
#                         [a-zA-Z0-9]                    # last char must not be a special char
#                         @
#                         ([a-zA-Z0-9\.])+
#                         \.
#                         [a-zA-Z]*
#                         ''')
#
# email_regex = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9!#$%&\'*+-/=?^_`{|]*[a-zA-Z0-9]@([a-zA-Z0-9.])+\.[a-zA-Z]+')

email_regex = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def matches(text):
    match_numbers = phone_number_regex.findall(text)
    match_emails = email_regex.findall(text)
    print('\n'.join(match_numbers))
    print('\n'.join(match_emails))
    #print(f'{match_emails.group()}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ('''Usage: python phone_mail_clipboard.py
               Takes text from clipboard, matches email addresses and phone numbers,
               arranges them neatly and copies into the clipboard.
               ''')
    else:
        #matches(pyperclip.paste())
        matches('fdaskfo   Ffa zbigniew.malan@nekro.com fsd+48-5443-43-23agas robert.koczobut@netka.pl gfda +48538897445 shdsfh')