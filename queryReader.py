
import myTrie
import resolveCorpus
import globals


def addQwery(qwery):
    myqwery=resolveCorpus.fixString(qwery)
    tempTrie=myTrie.Trie()
    for item in myqwery:
        tempTrie.insert(item)
    globals.qweryDicc["qwery"]=tempTrie