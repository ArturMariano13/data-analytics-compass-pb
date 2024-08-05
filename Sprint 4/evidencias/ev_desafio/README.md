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
