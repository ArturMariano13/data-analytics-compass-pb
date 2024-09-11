# SPRINT 7 - Plataformas Big Data (Spark, Hadoop)

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
## Curso: Formação Spark com Pyspark
### Introdução ao Spark
- **Spark** é uma **ferramenta de processamento de dados**.
    - Distribuúido em um **Cluster**
    - Em memória
    - Veloz
    - Escalável
    - Dados em HDFS ou Cloud
    - Particionamento
    - **Replicação e Tolerância a falhas**: dados são copiados entre os nós do cluster.

### Arquitetura e Componentes

**COMPONENTES**
- Machine Learning (Mlib)
- SQL (Spark SQL)
    - Permite ler dados tabulares de várias fontes (CSV, JSON, Parquet, etc).
    - Pode usar sintaxe SQL.
- Processamento em Streaming (Spark Structured Steraming)
    - Dados estruturados.
    - Novos registros adicionados ao final da tabela.
- Processamento de Grafos (GraphX)

**ESTRUTURA**
- **Driver**: inicializa SparkSession, solicita recursos computacionais do Cluster Manager, transforma as operações em DAGs, distribui estas pelos executers.
- **Manager:** gerencia os recursos do cluster. Quatro possíveis: built-in standalone, YARN, Mesos e Kubernetes
- **Executer:** roda em cada nó do cluster executando as tarefas.

**ELEMENTOS**
- SparkSession: seção
- Application: programa

**TRANSFORMAÇÕES E AÇÕES**
- Um data frame é imutável: traz tolerância a falha.
- Uma transformação gera um novo data frame.
- O processamento de transformação de fato só ocorre quando há uma Ação: Lazy Evaluation.

**COMPONENTES**
- **Job:** tarefa
- **Stage:** divisão do job
- **Task:** menor unidade de trabalho. Uma por núcleo e por partição.

### Context e Session
- **SparkContext:** conexão transparente com o Cluster.
- **SparkSession:** acesso ao SparkContext.

> Pode rodar script Spark no shell (pyspark). O Spark cria uma sessão automaticamente chamada **spark**.


### Formatos de Big Data
- Armazéns de dados modernos tendem a armazenar dados em formatos "desacoplados" de ferramentas e abertos.
- Formatos **binários**, compactados.
- Suportam *Schema*.
- Podem ser particionados entre discos:
    - Redundância
    - Paralelismo

**FORMATOS**
- **Parquet:** colunar, padrão do Spark
- **ORC:** colunar, padrão do Hive
- **Avro:** linha

> Muitos atributos e mais escrita = linha
> Menos atributos e mais leitura = coluna

**QUAL ESCOLHER?**
- Em geral, ORC é mais eficiente na criação (escrita) e na compressão.
- Parquet tem melhor performance na consulta (leitura).

> IDEAL: fazer um **benchmark**


--- 
## Leitura Obrigatória: Apache Hadoop e Apache Spark
### Apache Hadoop
É um **framework** Open Source, assim como o Spark, que **permite gerenciar e processar big data com eficiência em um ambiente de computação distribuído**.

Consiste em **quatro** módulos principais:

1. **Hadoop Distributed File System (HDFS):** É um sistema de armazenamento que usa tecnologia de armazenamento de objetos armazenando os dados como objetos de tamanho variável.
    - Características do *object storage*: durabilidade, alta disponibilidade, replicação e elasticidade.
    - Cada item é um objeto com um identificador único.
    - Seguindo essa tendência, os principais provedores de nuvem têm suas implementações de *object storage*, como o AWS S3, o Oracle Object Storage, o Azure Blob Storage e o Google Cloud Storage.

2. **Yet Another Resource Navigator (YARN):** facilita tarefas agendadas, gerenciamento completo e monitoramento de nós de cluster entre outros recursos.

3. **MapReduce:** o módulo Hadoop MapReduce ajuda os programas a realizar computação paralela de dados. 
    - Map: converte os dados em pares chave-valor. 
    - Reduce: consome a entrada, agrega-a e produz o resultado. 

