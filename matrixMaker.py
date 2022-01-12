import globals
import myTrie

#recibe una lista de files para buscar en el corpus y el parametro chain si es verdadero buscara substrings tambien
def simpleMatrixCount(fileList,chain=False):
    wordsList=globals.qweryDicc["qwery"].giveAllWords()
    resultList=[]
    currentDicc=None
    i=0
    for word in wordsList:   
        resultList.append([]) 
        for file in fileList:
            myTrie=globals.corpusDicc[file]
            tup=myTrie.lookUpAndCount(word)
            #caso en que queremos el count de la palabra sin que sea un substring de otra palabra
            if not chain: 
                if tup[0]:
                    resultList[i].append(tup[2])
                else:
                    resultList[i].append(0)
            #caso en que queremos el count de la palabra aun siendo un substring de otra palabra
            else:
                if tup[0]:
                    resultList[i].append(tup[1])
                else:
                    resultList[i].append(0)
        i+=1
    
    return resultList