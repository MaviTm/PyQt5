from myQt import pencere

pencerem = pencere.myWin()
elemanlar = pencere.myForm()
elemanlar.pencereSet(pencerem)

pencerem.winResize(300, 250).\
    winMove(250, 250).\
    winTitle("BOTOX Spinli botlar")

# gridLayout =
elemanlar.jsonUrlData('http://127.0.0.1/test/jsonOut/')
#json ile form oluşturma işlemini yapıyor
# yeni içerik yönetimi paneli webde değil masa stünde :D
elemanlar.formVizard()

pencerem.winShow()


