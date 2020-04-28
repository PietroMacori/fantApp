from astaManager import *
from calciatore import *
from movimento import *
from portiere import *

if __name__=="__main__":
    manager=astaManager();

    list=manager.loadPlayer("/Users/pietromacori/github/fantApp/Quotazioni_Fantacalcio_Test.xlsx","/Users/pietromacori/github/fantApp/Statistiche_Fantacalcio_2018-19_Test.xlsx")

    for x in list:
        print(x)
