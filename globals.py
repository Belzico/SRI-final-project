import time


#direccion de los archivos
dir="./testCases"

corpusDicc={}
qweryDicc={}
alphaValue=0.4

numberNameDicc={}

pronounsAndOthers=None

qweryString=''

sugestionDicc={}

returnCount=1000000

resultSearch=[]

filesNames=''

bannedWords=["el","la","los","las","Un","uno","unos","una","unas","lo","al","yo","me", "mi","conmigo","tu", "te", "ti", "contigo","usted" ,"vos","el","lo" ,"le" ,"se" ,"si" ,"consigo" ,"ella" , "la", "ellos", "lo", "nosotros", "nos", "nosotras","vosotros","vosotras" , "os", "ustedes","Ellos", "ellas", "los", "las", "les", "se", "si", "consigo","somebody","enough","mine","somewhat","whatever","wherein","whereof","any","ourself","I","herself","neither","everyone","whatnot","anybody","that","some","nothing","one","there","it","something","such","both","whereto","whether","itself","he","where","nobody","whom","several","our","its","theirself","naught","wherever","whomever","whomso","this","thee","whomsoever","whose","everything","whosesoever","theirselves","anyone","whosever","them","whosoever","you","whichsoever","your","wherefrom","him","yourselves","which","her","whereinto","whereunto","who","me","none","what","those","hers","other","ourselves","these","themself","many","ought","as","anything","someone","my","whence","themselves","everybody","whoever","another","wherewith","she","few","himself","whereby","we","ours","aught","wherewithal","suchlike","us","whatsoever","their","all","either","his","myself","wheresoever","most","others","they","theirs","whichever","each","yours","yourself","idem"]
#bannedWords=[]

holgura=0.4

def setHolgura(value):
    if float(value)>=0.0:
        holgura=0.1
    if float(value)>0.1:
        holgura=0.9

useBanned=False

concurrencyCorpus={}



firstFolderAccess=False

def insertSuggestion(word, sugestion):
    if not word in sugestionDicc:
        return
    if sugestionDicc[word]==None:
        sugestionDicc[word]=sugestion
    elif len(sugestion)>0 and len(sugestion)>len(sugestionDicc[word]):
        sugestionDicc[word]=wordRank(word,sugestionDicc[word],sugestion)
        

def wordRank(word, currentSugestion, posibleSugestion):
    if currentSugestion==word:
        return currentSugestion
    if posibleSugestion==word:
        return posibleSugestion
    temp1=0
    temp2=0
    for i in range(len(word)):
        if currentSugestion[i]==word[i]:
            temp1+=1
        if posibleSugestion[i]==word[i]:
            temp2+=1
        if temp2>temp1:
            return posibleSugestion
        elif temp1>temp2:
            return currentSugestion
    return currentSugestion