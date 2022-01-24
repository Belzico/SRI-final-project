import globals
import resolveCorpus
import os


        
def newDocSearch():
    myFilesNames= os.listdir(globals.dir)
    doit=False
    for item in myFilesNames:
        if item not in globals.corpusDicc:
            doit= True 
            break
    if doit:
        globals.concurrencyCorpus=resolveCorpus.resolveCorpus()
        globals.corpusDicc=globals.concurrencyCorpus
        globals.concurrencyCorpus={}