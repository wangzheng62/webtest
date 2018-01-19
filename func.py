from test__mysqlmetaclass import Mysqlserver,MysqlDB,MysqlTable


class DBserver(Mysqlserver):
    pass


class Groupdata1(MysqlDB, DBserver):
    pass


class Group10(MysqlTable, Groupdata1):
    pass