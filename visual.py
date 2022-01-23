#menu

from optparse import Values
import PySimpleGUI as sg
import os.path


sg.theme("DarkGreen6")

qwery=''
location=''
#windows 2 columns


location= sg.In(size=(25,1), enable_events=True,key="-FOLDER-")

fileListColumn=[
    [
        sg.Text("Corpus Folder"),
        location,
        sg.FolderBrowse(),
        ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(45,20),
            key="-FILE LIST-",
            expand_x=True,
            expand_y=True,
            horizontal_scroll=True
        )
        ],
    ]


qwuery=  sg.In(size=(25,1), enable_events=True,key="-QWERY-")
#solo enseña el nombre del archivo seleccionado
resultListColumn=[
    [
        sg.Text("Qwuery Search"), 
        qwuery, 
        sg.Button(button_text="Search",enable_events=True,key="-ACCEPTQWERY-")
        ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(45,20),
            key="-RESULT LIST-",
            expand_x=True,
            expand_y=True,
            horizontal_scroll=True
        )
        ],
]

textColumn=[
    [
        sg.Text("Result Text"), 
    ],
    [
        sg.Multiline(
            enable_events=True,size=(45,20),
            key="-QWERY DOCS LIST-",
            expand_x=True,
            expand_y=True,
            default_text='Your text will show up here.',
            autoscroll=True,
            disabled=True
            

        )
        ]
]

# full layout
layout = [
    [
        sg.Column(fileListColumn),
        sg.VSeparator(),
        sg.Column(resultListColumn),
        sg.VSeparator(),
        sg.Column(textColumn)
        
    ]
]

#window =sg.Window("BV-Search",layout)

#event loop

    
                
#window.Close()