import misc



resultList=open(".\desechable\cranqrel.txt","r")
                
text=resultList.read()


def removeBlank(mylist):
    resultList=[]
    for item in mylist:
        if item !='':
            resultList.append(item)
    return resultList

resultList.close()
textList=removeBlank( misc.fixString(text))
diccResults={}
for element in range(len(textList)):
    if element%3==0:
        try:
            if not int(textList[element]) in diccResults:
                diccResults[int(textList[element])]=1
            else:
                diccResults[int(textList[element])]=diccResults[int(textList[element])]+1
        except:
            pass
print("a")

