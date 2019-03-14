from bs4 import BeautifulSoup
import csv
import requests


source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

article = soup.find('article')
print(article.prettify())

headline = article.h2.a.text
print(headline)

print()
summary = article.find('div', class_='entry-content').p.text
print(summary)

print()
# vid_src = article.find('iframe', class_='youtube-player')
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)

print()
#vid_id = vid_src.split('/')
vid_id = vid_src.split('/')[4]
print(vid_id)

print()
# vid_id_final = vid_id.split('?')
vid_id_final = vid_id.split('?')[0]
print(vid_id_final)

print()
youtube_link = f'http://youtube.com/watch?v={vid_id_final}'
print(youtube_link)

print()
print('*****************************************************************')

with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\paavan.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['headline_1', 'summary_1', 'youtube_link_1'])
	
	for article_1 in soup.find_all('article'):
		headline_1 = article_1.h2.a.text
		print(headline_1)
		print()
		
		summary_1 = article_1.find('div', class_='entry-content').p.text
		print(summary_1)
		print()
		
		try:
			vid_src_1 = article_1.find('iframe', class_='youtube-player')['src']
			# print(vid_src_1)
			
			vid_id_1 = vid_src_1.split('/')[4]
			# print(vid_id_1)
			
			vid_id_final_1 = vid_id_1.split('?')[0]
			# print(vid_id_final_1)
			
			youtube_link_1 = f'http://youtube.com/watch?v={vid_id_final_1}'
			
		except Exception as e:
			youtube_link_1 = None
			
		print(youtube_link_1)
		print()
		print('******************************************************************')
		
		print()

		csv_writer.writerow([headline_1, summary_1, youtube_link_1])
