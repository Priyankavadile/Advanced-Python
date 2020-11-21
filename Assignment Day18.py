18
#Question 1:
#write a program to find the given string in the root directory that contains a text file

import os
root="D:\\Compaines\\google"
for root,dir,files in os.walk(root):
  for f in files:
    path=root+"\\"+f
    print(path)

def check_string_in_file(f, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
             if lookup in line:
               print('found at line:', num)

