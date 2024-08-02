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
- Reduz linhas de código, possibilita reutilização de código.

### Capacidades implementadas
- *First Class Functions*: consegue trabalhar funções como dados (uma variável pode armazenar uma função)
- *High Order Functions*: funções podem receber outras como parâmetros, ou retornar uma outra função.
- *Anonymous Functions*: sem nome => lambda
- *Closure*
- *Recursion*
- *Immutability*: importante para uso de *threads*.
- *Lazy Evaluation*

#### *First Class Functions*
Capacidade de usar as funções como entidades de primeira classe, em variáveis por exemplo.
```python
#!/usr/bin/python3
def dobro(x):
    return x * 2
def quadrado(x):
    return x ** 2

if __name__ == '__main__':
    # Retornar alternadamente o dobro ou quadrado nos números de 1 a 10
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}') 
```

#### *High Order Functions* 
Capacidade de uma função de receber como parâmetro e/ou retornar outras funções.
```python
from first_class_functions import dobro, quadrado

def process(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
    print(i, '=>', funcao(i))

if __name__ == '__main__':
    process('Dobros de 1 a 10', range(1, 11), dobro)
    process('Quadrados de 1 a 10', range(1, 11), quadrado) 
```

#### *Closure*
Funções que podem ser aninhadas e ter acesso ao escopo da função na qual foi definida, inclusive impedindo o *Garbage Collector* de liberá-las.
```python
def multiplier(times):
    def calc(x):
        return x * times
    return calc

if __name__ == '__main__':
    dobro = multiplier(2)
    triplo = multiplier(3)
    print(dobro, triplo)
    print(f'O triplo de 3 é {triplo(3)}') # 9
    print(f'O dobro de 7 é {dobro(7)}') # 14    
    print(f'O dobro de 3 é {dobro(3)}') # 6
```

#### Funções anônimas *LAMBDA*
São úteis quando precisamos de uma função simples, que será utilizada apenas uma vez e não precisa ser reutilizada em outro lugar do código.
```python
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)
totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais:', list(totais))
print('Total geral:', sum(totais))
```

#### Map
- A função `map` aplica uma função a cada item de um iterável e retorna um iterador com os resultados transformados.
- `map` retorna um iterador, então usamos `list()` para converter o resultado em uma lista.
- `map` é útil para transformar dados de forma compacta e eficiente.

#### Filter
A função `filter` aplica uma função a cada item de um iterável e retorna um iterador que contém apenas os itens para os quais a função retorna *True*.

#### Reduce
- É usada para aplicar uma função específica, passada como argumento, a todos os elementos da lista mencionada na sequência fornecida.
- A função pertence ao módulo *functools*.
```python
from functools import reduce
```

### Abordagem Imperativa
- Manda como o computador deve ser feito.
- Contrário à programação funcional.

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
#### O que são?
- Forma prática de persistir dados;
- Todo dado criado por um container é salvo nele.
- Precisaremos dos volumes para gerenciar os dados e também fazer **backups**.

#### Tipos
- **Anônimos**: diretórios criados pela flag `-v`, porém com nome aleatório.
- **Nomeados**: volumes com nomes, podemos nos referir a eles facilmente.
- **Bind mounts**: forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informando um diretório para este fim.
    - Pode servir para atualizar os códigos em tempo real.

**OBS.:** Volumes solucionam o problema da persistência: se criarmos um container com alguma imagem, todos os arquivos que geramos dentro dele serão do container. Quando ele for removido, perderemos esses arquivos. Para isso servem os **volumes**! 

#### Criar um volume
- `docker volume create <nome>`

#### Listar volumes
- `docker volume ls`
- Tem-se acesso a todos os *named* e *anonymous* volumes.

#### Checar um volume
- `docker volume inspect <nome>`

#### Remover um volume
- `docker volume rm <nome>`
- Remove também todos os dados.

OBS.: remoção de volumes não utilizados: `docker volume prune`

#### Volume apenas de leitura
- Pouco utilizado, quando tiver bases de consulta.
- `docker run -v volume:/data:ro`
- `:ro` = *read only*.

### Redes (*networks*)
#### O que são?
- Forma de **gerenciar a conexão do Docker** com outras plataformas ou até mesmo entre containers.
- São criadas separadas dos containers.
- Existem alguns **drivers de rede**.

#### Tipos de conexão
- **Externa:** conexão com uma API de um servidor remoto.
- **Com o host:** comunicação com a máquina que está executando o Docker.
- **Entre containers:** comunicação que utiliza o driver bridge e permite a comunicação entre containers.

