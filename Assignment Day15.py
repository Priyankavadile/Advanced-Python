15 
import requests
import re
url="https://study-ccna.com/classes-of-ip-addresses/"
a=requests.get(url)
data_ip=a.text
ip=r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]"
list_ip=re.findall(ip,data_ip)
for each in list_ip:
  print(each)
