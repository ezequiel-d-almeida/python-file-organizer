from pathlib import Path
import os
from tkinter.filedialog import askdirectory

def selecionar_pasta():
    caminho = askdirectory(title='Selecione a pasta')
    if caminho:
        return Path(caminho)
    else:
        return None