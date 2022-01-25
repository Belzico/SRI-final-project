from calendar import c
import globals
import myTrie
import math

#recibe una lista de files para buscar en el corpus y el parametro chain si es verdadero buscara substrings tambien
def simpleMatrixCount(fileList,chain=False):
    wordsList=globals.qweryDicc["qwery"].giveAllWords()
    #borrar
    wordsUse=[]
    for x in wordsList:
        print("la palabra "+x + " importa")
        wordsUse.append(x)
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
    
    return (resultList,everApear,wordsUse)

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
        countOcurrency=0
        if resultMatrix[1][column]==0:
            tempLog=0
        else:
            tempLog=math.log(float(resultMatrix[0][column]/float(resultMatrix[1][column])),10)
        resultMatrix[2].append(tempLog)
            
    return resultMatrix
        
def pesosMatrix(fNmatrix,logMatrix):
    a=globals.alphaValue
    resultMatrix=[]
    for row in range(len(fNmatrix)):
        resultMatrix.append([])
        for column in range(len(fNmatrix[0])):
            resultMatrix[row].append(fNmatrix[row][column]*logMatrix[2][column])
    return resultMatrix

def fNmatrixQweryBuilder():
    wordsList=globals.qweryDicc["qwery"].giveAllWords()
    maxCount=1
    resultList=[]
    for word in wordsList:
        tempSearch=globals.qweryDicc["qwery"].lookUpAndCount(word)
        resultList.append(tempSearch[2])
        if tempSearch[2]>maxCount:
            maxCount=tempSearch[2]
    for item in range(len(wordsList)):
        resultList[item]=resultList[item]/maxCount        

    return resultList
    
    
def pesosQweryCalculator(logMatrixQwery,fNmatrixQwery):
    
    resultList=[]
    for column in range(len(fNmatrixQwery)):
        tem1=globals.alphaValue+(1-globals.alphaValue)
        tem2=tem1*fNmatrixQwery[column]
        temp3=tem2*logMatrixQwery[2][column]
        resultList.append(temp3)
    
    return resultList
        



def sumWeitghs(pesosDoc, pesosQwery):
    
    
    
    
    currentImportantDoc=[]
    numerator=0
    denominatorRigth=0
    denominatorLeft=0
    
    for i in range(len(pesosDoc)):
        for j in range(len(pesosQwery)):
            numerator+=pesosDoc[i][j]*pesosQwery[j]
            denominatorLeft+=pow(pesosDoc[i][j],2)
            denominatorRigth+=pow(pesosQwery[j],2)
        
        denominatorRigth=math.sqrt(denominatorRigth)
        denominatorLeft=math.sqrt(denominatorLeft)
        if denominatorLeft==0 or denominatorRigth==0:
            currentImportantDoc.append(0)
        else:    
            currentImportantDoc.append(numerator/(denominatorLeft*denominatorRigth))
        
        numerator=0
        denominatorRigth=0
        denominatorLeft=0
    
    #aca esto se debe separar en otro metodo para cuando se tomen otros criterios a la hora de devolver los mas importantes
    resultList=[]
    banned={}
    tempCount=0
    currentImportantPos=0
    weChange=False
    for i in range(min([globals.returnCount,len(currentImportantDoc)])):
        currentMaxSum=0
        for j in range(len(currentImportantDoc)):
            if currentImportantDoc[j]>currentMaxSum and j not in banned and currentImportantDoc[j]>0.4:
                currentMaxSum=currentImportantDoc[j]
                currentImportantPos=j
                weChange=True
        if weChange:
            banned[currentImportantPos]=True
            resultList.append(globals.numberNameDicc[currentImportantPos])
            currentImportantPos=0
            weChange=False
            tempCount+=1
            
    print(tempCount)    
    return resultList

def wordInDocsList(listwords):
    resultList=[]
    for word in listwords:
        resultList.append(""+word+" => "+str(wordInDocs(word)))
    return resultList
    

def wordInDocs(word):
    result=0
    docs=[]
    for key in globals.corpusDicc:
        temp= globals.corpusDicc[key].lookUpAndCount(word)
        if temp[0]:
            result+=1
            docs.append(key)
            
    return (result,docs)

def countOcurrency(countMatrix):
    result=[]
    docs=[]
    for column in range(len(countMatrix[0])):
        result.append(0)
        docs.append([])
        for row in range(len(countMatrix)):
            result[column]+=countMatrix[row][column]
            docs[column].append(row)
    return (result,docs)
    