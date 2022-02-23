from glob import glob
from os import write
import misc
import queryReader
import globals
import resolveCorpus
import matrixMaker
import visual
import misc
import re
from myTrie import Trie


def MetricEvaluation(cases, ListResult, ListEsperados, rank):
    total_cases = len(cases)
    arc_R = len(ListResult)
    arc_Esp = len(ListEsperados)
    
    T_esperados = Trie()
    for arch in ListEsperados:
        T_esperados.insert(arch)
    
    T_cases = Trie()
    for arch in cases:
        T_cases.insert(arch)
    
    RR = 0
    RI = 0
    NR = 0
    NI = 0
    
    RR_rank = 0
    RI_rank = 0
    NR_rank = 0
    NI_rank = 0
    
    n = 0
    # Revisamos de los resultados previstos y cuales no son de interés
    for arch in ListResult:
        result = T_esperados.lookUpAndCount(arch)
        if result[0] == False:
            RI += 1
            if n < rank:
                RI_rank += 1
        else:
            RR += 1
            if n < rank:
                RR_rank += 1
        n += 1 
    
    # Los documentos no relevantes recuperados es el resultado de eliminar de los esperados
    # los doumentos ya recuperados de relevancia 
    NR = arc_Esp - RR
    NR_rank = arc_Esp - RR_rank
    
    # Los documentos irrelevantes no recuperados es el resultado de eliminar los esperados
    # del total de casos y los recuperados irrelevantes
    NI = total_cases - arc_Esp - RI
    NI_rank = total_cases - arc_Esp - RI_rank
    
    # En este diccionario guardaremos los resultados de cada métrica 
    result_metric = {}
    
    #Medida de precisión
    P = RR / (RR + RI)
    result_metric["Precisión"] = P
    
    P_rank = RR_rank / (RR_rank + RI_rank)
    result_metric["Precisión_"+str(rank)] = P_rank
    
    #Medida de Recobrado
    R = RR / (RR + NR)
    result_metric["Recobrado"] = R
    
    R_rank = RR_rank / (RR_rank + NR_rank)
    result_metric["Recobrado_"+str(rank)] = R_rank
    
    # Medida F1
    F1 = '-'
    if P != 0 and R != 0:
        F1 = 2*P*R / (P + R)
    result_metric["F1"] = F1
    
    F1_rank = '-'
    if P_rank != 0 and R_rank != 0:
        F1_rank = 2*P_rank*R_rank / (P_rank + R_rank)
    result_metric["F1_"+str(rank)] = F1_rank
    
    # Proporcion de fallo
    Fallout = RI / (RI + NI)
    result_metric["Fallout"] = Fallout
    
    Fallout_rank = RI_rank / (RI_rank + NI_rank)
    result_metric["Fallout_" + str(rank)] = Fallout_rank
    
    PrintResult_Metric(result_metric,rank)
    return result_metric

def consult(qwery, cases):
    arch = open("./adi/ADIREL",'r')
    text = arch.read()
    doc = str.split(text,"\n")
    arch.close()
    
    linesplits = []
    for line in doc:
        temp = str.split(line,' ')
        temparr = []
        for val in temp:
            if val == "":
                continue
            temparr.append(val)
            
        linesplits.append(temparr)
    
    listnarch = []
    
    for line in linesplits:
        if line[0] != qwery:
            continue
        listnarch.append(line[1])
    
    listresult = {}
    for archrel in listnarch:
            if archrel in cases:
                listresult[archrel] = cases[archrel]
    
    return listresult    

def PrintResult_Metric(result_metric,rank):
    print("Metric-Evaluation:")
    print("Precision: " + str(result_metric["Precisión"]))
    print("Recobrado: " + str(result_metric["Recobrado"]))
    print("F1: " + str(result_metric["F1"]))
    print("Fallout: " + str(result_metric["Fallout"]))
    print("-------------------------------")
    print("Precision_"+str(rank) +": " + str(result_metric["Precisión_"+str(rank)]))
    print("Recobrado_"+str(rank) + ": " + str(result_metric["Recobrado_"+str(rank)]))
    print("F1_"+str(rank) + ": " +  str(result_metric["F1_"+str(rank)]))
    print("Fallout_" + str(rank) + ": " + str(result_metric["Fallout_" + str(rank)]))

def RevResult(dirc,dirq):
    cases = DetectArch_Folder(dirc)
    Lqwery = ParsQwery(dirq)
    
    i = 0
    globals.corpusDicc = cases
    resultmetric = []
    
    for qwery in Lqwery:
        
        globals.qweryString = qwery
        
        if len(qwery)==0: continue
        queryReader.addQwery(qwery)
        resultSearch = fileResolve()
        if resultSearch == "": continue

        fixedStrings=misc.fileToString(resultSearch)
        ListResult = Filtre_ListLink(fixedStrings)
        
        print("------------- Qwery " + str(i+1) + " ------------------")
        dic = EvalSistem(str(i+1),cases, ListResult, 10)
        print("------------------------------------------------")  
        i += 1
        
        resultmetric.append(dic)
    
    PromMetric(resultmetric,10)
    
