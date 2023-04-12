"""
if you wan't to scrap a website
1. use the API
2. HTML web scraping using some tools like bs4

step 0 - install all the requirements
1. pip install requests
3. pip install html5lib

"""
import requests
from bs4 import BeautifulSoup
url=input()

# step 0-gather all requirements
# step 1-get the HTML
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# step 2-Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# step 3-HTML tree traversal

# commonly used types of objects 
# 1. Tag -print(type(title.string))
# 2. NavigableString
# 3. BeautifulSoup- print(type(soup))
# 4. Comment 
# markup="<p><!--this is a comment--></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

# get title of HTML page 
title=soup.title
# print(title)

# get all the paragraphs from the page
paras=soup.find_all('p')
# print(paras) 

# get the anchor tags 
anchors=soup.find_all('a')
# print(anchors)

# get first element
print(soup.find('p'))
# get classes of any element 
print(soup.find('p')['class'])
# print(soup.find('p')['id']) throws key error

# find all the elements with class lead
print(soup.find_all("p",class_="lead"))


# get the text from the elements 
print(soup.find('p').get_text())
# print(soup.get_text())


# get all anchor tags frm the page 
anchors=soup.find_all('a')
all_links=set()

# get all the links on page 
for link in anchors:
	if(link.get('href')!='#'):
		linkText="https://codewithharry.com"+link.get('href')
		all_links.add(link)
		# print(linkText)

	navbarSupportedContent=soup.find(id='navbarSupportedContent')
