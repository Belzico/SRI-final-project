import globals


class Node:
    def __init__(self, letter):
        self.letter=letter
        self.childrens={}
        self.count=1
        self.terminalCount=0

    def appendChild(self, child):
        self.childrens[child.letter]=child

    def allWords(self, wordList, currentWord):
        newWord=currentWord+self.letter
        if len(self.childrens)==0:
            wordList.append(newWord)
            return
        for item in self.childrens:
            self.childrens[item].allWords(wordList,newWord)
            
            
    
class Trie:
    def __init__(self):
        self.root=Node("")
        self.totalNodes=0
        self.words=0
        self.differentWords=0
            
    def getNextSon(self, parentNode, key):
        if key in parentNode.childrens:
            return parentNode.childrens[key]
        else:
            return None 
        
        
    def insert(self, word):

        lower_word=word.lower()
		#Empezamos desde la raíz. 
        node=self.root
        prefix=[]

        lenCount=0
        
        for letter in lower_word:
			
            lenCount+=1
            next_node=self.getNextSon(node, letter)

			#No hay siguiente nodo con tal prefijo, se crea
			#como hijo del nodo actual
            if next_node==None:
                self.totalNodes+=1
                new_node=Node(letter)
                node.appendChild(new_node)	
                node=new_node
			#Hay un nodo con tal prefijo, reemplazamos
			#el nodo actual con ese.
            else:
                node.count+=1
                node=next_node
                

            
		#Se terminó la palabra. El último nodo obtenido o insertado,
		#se marca como terminal. 	
            if lenCount==len(word):
                if node.terminalCount==0:
                    self.differentWords+=1
                node.terminalCount+=1
                self.words+=1
                
    #devuel si aparece,el count de la cadena,cuantas veces es terminal            
    def lookUpAndCount(self,word):
        myWord=''
        currentNode=self.root
        for letter in word:
            if letter in currentNode.childrens:
                currentNode=currentNode.childrens[letter]
                myWord+=letter
            else: 
                
                globals.insertSuggestion(word,refillPrefix(currentNode,myWord))
                return (False,currentNode.count,currentNode.terminalCount)
            
        globals.insertSuggestion(word,word)
        return(True,currentNode.count,currentNode.terminalCount)    
    
    def giveAllWords(self):
        result=[]
        self.root.allWords(result,"")
        return result

def refillPrefix(node,chain):
    currentNode=node
    resultChain=chain
    while len(currentNode.childrens)>0:
        for letter in currentNode.childrens:
            resultChain+=letter
            currentNode=currentNode.childrens[letter]
            break
        if currentNode.terminalCount>0:
            return resultChain
    return resultChain    
    
#myTrie=Trie()
#myTrie.insert("wacamole")
#print( myTrie.lookUpAndCount("wacamole"))
#print( myTrie.lookUpAndCount("wacamo"))
#print( myTrie.lookUpAndCount("le"))