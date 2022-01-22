
import myTrie
import misc
import globals


def addQwery(qwery):
    myqwery=misc.fixString(qwery)
    tempTrie=myTrie.Trie()
    for item in myqwery:
        tempTrie.insert(item)
    globals.qweryDicc["qwery"]=tempTrie
    
    
addQwery(globals.qweryString)
#print(9)
#a=globals.qweryDicc["qwery"].giveAllWords()
#for word in a:
#    print(a)