from bs4 import BeautifulSoup

with open('simple.html', 'r') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

print()
# print(soup)
print(soup.prettify())

print()
# match_1 = soup.title
match = soup.title.text
# print(match_1)
print(match)

print()
match_2 = soup.div
print(match_2)

print()
match_3 = soup.find('div', class_='footer')
print(match_3)

print()
article = soup.find('div', class_='article')
print(article)

print()
headline = article.h2.a.text
print(headline)

print()
summary = article.p.text
print(summary)

print()
print('**************************************************')
print()

for article_1 in soup.find_all('div', class_='article'):
	
	headline = article_1.h2.a.text
	print(headline)
	
	summary = article_1.p.text
	print(summary)
	
	print()

