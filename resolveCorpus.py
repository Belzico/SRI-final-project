import os
import myTrie
import globals


def giveFileList(dir):
    filesNames = os.listdir(dir)
    fileDic={}
    currentText=""
    for item in filesNames:
        file = open(str(dir)+"/"+item,"r")
        currentText=file.read()
        fileDic[item]=currentText
        file.close()
    
    return fileDic    


def resolveCorpus():
    finalDic={}
    fileDic=giveFileList(globals.dir)
    for file in fileDic:
        tempTrie=myTrie.Trie()
        line=fileDic[file]
        removeEndLine=line.split("\n")
        joinText=" ".join(removeEndLine)
        words=joinText.split(" ")
        for word in words:
            tempTrie.insert(word)
        finalDic[file]=tempTrie      
    
    return finalDic    

finalDic= resolveCorpus()
        
print("Final!!!!!!!!!!!!!!!!!!!!!!!!!")

text="prueba#2 la vida es bella."
test=text.split(" ")

print("3")