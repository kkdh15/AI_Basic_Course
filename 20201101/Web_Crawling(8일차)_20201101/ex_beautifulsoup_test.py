# 인스톨은 필수!
# pip install beautifulsoup4
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title></head>
<body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>

    <p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

print("soup.title :", soup.title)
print("soup.title.name :",soup.title.name) #name => tag name
print("soup.title.string :",soup.title.string)
print("soup.title.parent.name :",soup.title.parent.name)
print("soup.p :", soup.p)
print("soup.p['class'] :",soup.p['class'])
print("soup.a :", soup.a) # 첫번째 가져오기
print("soup.find_all('a') :", soup.find_all('a') ) #전체 가져오기
print('soup.find(id="link3") : ', soup.find(id="link3"))
print('soup.find(id="link3").string : ', soup.find(id="link3").string)

for link in soup.find_all('a'):
    #<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    print(link.get('href'))

print(soup.get_text())