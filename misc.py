import re
import myTrie
import globals

def fixString(data):
    #print("The original string is : " + data)

    result = re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', data)
# . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    return result


def fileToString(fileList):
    result=[]
    for item in fileList:
        result.append(item.name)
    return result

def pronounDeletion():
    tempTrie=myTrie.Trie("pronoun")
    for item in globals.bannedWords:
        tempTrie.insert(item)
    globals.pronounsAndOthers=tempTrie