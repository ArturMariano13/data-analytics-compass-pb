# SPRINT 6 - Serviços Analíticos (AWS)


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
## 1. Noções básicas de Analytics na AWS

## Machine Learning

### Análise de Dados   X   *Data Analytics*

- **Análise de Dados:** processo de interpretação de dados que leva à tomada de decisões significativas (é uma parte de Data Analytics).
- ***Data Analytics:*** conceito mais amplo. Utiliza dados brutos capturados de várias fontes para processar, analisar e interpretar o que pode acontecer e como uma organização pode usar esse conhecimento a seu favor.

### Benefícios de *Data Analytics*

- Encontrar padrões
- Descobrir oportunidades
- Prever eventos e ações
- Tomar decisões bem informadas

### Tipos de *Analytics*

- **Descritiva**
    - Responde à pergunta: “**O que aconteceu?”**
    - Resume dados históricos para entender o que aconteceu ou o que está acontecendo.
    - Visualizações de dados (gráficos de pizza, de barras, de linha, tabelas, etc)
- **Diagnóstica**
    - Compara dados históricos com outros conjuntos de dados.
    - Responde à pergunta: **“Por que isso aconteceu?”**
    - Mineração,  detalhamento, correlação.
    - Utiliza-se operações de dados e transformações.
    - Requer julgamento humano.
- **Preditiva**
    - Responde **“O que pode acontecer?”**
    - Usa dados históricos e algoritmos estatísticos para **fazer previsões** sobre resultados futuros.
    - Técnicas: machine learning, previsão, correspondência de padrões…
- **Prescritiva**
    - Baseada na preditiva.
    - **Recomenda ações ou respostas** para os resultados previstos.
    - Machine learning, análise de gráficos, simulação, redes neurais de processamento de eventos complexos…

## Machine Learning

- É um **subconjunto da IA.**
- Os computadores utilizam ML para **aprender com os dados e fazer previsões com base neles.**
- Modelos de ML podem prever o que pode acontecer no futuro (analytics preditiva) e oferecer um curso de ação (analytics prescritiva).
- Esses modelos se tornam mais precisos por meio de um processo chamado **treinamento**. Durante o treinamento, os **dados são executados nas aplicações repetidas vezes usando regras e restrições**.

### Conceitos

- **Inteligência Artificial (IA):** amplo ramo da ciência da computação envolvido na construção de máquinas inteligentes que podem executar tarefas que exigem inteligência humana.
- **Modelo de *machine learning*:** um programa de computador projetado para encontrar padrões em um conjunto de dados não analisado.
- **Algoritmo de ML:** um programa de computador que ajuda os computadores a entender padrões ocultos nos dados, fazer previsões sobre os dados e recomendar ações a serem tomadas.

### Analytics para ML

- O ML automatiza o processo de extração de informações e padrões dos dados, economizando tempo e esforço.
- O ML é essencial para que a analytics revele conhecimentos valiosos e promova a inovação nas organizações.

### ML na AWS

- Pode-se utilizar os serviços de IA pré-treinados da AWS para automatizar a extração e análise de dados, personalizar a experiência do cliente, detectar atividades on-line fraudulentas e muito mais.

### IA generativa na AWS

- A IA generativa é um tipo de modelo de ML que cria novos conteúdos e ideias a partir das solicitações do usuário. Além de dados, a IA generativa também gera conteúdo como conversas, histórias, imagens, vídeos e músicas.

### **Amazon CodeWhisperer**

- É um **serviço de geração de código** que analisa seu código e comentários enquanto você escreve código no ambiente de desenvolvimento integrado (IDE). A solução vai além do preenchimento de código ao usar o processamento de linguagem natural para entender os comentários no código.

## 5 V’s do *Big Data*

- **Big data:** grandes volumes de dados de várias fontes que são armazenados rapidamente e que são complicados de proteger, analisar e obter informações valiosas por parte das organizações.

### 1. Volume

Quantidade de dados que serão ingeridos pela solução, ou seja, o tamanho total dos dados recebidos.

- Desafio: armazenar grandes quantidades de dados.
- **Exemplos de fontes de dados:**
    - **Dados transacionais:** incluem informações do cliente, compras de produtos on-line e contratos de serviço.
    - **Dados temporários:** incluem movimentos que você faz em um videogame on-line, cache do navegador da internet.
    - **Objetos:  i**magens, mensagens de e-mail, arquivos de texto, conteúdo de mídias sociais, mensagens de texto, vídeos.

### 2. Variedade

Significa a quantidade de diferentes fontes e os tipos de fontes que a solução usará.

