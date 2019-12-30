import urllib.request
from bs4 import BeautifulSoup
import sys

root_url = 'http://www.iciba.com/'

def LookUp(word):
	url = root_url +  word  # 拼接URL
	
	tag_soup=None
	speak_soup=None
	while tag_soup==None:
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'lxml')
		tag_soup = soup.find(class_='base-list switch_part')
		speak_soup = soup.find(class_='base-top-voice')

	meanings= tag_soup.find_all(class_='clearfix')
	pronuciation=speak_soup.find_all(class_='base-speak')
	return (word,
			[each.get_text().replace('\n',' ').strip() for each in pronuciation][0].split(' ')[1],
			[each.get_text().replace('\n',' ').strip() for each in meanings])


wordlist=open("cet4-rawlist.txt")
tot=wordlist.read().split('\n')
# print('open:',type(tot),len(tot))
for i,line in enumerate(tot):
	# print(type(line),line)
	print("i=",i, file=sys.stderr)
	if i>=100:
		break
	if i>=0:
		lookup=LookUp(line)
		# print(lookup)
		print(lookup,file=sys.stderr)
