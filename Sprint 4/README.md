# SPRINT 4 - Paradigma Funcional (Python), Containers e Introdução AWS

## Certificados
Para maiores informações sobre os certificados, siga o link: [certificados](certificados)

## Desafio
Para maiores informações sobre o desafio final, siga o link: [desafio](desafio)

## Evidências
Para maiores informações sobre as evidências, siga o link: [evidências](evidencias)

## Exercícios
Para maiores informações sobre os exercícios, siga o link: [exercícios](exercicios)

___

# Resumo dos estudos
## 🧩 Paradigma Funcional
- Python é uma linguagem **multi-paradigma**, não necessariamente funcional.
- Paradigma funcional trabalha com dados imutáveis.
- Deixar processamento para quando for realmente necessário (exemplo: *generator*, que gera elementos sob demanda).

### Capacidades implementadas
- *First Class Functions*: consegue trabalhar funções como dados (uma variável pode armazenar uma função)
- *High Order Functions*: funções podem receber outras como parâmetros, ou retornar uma outra função.
- *Anonymous Functions*: sem nome => lambda
- *Closure*
- *Recursion*
- *Immutability*: importante para uso de *threads*.
- *Lazy Evaluation*

#### *First Class Functions*

## Docker para Desenvolvedores (Udemy) 🐳
### O que é? 🤔
- Docker é uma plataforma que reduz a complexidade de configuração e setup de aplicações.
- Utiliza **containers**, que são ambientes isolados para rodar aplicações.
- Permite criar **ambientes independentes** que funcionam em diversos sistemas operacionais.
- **Melhora o desempenho** dos projetos ao proporcionar consistência entre diferentes ambientes.
- Reduz o tempo gasto em manutenção e resolução de problemas relacionados a dependências e configuração.
- É **similar a uma máquina virtual (VM)**, mas é mais leve, pois não executa um sistema operacional completo, apenas o necessário para rodar a aplicação.

### Containers 🧱
- São **pacotes de código que podem executar uma ação**, por exemplo: rodar uma aplicação de Node.js, PHP, Python...
- Utilizam imagens para poderem ser executados.
- Múltiplos containers podem rodar juntos.

- **CONTAINER X IMAGEM**
    - **Imagem:** é o projeto que será executado pelo container (possuirá todas as instruções).
    - **Container:** é o Docker rodando alguma imagem (executando algum código).
    - O fluxo é: criar uma imagem e, em seguida, executar um container a partir dessa imagem.

#### Executar uma imagem:
```shell
docker run <imagem>
```

#### Verificar containers executados
```shell
docker ps
# mostra todos os containers rodando
```
- `-a`: mostra todos os containers que já rodaram.

#### Executar com interação
- Aloca o terminal para a execução daquele container.
- **Comando:** `docker run -it <imagem>`

#### Executar em *background*
- Utilizar a flag `-d`.
- **Comando:** `docker run -d <imagem>`

#### Expor portas de container
- Utilizar a flag `-p`.
- **Exemplo:** `docker run -d -p 80:80 <imagem>` => nesse caso, o container rodará em background na porta 80.

#### Parar containers
- Libera recursos que estão sendo gastos pelo mesmo.
- **Comando:** `docker stop <id ou nome>`

#### Reiniciando containers
- Caso seja necessário aproveitar um antigo, optar pelo `start`.
- **Comando:** `docker start <id>`
- Pode-se utilizar a flag `-i` para reiniciar no modo interativo.

#### Definindo nome do container
- Se não utilizar, o docker dá um nome aleatório.
- **Comando:** `docker run --name <nome> <imagem>`

#### Verificando logs
- Podemos **verificar o que aconteceu** em um container.
- **Comando:** `docker logs <id>`

#### Removendo containers
- O container removido não é mais listado em `docker ps -a`.
- **Comando:** `docker rm <id>`
- A flag -f pode forçar a remoção.

### Imagem 🖼️
- São **originadas de arquivos que programamos** para que o Docker crie uma estrutura que execute determinadas ações em containers.
- Elas contêm informações como: imagens base, diretório base, comandos a serem executados, porta de aplicação, etc.
- Ao executar um container baseado na imagem, as **instruções serão executadas em camadas**.

#### Criando uma imagem
- Precisaremos de um arquivo **Dockerfile**.
- **FROM:** imagem base
- **WORKDIR:** diretório de aplicação
- **EXPOSE:** porta da aplicação
- **COPY:** quais arquivos precisam ser copiados

#### Executando uma imagem
- Para executar a imagem, primeiramenta vamos precisar fazer o *build*.
- **Comando *build*:** `docker build <diretório da imagem>`
- **Comando EXECUÇÃO:** `docker run <imagem>`

OBS.: especificar a porta e o nome no comando de execução

#### Alterando uma imagem
- Sempre que alteramos o código de uma imagem, vamos precisar **fazer o *build* novamente**.
- O docker interpreta como uma imagem nova => novo id.

#### Camadas das imagens
- As imagens do Docker são divididas em **camadas**.
- Cada instrução do Dockerfile representa uma camada.
- Quando algo é atualizado, apenas as layers depois da linha atualizada são refeitas.

#### Download de imagens
- Podemos fazer o download de alguma imagem do hub e deixá-la em nosso ambiente.
- **Comando:** `docker pull <imagem>`

#### Alterando o nome da imagem e tag
- Podemos nomear a imagem que criamos.
- **Comando:** `docker tag <nome>`

#### Removendo imagens
- **Comando:** `docker rmi <id>`
- Obs.: pode-se forçar a execução também: `-f`

#### Removendo imagens e containers
- Podemos remover imagens, containers e networks não utilizados
- `docker system prune`

#### Remover após usar
- **Comando:** `docker run -rm <container>`

#### Copiando arquivos entre containers
- Pode ser utilizado para copiar um arquivo de um diretório para um container;
- Ou de um container para um diretório determinado.
- **Comando:** `docker cp`

#### Verificar informações de processamento
- Podemos ter acesso a quando ele foi iniciado, id do processo, descrição do comando CMD.
- **Comando:** `docker top <container>`

#### Inspecionando container
- Conseguimos entender como o container está configurado.
- **Comando:** `docker inspect <container>`

#### Autenticação no Docker Hub
- Serve para poder enviar imagens para o Docker Hub.
- `docker login` no terminal
- **Logout:** `docker logout`

#### Envio de imagens no Docker Hub
- Para enviar uma imagem nossa ao Docker Hub utilizamos o comando `docker push <imagem>`.
- Antes é necessário **criar o repositório** para a mesma no site do Hub.
- Necessário estar autenticado.

#### Utilizando uma imagem nossa
**1º:** fazer o build;

**2º:** trocar a tag da imagem para a versão atualizada;

**3º:** fazer um push novamente para o repositório.

### Volumes



