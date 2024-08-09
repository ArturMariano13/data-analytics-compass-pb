# SPRINT 4 - Paradigma Funcional (Python), Containers e Introdução AWS
Nessa sprint, realizei muitos cursos e aprendi diversas coisas: Python: Programação Funcional, Docker para Desenvolvedores, AWS Credenciamento Técnico, Estatística Descritiva com Python e finalizei o curso de Métodos Ágeis.

Para ver e conseguir absorver os conceitos do curso de Métodos Ágeis, dividi em partes em cada *Sprint*, finalizando agora na sprint 4, conforme havia sido recomendado.

A Sprint foi desafiadora, com diversos conceitos novos para mim, exigindo muito estudo e capacidade de absorver conceitos.

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

### *First Class Functions*
- Consegue trabalhar **funções como dados** (uma **variável** pode armazenar uma função).
- Capacidade de usar as funções como entidades de primeira classe, em variáveis por exemplo.
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

### *High Order Functions* 
- Capacidade de uma função de **receber como parâmetro e/ou retornar outras funções**.
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

### *Closure*
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

### Funções anônimas *LAMBDA*
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

### Map
- A função `map` aplica uma função a cada item de um iterável e retorna um iterador com os resultados transformados.
- `map` retorna um iterador, então usamos `list()` para converter o resultado em uma lista.
- `map` é útil para transformar dados de forma compacta e eficiente.

### Filter
A função `filter` aplica uma função a cada item de um iterável e retorna um iterador que contém apenas os itens para os quais a função retorna *True*.

### Reduce
- É usada para aplicar uma função específica, passada como argumento, a todos os elementos da lista mencionada na sequência fornecida.
- A função pertence ao módulo *functools*.
```python
from functools import reduce
```

### Abordagem Imperativa
- Manda como o computador deve ser feito.
- Contrário à programação funcional.

___

## Docker para Desenvolvedores (Udemy) 🐳
### O QUE É? 🤔
- Docker é uma plataforma que reduz a complexidade de configuração e setup de aplicações.
- Utiliza **containers**, que são ambientes isolados para rodar aplicações.
- Permite criar **ambientes independentes** que funcionam em diversos sistemas operacionais.
- **Melhora o desempenho** dos projetos ao proporcionar consistência entre diferentes ambientes.
- Reduz o tempo gasto em manutenção e resolução de problemas relacionados a dependências e configuração.
- É **similar a uma máquina virtual (VM)**, mas é mais leve, pois não executa um sistema operacional completo, apenas o necessário para rodar a aplicação.

### CONTAINERS 🧱
- São **pacotes de código que podem executar uma ação**, por exemplo: rodar uma aplicação de Node.js, PHP, Python...
- Utilizam imagens para poderem ser executados.
- Múltiplos containers podem rodar juntos.

- **CONTAINER X IMAGEM**
    - **Imagem:** é o projeto que será executado pelo container (possuirá todas as instruções).
    - **Container:** é o Docker rodando alguma imagem (executando algum código).
    - O fluxo é: criar uma imagem e, em seguida, executar um container a partir dessa imagem.

### Executar uma imagem:
```shell
docker run <imagem>
```

### Verificar containers executados
```shell
docker ps
# mostra todos os containers rodando
```
- `-a`: mostra todos os containers que já rodaram.

### Executar com interação
- Aloca o terminal para a execução daquele container.
- **Comando:** `docker run -it <imagem>`

### Executar em *background*
- Utilizar a flag `-d`.
- **Comando:** `docker run -d <imagem>`

### Expor portas de container
- Utilizar a flag `-p`.
- **Exemplo:** `docker run -d -p 80:80 <imagem>` => nesse caso, o container rodará em background na porta 80.

### Parar containers
- Libera recursos que estão sendo gastos pelo mesmo.
- **Comando:** `docker stop <id ou nome>`

### Reiniciando containers
- Caso seja necessário aproveitar um antigo, optar pelo `start`.
- **Comando:** `docker start <id>`
- Pode-se utilizar a flag `-i` para reiniciar no modo interativo.

### Definindo nome do container
- Se não utilizar, o docker dá um nome aleatório.
- **Comando:** `docker run --name <nome> <imagem>`

### Verificando logs
- Podemos **verificar o que aconteceu** em um container.
- **Comando:** `docker logs <id>`

### Removendo containers
- O container removido não é mais listado em `docker ps -a`.
- **Comando:** `docker rm <id>`
- A flag -f pode forçar a remoção.



### IMAGEM 🖼️
- São **originadas de arquivos que programamos** para que o Docker crie uma estrutura que execute determinadas ações em containers.
- Elas contêm informações como: imagens base, diretório base, comandos a serem executados, porta de aplicação, etc.
- Ao executar um container baseado na imagem, as **instruções serão executadas em camadas**.

### Criando uma imagem
- Precisaremos de um arquivo **Dockerfile**.
- **FROM:** imagem base
- **WORKDIR:** diretório de aplicação
- **EXPOSE:** porta da aplicação
- **COPY:** quais arquivos precisam ser copiados

### Executando uma imagem
- Para executar a imagem, primeiramente vamos precisar fazer o *build*.
- **Comando *build*:** `docker build <diretório da imagem>`
- **Comando EXECUÇÃO:** `docker run <imagem>`

OBS.: especificar a porta e o nome no comando de execução

### Alterando uma imagem
- Sempre que alteramos o código de uma imagem, vamos precisar **fazer o *build* novamente**.
- O docker interpreta como uma imagem nova => novo id.

### Camadas das imagens
- As imagens do Docker são divididas em **camadas**.
- Cada instrução do Dockerfile representa uma camada.
- Quando algo é atualizado, apenas as layers depois da linha atualizada são refeitas.

### Download de imagens
- Podemos fazer o download de alguma imagem do hub e deixá-la em nosso ambiente.
- **Comando:** `docker pull <imagem>`

### Alterando o nome da imagem e tag
- Podemos nomear a imagem que criamos.
- **Comando:** `docker tag <nome>`

### Removendo imagens
- **Comando:** `docker rmi <id>`
- Obs.: pode-se forçar a execução também: `-f`

### Removendo imagens e containers
- Podemos remover imagens, containers e networks não utilizados
- `docker system prune`

### Remover após usar
- **Comando:** `docker run -rm <container>`

### Copiando arquivos entre containers
- Pode ser utilizado para copiar um arquivo de um diretório para um container;
- Ou de um container para um diretório determinado.
- **Comando:** `docker cp`

### Verificar informações de processamento
- Podemos ter acesso a quando ele foi iniciado, id do processo, descrição do comando CMD.
- **Comando:** `docker top <container>`

### Inspecionando container
- Conseguimos entender como o container está configurado.
- **Comando:** `docker inspect <container>`

### Autenticação no Docker Hub
- Serve para poder enviar imagens para o Docker Hub.
- `docker login` no terminal
- **Logout:** `docker logout`

### Envio de imagens no Docker Hub
- Para enviar uma imagem nossa ao Docker Hub utilizamos o comando `docker push <imagem>`.
- Antes é necessário **criar o repositório** para a mesma no site do Hub.
- Necessário estar autenticado.

### Utilizando uma imagem nossa
**1º:** fazer o build;

**2º:** trocar a tag da imagem para a versão atualizada;

