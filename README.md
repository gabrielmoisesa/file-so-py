# FileSO.py <img width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python logo" align="center"/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)

Programa em Python, executado no terminal/console, que cria, lê, renomeia e exclui um arquivo contendo informações do sistema operacional em que está sendo executado.

Projeto desenvolvido como desafio prático da disciplina de Sistemas Operacionais, cobrindo os desafios das categorias **Arquivos** e **Sistema** do catálogo.

<details>
  <summary>Índice</summary>

  1. [Desafios Cobertos](#desafios-cobertos)
  2. [Funcionalidades](#funcionalidades)
  3. [Estrutura do Projeto](#estrutura-do-projeto)
  4. [Como Executar](#como-executar)
  5. [Exemplo de Saída](#exemplo-de-saída)
  6. [Licença](#licença)

</details>

## Desafios cobertos

**Arquivos**
- Criar arquivo
- Escrever e ler dados
- Renomear / excluir arquivo

**Sistema**
- Obter informações do SO

## Funcionalidades

O programa é uma aplicação de linha de comando (CLI) que exibe um menu interativo no terminal com as seguintes opções:

1. Criar arquivo com informações do SO (sistema operacional, versão, arquitetura, nome da máquina, usuário e versão do Python)
2. Ler o conteúdo do arquivo
3. Renomear o arquivo
4. Excluir o arquivo
5. Mudar o arquivo/caminho padrão
- `m` — Exibir o menu novamente
- `q` — Sair do programa

## Estrutura do projeto

```
src/
├── file_ops.py
├── main.py
└── sys_info.py
.gitignore
LICENSE
README.md
```

- **src/main.py** — menu principal e fluxo do programa
- **src/sys_info.py** — coleta as informações do sistema operacional
- **src/file_ops.py** — operações de criar, ler, renomear e excluir arquivo

## Como executar

A partir da raiz do projeto:

```bash
python src/main.py
```

Ou, entrando na pasta `src`:

```bash
cd src
python main.py
```

Nenhuma dependência externa é necessária — o projeto usa apenas módulos nativos do Python (`os`, `platform`, `socket`, `json`).

## Exemplo de saída

Ao escolher a opção de criar arquivo, o programa gera um `.json` parecido com este:

```json
{
    "sistema_operacional": "Linux",
    "release": "6.8.0",
    "versao": "#1 SMP PREEMPT_DYNAMIC",
    "arquitetura": "x86_64",
    "nome_maquina": "meu-computador",
    "usuario": "usuario",
    "versao_python": "3.11.4"
}
```

## Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.