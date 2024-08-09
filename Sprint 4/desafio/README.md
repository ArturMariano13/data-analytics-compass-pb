# 🧩 Desafio da Sprint 4
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

## 📝 Enunciado(s)
1. Construir uma imagem a partir de um arquivo de instruções *Dockerfile* que execute o código *carguru.py*. Após, executar um container a partir da imagem criada.

2. Responder: É possível reutilizar containers? Em caso positivo, apresentar o comando necessário para reiniciar um dos containers parados em seu ambiente Docker. Não sendo possível reutilizar, justifique sua resposta.

3. Executar um container que permita receber inputs durante a sua execução.
    1. Criar novo script Python que implementa o algoritmo a seguir:
    - Receber uma string via input
    - Gerar o hash da string por meio do algoritmo SHA-1
    - Imprimir o hash em uma tela, utilizando o método *hexdigest*
    - Retornar ao passo 1
    
    2. Criar uma imagem Docker chamada **mascarar-dados** que execute o script Python criado anteriormente.

    3. Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento.

    4. Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização neste espaço.

## Resposta(s)
1. [Etapa 1](etapa-1/README.md)
2. [Etapa 2](etapa-2/README.md)
3. [Etapa 3](etapa-3/README.md) 

___

### ↩️ [Retornar ao início](../../README.md)