- TIPOS DE DADOS
    - **Dados estruturados:** dados organizados por um modelo relacional ou esquema, que define os elementos dos dados e as relações entre eles. Eles costumam ser encontrados em bancos de dados relacionais. Pouca flexibilidade.
        - Sistema de Gerenciamento do relacionamento com o cliente (CRM)
        - Formulários on-line
        - Registros de rede
        - Sistema de reserva de eventos
    - **Dados semiestruturados:** geralmente são armazenados em bancos de dados não relacionais ou na forma de elementos e atributos em um arquivo. Geralmente temporários. Mais flexíveis.
        - CSV
        - JSON
        - XML
    - **Dados não estruturados:** geralmente são arquivos ou objetos.
        - E-mails
        - Documentos
        - PDFs
        - Fotos
        - Vídeos
                        
- MÉTODOS DE ARMAZENAMENTO DE DADOS
    - **Armazenamento de dados estruturados**
        - Bancos de Dados relacionais.
    - **Armazenamento de dados semiestruturados**
        - Bancos de Dados NoSQL: armazenam dados como uma coleção de documentos ou pares de chave-valor.
    - **Sistemas OLTP e OLAP**
        - OLTP: Processamento de Transação online (Bancos de Dados transacionais - consultas de pesquisa)
        - OLAP: Processamento Analítico online (consultas agregadas)


- Armazenamento de Dados com propósito específico

**Tabela com os serviços da AWS que fornecem armazenamentos de dados com propósito específico.**

| **Amazon Aurora** | Sistema de gerenciamento de banco de dados relacional sem servidor (RDBMS) de alto desempenho, alta disponibilidade, escalável e proprietário com compatibilidade total com MySQL e PostgreSQL. |
| --- | --- |
| **Amazon Relational Database Service (Amazon RDS)** | Serviço gerenciado de banco de dados relacional na nuvem com várias opções de mecanismo de banco de dados. |
| **Amazon Redshift** | Armazenamento de dados baseado na nuvem com ML para oferecer o melhor custo-benefício em qualquer escala. |
| **Amazon DynamoDB** | Banco de dados NoSQL rápido, flexível e altamente escalável. |
| **Amazon ElastiCache** | Serviço de cache de dados totalmente gerenciado, econômico e altamente escalável para desempenho em tempo real. |
| **Amazon MemoryDB para Redis** | Banco de dados em memória durável e compatível com Redis para desempenho ultrarrápido. |
| **Amazon DocumentDB (compatível com MongoDB)** | Banco de dados de documentos JSON totalmente gerenciado e escalável. |
| **Amazon Keyspaces (para Apache Cassandra)** | Serviço de banco de dados gerenciado, sem servidor, de alta disponibilidade, escalável e compatível com Apache Cassandra. |
| **Amazon Neptune** | Banco de dados gráfico sem servidor, escalável e de alta disponibilidade. |
| **Amazon Timestream** | Banco de dados de série temporal rápido, escalável e sem servidor. |
| **Amazon Quantum Ledger Database (QLDB)** | Banco de dados ledger totalmente gerenciado e verificável com criptografia |
| **AWS Database Migration Service (DMS)** | Serviço gerenciado e automatizado de migração e replicação para mover cargas de trabalho de banco de dados e analytics para a AWS com o mínimo de tempo de inatividade e zero perda de dados. |

### 3. Velocidade

Trata-se da velocidade com que os dados chegam e avançam para serem processados. Muitas organizações precisam de ingestão e processamento de dados quase em tempo real.

A alta velocidade dos dados resulta em um tempo de análise menor do que o fornecido pelo processamento de dados tradicional.

- TIPOS DE PROCESSAMENTO DE DADOS
    - **Em lote:** processa o conteúdo em levas ou grupos. É usado quando há muitos dados para processar e isso precisa ser feito em intervalos.
    - **Streams:** processa dados que são gerados de forma contínua. O processamento de streams é usado, por exemplo, para feedback em tempo real ou informações contínuas.

### 4. Veracidade

É o grau de exatidão, precisão e confiança dos dados. **Isso depende da integridade e credibilidade dos dados.

