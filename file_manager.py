import pathlib

def criar_mapa_extensoes(locais):
    mapa = {}
    for pasta, extensoes in locais.items():
        for ext in extensoes:
            mapa[ext.lower()] = pasta
    return mapa

def organizador_de_arquivos(caminho: Path, locais: dict):
    mapa_extensoes = criar_mapa_extensoes(locais)

    for arquivo in caminho.intedir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()

            if extensao in mapa_extensoes:
                pasta_destino = caminho / mapa_extensoes[extensao]
                pasta_destino.mkdir(exist_ok=True)

                destino = pasta_destino / arquivo.name

                if not destino.exists():
                    arquivo.rename(destino)