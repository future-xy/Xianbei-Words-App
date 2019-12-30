fin=open('raw_page.html')
fout=open('raw_page.txt','w')
total=fin.read().split('\n')
for i, line in enumerate(total):
	if i%2==1:
		print(line+',',file=fout)