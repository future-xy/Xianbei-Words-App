import psycopg2


class sillySQL:
    def __init__(self):
        self.conn = None
        self.cur = None

    def _valueToStr(self, val):
        if type(val) == str:
            return "'%s'" % val
        else:
            return str(val)

    # 连接和断开本地psql数据库
    def bind(self):
        self.conn = None
        self.cur = None
        try:
            self.conn = psycopg2.connect(database="untitled0", user="postgres", password="OPEN", host="127.0.0.1",
                                         port="5432")
        except:
            print('Unanble to connect to the dababase')
            return

        self.cur = self.conn.cursor()

    def release(self):
        if self.conn != None:
            self.conn.commit()
        self.conn.close()
        self.cur = None
        self.conn = None

    # 简单的查询
    def SELECTfromWHERE(self, tablename, condition=None):
        statement = 'SELECT * FROM %s' % tablename
        if condition != None:
            statement += ' WHERE %s' % condition
        statement += ';'
        self.cur.execute(statement)
        TABLE_result = self.cur.fetchall()
        TABLE_header = list(map(lambda x: x[0], self.cur.description))
        TABLE_result.insert(0, tuple(TABLE_header))
        return TABLE_result

    def SELECTfromTwoTableWHERE(self, tablename1, tablename2, condition=None):
        statement = 'SELECT * FROM %s NATURAL JOIN %s' % (tablename1, tablename2)
        if condition != None:
            statement += ' WHERE %s' % condition
        statement += ';'
        self.cur.execute(statement)
        TABLE_result = self.cur.fetchall()
        TABLE_header = list(map(lambda x: x[0], self.cur.description))
        TABLE_result.insert(0, tuple(TABLE_header))
        return TABLE_result

    def UPDATEprecise(self, tablename, item, new_value, condition=None):
        # statement='UPDATE '+tablename+' SET '+ITEM+'='+str(new_value)
        statement = "UPDATE %s SET %s = %s" % (tablename, item, self._valueToStr(new_value))
        if condition != None:
            statement += " WHERE %s" % condition
        statement += ";"
        self.cur.execute(statement)
        self.conn.commit()
        return

    def DELETEprecise(self, tablename, condition=None):
        if condition == None:
            print('Condition Needed, or the whole tabel will be removed.')
            return
        statement = 'DELETE FROM %s WHERE %s;' % (tablename, condition)
        self.cur.execute(statement)
        self.conn.commit()
        return

    # type(values)==tuple
    def INSERTvalues(self, tablename, values):
        statement = "INSERT INTO %s VALUES(" % tablename
        for v in values:
            statement += self._valueToStr(v) + ","  # if type(v)==str , may be bug?
        statement = statement[:-1] + ");"
        print(statement)
        self.cur.execute(statement)
        self.conn.commit()
        return

    # 其他高级一点的需求？
    def LoadDictionary(self, dictionary):
        pass

    def LoadVocabulary(self, wordlistname, wordlist):
        pass

    def StoreFeedBack(self, feedback):
        pass

    def LoadUserMessage(self, userInformation):
        pass