**3º:** fazer um push novamente para o repositório.

### VOLUMES
### O que são?
- Forma prática de persistir dados;
- Todo dado criado por um container é salvo nele.
- Precisaremos dos volumes para gerenciar os dados e também fazer **backups**.

### Tipos
- **Anônimos**: diretórios criados pela flag `-v`, porém com nome aleatório.
- **Nomeados**: volumes com nomes, podemos nos referir a eles facilmente.
- **Bind mounts**: forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informando um diretório para este fim.
    - Pode servir para atualizar os códigos em tempo real.

**OBS.:** Volumes solucionam o problema da persistência: se criarmos um container com alguma imagem, todos os arquivos que geramos dentro dele serão do container. Quando ele for removido, perderemos esses arquivos. Para isso servem os **volumes**! 

### Criar um volume
- `docker volume create <nome>`

### Listar volumes
- `docker volume ls`
- Tem-se acesso a todos os *named* e *anonymous* volumes.

### Checar um volume
- `docker volume inspect <nome>`

### Remover um volume
- `docker volume rm <nome>`
- Remove também todos os dados.

OBS.: remoção de volumes não utilizados: `docker volume prune`

### Volume apenas de leitura
- Pouco utilizado, quando tiver bases de consulta.
- `docker run -v volume:/data:ro`
- `:ro` = *read only*.

### REDES (*networks*)
### O que são?
- Forma de **gerenciar a conexão do Docker** com outras plataformas ou até mesmo entre containers.
- São criadas separadas dos containers.
- Existem alguns **drivers de rede**.

### Tipos de conexão
- **Externa:** conexão com uma API de um servidor remoto.
- **Com o host:** comunicação com a máquina que está executando o Docker.
- **Entre containers:** comunicação que utiliza o driver bridge e permite a comunicação entre containers.

### Tipos de rede
- **Bridge:** *default* do Docker, utilizado quando containers precisam se conectar.
- **host:** permite a conexão entre um container e a máquina que está hosteando o Docker.
- **macvlan:** permite a conexão a um container por um MAC *address*.
- **none:** remove todas as conexões de rede de um container.
- **plugins:** permite extensões de terceiros para criar outras redes.

### Listando redes
- `docker network ls`
- Algumas redes já são criadas na configuração inicial do Docker.

### Criar rede
- `docker network create <nome>`
    - Essa rede será do tipo *bridge*, que é o **mais usado**.

OBS.: Criar rede com driver diferente: `docker network create -d <nome-driver> <nome-rede>`

### Remover rede
- `docker network rm <nome>`
- Devemos tomar cuidados com containers já conectados.

OBS.: remover redes **não utilizadas no momento**: `docker network prune`

### Conexão externa
- Os containers podem se conectar livremente ao mundo externo.

### Conectar container a uma REDE
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

### Comentários: **#**

### Tipos de dados
- **Inteiros:** 12
- **Floats:** 1.8

### Strings
- Pode ser **com aspas** ou **sem aspas** => ambos textos válidos.

### Dados nulos
- **~**
- **null**
- Ambos resultam em *None*

### Booleanos ✅❌
- **True** e **On** = VERDADEIRO
- **False** e **Off** = FALSO 

### *Arrays* (listas)
- Em forma de lista: `[1, 2, 3, 4, 5]`
- Em itens:
    ```yaml
    items:
        - 1
        - 2
        - 3
    ```

### Dicionários (objetos) 📚
- Tipos de dados com chave: valor.
- Como objeto: `obj: {a: 1, b: 2, c: 3}`
- Ou:
    ```yaml
    objeto:
        chave: 1
        chave: 2 
    ```

### *DOCKER COMPOSE*
- Ferramenta para **rodar múltiplos containers**.
- Possui UM arquivo de configuração, o qual orquestra tudo.
- Forma de **rodar múltiplos *builds* e *runs* com um comando**.
- Essencial em projetos maiores.

### Criar arquivo Compose
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

### Rodar o Compose
- **Comando:** `docker-compose up`
- Parar: "Ctrl + C"

### Rodar em background
- Utiliza a flag `-d`.

### Parar um Compose
- **Comando:** `docker-compose down`

### Variáveis de ambiente
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

### Redes no Compose
- O Compose cria uma **rede básica** entre os containers da aplicação.
- Podemos isolar as redes com a chave **network**.

### Verificação dos serviços do Compose
- `docker-compose ps`
- Recebemos um **resumo dos serviços que sobem** ao rodar o Compose.

### *DOCKER SWARM*
- **Ferramenta** para **orquestrar containers**.
- Podendo **escalar horizontalmente** os projetos.
- **Cluster**.
- Comandos semelhantes ao Docker.

### Orquestração de containers
    - Ato de conseguir **gerenciar e escalar** os containers da aplicação.
    - **Serviço que rege sobre outros serviços**.
    - Exemplos de serviços: Swarm, Kubernetes e Apache Mesos.

### Conceitos fundamentais
- **Nodes:** instâncias (máquinas) do Swarm.
- **Manager Node:** node gerenciador.
- **Worker Node:** nodes que trabalham em função do gerenciador.
- **Service:** conjunto de tasks que o manager manda para os workers.
- **Task:** comandos que são executados nos Nodes.

### Inicialização do Swarm
- **Comando:** `docker swarm init`
- Em alguns casos precisamos declarar o IP do servidor com a flag `--advertise-addr`
- Faz com que a instância vire um *Node*.
- Transforma o Node em um ***manager***.

### Listar Nodes ativos
`docker node ls`
- Serviços serão exibidos no terminal.

### Adicionar máquinas
`docker swarm join --token <TOKEN> <IP>:<PORTA>`
- Dessa forma, duas máquinas estarão conectadas.
- A nova máquina entra como **worker**.

### Subir serviço
`docker service create --name <nome> <imagem>`

### Verificar serviços rodando no Swarm
`docker service ls`

### Replicando serviços
`docker service create --name <nome> --replicas <numero> <imagem>`
- Inicia-se, de fato, a **orquestração**.

### Checar token do Swarm
`docker swarm join-token manager`
- Recebemos o token pelo terminal.

### Checar Swarm
`docker info`
- ID node, número nodes, managers...

### Remover instância do Swarm
`docker swarm leave`
- A inastância não é mais um entendido como Node para o Swarm.

### Remover Node do Swarm
`docker node rm <ID>`
- A instância não será mais um Node, saindo do Swarm
- Utilizar `-f`

### Inspecionar serviços
`docker service inspect <ID>`

### Verificar containers rodando
`docker service ps <ID>`
- Semelhante ao *docker ps -a*

### Compose com Swarm
`docker stack deploy -c <ARQUIVO.YAML> <NOME>`

### Atualizar Imagem
`docker service update --image <IMAGEM> <SERVICO>`
- Apenas os nodes com status *active* receberão atualizações.

### KUBERNETES
- Ferramenta de orquestração de containers.
- Escala projetos, formando um **cluster**.
- Criada pelo Google.

### Conceitos Fundamentais
- ***Control Plane:*** onde é gerenciado o controle dos processos dos Nodes.
- ***Nodes*:** máquinas gerenciadas pelo *Control Plane*.
- ***Deployment*:** execução de uma imagem/projeto em um Pod.
- ***Pod*:** um ou mais containers que estão em um *Node*.
- ***Services*:** serviços que expõem os Pods ao mundo externo.
- ***kubectl*:** cliente de linha de comando para o Kubernetes.