- FASES DO CICLO DE VIDA DOS DADOS
    1. **Criação:** integridade dos dados significa garantir que os dados sejam precisos. Isso geralmente envolve auditorias baseadas em software.
    2. **Agregação:** geralmente há poucos erros na geração de agregados. Os problemas surgem quando quem cria os agregados deturpa o que está contido nos agregados.
    3. **Armazenamento:** os dados em repouso podem ser adulterados. Eles podem ser atualizados. A auditoria é muito importante para garantir a integridade dos dados.
    4. **Acesso:** os usuários podem acessar os dados analíticos. Os sistemas devem ser somente leitura e auditados regularmente para detectar padrões de acesso incomuns.
    5. **Compartilhamento:**  a veracidade do sistema é testada. Os usuários geralmente sabem muito bem o que esperar dos relatórios que executam. Quando os números não corresponderem às expectativas, a veracidade dos dados será questionada.
    6. **Arquivamento:** em algum momento os dados chegam a um ponto em que perdem o valor imediato. Quando isso acontece, eles devem ser arquivados. A segurança dos dados é o fator mais importante. Os repositórios devem ter uma lista de acesso muito limitada que deve ser somente leitura.
    7. **Descarte:** importante em alguns ambientes regulatórios. Manter dados que não têm nenhuma utilidade expõe a organização a riscos desnecessários. Os dados precisam ser destruídos em algum momento para segurança e conformidade com regulamentos, como o Regulamento geral de proteção de dados da UE, ou RGPD.
- **ETL - Extração, Transformação e Carregamento**
    - Processo de coletar dados de fontes de dados brutas e transformá-los em um tipo comum.
    - **Objetivos:**
        - Garantir que os dados tenham a acurácia, precisão e o detalhamento necessários.
        - Reunir dados de diferentes fontes para ter uma visão completa.
        - Criar conjuntos de dados com propósito específico para responder às principais perguntas de negócios.
        
    - Etapas do ELT (ordem diferente):
        1. Garantir que os dados tenham a acurácia, precisão e o detalhamento necessários.
        2. Reunir dados de diferentes fontes para ter uma visão completa.
        3. Criar conjuntos de dados com propósito específico para responder às principais perguntas de negócios.
- **Uma comparação dos processos de ETL e ELT**
    - Data scientists usam principalmente o **ETL para carregar bancos de dados legados no data warehouse** e usam o **ELT com bancos de dados modernos.**

### 5. Valor

É a capacidade extrair informações significativas dos dados que foram armazenados e analisados.

- Consulta e geração de relatórios;
- Visualização de dados.

## Serviços da AWS para Analytics

### Serviços da AWS para Volumes

- **Amazon S3**: Armazene qualquer quantidade de objetos com escalabilidade, disponibilidade e segurança. Armazena todos os tipos de dados.
- **AWS Lake Formation:** Construa, gerencie e proteja data lakes de forma mais rápida e fácil.
- **Amazon Redshift:** Utilize data warehousing na nuvem com o melhor custo-benefício. Usado para dados estruturados.

### Serviços da AWS para Variedade

- **Amazon RDS:** Banco de dados relacional baseado na nuvem para fácil configuração, operação e escalabilidade.
    - Suporte para produtos de banco de dados que você já conhece (Amazon Aurora, MySQL, PostgreSQL, MariaDB, Oracle e SQL Server).
    - Alta disponibilidade, alto throughput e armazenamento escalável.
- **Amazon Redshift:** Melhor relação preço/desempenho para armazenamento de dados na nuvem.
    - Análise de dados em bancos de dados operacionais, data lakes e data warehouse.
    - Integração de serviços da AWS com bancos de dados, analytics e serviços de ML da AWS.
    - Consulta de dados em tempo real em organizações, contas e Regiões.
    - Otimização automática do data warehouse.
    - Opções totalmente gerenciadas e sem servidor.
- **Amazon OpenSearch Service:** Pesquisa, monitoramento e análise em tempo real de dados empresariais e operacionais.
    - Analise de logs de atividades de aplicações ou sites voltados para o cliente.
    - Analise de dados de uso de produtos provenientes de outros serviços e sistemas.
    - Analise de sentimentos em mídias sociais, de dados de CRM e identificação de tendências para sua organização ou serviço.
    - Monitoramento do uso dos aplicativos móveis.
- **Amazon DynamoDB:** Banco de dados NoSQL rápido, flexível e totalmente gerenciado para alto desempenho em qualquer escala.
    - Serviço de banco de dados NoSQL rápido, flexível e escalável com desempenho de um dígito em milissegundos.
    - Throughput e armazenamento ilimitados.
    - Replicação automática em várias regiões.
    - Proteção de dados com criptografia em repouso, backup e restauração automáticos.
    - Desempenho confiável de um dígito em milissegundos e disponibilidade de até 99,999%.

OBS.: RESUMO: 

- O Amazon RDS é usado como um banco de dados relacional baseado na nuvem.
- O Amazon Redshift é usado como um data warehouse baseado na nuvem para armazenar grandes quantidades de dados estruturados e semiestruturados de bancos de dados operacionais, data warehouses e data lakes para análises complexas.
- O AWS DynamoDB é usado como um banco de dados NoSQL baseado na nuvem.
- O Amazon OpenSearch Service é usado para implantar clusters do OpenSearch gerenciados pela AWS para visualização de pesquisa e análise de texto e dados não estruturados.

