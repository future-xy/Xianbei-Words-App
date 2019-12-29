import urllib.request
from bs4 import BeautifulSoup

root_url = 'http://www.iciba.com/'

def LookUp(word):
	url = root_url +  word  # 拼接URL
	response = urllib.request.urlopen(url)
	html = response.read()

	soup = BeautifulSoup(html, 'lxml')
	tag_soup = soup.find(class_='base-list switch_part')
	# print(tag_soup)

	meanings= tag_soup.find_all(class_='clearfix')

	return (word,[each.get_text().replace('\n',' ').strip() for each in meanings])



wordlist=['hello', 'word', 'filibuster']
for w in wordlist:
	print(LookUp(w))