#### Tipos de rede
- **Bridge:** *default* do Docker, utilizado quando containers precisam se conectar.
- **host:** permite a conexão entre um container e a máquina que está hosteando o Docker.
- **macvlan:** permite a conexão a um container por um MAC *address*.
- **none:** remove todas as conexões de rede de um container.
- **plugins:** permite extensões de terceiros para criar outras redes.

#### Listando redes
- `docker network ls`
- Algumas redes já são criadas na configuração inicial do Docker.

#### Criar rede
- `docker network create <nome>`
    - Essa rede será do tipo *bridge*, que é o **mais usado**.

OBS.: Criar rede com driver diferente: `docker network create -d <nome-driver> <nome-rede>`

#### Remover rede
- `docker network rm <nome>`
- Devemos tomar cuidados com containers já conectados.

OBS.: remover redes **não utilizadas no momento**: `docker network prune`

#### Conexão externa
- Os containers podem se conectar livremente ao mundo externo.

#### Conectar container a uma REDE
- `docker network connect <rede> <container>`
- DESCONECTAR: `docker network disconnect <rede> <container>`
- INSPECIONAR: `docker network inspect <nome>`
    - Informações como data de criação, driver, nome...

### YAML
- O Docker Compose utiliza o YAML para **configuração**.
- ***YAML ain't Markup Language***
- Usada geralmente para arquivos de configuração.
- Possui **chaves** e **valores**.
- **Não** necessita ponto e vírgula ';'.

#### Comentários: **#**

#### Tipos de dados
- **Inteiros:** 12
- **Floats:** 1.8

#### Strings
- Pode ser **com aspas** ou **sem aspas** => ambos textos válidos.

#### Dados nulos
- **~**
- **null**
- Ambos resultam em *None*

#### Booleanos ✅❌
- **True** e **On** = VERDADEIRO
- **False** e **Off** = FALSO 

#### *Arrays* (listas)
- Em forma de lista: `[1, 2, 3, 4, 5]`
- Em itens:
    ```yaml
    items:
        - 1
        - 2
        - 3
    ```

#### Dicionários (objetos) 📚
- Tipos de dados com chave: valor.
- Como objeto: `obj: {a: 1, b: 2, c: 3}`
- Ou:
    ```yaml
    objeto:
        chave: 1
        chave: 2 
    ```

### Docker Compose
- Ferramenta para **rodar múltiplos containers**.
- Possui UM arquivo de configuração, o qual orquestra tudo.
- Forma de **rodar múltiplos *builds* e *runs* com um comando**.
- Essencial em projetos maiores.

#### Criar arquivo Compose
- Criar um arquivo *docker-compose.yaml* na raiz do projeto.
    - Arquivo que vai **coordenar os containers e imagens**.
- *version*: versão do Compose
- *services*: containers/serviços que vão rodar nessa aplicação.
- *volumes*: possível adição de volumes.

**EXEMPLO:**
```yaml
version: '3.3'

services:
    db:
        image: mysql:5.7
        volumes:
            - db_data:/var/lib/mysql
    restart: always
    environment:
        MYSQL_ROOT_PASSWORD: wordpress
        MYSQL_DATABASE: wordpress
        MYSQL_USER: fulano
        MYSQL_PASSWORD: secret

    wordpress:
        depends_on:
            - db
        image: wordpress:latest
        ports:
            - "8000:80"
        restart: always
        environment: 
            WORDPRESS_DB_HOST: db:3306
            WORDPRESS_DB_USER: fulano
            WORDPRESS_DB_PASSWORD: secret
            WORDPRESS_DB_NAME: wordpress
    volumes:
        db_data: {}
``` 

#### Rodar o Compose
- **Comando:** `docker-compose up`
- Parar: "Ctrl + C"

#### Rodar em background
- Utiliza a flag `-d`.

#### Parar um Compose
- **Comando:** `docker-compose down`

#### Variáveis de ambiente
- Define-se um arquivo base **.env**.
    - Define-se no .yaml a localização do **env_file**
    ```yaml
    env_file:
        - ./config/arquivo.env
    ```
- Variáveis chamadas pela sintaxe: `${VARIAVEL}`
- Útil **quando o dado a ser inserido é sensível/não pode ser compartilhado**.

**EXEMPLO:** 
```.env
MYSQL_ROOT_PASSWORD=wordpress
MYSQL_DATABASE=wordpress
MYSQL_USER=fulano
MYSQL_PASSWORD=secret
```

#### Redes no Compose
- O Compose cria uma **rede básica** entre os containers da aplicação.
- Podemos isolar as redes com a chave **network**.

#### Verificação dos serviços do Compose
- `docker-compose ps`
- Recebemos um **resumo dos serviços que sobem** ao rodar o Compose.

### Docker Swarm
- Forma de **orquestrar containers**.