### Serviços da AWS para Velocidade

- **Amazon EMR:** usado como uma plataforma de big data escalável e gerenciada que processa e analisa grandes volumes de dados em velocidades variáveis.
    - Execução de aplicações de big data e análises em escala de petabytes de forma rápida.
    - Menos da metade do custo das soluções on-premises.
    - Integração perfeita com o Amazon SageMaker.
    - Execução de tarefas de machine learning em grandes conjuntos de dados.
    - Utiliza frameworks de big data de código aberto (Spark, Hadoop, HBase, Hive, Hudi, Presto) para distribuir tarefas de processamento de dados.
    - Utiliza recursos de processamento paralelo para garantir que os dados possam ser ingeridos, transformados e analisados de forma rápida.
- **Amazon MSK:** usado como um serviço totalmente gerenciado que utiliza o Apache Kafka para processar fluxos de dados de alta velocidade.
    - Provisionamento de servidores, configuração de clusters Apache Kafka e substituição de servidores em caso de falha.
    - Orquestração de aplicação de patches e atualizações do servidor.
    - Arquitetura de clusters para alta disponibilidade e garantia de que os dados serão armazenados e protegidos de forma durável.
    - Configuração de monitoramento e alarmes.
    - Execução de scaling para suportar mudanças de carga.
- **Amazon Kinesis:** usado para ingerir, processar e analisar dados em tempo real.
    - Coleta, processa e analisa dados de streaming em tempo real.
    - Ajuda você a receber informações em tempo hábil e a reagir rapidamente a novas informações.
    - Facilita a captura, o processamento e armazenamento de fluxos de dados em qualquer escala.
- **Amazon Lambda:** usado como serviço computacional sem servidor para processamento de dados em tempo real e orientado por eventos.
    - Promove uma arquitetura orientada por eventos, para que você possa criar aplicações que respondam a alterações de dados, interações de usuários ou outros eventos.
    - Cria sistemas responsivos que reagem às alterações na velocidade dos dados sem a necessidade de monitoramento ou intervenção constantes.

### Serviços da AWS para Veracidade

- **Amazon EMR:** usado para coleta e processamento de dados em escala de petabytes.
- **AWS Glue:** usado como um serviço de ETL gerenciado e sem servidor, e também para gerenciar a qualidade dos dados com o AWS Glue Data Quality.
    - Serviço de integração de dados de várias fontes, com tecnologia sem servidor, escalável e de alto desempenho
    - Alta integração com muitos serviços da AWS
    - Suporte a vários workloads, incluindo lote, microlote e streaming
    - Recomendações de regras
    - Regras e ações integradas de qualidade de dados
    - Data Quality Definition Language (DQDL)
- **AWS Glue DataBrew:** é usado como uma preparação visual de dados para limpar e normalizar dados e prepará-los para analytics e ML.
    - Conecta-se diretamente aos serviços da AWS, como o Amazon S3, Amazon Redshift, AWS Lake Formation, Amazon Aurora e Amazon RDS.
    - Mais de 250 transformações pré-criadas para automatizar tarefas de preparação de dados sem código.
    - Automatize anomalias de filtragem, converta dados em formatos padrão e corrija valores inválidos.
- **Amazon DataZone:** é usado como um serviço de gerenciamento de dados para catalogar, governar, compartilhar e analisar os seus dados.
    - Pesquise dados publicados e solicite acesso para trabalhar em projetos.
    - Colabore com equipes de projeto por meio de ativos de dados.
    - Gerencie e monitore ativos de dados em projetos.
    - Garanta que os dados corretos sejam acessados com um fluxo de trabalho governado.
    - Acesse análises com uma visualização personalizada dos ativos de dados em uma aplicação ou API baseada na web.

### Serviços da AWS para Valor

- **Amazon QuickSight:** *Business intelligence* unificado em escala de nuvem.
    - Fácil criação de painéis interativos, relatórios paginados e analytics incorporada, e uso de consultas em linguagem natural.
    - Suporte à integração com várias fontes de dados, como o Amazon S3, Amazon Redshift, Amazon RDS, Amazon Athena e bancos de dados de terceiros.
    - Pode se conectar a fontes de dados on-premises.
    - Limpa, transforma e molda os dados antes de criar as visualizações.
    - Permite combinar várias visualizações em painéis interativos.
    - Integra-se ao Amazon SageMaker para incorporar modelos de ML diretamente nas visualizações.
