import mysql.connector
from CONFIG import MYSQLDBSERVER


# 服务器

class Mysqlserver:
    DBSERVER = MYSQLSERVER

    @property
    def dbes(self, __dbes=None):
        return __dbes

    @dbes.getter
    def dbes(self):
        conn = mysql.connector.connect(**self.DBSERVER)
        cr = conn.cursor()
        sql = 'show databases;'
        cr.execute(sql)
        t = cr.fetchall()
        __dbes = []
        for tp in t:
            __dbes.append(tp[0])
        return __dbes


# 数据库
class MysqlDBmetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['dbname'] = name
        attrs['dbconn'] = {'database': name}
        return type.__new__(mcs, name, bases, attrs)


class MysqlDB(Mysqlserver, metaclass=MysqlDBmetaclass):
    def __getconn(self):
        local_db = dict(self.DBSERVER, **self.dbconn)
        conn = mysql.connector.connect(**local_db)
        return conn

    def getdata(self, sql):
        conn = self.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        t = cr.fetchall()
        return t
    def changedata(self, sql):
        conn = self.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        conn.commit()

    @property
    def tables(self, __tables=None):
        return __tables

    @tables.getter
    def tables(self):
        conn = self.__getconn()
        cr = conn.cursor()
        sql = 'show tables;'
        cr.execute(sql)
        t = cr.fetchall()
        __tables = []
        for tp in t:
            __tables.append(tp[0])
       
        return __tables


# 表

class MysqlTableMetaclass(MysqlDBmetaclass):
    def __new__(mcs, name, bases, attrs):
        attrs['tablename'] = name
        return type.__new__(mcs, name, bases, attrs)


class MysqlTableBase(metaclass=MysqlTableMetaclass):
    # 获取列名
    @property
    def colnames(self):
        sql = 'select column_name from information_schema.columns where table_schema =\'{}\' and table_name = \'{}\' ;'.format(
            self.dbname, self.tablename)
        t = self.getdata(sql)
        l = []
        for tp in t:
            l.append(tp[0])
        return l

    # 获取列值
    def getvalue(self, **kw):
        condition = ''
        if len(kw) == 0:
            pass
        else:
            condition = 'where '
            for key in kw:
                temp = '%s =\'%s\' and ' % (key, kw[key])
                condition = condition + temp
            condition = condition[:-4]
        sql = "select * from {} {};".format(self.tablename, condition)
        res = self.getdata(sql)
        return res


class MysqlTable(MysqlTableBase):
    def __init__(self, **kw):
        self.info = kw

    # 辅助功能
    @property
    def isexist(self):
        values = self.getvalue(**self.info)
        if len(values) == 0:
            return False
        else:
            return True

    def iscolumnexist(self, key):
        if eval('self.getvalue(%s=\'%s\')' % (key, self.info[key])):
            return True
        else:
            return False

    def getkw(self):
        kw = {}
        colnames = self.getcolname()
        values = self.getvalue(**self.info)
        for name in colnames:
            kw[name] = []
        for row in values:
            colnum = 0
            for cell in row:
                kw[colnames[colnum]].append(cell)
                colnum += 1
        return kw

    # DML增删改
    @property
    def insert(self):
        'isexist is False'
        'all unique is null'
        if self.isexist:
            return False
        else:
            names = []
            values = []
            for key in self.colnames:
                if key in self.info:
                    names.append(key)
                    values.append(self.info[key])
            names = str(tuple(names))
            names = names.replace('\'', '')
            values = str(tuple(values))
            sql = 'insert into %s%s values %s;' % (self.tablename, names, values)
            self.changedata(sql)
            return True

    def update(self, **kw):
        'isexist is True'
        'all unique is null'
        if len(kw) == 0 or not self.isexist:
            return False
        else:
            data = ''
            for key in kw:
                temp = '%s =\'%s\' ,' % (key, kw[key])
                data = data + temp
            data = data[:-1]
            condition = ''
            for key in self.info:
                temp = '%s =\'%s\' and ' % (key, self.info[key])
                condition = condition + temp
            condition = condition[:-4]
            sql = 'UPDATE {} SET {} where {};'.format(self.tablename, data, condition)
            self.changedata(sql)
            return True

    def delete(self):
        'isexist is True'
        condition = 'where '
        for key in self.info:
            temp = '%s =\'%s\' and ' % (key, self.info[key])
            condition = condition + temp
        condition = condition[:-4]
        sql = 'delete from %s %s;' % (self.tablename, condition)
        self.changedata(sql)
        return True

    # DDL   "ALTER TABLE tablename [ADD,DROP,MODIFY] colname datatype [UNIQUE,NOT NULL]"

    def __alter(self, colname, action='', datatype='varchar(10)', constraint=''):
        sql = 'alter table {} {} {} {} {};'.format(self.tablename, action, colname, datatype, constraint)
        print(sql)

    def coladd(self, colname, datatype='varchar(10)', constraint=''):
        self.__alter(colname, action='add', datatype='varchar(10)', constraint='')

    def coldrop(self, colname):
        self.__alter(colname, action='drop', datatype='')


if __name__ == '__main__':
    class Groupdata1(MysqlDB):
        pass


    class Group10(MysqlTable, Groupdata1):
        """aaaa"""
        pass


    class Crm(MysqlDB):
        pass


    class Userlist(MysqlTable, Crm):
        pass


    l = Group10()
    s = Userlist()
    print(l.DBSERVER)
    print(l.dbes)
    print(l.tables)
    print(l.colnames)
    print(s.DBSERVER)
    print(s.dbes)
    print(s.tables)
    print(s.colnames)
    print(l.coldrop('hahhaa1'))
