import re


def fixString(data):
    print("The original string is : " + data)

    result = re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', data)
# . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    return result


def fileToString(fileList):
    result=[]
    for item in fileList:
        result.append(item.name)
    return result