- **Amazon SageMaker:** Crie, treine e implante modelos de ML para qualquer caso de uso com infraestrutura, ferramentas e fluxos de trabalho totalmente gerenciados.
    - A limpeza e a transformação de dados são realizadas utilizando ferramentas de pré-processamento de dados.
    - Acesse, rotule e processe grandes quantidades de dados estruturados e não estruturados para garantir que estejam prontos para ML.
    - Oferece algoritmos de ML integrados que são otimizados para desempenho e podem ser aplicados com facilidade a tarefas de analytics preditiva.
    - Oferece a opção de criar modelos de ML personalizados.
    - Você pode implantar modelos preditivos como um endpoint altamente disponível e escalável.
    - Integre de forma fácil suas previsões de modelo em outras aplicações ou sites para fazer previsões sobre novos dados.
- **Amazon Bedrock:** Crie e escale aplicações de IA generativa com modelos de base.
    - Escolha entre diversos modelos de base.
    - Personalize os modelos de base de forma privada.
    - Integre de forma fácil usando uma única API.
    - Conecte modelos de base a fontes de dados.
    - Detecção automática da fonte de dados.
- **Amazon Athena:** Analise dados em escala de petabytes onde eles estiverem.
    - Uma maneira simplificada e flexível de analisar petabytes de dados sem a necessidade de configurar e gerenciar a infraestrutura.
    - Salva o histórico e os resultados das consultas, facilitando a revisão de consultas anteriores, a análise do desempenho anterior e a solução de problemas de discrepância.
    - Integra-se de imediato com o AWS Glue.
    - Controla o acesso aos dados usando políticas do IAM.

## Data Lake

- É um repositório centralizado que uma organização pode usar para armazenar dados em escala, estruturados e não estruturados, em seu formato original (brutos).
- Armazenamento altamente escalável e seguro.
- Na AWS, um *data lake* pode ser composto por **vários serviços integrados:**
    - S3 é o principal
    - AWS Database Migration Service, Amazon Kinesis Data Streams, Amazon Kinesis Data Firehouse e Amazon EMR ajudam na ingestão dos dados.
    - AWS Glue e Amazon EMR podem analisar dados brutos para detectar padrões. Podem, em seguida, automatizar o processo de ETL.
    - AWS Lake Formation simplifica a instalação e a configuração - reduz os tempos típicos de implantação de semanas para dias

### Benefícios dos *data lakes*

- **Escalabilidade**: armazenar grandes quantidades e vários tipos de dados, possibilidade de aumentar ou reduzir a escala conforme necessário.
- **Eficiência de custos:** reduzir os custos com armazenamento de baixo custo (S3 ou EMR).
- **Flexibilidade:** armazenar dados estruturados, não estruturados e semiestruturados, carregamento fácil de novas fontes e tipos de dados.
- **Análise mais rápida:** evita os processos de ETL e ELT, processamento em tempo real e em lote.
- **Visualização centralizada:** visualize o repositório em uma única exibição, consulta de uma única fonte confiável e aplicação de políticas comuns de governança e segurança.

### Funções de um *data lake*

- Ingestão e armazenamento
- Catalogação e pesquisa
- Proteção e segurança
- Analytics e informações

### Arquitetura de *data lake* (AWS)

- Geralmente consiste no Amazon **S3** como **armazenamento principal** (dados coletados e armazenados no formato original).
- AWS Glue utilizado para fazer *crawling*, catalogar e extrair esquemas dos diversos dados.
- Serviços adicionais, como AWS Lambda, Amazon Kinesis e Amazon EMR para processar, transformar e analisar dados no *data lake*.

### Lake Formation

- É um serviço gerenciado que simplifica a criação, proteção e o gerenciamento de *data lakes.*
- Automatiza a ingestão, catalogação, limpeza e transformação de dados de diversas fontes em um *data lake* no Amazon S3.
- Usa *machine learning* e políticas para proteger, organizar e catalogar dados automaticamente.
- **Benefícios:**
    - Serviços com tecnologia sem servidor totalmente gerenciados
    - Data lake desenvolvido em dias
    - Baixo custo
    - Gerenciamento simplificado de permissões
    - Acesso monitorado e auditado para verificar a conformidade
    - Compartilhamento de dados
    - Integração com muitas ferramentas de analytics e machine learning

## *Data warehousing*

- Repositório central de informações especialmente projetado para **analytics**.
- Os dados fluem para um data warehouse a partir de aplicações de negócios, bancos de dados e outras fontes.
- Usuários acessam os dados por meio de ferramentas de *business inteligence* (BI), clientes SQL e outras aplicações de analytics.
- Um data warehouse **alimenta relatórios, painéis e ferramentas de analytics,** armazenando dados de forma eficiente.

