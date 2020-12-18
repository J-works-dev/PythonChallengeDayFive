import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:")

iban=requests.get(url)

indeed_soup = BeautifulSoup(iban.text, "html.parser")

pagination = indeed_soup.find("tbody")
c_list = pagination.find_all("td")

data = []
temp = []

for i in c_list:
  temp.append(i.string)

dic={}
x=0
num=0
for i in temp:
  x += 1
  if x%4 == 1:
    dic['country'] = i.capitalize()
  elif x%4 == 2:
    dic['currency'] = i
  elif x%4 == 3:
    dic['code'] = i
  else: # x%4 == 0:
    x = 0
    if "No universal currency" in dic['currency']:
      dic = {}
      pass
    else:
      num += 1
      dic['number'] = num
      data.append(dic)
      dic = {}

for i in data:
  print(f"# {i['number']} {i['country']}")

def get_num():
  got = input("#: ")
  try:
    searching_num = int(got)

    if 0 <= searching_num < len(data)+1:
      # searching_num -= 1
      print(f"You chose {data[searching_num-1]['country']}\nThe currency code is {data[searching_num-1]['code']}")
    else:
      print("Choose a number from the list.")
      get_num()
  except ValueError:
    print("That wasn't a number.")
    get_num()

get_num()
