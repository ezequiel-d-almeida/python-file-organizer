import os
from tkinter.filedialog import askdirectory

def selecionar_pasta():
    caminho = askdirectory(title='Selecione a pasta')
    if caminho:
        return caminho
    else:
        return None