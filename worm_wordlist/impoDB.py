from sillySQL import sillySQL

import sys
import logging

# 日志系统配置
handler = logging.FileHandler('app.log', encoding='UTF-8')
# 设置日志文件，和字符编码
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
# app logger
# app.logger.addHandler(handler)
# database logger
db_logger = logging.getLogger('Database')
db_logger.addHandler(handler)
shandler = logging.StreamHandler(sys.stderr)
shandler.setFormatter(logging_format)
shandler.setLevel(logging.DEBUG)
db_logger.addHandler(shandler)
db_logger.setLevel(logging.DEBUG)
db_logger.info('123')
# database = sillySQL(logger=db_logger)

db = sillySQL(logger=db_logger)
db.bind()

dic=db.SELECTfromWHERE('dictionary')
widcol=dic[0].index('wid')
maxwid=0
print(dic[0], widcol)
for r in dic[1:]:
	maxwid=max(maxwid, int(r[widcol]))
print('Max wid=',maxwid)

# db.SELECTfromWHERE('Vocabulary')
take=db.SELECTfromWHERE('takes')
maxtid=0
for r in take[1:]:
	maxtid=max(maxtid,int(r[0]))
print(maxtid)

fin=open('raw_grepage.txt')
vid='0001'
for i, line in enumerate(fin.read().split('\n')):
	total=line.split('\t')
	w=total[0]
	pron=total[1]
	desc=total[2:-1]
	if pron=='None' or desc==['None']:
		continue
	print(w,end='\t')
	lookup=db.SELECTfromWHERE('dictionary',{'english':[w]})
	#update dictionary
	if len(lookup)==1:
		maxwid+=1
		db.INSERTvalues('dictionary',('%04d'%maxwid,w,pron,desc))
	wid=db.SELECTfromWHERE('dictionary',{'english':[w]})[1][0]
	#update take
	lookup=db.SELECTfromWHERE('takes',{'wid':[wid],'vid':[vid]})
	if len(lookup)==1:
		maxtid+=1
		db.INSERTvalues('takes',('%04d'%maxtid,vid,wid))   #(tid,vid, wid):
		# print('takes insert :',('%04d'%(maxtid+1),vid,wid))

db.release()