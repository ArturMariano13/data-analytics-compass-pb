# Evidências do Desafio da Sprint 4

## Passo a passo

### 0. Preparação
- Download do arquivo *carguru.py*.
- Verificação da instalação correta da solução para containers.

### 1. Etapa 1
1. Criação do Dockerfile
- **FROM:** Optar por python:3.10-slim é uma boa escolha por ser mais leve e adequado para a maioria das aplicações Python.
- **WORKDIR:** /app é uma escolha comum e adequada para o diretório de trabalho no container.
- **COPY:** O comando COPY carguru.py . copia o arquivo carguru.py do diretório onde o Dockerfile está localizado para o diretório /app no container.
- **CMD:** O comando CMD ["python", "carguru.py"] define o comando padrão que será executado quando o container iniciar. No caso, ele executa o script Python.

2. Build da Imagem
- **Comando:** `docker build -t carguru-image .`
    - **-t carguru-image**: Adiciona a tag carguru-image à imagem. Por padrão, a tag será *latest*.
    - **'.'**: O ponto indica o diretório atual como o contexto de *build*.

3. Execução da imagem
- **Comando:** docker run --name carguru-container carguru-image
    - `--name carguru-container`: Dá um nome ao container (carguru-container), o que facilita a referência e o gerenciamento.
    - `carguru-image`: O nome da imagem a ser usada para criar o container.

### 2. Etapa 2
- [Resposta](../../desafio/etapa-2/README.md)

### 3. Etapa 3
**0. Preparação**
- Verificação se o Docker está em execução no seu sistema `docker info`.

**1. Script Python**
- Um script Python que recebe uma string, gera o hash SHA-1 da string e imprime o resultado.
- Biblioteca *hashlib*, a qual oferece uma interface simples e direta para a criação de hashes usando vários algoritmos de hash, incluindo SHA-1. 

**2. Criação do Dockerfile**
- `FROM`: Utiliza a imagem base python:3.10-slim, que é uma versão leve do Python 3.10.
- `WORKDIR`: Define o diretório de trabalho dentro do container como /app.
- `COPY`: Copia o arquivo mascarar_dados.py do diretório onde o Dockerfile está localizado para o diretório /app no container.
- `CMD`: Define o comando a ser executado quando o container iniciar, que é python mascarar_dados.py.

**3. Build da imagem**
- Comando: `docker build -t mascarar-dados .`
    - `-t mascarar-dados`: Adiciona a tag mascarar-dados à imagem.
    - `.`: O ponto indica o diretório atual como o contexto de build.

**4. Execução container**
- Comando: `docker run --name mascarar-dados-container -it mascarar-dados`
    - `--name mascarar-dados-container`: Define o nome do container.
    - `-it`: Permite **interação** com o terminal (modo interativo), essencial para enviar strings ao script.
    - *mascarar-dados*: Nome da imagem a ser usada para criar e executar o container.

___
### ↩️ [Retornar ao início](../../../README.md)