### Dependências necessárias
- Cliente: *kubectl* = maneira de executar o Kubernetes
- ***Minikube*:** espécie de simulador de Kubernetes para não precisarmos de vários servidores.
- **No Windows:** 
    - Instalar gerenciador de pacotes **Chocolatey**
    - Seguir a documentação de instalação de *client* do Kubernetes.
    - Instalar o VirtualBox.
    - Instalar *Minikube*.


### Minikube
**Inicializar**: `minikube start --driver=<DRIVER>`

**Parar:** `minikube stop`

**Verificar:** `minikube start`

**Acessar a dashboard:** `minikube dashboard`

### Deployment
- Parte fundamental do Kubernetes.
- Com ele criamos nosso serviço que vai rodar nos **Pods**.
- Definimos uma imagem e um nome.

- **Criar Deployment:** `kubectl create deployment <NOME> --image=<IMAGEM>`
- **Verificar Deployments:** `kubectl get deployments` | `kubectl describe deployments`
- **Deletar Deployments:** `kubectl delete deployment <NOME>`

- **Checar Pods:** `kubectl get pods` | `kubectl describe pods`

- **Desfazer alteração de projeto:** `kubectl rollout undo deployment/<NOME>`

### Services
- Aplicações do Kubernetes não têm conexão com o mundo externo.
- *Service* servem para isso.
- Service é uma entidade separada dos Pods, que **expõe eles a uma rede**.

- **Criar Service:** `kubectl expose deployment <NOME> --type=<TIPO> --port=<PORT>`
    - Nome do deployment já criado
- **Gerar IP:** `minikube service <NOME>` - o IP aparece no terminal.
- **Deletar Services:** `kubectl delete service <NOME>`

- **Detalhes:**
    - Obter detalhes: `kubectl get services`
    - Descrever um serviço específico: `kubectl describe services/<NOME>`

### Modo Declarativo
- Guiado por um **arquivo**
- Centraliza tudo em **um comando.**
- Escrevemos em YAML o arquivo Kubernetes.
- **Chaves mais utilizadas:**
    - ***apiVersion***: versão utilizada da ferramenta.
    - ***kind***: tipo do arquivo (Deployment, Service).
    - ***metadata***: descrever algum objeto, inserindo chaves como *name*.
    - ***replicas***: número de réplicas de Nodes/Pods.
    - ***containers***: definir as especificações de containers como: nome e imagem.

- **Criando arquivo p/ Deployment:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: 
    name: <nome-do-deployment>
spec:
    replicas: 4
    selector:
        matchLabels:
            app: flask-app
    template:
        metadata:
            labels:
                app: flask-app
        spec:
            containers:
                - name: flask
                  image: <nome-da-imagem> 
```

- **Executar arquivo:** `kubectl apply -f <arquivo>`
- **Parar deployment:** `kubectl delete -f <arquivo>`

- **Criando arquivo p/ Service:**
```yaml
apiVersion: v1
kind: Service
metadata: 
    name: <nome-do-service>
spec:
    selector:
        app: flask-app
    ports:
        - protocol: 'TCP'
          port: 5000
          targetPort: 5000
    type: LoadBalancer