> Um data warehouse on-premise apresenta muitos desafios, sendo pouco viável atualmente.
> 

### Modernização de *data warehouses* usando o Amazon Redshift

- O Amazon Redshift ajuda as organizações a configurar e implantar um novo *data warehouse* em minutos.
- Foi criado para armazenar e consultar conjuntos de dados com tamanhos que variam de gigabytes a petabytes.

![https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1724785200/87YD4BCFDlJTNDhAhS5cig/tincan/938093_1713742352_o_1hs1fij3h1c3iv8ek58148032db_zip/assets/redshiftArchitecture_pt-BR.svg](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1724785200/87YD4BCFDlJTNDhAhS5cig/tincan/938093_1713742352_o_1hs1fij3h1c3iv8ek58148032db_zip/assets/redshiftArchitecture_pt-BR.svg)

- Além disso, o Amazon Redshift tem suporte integrado para **ETL zero**.

## Arquitetura de dados moderna

- Uma arquitetura de dados moderna remove os limites entre sistemas diferentes e integra perfeitamente o data lake, o data warehouse e os armazenamentos de banco de dados com propósito específico.
- **O principal recurso de uma arquitetura de dados moderna é a governança unificada. Ela garante a conformidade de forma unificada para proteger, monitorar e gerenciar o acesso aos dados simplificando a aquisição, o processamento e a transmissão de dados.**

### Padrões de movimentação de dados na arquitetura de dados moderna

- **Movimentação de dados de dentro para fora:** dados são armazenados em um data lake e, em seguida, partes dos dados são movidas para um armazenamentos de dados com propósito específico para fazer Machine Learning adicional ou analytics.
- **Movimentação de dados de fora para dentro:** dados em armazenamento de dados com propósito específico como data warehouse ou banco de dados. Para executar analytics adicional, uma parte desses dados é movida do armazenamento de dados para um data lake.
- **Movimentação de dados no perímetro:** mostra uma forte integração do seu data lake, data warehouse e armazenamentos de dados com propósito específico para mover dados de um armazenamento para outro ao redor do perímetro. Um armazenamento de dados com propósito específico foi projetado para executar funções específicas de forma rápida e eficiente. A ferramenta certa para o trabalho certo.
- **Compartilhamento em toda a movimentação de dados:** Os clientes usam arquitetura de dados moderna para governança direta e compartilhamento de dados entre limites lógicos e físicos para criar domínios de dados alinhados às linhas de negócios. Uma arquitetura de dados moderna faz uso do padrão de malha de dados para compartilhamento de dados sem esforço. Uma malha de dados é uma arquitetura distribuída, orientada por domínio e centrada no conceito de dados como um produto.

### Pilares

1. Data lakes escaláveis
2. Serviços de analytics com propósito específico
3. Acesso unificado a dados
4. Governança unificada
5. Desempenho e relação custo-benefício

### Movimentação de dados (conceitos)

- Minimização do trânsito
- Uso da gravidade dos dados
- Uso de fluxos de trabalho mínimo de extração-carregamento-transformação (ELT) ou ETL zero
- Orquestração de pipelines
- Streaming para processamento contínuo de dados

![https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1724785200/87YD4BCFDlJTNDhAhS5cig/tincan/938093_1713742352_o_1hs1fij3h1c3iv8ek58148032db_zip/assets/mdaDataMovement_pt-BR.png](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1724785200/87YD4BCFDlJTNDhAhS5cig/tincan/938093_1713742352_o_1hs1fij3h1c3iv8ek58148032db_zip/assets/mdaDataMovement_pt-BR.png)

### Arquitetura de malha de dados para compartilhamento de dados

- A malha de dados adota um modelo descentralizado, onde os **dados são tratados como produtos** gerenciados por equipes de domínio, aumentando a eficiência no compartilhamento de dados.
- Equipes de domínio ou unidades de negócios gerenciam plataformas de dados autônomas que suportam análises específicas, aplicações e machine learning.
- Embora descentralizada, a malha de dados mantém governança e consistência através de uma infraestrutura central que gerencia serviços compartilhados como catálogos de dados e observabilidade.
- Os consumidores de dados, produtores de dados, e a governança central são separados para facilitar a organização e o acesso seguro aos dados.
- Os produtos de dados são armazenados em data lakes específicos que são catalogados e esquematizados, permitindo acesso direto por meio de serviços de nuvem.
- A malha de dados interconecta data lakes e domínios de aplicação, promovendo a colaboração e a agilidade na análise de dados.

### Amazon DataZone

