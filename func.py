from test__mysqlmetaclass import Mysqlserver,MysqlDB,MysqlTable


class DBserver(Mysqlserver):
    pass


class Crm(MysqlDB, DBserver):
    pass


class Employee(MysqlTable, Crm):
    pass
class Orders(MysqlTable, Crm):
    pass
class Product(MysqlTable, Crm):
    pass
class History(MysqlTable, Crm):
    pass
