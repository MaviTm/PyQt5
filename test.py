# import myQt
# from myQt import pencere
# #print(dir(pencere.myWin),sep="\n")
#
# pencerem = pencere.myWin()
#
# pencerem.winResize(300, 250).\
#     winMove(250, 250).\
#     winTitle("Zincirli form").\
#     winHeadText("Babaya selam de :)").\
#     winShow()
###################################################

from myQt import db

mdb = db.myDb
mdb.setConf({
    'dbType':'QMYSQL',
    'dbHost':'localhost',
    'dbName':'caspalYem',
    'dbUser':'root',
    'dbPass':''
})

mdb.myDbConnect(True)

######################### RETURN RESULT #########################
# resultt = mdb.setSql("SELECT * FROM bln_contents").runSql(True).getResult()
# while resultt.next():
#     print(resultt.value(0), resultt.value('id'))
#     break


######################### DICT ARG #########################

# mdb.setSql("SELECT * FROM bln_contents WHERE id > :id").setArg({":id":0}).runSql(True)
# print(mdb.getAll())


######################### LOOPS ARG #########################
# mdb.setSql("SELECT * FROM bln_contents WHERE id > :id AND modul = :modul").\
#     setArg(":id",0).\
#     setArg(":modul","staf").\
#     runSql(True)
# print(mdb.getAll())

