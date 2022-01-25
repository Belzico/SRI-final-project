from glob import glob
import queryReader
import globals
import resolveCorpus
import matrixMaker
import visual
import misc
import time
import miniCrwaler
import threading

def concurrencyResolve():
    while True:
        if globals.firstFolderAccess:
            miniCrwaler.newDocSearch()
            #visual.sg.popup_error(f'Im searching!')
        time.sleep(200)

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
    #print("a")

window =visual.sg.Window("SRI-Search",visual.layout,size = (1120,400),resizable = True)

def main():
    while(True):
        event, values = window.read()
    
    #EXITING
        if event=="Exit" or event == visual.sg.WIN_CLOSED:
            try:
                window.close()
                break
            except:
                pass
            
        if event =="-FOLDER-":
            
            try:
                try:
                    holgura = float(values["-HOLGURA INPUT-"])
                    globals.setHolgura(holgura)
                except:
                    pass
                
                visual.sg.Popup("Please wait a bit")
                #visual.sg.popup_error(f"Please wait a bit")
                myDir = values["-FOLDER-"]
                misc.pronounDeletion()
                globals.dir=myDir
            
                if len(myDir)==0: continue
                globals.corpusDicc= resolveCorpus.resolveCorpus()
                window["-FILE LIST-"].update(globals.filesNames)
            except:
                pass

        
        if event=="-RESULT LIST-":
            try:
                myDir=values["-RESULT LIST-"][0]
                currentFile=open(myDir,"r")
                
                window["-QWERY DOCS LIST-"].update(currentFile.read())

                currentFile.close()
            except:
                pass
            
    #Nor Check Boxes
        if event =="-ACCEPTQWERY-":
            visual.sg.Popup(f"Please wait a bit")
            #try:
            if len(globals.corpusDicc)==0: continue

            globals.qweryString=values["-QWERY-"]

            if len(globals.qweryString)==0: continue
            queryReader.addQwery(globals.qweryString)
            globals.resultSearch= fileResolve()
            if globals.resultSearch == "": continue

            fixedStrings=misc.fileToString(globals.resultSearch)
            window["-RESULT LIST-"].update(fixedStrings)
                
            globals.firstFolderAccess=True
                
            textSuggestion= queryReader.stringSugestionMaker()
            visual.sg.Popup(textSuggestion)
            #except:
            #    pass


hilo1=threading.Thread(target=concurrencyResolve)
hilo1.start()
main()