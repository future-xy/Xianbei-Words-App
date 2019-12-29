import psycopg2
from psycopg2 import errors, errorcodes


class sillySQL:
    def __init__(self, logger=None):
        self.conn = None
        self.cur = None
        self.logger = logger
        self.bind()

    def _valueToStr(self, val):
        if val == None:
            return 'Null'
        if type(val) == str:
            return "'%s'" % val.replace("'", "''")
        elif type(val)==list:
            result=""
            for v in val:
                if len(result)>0:
                    result+=","
                result += str(v)
            return "'{"+result+"}'"
        else:
            return str(val)

    def _conditionToStr(self, condition):
        condition_statement = ""
        for (key, val) in condition.items():
            if len(condition_statement) > 0:
                condition_statement += " and "
            sub_condition_statement = ""
            for v in val:
                if len(sub_condition_statement) > 0:
                    sub_condition_statement += " or "
                sub_condition_statement += key + "=" + self._valueToStr(v)

            condition_statement += "(" + sub_condition_statement + ")"
        return condition_statement

    # 连接和断开本地psql数据库
    def bind(self):
        self.conn = None
        self.cur = None
        try:
            self.conn = psycopg2.connect(database="database0", user="postgres", password="sysu_sdcs_db2019",
                                         host="111.231.250.160", port="5432")
        except errors.Error as e:
            self.logger.critical('Unanble to connect to the dababase')
            self.logger.critical(e.args)
            # print('Unanble to connect to the dababase')
            return False
        except BaseException as b:
            self.logger.error(b.args)
            # print(b.args)
            return False
        else:
            self.logger.info('Successfully connect to the database')
            self.cur = self.conn.cursor()
            return True

    def release(self):
        if self.conn != None:
            self.conn.commit()
        self.conn.close()
        self.cur = None
        self.conn = None

    # 简单的查询
    def SELECTfromWHERE(self, tablename, condition=None):
        statement = "SELECT * FROM %s" % tablename
        if condition != None:
            statement += " WHERE %s" % self._conditionToStr(condition)
        statement += ';'
        try:
            self.cur.execute(statement)
        except errors.Error as e:
            self.logger.error(e.pgerror)
            self.conn.rollback()
            return False
        except BaseException as b:
            self.logger.error(b.args)
            return False
        TABLE_result = self.cur.fetchall()
        TABLE_header = list(map(lambda x: x[0], self.cur.description))
        TABLE_result.insert(0, tuple(TABLE_header))
        return TABLE_result

    def SELECTfromTwoTableWHERE(self, tablename1, tablename2, condition=None):
        statement = "SELECT * FROM %s NATURAL JOIN %s" % (tablename1, tablename2)
        if condition != None:
            statement += " WHERE %s" % self._conditionToStr(condition)
        statement += ";"
        try:
            self.cur.execute(statement)
        except errors.Error as e:
            self.logger.error(e.pgerror)
            self.conn.rollback()
            return False
        except BaseException as b:
            self.logger.error(b.args)
            return False
        TABLE_result = self.cur.fetchall()
        TABLE_header = list(map(lambda x: x[0], self.cur.description))
        TABLE_result.insert(0, tuple(TABLE_header))
        return TABLE_result

    def UPDATEprecise(self, tablename, item, new_value, condition=None):
        # statement='UPDATE '+tablename+' SET '+ITEM+'='+str(new_value)
        statement = "UPDATE %s SET %s = %s" % (tablename, item, self._valueToStr(new_value))
        if condition != None:
            statement += " WHERE %s" % self._conditionToStr(condition)
        statement += ";"
        try:
            self.cur.execute(statement)
        except errors.Error as e:
            self.logger.error(e.pgerror)
            self.conn.rollback()
            return False
        except BaseException as b:
            self.logger.error(b.args)
            return False

        self.conn.commit()
        return True

    def DELETEprecise(self, tablename, condition=None):
        if condition == None:
            self.logger.warning('Condition Needed, or the whole tabel will be removed.')
            return False
        statement = "DELETE FROM %s WHERE %s;" % (tablename, self._conditionToStr(condition))
        try:
            self.cur.execute(statement)
        except errors.Error as e:
            self.logger.error(e.pgerror)
            self.conn.rollback()
            return False
        except BaseException as b:
            self.logger.error(b.args)
            return False
        self.conn.commit()
        return True

    # type(values)==tuple
    def INSERTvalues(self, tablename, values):
        statement = "INSERT INTO %s VALUES(" % tablename
        for v in values:
            statement += self._valueToStr(v) + ","  # if type(v)==str , may be bug?
        statement = statement[:-1] + ");"
        self.logger.info(statement)
        try:
            self.cur.execute(statement)
        except errors.Error as e:
            self.logger.error(e.pgerror)
            self.conn.rollback()
            return False
        except BaseException as b:
            self.logger.error(b.args)
            return False
        self.conn.commit()
        return True

    # 其他高级一点的需求？
    def LoadDictionary(self, dictionary):
        pass

    def LoadVocabulary(self, wordlistname, wordlist):
        pass

    def StoreFeedBack(self, feedback):
        pass

    def LoadUserMessage(self, userInformation):
        pass

    def createViewFor(self):
        pass
