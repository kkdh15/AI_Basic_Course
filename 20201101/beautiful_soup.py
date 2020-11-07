soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

print("soup.title :",soup.title)
print("soup.title.name :",soup.title.name)
print("soup.title.string :",soup.title.string)