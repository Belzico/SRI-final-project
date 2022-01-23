

#direccion de los archivos
dir="./testCases"

corpusDicc={}
qweryDicc={}
alphaValue=0.4

numberNameDicc={}

pronounsAndOthers={}

qweryString=''

returnCount=10

resultSearch=[]

filesNames=''

bannedWords=["el","la","los","las","Un","uno","unos","una","unas","lo","al","yo","me", "mi","conmigo","tu", "te", "ti", "contigo","usted" ,"vos","el","lo" ,"le" ,"se" ,"si" ,"consigo" ,"ella" , "la", "ellos", "lo", "nosotros", "nos", "nosotras","vosotros","vosotras" , "os", "ustedes","Ellos", "ellas", "los", "las", "les", "se", "si", "consigo","somebody","enough","mine","somewhat","whatever","wherein","whereof","any","ourself","I","herself","neither","everyone","whatnot","anybody","that","some","nothing","one","there","it","something","such","both","whereto","whether","itself","he","where","nobody","whom","several","our","its","theirself","naught","wherever","whomever","whomso","this","thee","whomsoever","whose","everything","whosesoever","theirselves","anyone","whosever","them","whosoever","you","whichsoever","your","wherefrom","him","yourselves","which","her","whereinto","whereunto","who","me","none","what","those","hers","other","ourselves","these","themself","many","ought","as","anything","someone","my","whence","themselves","everybody","whoever","another","wherewith","she","few","himself","whereby","we","ours","aught","wherewithal","suchlike","us","whatsoever","their","all","either","his","myself","wheresoever","most","others","they","theirs","whichever","each","yours","yourself","idem"]

useBanned=False