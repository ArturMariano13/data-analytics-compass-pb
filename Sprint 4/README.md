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


___
### ↩️ [Retornar ao início](../README.md)