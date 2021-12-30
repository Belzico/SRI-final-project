import os
import myTrie
import globals
import re

def fixString(data):
    print("The original string is : " + data)

    result = re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', data)
# . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    return result


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
        words= fixString(line)
        for word in words:
            if len(word)>0:
                tempTrie.insert(word)
        finalDic[file]=tempTrie      
    
    return finalDic    

finalDic= resolveCorpus()
        
print("Final!!!!!!!!!!!!!!!!!!!!!!!!!")










