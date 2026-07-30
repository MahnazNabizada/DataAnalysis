import requests
from bs4 import BeautifulSoup

with open("BeautifulSoup.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 1. Write a Python program to find the title tags from a given html document 
title_tag = soup.find("title")
print(f"The title tags are: {title_tag}")

# 2. Write a Python program to get the number of paragraph tags of a given
paragraphs = soup.find_all("p")
print(f"The number of paragraphs: {len(paragraphs)}")

# 3. Write a Python program to extract the text in the first paragraph tag of a given html document. 
first_paragraph = paragraphs[0].text
print(f"The text from the 1st paragraph: {first_paragraph}")

# 4. Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from 
url = "http://python.org"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
li_tags = soup.find_all("li")
links = []
for li in li_tags:
    a = li.find("a")
    links.append(a.attrs['href'])
print(f"All the URLs from the webpage python.org : {links}")

# 5. Write a Python program to extract all the text from a given web page. 
text = soup.get_text(separator="\n", strip=True)
print(f"All text from {url}: {text}")

# 6. Write a Python program to retrieve the HTML code of the title, its text, and the HTML code of its parent. 
print(f"Title tag : {title_tag}")
print(f"Title tag text: {title_tag.text}")
print(f"Title tag parent: {title_tag.parent}")

# 7. Write a Python program to create a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each HTML/XML tag and string. 
print(soup.prettify())

# 8. Write a Python program to remove the contents of a tag in a given html document. 
tag = input("Which tag do you wamt to clean the content: ")

find_tags = soup.find_all(tag)
if find_tags:
    for t in find_tags:
      t.clear()
else:
    print("Tag not found!")

print(soup.prettify())


# 9. Write a Python program to wrap an element in the specified tag and create the new wrapper. 
element = input("Which element do you wamt to wrap? Ex. p, label, span... : ")
wrapper = input("Which wrapper do you wamt to wrap the element? Ex. div, section, main, footer... : ")

tags = soup.find_all(element)
new_wrapper = soup.new_tag(wrapper)

if tags:
    for t in tags:      
      t.wrap(new_wrapper)
else:
    print("Tag not found!")

print(soup.prettify())

# 10. Write a Python program to remove a tag from a given tree of html document and destroy it and its contents. 
tag = input("Which tag do you wamt to remove : ")

find_tags = soup.find_all(tag)
if find_tags:
    for t in find_tags:
      t.decompose()

print(soup.prettify())