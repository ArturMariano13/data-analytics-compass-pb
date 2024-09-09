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




___

### ↩️ [Retornar ao início](../README.md)