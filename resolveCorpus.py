import os
import myTrie
import globals
import misc




def giveFileList(dir):
    globals.filesNames= os.listdir(dir)
    fileDic={}
    currentText=""
    i=0
    for item in globals.filesNames:
        file = open(str(dir)+"/"+item,"r")
        
        globals.numberNameDicc[i]=file
        globals.numberNameDicc[file]=i
        
        currentText=file.read()
        fileDic[item]=currentText
        file.close()

        i+=1
    return fileDic    


def resolveCorpus():
    finalDic={}
    fileDic=giveFileList(globals.dir)
    for file in fileDic:
        tempTrie=myTrie.Trie("corpus")
        line=fileDic[file]
        words= misc.fixString(line)
        for word in words:
            
            if len(word)>0:
                isPronoun=globals.pronounsAndOthers.lookUpAndCount(word.lower())
                if isPronoun[0]:
                    if not globals.useBanned:
                        continue
                        
                tempTrie.insert(word.lower())
        finalDic[file]=tempTrie      
    
    return finalDic    



print("Final!!!!!!!!!!!!!!!!!!!!!!!!!")










