import queryReader
import globals
import resolveCorpus
import matrixMaker
import visual
import misc

def fileResolve():
    myFiles=[]
    for item in globals.corpusDicc:
        myFiles.append(item)
    #matrices
    tempCount=matrixMaker.simpleMatrixCount(myFiles)    
    counts=tempCount[0]
    if not tempCount[1]:
        visual.sg.popup_error(f'We cant\'t find that!')

        return ""
    normalizeFrecuency=matrixMaker.frecuenciaNormalizada(counts)
    logaritms=matrixMaker.logMatrix(counts)
    weitghs=matrixMaker.pesosMatrix(normalizeFrecuency,logaritms)

    fileList=matrixMaker.sumWeitghs(weitghs)
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
            try:
                if len(globals.corpusDicc)==0: continue

                globals.qweryString=values["-QWERY-"]

                if len(globals.qweryString)==0: continue
                queryReader.addQwery(globals.qweryString)
                globals.resultSearch= fileResolve()
                if globals.resultSearch == "": continue

                fixedStrings=misc.fileToString(globals.resultSearch)
                window["-RESULT LIST-"].update(fixedStrings)
            except:
                pass
main()