from calendar import c
import globals
import myTrie
import math

#recibe una lista de files para buscar en el corpus y el parametro chain si es verdadero buscara substrings tambien
def simpleMatrixCount(fileList,chain=False):
    wordsList=globals.qweryDicc["qwery"].giveAllWords()
    resultList=[]
    currentDicc=None
    everApear=False
    i=0
    for file in fileList:
        resultList.append([]) 
        myTrie=globals.corpusDicc[file]
        for word in wordsList:
            
            tup=myTrie.lookUpAndCount(word)
            #caso en que queremos el count de la palabra sin que sea un substring de otra palabra
            if not chain: 
                if tup[0]:
                    resultList[i].append(tup[2])
                    everApear=True
                else:
                    resultList[i].append(0)
            #caso en que queremos el count de la palabra aun siendo un substring de otra palabra
            else:
                if tup[0]:
                    resultList[i].append(tup[1])
                    everApear=True
                else:
                    resultList[i].append(0)
        i+=1
    
    return (resultList,everApear)

def frecuenciaNormalizada(countMatrix):
    currentMax=0
    resultMatrix=[]
    for row in range(len(countMatrix)):
        resultMatrix.append([])
        for column in range(len(countMatrix[row])):
            if countMatrix[row][column]>currentMax:
                currentMax=countMatrix[row][column]
        for column in range(len(countMatrix[row])):
            if currentMax==0:
                resultMatrix[row].append(0)
            else:
                resultMatrix[row].append(countMatrix[row][column]/currentMax)
        currentMax=0
    
    return resultMatrix            


def logMatrix(countMatrix):
    resultMatrix=[]
    resultMatrix.append([])
    resultMatrix.append([])
    resultMatrix.append([])

    
    for column in range(len(countMatrix[0])):
        resultMatrix[0].append(len(countMatrix))
        countOcurrency=0
        for newRow in range(len(countMatrix)):
            if countMatrix[newRow][column]!=0:
                countOcurrency+=1
                
        resultMatrix[1].append(countOcurrency)
        
        if resultMatrix[1][column]==0:
            tempLog=0
        else:
            tempLog=math.log10(int(resultMatrix[0][column]/int(resultMatrix[1][column])))
        resultMatrix[2].append(tempLog)
            
    return resultMatrix
        
def pesosMatrix(fNmatrix,logMatrix):
    a=globals.alphaValue
    resultMatrix=[]
    for row in range(len(fNmatrix)):
        resultMatrix.append([])
        for column in range(len(fNmatrix[0])):
            resultMatrix[row].append((a+(1-a)*fNmatrix[row][column])*logMatrix[2][column])
    return resultMatrix


def sumWeitghs(pesos):
    
    currentMaxSum=0
    currentImportantDoc=[]
    
    for i in range(len(pesos)):
        for j in range(len(pesos[0])):
            currentMaxSum+=pesos[i][j]
        
        currentImportantDoc.append(currentMaxSum)
        currentMaxSum=0
    
    
    #aca esto se debe separar en otro metodo para cuando se tomen otros criterios a la hora de devolver los mas importantes
    resultList=[]
    banned={}
    currentImportantPos=0
    for i in range(min([globals.returnCount,len(pesos)])):
        currentMaxSum=0
        for j in range(len(currentImportantDoc)):
            if currentImportantDoc[j]>currentMaxSum and j not in banned:
                currentMaxSum=currentImportantDoc[j]
                currentImportantPos=j
        banned[currentImportantPos]=True
        resultList.append(globals.numberNameDicc[currentImportantPos])
        
        
    return resultList

            