4. **Hadoop Common:** usa bibliotecas Java que são padrões em todos os outros módulos.

**CAMADAS**
- **Armazenamento de dados:** há o sistema de arquivos distribuído HDFS.
- **Processamento de dados:** MapReduce.
- **Acesso aos dados:** Pig, Hive, Avro, Mahout, etc.

> Todo um ecossistema em volta do Hadoop é criado com ferramentas que suprem necessidades específicas.

### Arquitetura dos componentes básicos do Hadoop
- Para que o Hadoop funciona, são necessários cinco processos: 
    - NameNode
    - DataNode
    - SecondaryNameNode
    - JobTracker
    - TaskTracker

- **HDFS**
    - Sistema de arquivos distribuído
    - Responsável pela organização, armazenamento, localização, compartilhamento e proteção de arquivos.
    - Escalabilidade e disponibilidade => replicação de dados e tolerância a falhas.
    - Arquitetura do HDFS é estruturada em mestre-escravo, com dois processos principais:
        - **Namenode**: responsável por gerenciar os dados armazenados no HDFS, registrando as informações sobre quais datanodes são responsáveis por quais blocos de dados de cada arquivo, organizando isso em uma tabela de metadados. Fica localizado no nó mestre da aplicação, juntamente com o JobTracker.
        - **Datanode**: responsável pelo armazenamento do conteúdo dos arquivos nos computadores escravos. Um Datanode poderá armazenar múltiplos blocos, inclusive de diferentes arquivos, entretanto, eles precisam se reportar constantemente ao NameNode, informando-o sobre as operações que estão sendo realizadas.

- **MapReduce**
    - Modelo computacional para processamento paralelo das aplicações.
    - Abstrai as dificuldades do trabalho com dados distribuídos, eliminando quaisquer problemas que o compartilhamento de informações pode trazer em um sistema dessa natureza.
    - Possui três fases:
        - **Map:** recebe os dados de entrada, estruturados em uma coleção de pares chave/valor. Função deve ser codificada pelo desenvolvedor.
        - **Shuffle:** organizar o retorno da função Map, atribuindo para a entrada de cada Reduce todos os valores associados a uma mesma chave.
        - **Reduce:** ao receber os dados de entrada, a função Reduce retorna uma lista de chave/valor contendo zero ou mais registros, semelhante ao Map, que também deve ser codificada pelo desenvolvedor.
    - Arquitetura também segue o princípio master-slave, necessitando de três processos:
        - **JobTracker:** recebe a aplicação MapReduce e programa as tarefas map e reduce para execução, coordenando as atividades nos TaskTrackers. Designa diferentes nós para processar as tarefas de uma aplicação e monitorá-las enquanto estiverem em execução.
        - **TaskTracker:** processo responsável por executar as tarefas de map e reduce e informar o progresso das atividades. Uma aplicação Hadoop possui diversas instâncias de TaskTrackers, uma em cada um nó escravo.
        - **SecondaryNameNode:** utilizado para auxiliar o NameNode a manter seu serviço, e ser uma alternativa de recuperação no caso de uma falha do NameNode. Única função é realizar pontos de checagem do NameNode em intervalos pré-definidos.

- **Algoritmo de MapReduce**
    - O principal pilar de um sistema de MapReduce é um sistema de arquivos distribuído cuja funcionalidade básica é explicada facilmente: arquivos grandes são divididos em blocos de tamanho igual, que são distribuídos pelo cluster para armazenamento.

    - **Fase Map:** aplica a mapfunction para toda a entrada do algoritmo. Os mappers são executados em todos os nós computacionais do cluster, cuja tarefa é processar os blocos no arquivo de entrada que estão armazenados no HDFS.
    - **Shuffle:** ordena os pares resultantes da fase do map localmente por suas chaves, depois disso, o MapReduce os atribui a um reducer de acordo com suas chaves. O framework garante que todos os pares com a mesma chave sejam atribuídos ao mesmo reducer.
    - **Reduce:** finalmente a fase de reduce coloca todos os pares com a mesma chave e cria uma lista classificada dos valores. A chave e a lista ordenada de valores fornecem a entrada para a função Reduce. A função Reduce normalmente compacta a lista de valores para criar uma lista mais curta - por exemplo, agregando os valores.

