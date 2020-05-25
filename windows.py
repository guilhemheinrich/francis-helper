#! python

try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install('tkinter')

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    import glob
    import re
    import shutil
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
window = tk.Tk()


def export():
    # extension_list = re.split('[^\w]*,[^\w]*', extensions.get())
    with open(os.path.join(targetPath.get(), 'log.txt'), 'w') as out_file:
        for folder, subs, files in os.walk(sourcePath.get()):
            for filename in files:
                basename = os.path.splitext(filename)[0]
                if (len(basename) <= maxLength.get()) and (len(basename) >= minLength.get()):
                    shutil.copyfile(os.path.join(folder, filename), os.path.join(targetPath.get(), filename))
                    print(filename)
                    out_file.write(os.path.join(folder, filename) + '\n')


sourceString = tk.StringVar(value='Aucun dossier source sélectionné')
sourcePath = tk.StringVar()
def selectSource():
    folderString = filedialog.askdirectory()
    if folderString:
        sourcePath.set(folderString)
        sourceString.set('Source actuelle: ' + sourcePath.get())
   
sourceButton = tk.Button(window, text="Dossier source", command=selectSource)

targetString = tk.StringVar(value='Aucun dossier cible sélectionné')
targetPath = tk.StringVar()
def selectTarget():
    folderString = filedialog.askdirectory()
    if folderString:
        targetPath.set(folderString)
        targetString.set('Destination actuelle: ' + targetPath.get())

targetButton = tk.Button(window, text="Dossier cible", command=selectTarget)


executeButton = tk.Button(window, text="Execute", command=export)

minLength = tk.IntVar(value=5)
maxLength = tk.IntVar(value=5)
minLengthEntry = tk.Entry(window, textvariable=minLength )
maxLengthEntry = tk.Entry(window, textvariable=maxLength )
# extensions = tk.StringVar(value="jpg")
# extensionsEntry = tk.Entry(window, textvariable=extensions)
minLabel = tk.Label(window, textvariable=tk.StringVar(value="Taille du nom de fichier minimum"))
maxLabel = tk.Label(window, textvariable=tk.StringVar(value="Taille du nom de fichier maximum"))
# extensionsLabel = tk.Label(window, textvariable=tk.StringVar(value="Extensions (liste séparée par des virgules)"))
sourceSelected = tk.Label(window,  textvariable = sourceString)
targetSelected = tk.Label(window, textvariable = targetString)
# layout
minLabel.pack()
minLengthEntry.pack()
maxLabel.pack()
maxLengthEntry.pack()
# extensionsLabel.pack()
# extensionsEntry.pack()
sourceButton.pack()
targetButton.pack()
sourceSelected.pack()
targetSelected.pack()
executeButton.pack()
window.mainloop()

