import re


def fixString(data):
    print("The original string is : " + data)

    result = re.split(' |,|_|-|\.|\?|\!|;|\+|\*|\:|\[|\]|\^|\$|\(|\)|\{|\}|\=|\||\-|\\n', data)
# . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    return result