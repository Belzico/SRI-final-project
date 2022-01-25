
import myTrie
import misc
import globals


def addQwery(qwery):
    myqwery=misc.fixString(qwery)
    tempTrie=myTrie.Trie()
    for item in myqwery:
        isPronoun=globals.pronounsAndOthers.lookUpAndCount(item.lower())
        if isPronoun[0]:
            if not globals.useBanned:
                print("la palabra "+ item+" no importa")
                continue
        tempTrie.insert(item.lower())
    globals.qweryDicc["qwery"]=tempTrie
    
    addSugestion()
    
def addSugestion():
    globals.sugestionDicc={}
    for word in misc.fixString(globals.qweryString): 
        if word=="": continue
        globals.sugestionDicc[word]=None
        
def stringSugestionMaker():
    result="Las siguientes palabras no se encontraron pruebe cambiarlas por alguna similar o una de las sugeridas: "
    for key in globals.sugestionDicc:
        if not key==globals.sugestionDicc[key]:
            if globals.sugestionDicc[key]==None:
                pass
            else:
                result+=" word: "+key+"=>"+globals.sugestionDicc[key]+" "
    
    result+="."
    return result 




#addQwery(globals.qweryString)
#print(9)
#a=globals.qweryDicc["qwery"].giveAllWords()
#for word in a:
#    print(a)