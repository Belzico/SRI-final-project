import queryReader
import globals
import resolveCorpus
import matrixMaker


myFiles=[]
for item in globals.corpusDicc:
    myFiles.append(item)
#matrices    
counts=matrixMaker.simpleMatrixCount(myFiles)
normalizeFrecuency=matrixMaker.frecuenciaNormalizada(counts)
logaritms=matrixMaker.logMatrix(counts)
weitghs=matrixMaker.pesosMatrix(normalizeFrecuency,logaritms)

fileList=matrixMaker.sumWeitghs(weitghs)
print("a")