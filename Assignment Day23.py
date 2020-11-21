import os
import re
import time
t1=time.time()
dict1={}
i=1
def get_drives():
  resp=os.popen("wmic logical disk caption")
  drive=resp.read
  return drive.split()[1:]

def creatingindex(path):
  global i
  resp=os.walk(path)
  for root,d,files in resp:
    for files in file:
      path1=root+"\\"+gile
      print(path1)
      file1=file+"|"+str(i)
      dict1[file1]=path1
      i=i+1

def search(file1):
  for k,v in dict1.items():
    k=k.split("l")[0]
    m=re.search(file1,k,re.l)
    if m:
      print(k,":",v)


for d in get_drives():
  print(d)
  creatingindex(d+"//")
t2=time.time()
print(t2-t1)
file1=input("Enter the file name")
search(file1)
