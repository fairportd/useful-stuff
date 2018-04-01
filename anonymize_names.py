#! usr/bin/env python3

''' Loop through files in a folder and anonymize the names '''

import os
import random

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'

def get_char():
    '''Returns a random character from the CHARS list'''
    rand_num = random.randint(0, 35)
    return CHARS[rand_num]

def get_new_name():
    '''Returns a 64 character string'''
    name = ''
    for i in range(65):
        name += get_char()
    return name

folder = input("Enter target folder path: ")

for item in os.listdir(folder):
    old_name = item.split('.')[0] #get the old file name
    ext = item.split('.')[1] # get the file extension
    new_name = get_new_name() # get a random 64 chararacter name
    os.rename(os.path.join(folder,item), os.path.join(folder, new_name + '.' + ext))
    
