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

print(db.SELECTfromWHERE('vocabulary'))
print(db.SELECTfromWHERE('TAKES'))
# db.INSERTvalues('vocabulary',('0004','CET4',100,100,'大学四级'))
# db.INSERTvalues('dictionary',(
#         '0006','abandon', '[əˈbændən]', ['vt.  放弃，抛弃； 离弃，丢弃； 使屈从； 停止进行，终止', 'n.  放任，放纵； 完全屈从于压制；'])
#)
# db.INSERTvalues('record', ('1', '2', '2019', 1, 2, [1, 2], [3.0, 4.1], 0))
# value = db.SELECTfromWHERE('record', {'SID': ['1']})[1]
# db.DELETEprecise('record', {'SID': ['1']})
# print(value)
# value[6][0] += 1
# db.INSERTvalues('record', value)
# db.release()
# db.UPDATEprecise('VOCABULARY', 'COUNT', 3500, {"VID": ['0001']})
# db.INSERTvalues('VOCABULARY',('0004','BEST',2000,365,'Primary'))
# db.DELETEprecise('VOCABULARY', {"vid": ['0004']})
# print(db.SELECTfromWHERE('VOCABULARY',{'VID':['0003']}))
# print(db.SELECTfromTwoTableWHERE('USERS', 'PLAN', {'Proficiency': [100, 99]}))

# db.INSERTvalues('feedback', ('1', '2', '2019-01-01', " I' m wrong"))
# print(db.SELECTfromWHERE('feedbac'))

# tabe=db.SELECTfromTwoTableWHERE('USERS','PLAN')

# db.release()
