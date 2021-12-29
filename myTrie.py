


class Node:
    def __init__(self, letter):
        self.letter=letter
        self.childrens={}
        self.count=1
        self.terminalCount=0

    def appendChild(self, child):
        self.childrens[child.letter]=child

class Trie:
    def __init__(self):
        self.root=Node(None)
        self.totalNodes=0
        self.words=0
        self.differentWords=0
            
    def getNextSon(self, parentNode, key):
        if key in parentNode.childrens:
            return parentNode.childrens[key]
        else:
            return None 
        
        
    def insert(self, word):
    	
		#Empezamos desde la raíz. 
        node=self.root
        prefix=[]

        lenCount=0
        
        for letter in word:
			
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
                
    def lookUpAndCount(self,word):
        currentNode=self.root
        for letter in word:
            if letter in currentNode.childrens:
                currentNode=currentNode.childrens[letter]
            else: 
                return (False,currentNode.count)
        
        return(True,currentNode.count,currentNode.terminalCount)    
    
                
                
#myTrie=Trie()
#myTrie.insert("wacamole")
#print( myTrie.lookUpAndCount("wacamole"))
#print( myTrie.lookUpAndCount("wacamo"))
#print( myTrie.lookUpAndCount("le"))