- A AWS implementa o padrão de malha de dados por meio do Amazon DataZone.
- Serviço ajuda as organizações a gerenciar, governar e compartilhar ativos de dados na AWS, em fontes on-premises e em fontes de terceiros.
- O Amazon DataZone se integra a vários serviços da AWS. Ele pode publicar ativos de dados de fontes como AWS Glue Data Catalog, Amazon Redshift e Amazon S3 no catálogo do Amazon DataZone.

### Serviços da AWS para arquitetura de dados moderna (pilares)

1. **Serviços da AWS para data lakes escaláveis**
- Amazon S3
- AWS Glue Data Catalog
- AWS Lake Formation

1. **Serviços da AWS para analytics com propósito específico**
- Amazon Managed Service for Apache Flink
- Amazon QuickSight
- Amazon OpenSearch Service
- Amazon Redshift
- Amazon EMR
- Amazon SageMaker
- Serviços da AWS para IA
- Serviços da AWS para IA generativa
- Amazon Athena
- Amazon RDS
- Amazon Aurora
- Amazon DynamoDB

1. **Serviços da AWS para acesso unificado a dados**
- AWS Glue
- Amazon Kinesis Data Firehouse

1. **Serviços da AWS para governança unificada**
- Amazon DataZone
- AWS Lake Formation

1. **Serviços da AWS para desempenho e economia**
- Serviços como Amazon S3, Amazon Redshift, Amazon EMR e AWS Glue oferecem a melhor relação entre preço e desempenho em suas categorias.

## Casos de uso comuns

- **Saúde**: colete, armazene e analise grandes volumes de dados médicos.
- **Setor automotivo**: tornando os resultados de análises mais significativos e acessíveis.
- **Setor de energia:** usando data lakes e analytics para ativos de energia renovável.

## Arquitetura de referência

- **Fontes de dados**: os dados são coletados de várias fontes da organização.
- **Ingestão de dados:** dependendo do tipo da fonte de dados, os dados são ingeridos em lote ou streaming.
- **Data lake escalável**:  depois de ingerir os dados, eles precisam ser armazenados e gerenciados. Serviços diferentes são usados para armazenar e gerenciar dados e criar os data lakes.
- **Movimentação contínua de dados:** durante a movimentação de dados, os dados são transformados e catalogados nos armazenamentos. O AWS Glue e o AWS Glue DataBrew são usados para uma movimentação contínua de dados entre os armazenamentos e as ferramentas de analytics.
- **Analytics com propósito específico e informações:** os usuários podem executar consultas analíticas sofisticadas diretamente em seus armazenamentos de dados sem precisar copiar e carregar dados em plataformas de analytics ou data warehouses separados.

---

## 2. Serverless Analytics
- Vídeo que mostra uma forma de sintetizar diferentes dados usando ferramentas da AWS como:
    - AWS IoT Analytics
    - Amazon Cognito
    - AWS Lambda
    - Amazon SageMaker

- Conclusões: 
    - IoT não é apenas sobre dispositivos de borda, devemos pensar em uma comunicação de mão dupla.
    - IoT Analytics é uma maneira flexível de processar e armazenar dados de séries temporais.
    - Data lakes são uma maneira de baixo custo, com baixo esforço e flexíveis para se iniciar.

---

## 3. Introdução ao Amazon Athena

- Serverless
- Basta apontar ao S3 e realizar as queries
- Paga apenas pelas queries executadas
- Consulta dados diretamente no S3
- Suporta diversos formatos (JSON, CSV, etc)
- Escalável e alta disponibilidade
- Execução paralela

### Passos básicos

- Criar um bucket S3 e um objeto
- Criar um banco de dados de metadados
- Criar  um esquema
- Execute uma query

---

## 4. AWS Glue Getting Started
## O que o AWS Glue faz?

- É um serviço de integração de dados *serverless* (paga apenas o que utiliza).
- Com o AWS Glue, cientistas de dados, analistas e desenvolvedores podem descobrir, preparar e combinar dados para diversos propósitos.
    - Machine learning
    - Analytics
    - Desenvolvimento de aplicações

### Benefícios

- Integração de dados **mais rápida.**
- **Automatize a integração de dados em escala.**
- Sem infraestrutura para gerenciar.
- Cria, executa e monitora ETL sem necessidade de código.
- Pagamento do que se utiliza.

### Arquitetura e Casos de Uso

- Usando AWS Glue, podemos estabelecer conexões com diversas fontes de dados, incluindo bancos de dados relacionais populares com a AWS, ou fora dela.
- A arquitetura típica envolve conectar-se a fontes de dados usando conectores, rastrear os dados para identificar o esquema, limpar e padronizar, e desenvolver o processo de ETL para criar dados brutos e refinados.
- Esses dados refinados podem ser consumidos por ferramentas analíticas como Amazon Athena, Amazon Redshift e Amazon QuickSight.