```

- **Executar arquivo:** `kubectl apply -f <arquivo>`
- **Parar serviço (perde acesso):** `kubectl delete -f <arquivo>`


___
## AWS - Credenciamento Técnico
### MODELOS DE IMPLEMENTAÇÃO DA COMPUTAÇÃO EM NUVEM
- Foco no que realmente importa.
- Cada método de implantação provê diferentes níveis de **controle**, **flexibilidade** e **gerenciamento**.

### *On-premises* 🏢
- Antes da nuvem, empresas mantinham equipamentos de computação em seus **próprios *data centers***.
- Locação de **grandes departamentos de infraestrutura**.
- Com o aumento do uso da **Internet**, a **demanda** por **recursos computacionais aumentou**. 
- Surge assim a computação em nuvem.

### Nuvem ☁️
- **Computação em Nuvem:** Entrega sob demanda de recursos de TI pela internet.
- Principalmente baseado em **pagamento por uso**.
- Empresas não precisam gerenciar e manter hardware e data centers próprios.
- Empresas como Amazon Web Services (AWS) possuem e mantêm data centers.
- Tecnologias e serviços de **data centers virtuais disponibilizados pela internet**.

### Híbrido 🏢☁️
- Conecta recursos e aplicações entre a nuvem e recursos existentes que não estão na nuvem.
- Objetivo: Estender e expandir a infraestrutura de uma organização para a nuvem.

### Vantagens
- Pagamento conforme utilização de recursos.
- Economia devido à grande escala de clientes.
- Não necessita "adivinhar" os recursos necessários.
- Aumento da agilidade.
- Economia de custos.
- Globalização.

### Infraestrutura Global da AWS
- *Data centers* interligados (*Availability Zones*).
- Dividida em regiões (Oregon, São Paulo...).
- Preço varia de região para região.
- **Latência:** menor conforme mais perto da região acessada.
- *Data centers* => *Availability Zones* => Regiões => Infraestrutura Global da AWS

### Interação com a AWS: **"Toda ação que se faz na AWS é uma chamada a uma API que é autenticada e autorizada."**

### Modos de interagir
- *AWS Management Console*
- *AWS Command Line Interface*
- *AWS Software Development Kits*

### Cloud Adoption Framework (AWS CAF)
- O **AWS Cloud Adoption Framework (AWS CAF)** é uma estrutura criada pela AWS para auxiliar organizações na migração para a nuvem.
- O objetivo é ajudar os clientes a formular uma estratégia completa para a nuvem e a realizar a transição de forma eficiente.

### Importância da Nuvem

- Um estudo da McKinsey projeta que a nuvem gerará mais de **US$ 1 trilhão** para empresas da Fortune 500 até 2030.

### Fases do AWS CAF

**1. Concepção**

- **Objetivo:** Criar uma base sólida para a estratégia de nuvem, conectando metas de negócios às tecnologias e priorizando iniciativas.
- **Resultado:** Desenvolvimento de uma visão de prontidão para a nuvem.

**2. Alinhamento**

- **Objetivo:** Elaborar um plano de ação claro, identificando benefícios, desafios e uma abordagem para gerenciar mudanças.
- **Resultado:** Um plano prático e um entendimento das ações necessárias para alcançar a prontidão para a nuvem.

**3. Lançamento**

- **Objetivo:** Implementar o plano de ação, gerenciar preocupações e iniciar o uso da nuvem para obter valor comercial.
- **Resultado:** Fluxos de trabalho para a implantação e conclusão de projetos na nuvem.

**4. Medição e Escalonamento**

- **Objetivo:** Medir o sucesso, garantir que os benefícios comerciais sejam realizados e sustentados, e escalar operações.
- **Resultado:** Expansão de pilotos e ajuste contínuo dos planos de negócios.

### Estratégias de Migração

A AWS oferece sete estratégias comuns de migração, cada uma adequada a diferentes necessidades e contextos:

1. **Refatorar:**
   - **Objetivo:** Adicionar recursos, desempenho ou escala quando o design atual da aplicação não é suficiente.

2. **Redefinir a Plataforma:**
   - **Objetivo:** Migrar e dimensionar rapidamente para atender a novas necessidades de negócios.

3. **Recomprar:**
   - **Objetivo:** Substituir a aplicação atual por uma solução SaaS ou outra solução que atenda melhor às necessidades.

4. **Redefinir Hospedagem:**
   - **Objetivo:** Migrar a aplicação para a nuvem com mudanças mínimas na arquitetura.

5. **Realocar:**
   - **Objetivo:** Mover aplicações ou cargas de trabalho para a nuvem com tempo de inatividade mínimo e sem alterações nas operações ou pilha técnica.

6. **Reter:**
   - **Objetivo:** Manter a aplicação no ambiente atual, se for mais vantajoso ou necessário.

7. **Retirar:**
   - **Objetivo:** Descontinuar a aplicação que não é mais necessáv

## AWS Well-Architected Framework

- Ajuda a garantir que as cargas de trabalho na nuvem sigam as melhores práticas de arquitetura da AWS. 
- Framework orienta a criação e operação de sistemas confiáveis, seguros, de alto desempenho e econômicos na nuvem.

### Objetivos do Framework

- **Reduzir gastos com infraestrutura**
- **Guiar funcionários para um trabalho mais estratégico**
- **Diminuir o tempo de inatividade não planejado das aplicações**
- **Diminuir o tempo de lançamento de novos produtos no mercado**

### Pilares do Well-Architected Framework

1. **Excelência Operacional**
   - Foca na melhoria da eficiência das pessoas e dos processos.
   - Exemplos: gerenciamento e automação de alterações, resposta a eventos, definição de padrões para operações diárias.

2. **Segurança**
   - Foca em proteger dados, informações e sistemas.
   - Exemplos: acesso com privilégios mínimos, gerenciamento de credenciais, proteção de sistemas, controle de eventos de segurança.

3. **Confiabilidade**
   - Foca em projetar sistemas altamente disponíveis e resilientes.
   - Exemplos: configuração, planejamento de recuperação, gestão de mudanças.

4. **Eficiência de Desempenho**
   - Foca no uso eficiente dos recursos da AWS.
   - Exemplos: seleção de tipos e tamanhos de recursos, monitoramento de desempenho, elasticidade.

5. **Otimização de Custos**
   - Foca em maximizar o valor dos gastos.
   - Exemplos: monitoramento de gastos, seleção de recursos apropriados, análise de gastos ao longo do tempo.

6. **Sustentabilidade**
   - Foca em minimizar os impactos ambientais.
   - Exemplos: maximização da utilização de recursos, redução de impactos ambientais.

___
## Estatística Descritiva Com Python
### Bibliotecas utilizadas para Estatística
- [Numpy](https://www.numpy.org/): análise numérica, álgebra linear...
- [RPy](http://rpy.sourceforge.net): linkar linguagem R com Python.
- [Scipy](http://www.scipy.org/)
- [PyChem](http://pychem.sourceforge.net/)
- [Pandas](https://pandas.pydata.org/): Excel para o Python
- [Matplotlib](https://matplotlib.org/): geração de gráficos
- [Seaborn](https://seaborn.pydata.org/): gráficos

### Estatística
- Ciência utilizada para medir.

### Fundamentos

- **Aleatoriedade**
- **População:** Todos os elementos ou indivíduos cujas características estão sendo estudadas.
- **Censo:** Conjunto de características obtidas de todos os membros da população.
- **Amostra:** Parte coletada a partir da população.

### Gráficos

Os gráficos são ferramentas essenciais para a visualização de dados. Eles:

- Representam fenômenos de forma visual.
- Refletem padrões gerais dos dados.
- Facilitam a interpretação dos dados.
- Resumem informações complexas.
- Evidenciam tendências, valores mínimos e máximos, ordens de grandeza, entre outros aspectos.

**Todo gráfico deve seguir os princípios de:**

- **Simplicidade:** Deve ser fácil de entender.
- **Clareza:** Deve transmitir a informação de forma clara e objetiva.
- **Veracidade:** Deve representar os dados de forma precisa e honesta.

**Perguntas importantes ao criar um gráfico:**

- Qual é o público-alvo?
- Qual é o objetivo do gráfico?
- Que tipo de gráfico é mais apropriado?
- Como o gráfico deve ser apresentado?
- Quais são as dimensões ideais para o gráfico?

### Gráficos de Barras

Os gráficos de barras são usados para:

- Representar variáveis **qualitativas**.
- Utilizar retângulos horizontais ou verticais de larguras iguais para cada categoria.

**Objetivos dos gráficos de barras:**

- Comparar **grandezas** entre **categorias**.
- Representar categorias com designações extensas.

**Exemplo de gráfico de barras:**

<div>
  <h3>Gráfico de Barras</h3>
  <p>Este gráfico representa comparações entre diferentes países no consumo de café.</p>
  <img src="https://lh6.googleusercontent.com/UCBf_VFVBLaFip879NWf2OM_TcajKG9JQE5azVoAzfolB0DGgqm4YiThR97R87z9_QGeQ9Ziobe2BmP1xEd6B7UtaZLuoAUkwqxFZaDyVOD9jgUncp_Dy4vZqjfmH6vxJ93uRTAa" alt="Gráfico de Barras">
</div>


### Gráficos de Setores (Pizza)
- Comparar valor da categoria específica com o total.
- Número de categorias pequeno.

**Exemplo de gráfico de setores:**

<div>
  <h3>Gráfico de Setores</h3>
  <img src="https://static.mundoeducacao.uol.com.br/mundoeducacao/conteudo/Untitled-6(14).jpg" alt="Gráfico de Setores">
</div>


### Gráficos de Linhas
- Gráficos de séries cronológicas.
- Indicados para representar séries temporais.

**Exemplo de gráfico de linhas:**

<div>
  <h3>Gráfico de Linhas</h3>
  <img src="https://i.pinimg.com/736x/2e/10/cd/2e10cdca310e5ff1c413da07dee0000e.jpg" alt="Gráfico de Linhas">
</div>

### Histogramas
- Colunas justapostas para representar distribuição de frequência em dados.
- Eixo horizontal possui os limites das classes de agrupamento.

**Exemplo de histograma:**

<div>
  <h3>Histograma</h3>
  <img src="https://leansixsigmabrasil.com.br/site/wp-content/uploads/2020/01/Exemplo-de-histograma-de-temperatura.jpg" alt="Histograma">
</div>

### Medidas de Tendência Central (MTC)
- Indicam um ponto em torno do qual se concentram os dados.

**MÉDIA ARITMÉTICA**
- Soma de todos os valores pela quantidade deles.
- "Centro de gravidade" do conjunto de dados.
- **Desvantagem:** afetada por *outliers*.

**MODA**
- Maior frequência entre os valores.

**MEDIANA**
- Valor que ocupa a posição central dos dados ordenados.
- Quando for par, soma os dois centrais e divide por dois (média).

**Medidas Separatrizes**
- Quartil: divide o conjunto em **4 partes iguais**
- Decil: divide o conjunto em **10 partes iguais**
- Percentil: divide o conjunto em **100 partes iguais**

### Medidas de Dispersão
- Auxiliam as medidas de tendência central (MTC) a descrever os dados.
- Indicam o quanto os dados estão próximos uns aos outros.

**AMPLITUDE TOTAL**
- Diferença entre o maior e o menor valor.
- Não leva em consideração valores intermediários.

**AMPLITUDE INTERQUARTÍLICA**
- Diferença entre o primeiro e o terceiro quartil.
- Mais estável que amplitude total.
- Útil para detectar valores discrepantes.

**DESVIO MÉDIO**
- Diferença entre cada valor e a média.

**VARIÂNCIA e DESVIO PADRÃO**
- Servem para solucionar alguns problemas do desvio médio.
- **Variância:** permite determinar o afastamento da média que os dados de um conjunto analisado apresentam.
- **Desvio Padrão:** é calculado a partir da variância, ao ser a raiz quadrada desse parâmetro.
<div>
  <h3>Fórmula Variância</h3>
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGftYwN9M0YzUNjxT6dPTQ0Z-OVfh3Ejnv9g&s
  " alt="Variância">
  <h3>Fórmula Desvio Padrão</h3>
  <img src="https://images.educamaisbrasil.com.br/content/banco_de_imagens/guia-de-estudo/D/desvio-padrao-matematica.jpg" alt="Desvio Padrão">
</div>

**COEFICIENTE DE VARIAÇÃO**
- Indica a variabilidade da medida em relação à média.
<div>
  <h3>Fórmula Coeficiente de Variação</h3>
  <img src="https://pt-static.z-dn.net/files/da8/c9fa1b423b0d680b0ef3308a49546de6.jpg
  " alt="Coeficiente de Variação">
</div>

### Medidas de Assimetria
**MEDIDAS DE CURTOSE**
- Medida que quantifica a **concentração** ou **dispersão** dos valores de um conjunto de dados em relação às medidas de **tendência central**.
- Mede o grau de **achatamento** de uma distribuição.

### Aplicações em *Data Science*
**MÉTODO DE MONTE CARLO (MMC)**

É uma técnica de simulação que utiliza amostras aleatórias para estimar resultados e resolver problemas complexos. 
- Consiste em gerar múltiplas simulações para entender a variabilidade e a incerteza do sistema. 
- É amplamente usado em finanças, engenharia e ciências para avaliação de riscos e otimização. 
- A precisão depende do número de simulações realizadas e pode exigir alto custo computacional.

___

## Métodos Ágeis de A a Z: o curso completo

### Manifesto Ágil
- Criado em 2001 por um grupo de 17 desenvolvedores de software que buscavam uma abordagem mais eficiente e flexível para o desenvolvimento de software. 
- Conjunto de princípios que visa promover práticas de desenvolvimento ágil, permitindo a adaptação rápida às mudanças e a entrega contínua de valor.

### Valores do Manifesto Ágil
1. **Indivíduos e interações mais que processos e ferramentas**
2. **Software funcionando mais que documentação abrangente**
3. **Colaboração com o cliente mais que negociação de contratos**
4. **Responder a mudanças mais que seguir um plano**

### Princípios do Manifesto Ágil
1. **Satisfação do cliente** através da entrega contínua e antecipada de software de valor.
2. **Mudanças nos requisitos** são bem-vindas, mesmo em estágios tardios do desenvolvimento.
3. **Entrega frequente de software** funcionando, com um intervalo de semanas a meses, preferencialmente com menor duração.
4. **Colaboração diária** entre desenvolvedores e representantes de negócios durante o projeto.
5. **Construa projetos ao redor de indivíduos motivados**. Dê a eles o ambiente e o suporte necessários e confie neles para entregar resultados.
6. **Métodos ágeis** promovem desenvolvimento sustentável. Os patrocinadores, desenvolvedores e usuários devem ser capazes de manter um ritmo constante indefinidamente.
7. **Atenção contínua à excelência técnica** e bom design aumenta a agilidade.
8. **Simplicidade** – a arte de maximizar a quantidade de trabalho não feito – é essencial.
9. **As melhores arquiteturas, requisitos e designs** emergem de equipes auto-organizáveis.
10. **A equipe reflete regularmente** sobre como se tornar mais eficaz e ajusta seu comportamento em conformidade.
11. **Entrega de software funcional** como principal medida de progresso.
12. **Comunicação face a face** é a forma mais eficiente e eficaz de transmitir informações.

### Scrum
- É um *framework* ágil para gerenciar e completar projetos complexos. É amplamente utilizado no desenvolvimento de software, mas pode ser aplicado a qualquer área onde haja necessidade de entregar produtos de forma iterativa e incremental.

**ESTRUTURA DO SCRUM**

O Scrum é baseado em três pilares: **transparência**, **inspeção** e **adaptação**. Ele se organiza em torno de papéis, eventos e artefatos principais.

**PAPÉIS**

1. **Product Owner (PO)**
   - Responsável por maximizar o valor do produto e do trabalho da equipe de desenvolvimento.
   - Define e prioriza o Product Backlog (lista de requisitos e funcionalidades do produto).
2. **Scrum Master**
   - Facilita o processo Scrum e ajuda a equipe a seguir os princípios e práticas do Scrum.
   - Remove impedimentos que possam atrapalhar o progresso da equipe.
3. **Equipe de Desenvolvimento**
   - Conjunto de profissionais que trabalham na entrega do produto.
   - Organiza seu trabalho e entrega incrementos do produto ao final de cada Sprint.

**EVENTOS**

1. **Sprint**
   - Período fixo de tempo (geralmente de 1 a 4 semanas) em que um incremento do produto é desenvolvido.
   - Cada Sprint resulta em um incremento de produto potencialmente utilizável.

2. **Planejamento do Sprint (Sprint Planning)**
   - Reunião no início de cada Sprint para definir o que será feito e como será feito durante o Sprint.
   - O Product Owner apresenta o Product Backlog e a equipe define o Sprint Backlog (itens a serem trabalhados no Sprint).

3. **Reunião Diária (Daily Scrum)**
   - Reunião rápida (geralmente 15 minutos) realizada todos os dias durante o Sprint para sincronização e planejamento do trabalho do dia.

4. **Revisão do Sprint (Sprint Review)**
   - Reunião no final de cada Sprint para revisar o trabalho realizado e adaptar o Product Backlog conforme necessário.
   - A equipe apresenta o incremento do produto e recebe feedback dos stakeholders.

5. **Retrospectiva do Sprint (Sprint Retrospective)**
   - Reunião após a Revisão do Sprint para refletir sobre o Sprint e identificar oportunidades de melhoria no processo.

**Artefatos**

1. **Product Backlog**
   - Lista ordenada de tudo o que é necessário para o produto.
   - Mantido e priorizado pelo Product Owner.

2. **Sprint Backlog**
   - Lista de itens do Product Backlog selecionados para o Sprint, juntamente com um plano para entregar o incremento e alcançar o objetivo do Sprint.
   - Criado pela equipe durante o Planejamento do Sprint.

3. **Incremento**
   - Soma de todos os itens do Product Backlog concluídos durante o Sprint e todas as Sprints anteriores.
   - Deve estar em um estado utilizável e atender à definição de "Pronto" da equipe.

### Método Kanban
- É um método ágil de gerenciamento de projetos que visa melhorar a eficiência e a transparência do fluxo de trabalho. 
- Originado no Japão, o método Kanban é amplamente utilizado para otimizar processos e gerenciar fluxos de trabalho em diversas áreas, especialmente no desenvolvimento de software e na manufatura.

**PRINCÍPIOS**

O método Kanban é baseado em três princípios fundamentais:

1. **Visualização do Trabalho**
   - **Kanban Board (Quadro Kanban)**: Um quadro visual que mostra todas as tarefas em diferentes estágios do processo. Normalmente, o quadro é dividido em colunas que representam etapas do fluxo de trabalho, como "A Fazer", "Em Progresso" e "Concluído".
   - **Cartões Kanban**: Cada tarefa ou item de trabalho é representado por um cartão no quadro. Os cartões contêm informações sobre a tarefa e seu progresso.

2. **Limitação do Trabalho em Progresso (WIP)**
   - **Limites de WIP**: Restringem o número de tarefas que podem estar em cada coluna (ou fase do processo) ao mesmo tempo. Isso ajuda a evitar sobrecarga e a melhorar o fluxo contínuo, reduzindo o tempo de espera e a multitarefa.

3. **Gerenciamento do Fluxo**
   - **Otimização do Fluxo**: O foco é melhorar o fluxo de trabalho, identificando e removendo gargalos e impedimentos. O objetivo é garantir que as tarefas fluam suavemente através das etapas do processo, minimizando o tempo necessário para concluir cada tarefa.

**COMPONENTES**

1. **Quadro Kanban**
   - Um quadro visual dividido em colunas que representam diferentes estágios do fluxo de trabalho. Pode ser físico (como um quadro branco) ou digital (usando ferramentas de software).

2. **Cartões Kanban**
   - Representam tarefas ou itens de trabalho. Cada cartão mostra detalhes como descrição da tarefa, responsável, prazo e status atual.

3. **Colunas**
   - Dividem o quadro Kanban em diferentes etapas do fluxo de trabalho. As colunas comuns incluem "A Fazer", "Em Progresso", "Concluído", mas podem ser personalizadas conforme necessário.

4. **Limites de WIP**
   - Definem o número máximo de tarefas permitidas em cada coluna. A limitação ajuda a focar na conclusão das tarefas antes de iniciar novas.

**BENEFÍCIOS**
- **Transparência**: Proporciona uma visão clara do estado atual do trabalho e do fluxo de tarefas.
- **Flexibilidade**: Permite ajustes e mudanças contínuas no fluxo de trabalho sem necessidade de replanejamento extensivo.
- **Redução de Tempo de Ciclo**: Melhora o tempo necessário para concluir tarefas, promovendo um fluxo contínuo e eficiente.
- **Identificação de Gargalos**: Facilita a identificação e resolução de problemas que afetam o fluxo de trabalho.


### Método Lean

É uma abordagem de gerenciamento que visa maximizar o valor para o cliente e minimizar o desperdício. Originado na indústria automotiva japonesa, especialmente na **Toyota**, o Lean tem como objetivo melhorar continuamente processos e aumentar a eficiência organizacional.

**PRINCÍPIOS**

1. **Valor**
   - **Definição de Valor**: Valor é aquilo que o cliente está disposto a pagar. É essencial identificar o que realmente agrega valor para o cliente e focar na entrega desses elementos.

2. **Fluxo de Valor**
   - **Mapeamento do Fluxo de Valor**: Identificar e mapear todas as etapas envolvidas na criação de um produto ou serviço, desde a matéria-prima até a entrega final ao cliente. O objetivo é eliminar etapas que não agregam valor.

3. **Fluxo Contínuo**
   - **Melhoria do Fluxo**: Garantir que o trabalho flua sem interrupções e sem tempo ocioso. O objetivo é minimizar o tempo de ciclo e acelerar a entrega de valor ao cliente.

4. **Produção Puxada**
   - **Sistema Pull**: Produzir itens apenas quando há demanda real do cliente, em vez de produzir com base em previsões. Isso ajuda a reduzir o excesso de estoque e a sobrecarga de trabalho.

5. **Perfeição**
   - **Melhoria Contínua**: Buscar a perfeição através de melhorias contínuas e sistemáticas. Envolver todos os membros da equipe na identificação e eliminação de desperdícios e na melhoria dos processos.

**CONCEITOS CHAVE**

1. **Desperdício (Muda)**
   - **Identificação de Desperdícios**: Tudo o que não agrega valor ao cliente é considerado desperdício. Exemplos incluem tempo de espera, excesso de produção, transporte desnecessário e defeitos.

2. **Kaizen**
   - **Melhoria Contínua**: Filosofia que promove pequenas melhorias incrementais no processo, envolvendo todos os membros da equipe.

3. **Just-in-Time (JIT)**
   - **Produção Sob Demanda**: Produzir e entregar apenas o que é necessário, quando é necessário, para reduzir estoques e melhorar a eficiência.

4. **Jidoka**
   - **Autonomação**: Equipamentos e processos que têm a capacidade de identificar problemas e parar automaticamente para evitar a produção de defeitos.

5. **5S**
   - **Organização e Padronização**: Método para organizar o ambiente de trabalho para melhorar a eficiência e a segurança. Os 5S são: Seiri (Classificar), Seiton (Organizar), Seiso (Limpar), Seiketsu (Padronizar), e Shitsuke (Manter).

**BENEFÍCIOS**
- **Redução de Desperdícios**: Elimina atividades e processos que não agregam valor.
- **Aumento da Eficiência**: Melhora a produtividade e reduz o tempo de ciclo.
- **Melhoria da Qualidade**: Envolve todos os colaboradores na busca por processos melhores e produtos de maior qualidade.
- **Maior Satisfação do Cliente**: Foca na entrega de valor real para o cliente, melhorando a satisfação e fidelização.

### Extreme Programming (XP)

É uma metodologia ágil de desenvolvimento de software que se concentra na melhoria contínua e na capacidade de adaptação às mudanças. 

**PRINCÍPIOS** 

1. **Comunicação**
   - **Colaboração Frequente**: Promover uma comunicação aberta e contínua entre todos os membros da equipe e os stakeholders. Reuniões diárias e interações constantes são encorajadas.

2. **Simplicidade**
   - **Simples é Melhor**: Desenvolver soluções simples e eficazes que atendam às necessidades atuais. Evitar complexidade desnecessária e construir apenas o que é necessário no momento.

3. **Feedback**
   - **Iterações Curtas e Feedback Contínuo**: Obter feedback regular dos stakeholders e ajustar o desenvolvimento com base nesse feedback. Isso permite que o produto se alinhe com as expectativas e necessidades reais.

4. **Coragem**
   - **Tomar Decisões Difíceis**: Encorajar a equipe a tomar decisões difíceis e a realizar mudanças necessárias, mesmo que isso implique em refatorar ou reescrever partes do código.

5. **Respeito**
   - **Respeito pela Equipe e pelo Cliente**: Valorizar e respeitar todos os membros da equipe e os clientes, garantindo um ambiente de trabalho colaborativo e produtivo.

**PRÁTICAS**

1. **Programação em Pares (Pair Programming)**
   - Dois desenvolvedores trabalham juntos em um único computador, onde um escreve o código enquanto o outro revisa e oferece sugestões.

2. **Desenvolvimento Orientado a Testes (Test-Driven Development - TDD)**
   - Escrever testes automatizados antes de escrever o código. O código é desenvolvido para passar nos testes, e os testes ajudam a garantir a qualidade e a funcionalidade do código.

3. **Refatoração**
   - Melhorar e limpar o código continuamente sem alterar seu comportamento externo. Refatoração é usada para manter o código simples e limpo.

4. **Integração Contínua**
   - Integrar o código frequentemente (idealmente várias vezes ao dia) para detectar e resolver problemas de integração rapidamente.

5. **Entrega Contínua**
   - Entregar pequenas e frequentes atualizações do software para que o cliente possa ver o progresso e fornecer feedback mais rapidamente.

6. **Design Simples**
   - Construir o design do sistema de forma que seja o mais simples possível para atender às necessidades atuais, evitando antecipar futuras necessidades.

7. **Cliente no Local**
   - Ter um representante do cliente disponível na equipe para fornecer feedback contínuo e tomar decisões rápidas.

8. **Metas Claras**
   - Definir e seguir metas claras para cada iteração e para o projeto como um todo.

**BENEFÍCIOS**

- **Alta Qualidade de Software**: Através de práticas como TDD e refatoração, XP promove a criação de código mais limpo e confiável.
- **Flexibilidade e Adaptabilidade**: Permite responder rapidamente a mudanças nos requisitos e no ambiente do projeto.
- **Satisfação do Cliente**: Entrega contínua de valor e envolvimento constante do cliente garantem que o produto final esteja alinhado com suas expectativas.
- **Trabalho em Equipe Eficiente**: A comunicação constante e a programação em pares promovem uma equipe colaborativa e coesa.

### Design Sprint

O **Design Sprint** é uma metodologia criada pelo Google Ventures (GV) que visa acelerar o processo de desenvolvimento e validação de ideias de produtos. É uma abordagem estruturada para resolver problemas e testar ideias em um curto período de tempo, geralmente cinco dias.

**OBJETIVO**

O principal objetivo do Design Sprint é **resolver problemas críticos e validar ideias rapidamente**. Ele ajuda equipes a tomar decisões informadas e a reduzir o risco de falhas ao lançar novos produtos ou funcionalidades.

**ESTRUTURA**

O Design Sprint é dividido em cinco fases, uma para cada dia da semana, com cada fase tendo um objetivo específico:

**DIA 1: ENTENDER**

- **Objetivo**: Compreender o problema, o contexto e os objetivos do projeto.
- **Atividades**:
  - Reuniões com stakeholders para definir o desafio e os objetivos.
  - Mapeamento do problema e identificação das partes interessadas.
  - Coleta de informações e definição do escopo do sprint.

**DIA 2: ESBOÇAR**

- **Objetivo**: Gerar uma variedade de soluções e ideias para o problema identificado.
- **Atividades**:
  - Brainstorming de ideias e esboço de possíveis soluções.
  - Desenvolvimento de esboços e protótipos iniciais.
  - Exploração de diferentes abordagens e soluções criativas.

**DIA 3: DECIDIR**

- **Objetivo**: Escolher a melhor solução e preparar um protótipo para teste.
- **Atividades**:
  - Revisão das ideias e esboços desenvolvidos no Dia 2.
  - Votação para selecionar as melhores soluções.
  - Criação de um storyboard detalhado para o protótipo.
  - Planejamento do protótipo e divisão das tarefas.

**DIA 4: PROTOTIPAR**

- **Objetivo**: Construir um protótipo realista da solução escolhida.
- **Atividades**:
  - Desenvolvimento do protótipo com base no storyboard.
  - Construção de um protótipo de alta fidelidade, que pode ser um mockup ou um modelo interativo.
  - Preparação para testes com usuários reais.

**DIA 5: TESTAR**

- **Objetivo**: Testar o protótipo com usuários reais e coletar feedback.
- **Atividades**:
  - Condução de sessões de teste com usuários-alvo.
  - Coleta de feedback sobre o protótipo e as soluções propostas.
  - Análise dos resultados e identificação de melhorias necessárias.

**BENEFÍCIOS**

- **Velocidade**: Permite validar ideias e tomar decisões em apenas cinco dias, economizando tempo e recursos.
- **Foco**: Concentra a equipe em um único problema ou desafio por vez.
- **Feedback Rápido**: Obtém feedback valioso de usuários reais antes de investir no desenvolvimento completo.
- **Colaboração**: Promove a colaboração entre diferentes membros da equipe e stakeholders.

### Modelo Spotify Squads

É uma abordagem de organização e gerenciamento de equipes desenvolvida pela Spotify para promover agilidade e inovação. O modelo é conhecido por sua abordagem **flexível** e **adaptável** para o desenvolvimento de software e produtos.

**ESTRUTURA**

**1. Squads**

- **Definição**: Squads são equipes autônomas e multidisciplinares responsáveis por um aspecto específico do produto ou serviço.
- **Características**:
  - **Autonomia**: Cada squad tem a liberdade de decidir como trabalhar, escolher suas ferramentas e definir suas próprias práticas.
  - **Objetivos**: Focado em entregar valor para o cliente e atingir metas específicas relacionadas ao seu domínio.
  - **Composição**: Normalmente composta por membros com diferentes habilidades, como desenvolvedores, designers e analistas.

**2. Tribes**

- **Definição**: Tribes são grupos de squads que trabalham em áreas relacionadas ou produtos semelhantes.
- **Características**:
  - **Coordenação**: Facilita a comunicação e a colaboração entre squads que têm interdependências ou trabalham em áreas similares.
  - **Liderança**: Cada tribe possui um Tribe Lead, que ajuda a coordenar e a resolver conflitos entre squads.

**3. Chapters**

- **Definição**: Chapters são grupos de pessoas com funções semelhantes, como desenvolvedores ou designers, que se reúnem para compartilhar conhecimentos e melhores práticas.
- **Características**:
  - **Desenvolvimento Profissional**: Focado no desenvolvimento de habilidades e na melhoria contínua dos membros do chapter.
  - **Mentoria**: Oferece suporte e orientação para o crescimento profissional e técnico dos membros.

**4. Guilds**

- **Definição**: Guilds são comunidades informais que reúnem pessoas com interesses comuns em diferentes áreas, como tecnologias específicas ou práticas de desenvolvimento.
- **Características**:
  - **Compartilhamento de Conhecimento**: Promove a troca de informações e experiências entre diferentes equipes e áreas.
  - **Networking**: Facilita a colaboração e o aprendizado entre membros de diferentes squads e tribes.

**BENEFÍCIOS**

- **Autonomia e Empoderamento**: Squads têm a liberdade de tomar decisões, o que aumenta a inovação e a agilidade.
- **Coordenação Eficiente**: Tribes e chapters ajudam a manter a colaboração e a coerência em grandes organizações.
- **Desenvolvimento Contínuo**: Chapters e guilds promovem o crescimento e a especialização contínuos.
- **Flexibilidade**: O modelo é adaptável e pode ser ajustado para atender às necessidades específicas da organização.

**DESAFIOS**

- **Manutenção da Coerência**: Garantir que todos os squads estejam alinhados com os objetivos gerais da empresa pode ser desafiador.
- **Comunicação e Colaboração**: Manter uma boa comunicação entre squads, tribes e guilds exige esforço e ferramentas eficazes.

### Método SMART

É uma abordagem para definição de metas, garantindo que sejam claras e realizáveis. SMART é um acrônimo para:

**1. Específico (Specific)**

- **Definição**: A meta deve ser clara e detalhada.
- **Perguntas**: O que? Por quê? Quem? Onde? Quando?

**2. Mensurável (Measurable)**

- **Definição**: A meta deve ter critérios para medir o progresso.
- **Perguntas**: Quanto? Como saberemos quando está concluída?

**3. Atingível (Achievable)**

- **Definição**: A meta deve ser realista e possível de alcançar.
- **Perguntas**: É viável com os recursos disponíveis?

**4. Relevante (Relevant)**

- **Definição**: A meta deve ser significativa e alinhada com objetivos maiores.
- **Perguntas**: É importante? Contribui para o objetivo geral?

**5. Temporal (Time-bound)**

- **Definição**: A meta deve ter um prazo definido.
- **Perguntas**: Quando deve ser concluída?

**BENEFÍCIOS**

- **Clareza e Foco**: Metas bem definidas ajudam no foco e na clareza.
- **Motivação**: Metas realistas e relevantes aumentam a motivação.
- **Avaliação**: Permite o monitoramento e avaliação eficaz.

**DESAFIOS**

- **Metas Irrealistas**: Podem causar frustração.
- **Falta de Clareza**: Pode levar a confusão.

O método SMART ajuda a criar metas claras e eficazes, facilitando o planejamento e a execução.

### Trello

É uma **ferramenta de gerenciamento** de projetos e tarefas baseada em uma interface visual de quadros, listas e cartões. Utiliza o **método Kanban** para ajudar equipes e indivíduos a organizar e acompanhar o progresso de projetos de forma colaborativa e intuitiva.

**CARACTERÍSTICAS**

**1. Quadros**

- **Definição**: Contêiner principal para projetos e tarefas.
- **Funcionalidade**: Cada quadro representa um projeto ou uma área de trabalho.

**2. Listas**

- **Definição**: Divisões dentro de um quadro que organizam tarefas em diferentes fases.
- **Funcionalidade**: Normalmente usadas para representar estágios do fluxo de trabalho, como "A Fazer", "Em Progresso" e "Concluído".

**3. Cartões**

- **Definição**: Itens individuais de tarefas ou atividades.
- **Funcionalidade**: Cartões podem ser movidos entre listas, e podem conter detalhes como descrições, checklists, datas de vencimento, etiquetas, e anexos.

**4. Etiquetas e Filtros**

- **Definição**: Ferramentas para categorizar e organizar cartões.
- **Funcionalidade**: Etiquetas coloridas e filtros ajudam a identificar e priorizar tarefas.

**5. Colaboração**

- **Definição**: Recursos para trabalhar em equipe.
- **Funcionalidade**: Permite adicionar membros, comentar em cartões, e atribuir tarefas.

**6. Automação**

- **Definição**: Recursos para automatizar tarefas repetitivas.
- **Funcionalidade**: Utiliza o "Butler" para criar regras e comandos automáticos que simplificam processos.

**BENEFÍCIOS**

- **Visualização Clara**: Interface visual facilita o acompanhamento do progresso.
- **Flexibilidade**: Adaptável a diferentes tipos de projetos e fluxos de trabalho.
- **Colaboração**: Facilita o trabalho em equipe com recursos de comunicação e compartilhamento.

**DESAFIOS**

- **Complexidade em Projetos Grandes**: Pode se tornar difícil de gerenciar em projetos muito complexos.
- **Dependência de Internet**: Requer acesso à internet para uso completo das funcionalidades.

O Trello é uma ferramenta versátil e fácil de usar, ideal para organizar projetos e tarefas de maneira colaborativa e eficiente.

### Asana

É uma ferramenta de gerenciamento de projetos e tarefas projetada para ajudar equipes a coordenar e acompanhar o trabalho. Oferece uma variedade de funcionalidades para organização, colaboração e visualização do progresso dos projetos.

**CARACTERÍSTICAS**

**1. Projetos**

- **Definição**: Contêineres para agrupar tarefas relacionadas.
- **Funcionalidade**: Cada projeto pode ser visualizado de diferentes formas, como listas, quadros Kanban ou cronogramas.

**2. Tarefas**

- **Definição**: Itens individuais de trabalho dentro de um projeto.
- **Funcionalidade**: Tarefas podem incluir subtarefas, datas de vencimento, prioridades, responsáveis, descrições e anexos.

**3. Seções e Marcos**

- **Definição**: Elementos para organizar e acompanhar o progresso dentro de projetos.
- **Funcionalidade**: Seções dividem tarefas em grupos, enquanto marcos ajudam a identificar etapas importantes no projeto.

**4. Calendário e Cronograma**

- **Definição**: Ferramentas para visualização de tarefas e cronogramas.
- **Funcionalidade**: O calendário exibe prazos e eventos importantes, enquanto o cronograma (ou timeline) mostra o progresso das tarefas ao longo do tempo.

**5. Colaboração**

- **Definição**: Recursos para facilitar a comunicação e o trabalho em equipe.
- **Funcionalidade**: Permite comentários em tarefas, a atribuição de responsáveis e a adição de seguidores para notificações.

**6. Relatórios e Painéis**

- **Definição**: Ferramentas para acompanhar e analisar o progresso.
- **Funcionalidade**: Relatórios fornecem insights sobre o andamento dos projetos, enquanto os painéis oferecem uma visão geral das métricas e status.

**BENEFÍCIOS**

- **Organização Eficiente**: Ajuda a estruturar e organizar projetos complexos com várias tarefas e responsáveis.
- **Colaboração Facilitada**: Recursos de comunicação e compartilhamento melhoram a coordenação entre equipes.
- **Visibilidade e Monitoramento**: Ferramentas de visualização e relatórios oferecem uma visão clara do progresso e dos prazos.

**DESAFIOS**

- **Curva de Aprendizado**: Pode levar algum tempo para se familiarizar com todas as funcionalidades.
- **Complexidade em Projetos Muito Grandes**: Projetos muito complexos podem exigir uma configuração cuidadosa para manter a organização e a clareza.


### Ferramentas de Projetos

**1. *BRAINSTORMING***

- Técnica para gerar uma ampla gama de ideias criativas e inovadoras em equipe.

**2. MAPAS MENTAIS**

- Mapas mentais ajudam a visualizar e organizar informações ao redor de um tema central, facilitando o pensamento criativo.

**3. *MOODBOARD***

- *Moodboards* reúnem imagens e elementos visuais para definir e comunicar a estética e o tom de um projeto.

**4. PERSONAS E MAPA DE EMPATIA**

- Personas e mapas de empatia ajudam a entender melhor os usuários, suas necessidades e como se sentem em relação ao produto.

**5. GRUPOS DE USUÁRIOS**

- Grupos de usuários segmentam a base de clientes em categorias com características semelhantes para criar soluções mais personalizadas.

**6. JORNADA DO USUÁRIO**

- A jornada do usuário mapeia a experiência completa do cliente com um produto, identificando pontos críticos e oportunidades de melhoria.

**7. *STORYBOARD***

- *Storyboards* visualizam a sequência de eventos e a narrativa de um projeto, facilitando o planejamento e a comunicação da história.

___
### ↩️ [Retornar ao início](../README.md)