def DetectArch_Folder(dir):  
    misc.pronounDeletion()
    globals.dir = dir
            
    if len(globals.dir)==0: return None
    corpusDicc = resolveCorpus.resolveCorpus()
    
    if len(corpusDicc)==0: return None
    
    return corpusDicc

def ParsQwery(dir):
    myDir = dir
            
    if len(myDir)==0: return None
    
    arch = open(dir,'r')
    text = arch.read()
    doc = str.split(text,"\n")
    arch.close()
    
    qwery = ""
    l = []
    
    I_hc = False
    W_hc = False
    
    i = 0
    while i < len(doc):
        line = doc[i]
        
        if not I_hc and line[0] == '.' and line[1] == 'I':
            I_hc = True
            i += 1
            line = doc[i]
        
        if I_hc and line[0] == '.' and line[1] == 'W':
            qwery = ""
            W_hc = True
            
            i += 1
            line = doc[i]
            
        if I_hc and W_hc:
            while True:
                qwery += line
                if i == len(doc) - 1: break
                if doc[i+1] == "":
                    i+=1
                    line = doc[i] 
                    break
                if doc[i+1][0] == '.' and doc[i+1][1] == 'I': break
                i += 1
                line = doc[i]
                
                if line == "":
                    break
                
            l.append(qwery)
            I_hc = False
            W_hc = False
            
        else:
            print("error linea " + str(i))
            return "Error en conformacion de documentos de Qwery"
        
        i += 1
        
    return l

def EvalSistem(qwery,cases, ListResult, rank):
    listesperados = consult(qwery,cases)
    dic = MetricEvaluation(cases,ListResult,listesperados,rank)
    return dic
    
def fileResolve():
    
    temp=globals.qweryString
    myFiles=[]
    for item in globals.corpusDicc:
        myFiles.append(item)
    #matrices
    tempCount=matrixMaker.simpleMatrixCount(myFiles)  
    wordsUse=tempCount[2]  
    counts=tempCount[0]
    if not tempCount[1]:
        visual.sg.Popup('We cant\'t find that!')

        return ""
    normalizeFrecuency=matrixMaker.frecuenciaNormalizada(counts)
    
    #countBorrarList=matrixMaker.countOcurrency(counts)
    #borrar
    #tempListCountNi=matrixMaker.wordInDocsList(wordsUse)
    
    logaritms=matrixMaker.logMatrix(counts)
    weitghs=matrixMaker.pesosMatrix(normalizeFrecuency,logaritms)
    
    qweryNormFre=matrixMaker.fNmatrixQweryBuilder()
    
    pesosQwery=matrixMaker.pesosQweryCalculator(logaritms,qweryNormFre)

    fileList=matrixMaker.sumWeitghs(weitghs,pesosQwery)
    return fileList

def Filtre_Link(dir):
    listdr = str.split(dir,'/')
    return listdr[-1]

def Filtre_ListLink(lisL):
    lisarch = []
    for link in lisL:
        arch = Filtre_Link(link)
        lisarch.append(arch)
        
    return lisarch

def PromMetric(results,rank):
    dicr = {}
    for dic in results:
        for val in dic:
            if not val in dicr:
                dicr[val] = dic[val]

                    
            else:
                if dicr[val] == '-':
                    dicr[val] = 0
                
                if dic[val] != '-':
                    dicr[val] = dicr[val] + dic[val]
    
    for val in dicr:
        dicr[val] = dicr[val]/len(results)
    
    print("------------- General Result --------------")
    PrintResult_Metric(dicr,rank)
    return dicr

def WriteDocument(list, dir):
    i = 0
    for arch in list:
        i += 1
        f = open(dir + "/" + str(i), 'w')
        f.write(arch)
        f.close()

def ConstrDocs(dir):
    myDir = dir
            
    if len(myDir)==0: return None
    
    arch = open(dir,'r')
    text = arch.read()
    doc = text.split('\n')
    arch.close()
    
    qwery = ""
    l = []
    
    I_hc = False
    W_hc = False
    
    i = 0
    while i < len(doc):
        line = doc[i]
        
        if not I_hc and line[0] == '.' and line[1] == 'I':
            I_hc = True
            i += 1
            line = doc[i]
        
        if I_hc and line[0] == '.' and line[1] == 'T':
            qwery = ""
            W_hc = True
            
            i += 1
            line = doc[i]
            
        if I_hc and W_hc:
            while True:
                qwery += line + "\n"
                
                if i == len(doc) - 1: break
                if doc[i+1] == "":
                    i += 1
                    line = doc[i]
                    continue
                
                if doc[i+1][0] == '.' and doc[i+1][1] == 'I': break
                i += 1
                line = doc[i]
                
            l.append(qwery)
            I_hc = False
            W_hc = False
            
        else:
            print("error linea " + str(i))
            return "Error en conformacion de documentos de Qwery"
        
        i += 1
        
    return l

   
#l = ConstrDocs("./adi/ADI.ALL")
#WriteDocument(l,"./adi/adicases")
RevResult("./adi/adicases", "./adi/ADI.QRY")