### Apache Spark
É um framework de código aberto para Big Data que tem o **objetivo de processar grandes conjuntos de dados de forma paralela e distribuída.**

O Spark estende o modelo de programação MapReduce popularizado pelo Apache Hadoop, facilitando bastante o desenvolvimento de aplicações de processamento de grandes volumes de dados.

Permite a programação nas linguagens: R, Java, Scala, SQL e Python.

A biblioteca Pandas é amplamente utilizada para processamento de conjuntos de dados pequenos localmente e introduzir o conceito de DataFrames. No entanto, possui certas limitações quando se trata de Big Data por não conseguir fazer o processamento de forma paralela e distribuída.

- A leitura sugere um exercício prático, o qual está no diretório de evidências: [veja aqui](evidencias/HelloWorld.ipynb).
    - Escrever código utilizando as APIs da classe DataFrame torna mais fácil debugar o código em caso de erro e dividir o código em funções menores.
```python
from pyspark.sql.functions import when

df_full_name4 = df_filtered.withColumn(
    "fullname",
    when(
        col("middlename") == "",
        concat(
            col("firstname"),
            lit(" "),
            col("lastname")
        )
    ).otherwise(
        concat(
        col("firstname"),
        lit(" "),
        col("middlename"),
        lit(" "),
        col("lastname")
    )
    )
)
```

- No Spark, temos os conceitos de **TRANSFORMAÇÕES** e **AÇÕES**.
    - **Transformações**
        - Operações sobre um DataFrame que resultam num novo DataFrame com forma ou dados alterados. Somente ocorrem quando uma action é invocada.
        - A função `show()` é um exemplo de AÇÃO.
            - Sendo assim, o Python apenas executa as transformações no momento em que precisa realizar uma ação, como `show()` = ***lazy evaluation***

    - **Dados e schema**
        - StructType é uma estrutura que comporta um conjunto de colunas - e por isso ela é o primeiro nível do schema do nosso DataFrame - recebe como argumento uma lista de StructFields.
            - Cada StructField recebe como argumento do seu construtor 3 informações: nome da coluna, seu tipo e um booleano que indica se essa coluna pode conter valores nulos.
        - DataFrames são objetos imutáveis, ou seja, toda vez que precisamos fazer alguma alteração, na realidade, cria-se um novo objeto a partir do antigo.

- **Componentes**
    - **SparkSQL + Dataframes:** módulo utilizado para trabalhar com dados estruturados. Possibilita realizar consultas em dados estruturados dentro dos programas Spark, utilizando SQL ou a API do Spark para DataFrame.
    - **Spark Streaming:** módulo que permite criar aplicações de streaming escaláveis e tolerante a falhas. Permite reutilizar o mesmo código para processamento em lote, unir os fluxos em relação aos dados históricos ou executar consultas iterativas ou em lote (batch).
    - **GraphX:** API para grafos e computação paralela de grafos. Compete com o desempenho dos sistemas existentes de grafo. Mantendo a flexibilidade do Spark, com tolerância a falhas e simples de usar.
    - **MLlib:** biblioteca de aprendizado de máquina escalável. Contém uma extensa lista de algoritmos de aprendizado de máquina como: classificação, regressão, árvores de decisão, sistema de recomendação, clusterização, entre outros.
    - **Spark-Core:** é o mecanismo principal do Spark. Fornece serviços como gerenciamento de memória, agendamento de tarefas no cluster, recuperação de falhas, além de fornecer suporte para diversos sistemas de armazenamentos como HDFS, S3, etc.

