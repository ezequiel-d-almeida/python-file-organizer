from ui import selecionar_pasta
from file_manager import organizador_de_arquivos
from rules import locais

def main():
    caminho = selecionar_pasta()

    if caminho:
        organizador_de_arquivos(caminho, locais)
        print('Organização concluída!')

if __name__ == '__main__':
    main()