### Conceitos básicos do AWS Glue Studio

- **Conexão**: uma conexão AWS Glue é um objeto no Catálogo de Dados que carrega informações como login, credenciais, detalhes da VPC, etc.
- **Crawler**: conecta a várias fontes, identifica o seu esquema e categoriza em formato de dados.
- **Data store**: armazenamento **físico** onde os dados são destinados a persistir de forma permanente (buckets do S3 e bancos de dados relacionais como o Amazon RDS). Data target é um data store onde o resultado de um processo ou transformação é gravado.
- **AWS Glue interactive sessions:** usuários podem criar e testar a preparação de dados necessária para aplicações de analytics.
- **DynamicFrame:** tabela distribuída que facilita o armazenamento de dados aninhados, como estruturas e arrays. Com ele, não é necessário definir um esquema previamente, pois ele pode ser inferido sem interrupções, permitindo que as transformações ocorram em uma única passagem.
- **Trabalho:** a lógica de negócios necessária para realizar o trabalho de ETL consiste em um script de transformação, fontes de dados e destinos de dados.
- **Formatos de arquivos:** AWS Glue suporta dois tipos de arquivo de formatos:
    - Apache Parquet é um tipo de arquivo de formato que estrutura dados em forma de coluna, ao contrário de CSV ou Excel que estrutura em linhas.
    - Apache Hudi, Apache Iceberg e Delta Lake, que dão capacidades transacionais ao data lake no Amazon S3.
- **Tabela: a** **tabela de definição** é a metadata que representa os dados do usuário, definindo o esquema desses dados, independentemente de estarem armazenados em um arquivo Amazon S3, uma tabela Amazon RDS, ou outro local. Ela inclui nomes de colunas, tipos de dados, detalhes de partições e outras informações sobre o conjunto de dados. O **esquema** dos dados é representado na definição de tabela do AWS Glue, enquanto os dados reais permanecem no armazenamento original. Tabelas do AWS Glue no Data Catalog podem ser usadas como fontes ou destinos em tarefas de ETL.
- **Transform:** é a lógica de código usada para manipular dados e convertê-los em um formato diferente, traduzindo-os em lógica de negócios.
- **Triggers:** inicia um trabalho de ETL e pode ser definido com base em um horário programado ou um evento.

### Conceitos técnicos básicos do AWS Glue DataBrew

- **Dataset:** refere-se a dados obtidos de várias fontes, como um arquivo Amazon S3, uma fonte de dados JDBC suportada ou o Data Catalog. O dataset também inclui informações sobre como o DataBrew pode acessar os dados, caso não sejam carregados diretamente.
- **Profiling**: Validação dos dados através de avaliações para identificar tendências e irregularidades, acessando dados diretamente de data lakes, data warehouses e bancos de dados.
- **Data lineage**: Representação visual das transformações dos dados, desde a origem até o destino.
- **Data quality**: Processo para garantir a precisão dos dados, usando um conjunto de regras para identificar e corrigir dados incorretos. Inclui a comparação entre valores reais e desejados, com ajustes e reavaliações conforme necessário.
- **Recipes**: Sequência de operações para transformar dados. As etapas podem ser testadas em amostras antes de serem aplicadas ao dataset completo.
- **Project**: Plataforma centralizada para análise e manipulação de dados, composta por um dataset (acesso somente leitura) e uma recipe (ações de transformação).
- **Jobs**: Funções para executar recipes (transformações) ou profiles (inspeções e resumos dos dados). Os jobs de recipe limpam e padronizam dados, enquanto os de profile geram resumos para ajudar na preparação de dados.
- **File type**: Suporte a tipos e formatos de arquivos como CSV, Excel, JSON, ORC e Parquet.
- **Transform**: Conjunto de instruções ou algoritmos usados para converter dados em um formato diferente.

### Casos de Uso Típicos para o AWS Glue

1. **ETL Simplificado**: Desenvolva ETL sem gerenciar infraestrutura, usando Python/Scala ou geração automática de código.
2. **Catálogo de Dados**: Descubra e consulte datasets na AWS sem mover dados, usando Athena, EMR e Redshift Spectrum.
3. **Qualidade e Preparação de Dados**: Crie e aplique regras de qualidade de dados; use DataBrew para estatísticas e limpeza sem codificação.
4. **Orquestração Visual**: Crie e execute jobs ETL com um editor visual no AWS Glue Studio, incluindo monitoramento e dashboards.
5. **Processamento em Tempo Real**: Use AWS Glue Streaming ETL para processar e carregar dados em tempo real de fontes de streaming.



___

### ↩️ [Retornar ao início](../README.md)