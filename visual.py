#menu

from optparse import Values
import PySimpleGUI as sg
import os.path


#windows 2 columns

fileListColumn=[
    [
        sg.Text("Corpus Folder"),
        sg.In(size=(25,1), enable_events=True,key="-FOLDER-"),
        sg.FolderBrowse(),
        ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(40,20),
            key="-FILE LIST-"
        )
        ],
    ]

#solo enseña el nombre del archivo seleccionado
resultListColumn=[
   [
        sg.Text("Qwuery Search"), 
        sg.In(size=(25,1), enable_events=True,key="-QWERY-"),
        ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(40,20),
            key="-RESULT LIST-"
        )
        ],
]

# full layout
layout = [
    [
        sg.Column(fileListColumn),
        sg.VSeparator(),
        sg.Column(resultListColumn)
    ]
]

window =sg.Window("BV-Search",layout)

#event loop
while True:
    event, values=window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event=="-FOLDER-":
        folder =values["-FOLDER-"]
        try:
            #get list of the files in folder
            file_list =os.listdir(folder)
        except:
            file_list=[]
        
        fnames=[
            
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png",",gif"))
            ]
        window["-FILE LIST-"].update(fnames)

    
                
window.Close()