import queryReader
import globals
import resolveCorpus
import matrixMaker


myFiles=[]
for item in globals.corpusDicc:
    myFiles.append(item)
tempMatrix=matrixMaker.simpleMatrixCount(myFiles)
print("a")