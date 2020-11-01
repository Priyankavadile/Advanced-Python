#Assignment 9
# Generate a random password which has 6 letters 4 digits 2 special characters 

import random
import string

a=''.join((random.choice(string.ascii_letters) for i in range(6)))
a+=''.join((random.choice(string.digits) for i in range(4)))
a+=''.join((random.choice(string.punctuation) for i in range(2)))

new_list=list(a)
random.shuffle(new_list)
password=''.join(new_list)

print(password)