- **Arquitetura**
    - Aplicações Spark são executadas como conjuntos independentes de processos em um cluster, coordenados pelo objeto SparkContext em seu programa principal (**driver program**).
    - **Cluster Manager:** componente opcional que só é necessário se o Spark for executado de forma distribuída. Responsável por administrar as máquinas que serão utilizadas como workers.
        - Tipos de Cluster Manager
            - **Standalone:** gerenciador de cluster simples incluído no Spark que facilita a configuração de um cluster. Normalmente utilizado em execuções locais.
            - **Apache Mesos:** gerenciador geral de cluster que também pode executar Hadoop MapReduce.
            - **Hadoop YARN:** gerenciador de recursos no Hadoop 2.
            - **Kubernetes:** sistema de código aberto para automatizar a implantação, escalonamento e gerenciamento de aplicativos em contêineres.
        - Aplicações podem ser submetidas a um cluster Spark através do script spark-submit.
        - Cada Driver Program possui uma interface web, normalmente disponível na porta 4040.

        - **Glossário de termos do Apache Spark**
        | Termo           | Definição                                                                                                                                                                                                                                                                               |
        |-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | Aplicação       | Programa do usuário desenvolvido em Spark. Consiste em um Driver Program e executores no cluster.                                                                                                                                                                                       |
        | Application jar | Um jar contendo uma aplicação Spark do usuário. Em alguns casos, os usuários desejarão criar um '.jar' contendo sua aplicação junto com suas dependências. O jar do usuário nunca deve incluir as bibliotecas Hadoop ou Spark; elas serão adicionadas no tempo de execução.           |
        | Driver Program  | O processo que executa a função principal da aplicação e cria o SparkContext. Funciona como o `main()` do programa.                                                                                                                                                                      |
        | Cluster Manager | Um serviço externo para adquirir recursos no cluster (por exemplo, standalone, YARN).                                                                                                                                                                                                   |
        | Deploy mode     | Distingue onde o processo do driver é executado. No modo 'cluster', o framework inicia o driver dentro do cluster. No modo 'cliente', o solicitante inicia o driver fora do cluster.                                                                                                    |
        | Worker node     | Qualquer nó que pode executar o código da aplicação no cluster.                                                                                                                                                                                                                         |
        | Executor        | Um processo iniciado para uma aplicação Spark em um nó de trabalho, que executa tarefas e mantém os dados na memória ou armazenamento em disco. Cada aplicação possui seus próprios executores.                                                                                        |
        | Task            | Uma tarefa ou unidade de trabalho que será enviada a um executor.                                                                                                                                                                                                                       |
        | Job             | Uma computação paralela que consiste em várias tarefas que são geradas em resposta a uma ação do Spark.                                                                                                                                                                                 |
        | Stage           | Cada Job é dividido em conjuntos menores de tarefas chamados de estágios, que dependem uns dos outros (semelhante aos estágios map e reduce no MapReduce).                                                                                                                             |
            
    - **Workers:** máquinas que realmente executarão as tarefas que são enviadas pelo Driver Program.
        - No Spark local, a máquina será Driver Program e Worker ao mesmo tempo.

- **Directed Acyclic Graph (DAG)**
    - Sempre que uma ação é executada em um DataFrame, um DAG é criado.
        - DAG = grafo direcionado e sem ciclos.
    - Nas DAGs do Spark, cada vértice é uma função Spark, as tranasformações a serem realizadas e a ação que as invoca.
    - A DAG permite que o Spark otimize seu plano de execução e minimize o *shuffling*.

- **Código Spark**
    - Primeira parte: definida pela `SparkSession` ou `SparkContext`. 
        - `SparkContext`: é um ponto de entrada para Spark e é definido no pacote org.apache.spark desde a versão 1.x. É usado para criar programas Spark com RDD, acumuladores e variáveis de transmissão no cluster.
        - `SparkSession`: desde o Spark 2.x, a maioria das funcionalidades do Context está disponível no SparkSession. É uma classe combinada para todos os contextos diferentes como SQLContext, StreamingContext, etc.
        - Por isso, a primeira parte de um código Spark é a **criação de uma `SparkSession`** = maneira de acessar todas as funcionalidades do framework.


