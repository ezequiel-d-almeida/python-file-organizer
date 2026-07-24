# Organizador de Arquivos

Aplicação desktop desenvolvida em Python para automatizar a organização de arquivos em diretórios locais.

O projeto foi criado com o objetivo de eliminar a organização manual de arquivos, classificando documentos automaticamente conforme regras pré-definidas. Além de resolver um problema cotidiano, este projeto serviu como estudo de manipulação de arquivos, interfaces gráficas e automação utilizando Python.

---

## Objetivo

Organizar automaticamente os arquivos de um diretório, reduzindo o tempo gasto com tarefas repetitivas e diminuindo erros durante a organização manual.

---

## Funcionalidades

- Organização automática de arquivos.
- Classificação por tipo de arquivo.
- Interface gráfica para seleção da pasta.
- Regras de organização configuráveis.
- Manipulação segura de arquivos utilizando a biblioteca padrão do Python.

---

## Tecnologias Utilizadas

- Python 3
- Tkinter
- pathlib
- shutil
- os

---

## Estrutura do Projeto

```text
.
├── main.py
├── file_manager.py
├── rules.py
└── ui.py
```

### Responsabilidades dos módulos

| Arquivo | Responsabilidade |
|----------|------------------|
| `main.py` | Inicialização da aplicação |
| `ui.py` | Interface gráfica e interação com o usuário |
| `file_manager.py` | Manipulação e movimentação dos arquivos |
| `rules.py` | Definição das regras utilizadas na organização |

---

## Como executar

### Clone o repositório

```bash
git clone https://github.com/ezequiel-d-almeida/Organizador_de_Arquivos.git
```

### Acesse o diretório

```bash
cd Organizador_de_Arquivos
```

### Execute a aplicação

```bash
python main.py
```

---

## Como funciona

1. O usuário seleciona a pasta que deseja organizar.
2. A aplicação identifica os arquivos presentes no diretório.
3. Cada arquivo é analisado de acordo com as regras de classificação.
4. Os arquivos são movidos automaticamente para suas respectivas pastas.

---

## Possíveis melhorias

Este projeto foi desenvolvido como uma aplicação de estudo e pode evoluir com novas funcionalidades, como:

- suporte a organização por data de criação;
- organização por tamanho dos arquivos;
- sistema de desfazer operações;
- personalização das regras pela interface gráfica;
- geração de relatórios após a organização;
- suporte à execução via linha de comando (CLI);
- registro de logs das operações realizadas.

---

## Aprendizados

Durante o desenvolvimento deste projeto foram explorados conceitos importantes do ecossistema Python, entre eles:

- manipulação de arquivos e diretórios;
- criação de interfaces gráficas com Tkinter;
- separação de responsabilidades entre módulos;
- automação de tarefas locais;
- utilização de boas práticas na organização do código.

---

## Licença

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais informações.