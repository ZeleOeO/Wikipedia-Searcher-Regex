import re
import requests
from bs4 import BeautifulSoup
import string

name_pattern ="Born([^\(]*)"
age_pattern = "age[^[1-9]+(\d+)"
birthday_pattern = "Born[^\(]+[^[A-Z]+([^\(]+)"
#birthplace_pattern = "age \d+\)\n([^\n]+)"
education_pattern = "Education([^\(]+)(?=Occu)|Alma\\xa0mater(.+?)(?=Occu)"
death_pattern = ""
spouse_pattern="Spouse([^\\]+)[^\(]+\(([^0]+)0+(\d{4})"

def get_pattern_match(pattern: str, text: str):
  ans = re.findall(pattern, text)
  if " " in ans or not ans:
    return "None"
  return ans[0]


def extract_information(text: str):
  name = get_pattern_match(name_pattern, text)
  age = get_pattern_match(age_pattern, text)
  birthdate = get_pattern_match(birthday_pattern, text)
  #birthplace = get_pattern_match(birthplace_pattern, text)
  education = " ".join(get_pattern_match(education_pattern, text)) if isinstance(get_pattern_match(education_pattern, text), tuple) else get_pattern_match(education_pattern, text)
  # spouse = get_pattern_match(spouse_pattern, text)

  return {
      "Name":name.strip(),
      "Age":age.strip(),
      "Birth Date":birthdate,
      "Education": str(education).strip()
  }


import requests
from bs4 import BeautifulSoup
import string

name=input("Whose information do you want from WikiPedia: ")
name = string.capwords(name.lower())

name = name.replace(" ", "_")

url = f"https://en.wikipedia.org/wiki/{name}"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results= soup.find(id="mw-content-text")
try:
  texts = results.find(class_="infobox biography vcard").text.replace("\n","")
except:
  texts = "User not found"

texts

info = extract_information(texts) if len(texts) >=5 else "User not found"
info

print(url)

"""#Names That Have Been Tested

- jeff bezos
- viola davis
- oprah winfrey
- elon musk
- ice spice - not working
- rami malek
- isaac newton
- ariana grande
- nicki minaj
- kim kardashian 
- miley *cyrus*
- Scooter Braun
"""