### Apache Hadoop VS Apache Spark
| Hadoop                                                                                                                                          | vs                                            | Spark                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Desempenho mais lento, usa discos para armazenamento e depende da velocidade de leitura e gravação do disco.                                    | **Performance**                               | Desempenho rápido na memória com operações reduzidas de leitura e gravação em disco.                                                                                             |
| Uma plataforma Open-Source menos dispendiosa para operar. Usa hardware de consumo acessível.                                                    | **Custo**                                     | Uma plataforma Open-Source, mas depende da memória para computação, o que aumenta consideravelmente os custos de produção.                                                      |
| Melhor para processamento em batch. Usa MapReduce para dividir um grande conjunto de dados em um cluster para análise paralela.                 | **Processamento de Dados**                    | Adequado para análise de dados iterativa e análise em near real-time. Funciona com RDDs e DAGs para executar operações.                                                          |
| Um sistema altamente tolerante a falhas. Replica os dados entre os nós e os usa em caso de problema.                                            | **Tolerância a Falhas**                       | Rastreia o processo de criação do bloco RDD e pode reconstruir um conjunto de dados quando uma partição falha. O Spark pode também usar um DAG para reconstruir dados entre nós. |
| Facilmente escalável, adicionando nós ao cluster e discos para armazenamento. Suporta dezenas de milhares de nós sem um limite conhecido.       | **Escalabilidade**                            | Um pouco mais desafiador de escalar porque depende da RAM para computação. Suporta milhares de nós em um cluster.                                                                |
| Extremamente seguro. Suporta LDAP, ACLs, Kerberos, SLAs, etc.                                                                                   | **Segurança**                                 | Não é seguro por padrão. A segurança está desligada por padrão e depende da integração com o Hadoop para atingir o nível de segurança necessário.                               |
| Mais difícil de usar com menos linguagens suportadas. Usa Java ou Python para aplicações MapReduce.                                             | **Facilidade de Uso e Linguagens Suportadas** | Mais amigável. Permite o modo shell interativo. As APIs podem ser escritas em Java, Scala, R, Python, Spark SQL.                                                                 |
| Mais lento que o Spark. Os fragmentos de dados podem ser muito grandes e criar gargalos. Mahout é a biblioteca principal.                       | **Machine Learning**                          | Muito mais rápido com processamento na memória. Usa a biblioteca MLlib.                                                                                                          |
| Usa soluções externas. YARN é a opção mais comum para gerenciamento de recursos. O Oozie está disponível para agendamento de fluxo de trabalho. | **Gerenciamento de Recursos e Agendamento**   | Possui ferramentas integradas para alocação, programação e monitoramento de recursos.                                                                                            |
                                                                                         |


**PRINCIPAL DIFERENÇA**
- Está na abordagem do processamento: o Spark pode fazer isso na memória, enquanto o Hadoop precisa ler e gravar em disco, enquanto o Hadoop MapReduce precisa ler e gravar em um disco. Como resultado, a velocidade do processamento difere significativamente. O Spark pode ser até 100 vezes mais rápido. No entanto, o volume de dados processados também difere: o Hadoop MapReduce é capaz de trabalhar com conjuntos de dados muito maiores que o Spark.

**HADOOP MAPREDUCE É BOM PARA:**
1. Processamento linear de grandes conjuntos de dados. Caso o conjunto de dados seja maior que a RAM disponível, o Hadoop MapReduce pode superar o Spark.
2. Solução econômica se não houver resultados imediatos. Se a velocidade de processamento não for crítica, é uma boa opção.

**SPARK É BOM PARA:**
1. Processamento rápido de dados.
2. Processamento iterativo.
3. Processamento quase em tempo real. 
4. Aprendizado de máquina. Biblioteca MLlib.
5. Juntar conjuntos de dados.

___

### ↩️ [Retornar ao início](../README.md)