#!python3
import re
import sys

phone_num_regex = re.compile(r'(\d\d\d)?-?(\d\d\d-\d\d\d\d)')

my_number = 'My number is 415-555-4242'

mo = phone_num_regex.search(my_number)
print(f'Phone number found {mo.group()}')

area_code, the_rest = mo.groups()

print(f'Area code is {area_code} and the rest is {the_rest}')

print(f'{phone_num_regex.sub("xDD", my_number)}')