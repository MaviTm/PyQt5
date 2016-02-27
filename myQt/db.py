#sudo apt-get install libqt5sql5-mysql
from PyQt5.QtSql import * #QSqlDatabase, QSqlQuery
class myDb:
    __conf = {}
    __dbase = None
    __open = False
    __sql = ''
    __arg = {}
    __result = None;
    __tblInfo = {}
    __insertID = 0
    __numRows = 0
    __affRows = 0

    def __int__(self):
        pass

    @classmethod
    def setConf(cls, dbConf):
        myDb.__conf = dbConf
        return cls

    @classmethod
    def myDbConnect(cls, o=False):
        if(cls.__dbase == None):
            cls.__dbase = QSqlDatabase.addDatabase(cls.__conf['dbType'])
            cls.__dbase.setHostName(cls.__conf['dbHost'])
            cls.__dbase.setDatabaseName(cls.__conf['dbName'])
            cls.__dbase.setUserName(cls.__conf['dbUser'])
            cls.__dbase.setPassword(cls.__conf['dbPass'])
        if o != False:
            cls.dbOpen()
        return cls

    @classmethod
    def getMyConnection(cls):
        return cls.__dbase

    @classmethod
    def dbOpen(cls):
        if cls.__open != True:
            cls.__open = cls.__dbase.open()
        return cls

    @classmethod
    def dbClose(cls):
        cls.__dbase.close()
        cls.__open = False
        return cls

    @classmethod
    def setSql(cls, str=None):
        cls.__arg.clear()
        cls.__arg = {}
        cls.__tblInfo.clear()
        cls.__tblInfo = {}
        if str != None:
            cls.__sql = str
            cls.__insertID = cls.__numRows = cls.__affRows = 0

        return cls

    @classmethod
    def setArg(cls, Dictionary, opValue=None):
        if opValue == None:
            cls.__arg = Dictionary
        else:
            cls.__arg[Dictionary] = opValue
        return  cls

    @classmethod
    def runSql(cls, close=True):
        if cls.__dbase == None or cls.__open == False:
            cls.myDbConnect(cls, True)
        if cls.__open == False:
            return cls
        cls.__result = QSqlQuery()
        cls.__result.prepare(cls.__sql)
        if len(cls.__arg) > 0 and type(cls.__arg) is dict:
            for i in cls.__arg:
                cls.__result.bindValue(i, cls.__arg[i])
        cls.__result.exec_()
        cls.__numRows = cls.__result.size()
        cls.__affRows = cls.__result.numRowsAffected()
        if cls.__numRows < 1 and cls.__affRows > 0:
            cls.__numRows = cls.__affRows
        cls.__insertID = cls.__result.lastInsertId()
        if cls.__insertID == None or type(cls.__insertID) is not int:
            cls.__insertID = 0

        cls.__tblInfo['fieldCount'] = cls.__result.record().count()

        if close == True:
            cls.dbClose()

        return cls

    @classmethod
    def getResult(cls):
        cls.__result.seek(-1) #while reset
        return cls.__result

    @classmethod
    def getAll(cls, out='num'):
        cls.__result.seek(-1) #while reset
        r=[]
        while cls.__result.next():
            r.append((out != "num") and cls.__dictRowRead() or  cls.__numRowRead())
        return r

    @classmethod
    def getRow(cls, row=0, out='num'):
        if row > 0:
            row = (row - 1)
        if row < 0:
            row = 0
        cls.__result.seek(row)
        if out == "dict":
            return cls.__dictRowRead()
        else:
            return cls.__numRowRead()

    @classmethod
    def getOne(cls):
        cls.__result.seek(0)
        return cls.__result.value(0)

    @classmethod
    def __numRowRead(cls):
        r = []
        x = 0
        while x < cls.__tblInfo['fieldCount']:
            r.append(cls.__result.value(x))
            x += 1
        return r

    @classmethod
    def __dictRowRead(cls):
        r = {}
        x = 0
        while x < cls.__tblInfo['fieldCount']:
            r[cls.__result.record().fieldName(x)] = cls.__result.value(x)
            x += 1
        return r

    @classmethod
    def infoGet(cls, index):
        try:
            return cls.__tblInfo[index]
        except:
            return None