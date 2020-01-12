from urllib import request,parse
from bs4 import BeautifulSoup
import sys

root_url = 'http://www.iciba.com/'

def LookUp(word):
	url = root_url + parse.quote(word)  # 拼接URL
	tag_soup=None
	speak_soup=None
	soup=None
	while soup==None:
		response = request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'lxml')
		tag_soup = soup.find(class_='base-list switch_part')
		speak_soup = soup.find(class_='base-top-voice')
	if tag_soup==None or speak_soup==None:
		return [word,None,None]
	meanings= tag_soup.find_all(class_='clearfix')
	meanings=[each.get_text().replace('\n',' ').strip() for each in meanings]
	pronuciation=speak_soup.find_all(class_='base-speak')
	pronuciation=[each.get_text().replace('\n',' ').strip() for each in pronuciation][0].split(' ')
	if len(pronuciation)<2 or len(meanings)<1:
		return [word,None,None]
	return [word,pronuciation[1]]+meanings


if __name__ == "__main__":
	wordlist=open("gre-rawlist.txt")
	wordsget=open("raw_grepage.txt","a+")
	tot=wordlist.read().split('\n')
	# print('open:',type(tot),len(tot))
	for i,line in enumerate(tot):
		# print(type(line),line)
		print("i=",i, file=sys.stderr,end=' ')
		if i>=650:
			break
		if i>=506:
			lookup=LookUp(line)
			for e in lookup:
				print(e, end='\t',file=wordsget)
			print(file=wordsget)
			print(lookup,file=sys.stderr)
