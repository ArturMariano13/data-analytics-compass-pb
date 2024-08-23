# SPRINT 5 - Fundamentos de Computação em Nuvem (AWS)


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
## Jogo da AWS
- Missões envolvendo criação de instâncias EC2, grupos de segurança, S3s, DynamoDB, entre outros.
- Certificado: [ver](certificados/jogo_AWS.png)

___
## 📝 Curso Preparatório para o Exame
### 🗂️ Estrutura da prova
- **Domínio 1** - Conceitos da nuvem: 24%
- **Domínio 2** - Segurança e conformidade: 30% 
- **Domínio 3** - Tecnologia e serviços da nuvem: 34%
- **Domínio 4** - Cobrança, preços e suporte: 12%

## ☁️ Domínio 1: Conceitos de Nuvem
### O que é computação em nuvem?
1. Autoatendimento sob demanda
2. Acesso à rede
3. Agrupamento de recursos
4. Elasticidade
5. Uso de recursos monitorado e cobrado

- **Vantagens**
    - **Alta disponibilidade:** tempo mínimo de inatividade.
    - **Tolerância a falhas:** projetar para tempo de inatividade zero.
    - **Recuperação de desastres:** projetar sistemas para operar durante um desastre.

- **Princípios de criação**
    - Parar de tentar adivinhar a capacidade
    - Testar sistemas em escala de produção
    - Automatizar a arquitetura
    - Permitir alterações evolucionárias

### 🏛️ Pilares do Well Architected Framework
1. **EXCELÊNCIA OPERACIONAL**
    - Executar operações como código
    - Fazer alterações frequentes
    - Prever falhas
    - Aprender com todas as falhas operacionais

2. **🔒 SEGURANÇA**
    - Implementar uma base de identidade sólida
    - Manter a rastreabilidade
    - Aplicar segurança em todas as camadas
    - Proteger dados em trânsito e ociosos

3. **⚙️ CONFIABILIDADE**
    - Recuperar-se automaticamente de falhas
    - Testar os procedimentos de recuperação
    - Dimensionar horizontalmente para aumentar a disponibilidade agregada da carga de trabalho
    - Parar de tentar adivinhar a capacidade
    - Gerenciar alterações na automação

4. **🚀 EFICIÊNCIA DE DESEMPENHO**
    - Democratizar tecnologias avançadas
    - Ter alcance global em minutos
    - Usar arquiteturas sem servidor (*serverless*)
    - Experimentar com mais frequência
    - Considerar a afinidade mecânica

5. **💲 OTIMIZAÇÃO DE CUSTOS**
    - Capacidade de executar sistemas para entregar valor comercial pelo menor valor possível.

6. **🌍 SUSTENTABILIDADE**
    - Compreensão do seu impacto
    - Estabelecer metas de sustentabilidade
    - Usar serviços gerenciados

### 🌐 Benefícios e Estratégias de Migração para a nuvem AWS
- **7 R's ➡️ 7 estratégias de migração para a nuvem**
    - Retirar
    - Reter
    - Redefinir hospedagem
    - Realocar
    - Recomprar
    - Redefinir plataforma
    - Refatorar ou refazer arquitetura

### 💼 Aspectos Econômicos
- Menores gastos em data centers

**CUSTO TOTAL DE PROPRIEDADE (TCO)**
- **Despesas operacionais:** custos operacionais diários (serviços públicos, toner de impressoras, café, lanches)
- **Despesas de capital:** custos associados à criação de benefícios a longo prazo (compra de prédios, servidores) - são comprados UMA VEZ e auxiliam a organização por anos.
- **Custos de mão de obra:** para manutenção de sistemas on premises.
- **Custos de licenciamento de software:** ao migrar, custos de softwares licenciados podem sofrer modificações.

---

## 🔐 Domínio 2: Segurança e Conformidade
### Modelo de Responsabilidade Compartilhada
- **CLIENTE:** responsável pela segurança **NA** nuvem.
    - Dados do cliente;
    - Plataforma, aplicações, identidades, gerenciamento de acessos;
    - Configuração de Sistema Operacional, rede e *firewall*;
    - Criptografia de dados;
    - Proteção do tráfego de rede.
- **AWS:** responsável pela segurança **DA** nuvem.
    - Software:
        - Computação;
        - Armazenamento;
        - Banco de Dados;
        - Redes.
    - Infraestrutura Global de Hardware:
        - Regiões;
        - Zonas de Disponibilidade;
        - Locais de borda.

### 🔐 Conceitos de segurança, governança e conformidade da nuvem
- Conformidade (*compliance*) varia de serviço para serviço.

**SERVIÇOS DE SEGURANÇA DA AWS**
    - **AWS WAF:** firewall de aplicação web (ajuda a proteger aplicações de ameaças que podem afetar a disponibilidade).
    - **Amazon GuardDuty:** serviço de **detecção de ameaças** que monitora a existência de **atividade mal-intencionada** e **comportamento não autorizado**.
    - **AWS Shield** 🛡️: serviço contra ataques comuns de negação de serviços distribuídos (DDoS).
    - **AWS Security Hub**
    - **Amazon Inspector:** fornece recomendações de segurança
    - **AWS Marketplace:** software de terceiros que pode ser implantado na conta AWS.
    - **AWS Knowledge Center:** encontrar mais informações sobre segurança na AWS.


- **Criptografia**:
    - Criptografar *dados em repouso*
    - Criptografar *dados em trânsito*

- Serviços que monitoram e geram relatórios sobre a atividade da conta da AWS:
    - Amazon CloudWatch
    - Amazon CloudTrail
    - AWS Audit Manager

> **OBS.:** é essencial entender o que cada um desses serviços faz (diferenças entre eles).

### Recursos de gerenciamento de acesso da AWS
- É necessário **gerenciar** e **controlar** o acesso dos usuários.
- Nem todos os usuários necessitam ter o mesmo nível de acesso.

**Criação da conta AWS**
- **USUÁRIO-RAIZ (root)**: acesso completo e irrestrito a todos os serviços da conta AWS.
    - Não deve ser utilizado para realizar tarefas diárias na AWS.
    - AWS **recomenda criar um usuário *admin* no Centro de Identidade do IAM** para executar **tarefas diárias**. 

- Amazon Cognito --> fornece credenciais temporárias para acessar a conta AWS.

### Identificar os componentes e os recursos de segurança
- Entender quando utilizar grupos de segurança ou listas de controle de acesso
- **Listas de controle de acesso**
    - Atuam como um **firewall** para controlar o tráfego que passa por sua sub-rede.
    - Usadas para o tráfego que entra ou sai de uma sub-rede.
    - Associadas às sub-redes, não aos recursos.
    - Gerenciam apenas o tráfego que excede os limites da sub-rede.
    - *Stateless*: só veem o tráfego indo em uma direção.
    - Adicionar regra de saída também para controlar.
- **Grupos de segurança**
    - Protegem sua rede em **nível de recurso**.
    - Não operam a nível de sub-rede.
    - Têm regras de entrada e saída
    - *Stateful*
    - Veem grupo de entrada e saída como parte do mesmo stream.

---

## Domínio 3: Tecnologia e Serviços da Nuvem
### Métodos de implantação e operação na AWS
- **OPERAÇÃO**
    - Acesso programático
    - AWS Command Line (AWS CLI)
    - Console de Gerenciamento da AWS
    - Infraestrutura como **código**
- **IMPLANTAÇÃO**
    - Nativa da nuvem
    - Híbrida
    - On-premises

### Definir a infraestrutura global da AWS
- **Serviços resilientes globalmente**: opera globalmente (um BD em que os dados são replicados em diferentes regiões) - ex.: IAM, CloudFront e Amazon Route 53

- **Serviços resilientes regionais**: operam em UMA região - replicam os dados para zonas de disponibilidade dentro da região (se uma região falhar, o serviço também falha, mas se uma zona falhar, o serviço continua vivo) - ex.: Amazon EFS e AWS Batch

- **Serviços resilientes zonais**: são executados em uma Zona de Disponibilidade - ex.: Amazon EBS

**SERVIÇOS**
- **Computação:** EC2, Lambda
- **Armazenamento:** S3, EFS
- **Banco de Dados:** RDS, Aurora, DynamoDB

**REGIÕES, ZONAS DE DISPONIBILIDADE E LOCAIS DE BORDA**
- **Região AWS**
    - Área geográfica que consiste em uma ou mais Zonas de Disponibilidade.
- **Zonas de Disponibilidade**
    - Um ou mais *data centers* com energia, rede e conectividade redundantes.
        - Data center: edifício repleto de servidores, SANs, switches, balanceadores de carga, firewalls, etc.
- **Locais de Borda**
    - Serviço global e é um *endpoint* para a AWS usado para armazenar conteúdo em cache.
    - A AWS tem uma rede de entrega de conteúdo (CDN) = **CloudFront**.
    - Se um usuário solicitar determinadas informações, elas permanecerão armazenadas nos locais de borda para que, quando outro usuário solicitar as mesmas, elas serão entregues com maior velocidade.
    - **AWS Accelerator**
        - Melhora o desempenho das aplicações
        - Casos de uso de HTTP para um IP estático
        - *Failover* regional rápido

**MODELOS PARA A NUVEM**
- IaaS
- PaaS
- SaaS
- DaaS

### Serviços de Computação para a AWS
**1. Amazon EC2**
- Serviço computacional padrão da AWS.
- São **máquinas virtuais** e as instâncias são executadas em hosts do EC2 - hardware ou servidores físicos que a AWS gerencia.
- **Virtualização** e **infraestrutura** como serviço.
- Serviço resiliente de Zona de Disponibilidade.
- Têm armazenamento temporário.
- Diferentes tipos: 
    - T3 - uso geral (*default*)
    - R5a - otimizada para memória (+ memória que CPU)
    - C5 - otimizada para computação (+ CPU que memória)
    - F1 - computação acelerada
    - D2 - otimizada para armazenamento
- Imagens de Máquina da Amazon (AMI) podem ser criadas para uma instância.
    - **Golden AMI** - AMI que contém patches de segurança, software, configuração e agentes de software.

**2. Amazon Elastic Container Service (ECS)**
- Serviço que aceita contêineres com instruções sobre onde e como executá-los.
- Serviço de orquestração de contêineres comandado pela AWS.
- A diferença é que o ECS utiliza o SO do host para executar, os contêineres funcionam como **processos**.

- Há também o Amazon Kubernetes Service (AKS), que permite executar Kubernetes com tecnologia AWS em instâncias EC2.

**3. AWS Lambda**
- **Função** como serviço.
- Aceita funções.
- Orientado por eventos.
- *Serverless*.

---
### Serviços de Banco de Dados para a AWS

**1. Amazon Relational Database Service (RDS)**
- Banco de Dados como serviço.
- Suporte para:
    - MySQL
    - MariaDB
    - PostgreSQL
    - Oracle
    - Microsoft SQL Server
    - Amazon Aurora
- RDS utiliza **replicação síncrona** para outra Zona de Disponibilidade, garantindo alta disponibilidade e evitando falhas.
- **Réplica para leitura** oferece maior rapidez nas consultas (read-only) com replicação **assíncrona**.

**2. Amazon Aurora**
- Serviço de **banco de dados relacional**.
- Apresenta melhorias em comparação ao RDS:
    - Usa uma arquitetura baseada em **clusters**.
    - Réplicas de leitura melhoram a disponibilidade e otimizam as operações de leitura.
    - Melhor desempenho devido ao uso do cluster.
- Compatível com:
    - MySQL
    - PostgreSQL

**3. Amazon DynamoDB**
- Banco de Dados NoSQL.
- Localizado na zona pública da AWS.
- AWS gerencia o DynamoDB para o usuário.
- Capaz de lidar tanto com **dados simples de chave-valor** quanto com **dados estruturados**.

---

**Bancos de Dados Armazenados em Memória**

Servem para melhorar a performance e a escalabilidade das aplicações, proporcionando tempos de resposta extremamente rápidos e reduzindo a carga sobre os bancos de dados principais.

**3. Amazon ElastiCache**
- Serviço de cache em memória gerenciado, ideal para aplicações que exigem alto desempenho em leituras.
- Suporte para:
    - Redis
    - Memcached
- Comumente utilizado para **armazenamento de estados de sessão** e acelerar o acesso a dados frequentemente solicitados, reduzindo a carga em bancos de dados tradicionais.

**4. Amazon DynamoDB Accelerator (DAX)**
- Cache em memória gerenciado específico para o DynamoDB, projetado para melhorar a velocidade de leitura.
- Fornece acesso em **milissegundos**, ideal para aplicações que exigem baixa latência.
- Suporta **leituras eventualmente consistentes**, o que permite uma performance ainda mais rápida em cenários onde a consistência imediata não é essencial.

---

**5. Amazon Redshift**
- Solução de *data warehousing* na escala de petabytes.
- Baseado em coluna.
- Usado para **análise de armazenamento de dados**.
- Ótimos para consultas.
- Baseado em PostgreSQL.
- Usa arquitetura de cluster.
- Baixa e faz upload no Amazon S3.

**Migração de Banco de Dados**
- **AWS Snowfamily**
    - **AWS Snowcone:** menor e mais portátil, coleta de dados em locais remotos ou com conectividade limitada, até 8 TB de armazenamento.
    - **AWS Snowball:** tamanho médio, disponível em duas versões: Snowball Edge Storage Optimized e Snowball Edge Compute Optimized, para transferências de dados de até petabytes, recursos de computação para processar dados localmente.
    - **AWS Snowmobile:** contêiner de dados em escala de exabytes, migrações massivas de dados, ideal para empresas que precisam mover grandes volumes de dados para a AWS rapidamente e de maneira segura.
- **AWS Database Migration Service (DMS)**: migração de dados e conversão de esquema => aumentar ou diminuir recursos com POUCO TEMPO de inatividade.
- **AWS Schema Conversion Tool (SCT)**: ajudar na transformação entre diferentes mecanismos de banco de dados para a migração => mover dados entre diferentes mecanismos de BD.
- **AWS DataSync**: facilita e agiliza a movimentação de grandes quantidades de dados on-line entre o armazemamento on-premises e Amazon S3, Amazon EFS...

---

### Recursos de Rede da AWS
**Virtual Private Cloud (VPC)**
- Serviço que usamos para criar **redes privadas** na AWS.
- Ajuda a controlar o acesso aos recursos.
- É o seu próprio data center na nuvem.
- Oferece diferentes camadas de segurança, listas de controle de acesso de rede e grupos de segurança.
- VPC fica em uma conta e em uma região específica (resiliência entre zonas).
- Por padrão: isolada e privada
- Cada VPC tem um roteador de VPC altamente disponível.
- Só pode ter UM Gateway.
- Tipos:
    - **VPC-padrão**
        - Pode possuir apenas uma por região.
        - Criada pela AWS ao criar a conta.
        - AWS define a configuração.
    - **VPCs Personalizadas**
        - Configuradas pelo usuário conforme necessidade.
    
**AWS VPN**
- Pode-se também criar a própria rede privada virtual (VPN) entre o ambiente on-premises e a Amazon VPC (modelo híbrido).
- Utiliza-se a AWS como extensão do ambiente on-premises.
- É um serviço da AWS que permite configurar uma VPN de hardware entre a Amazon VPC e ambientes on-premises.

**AWS Direct Connect**
- É uma **conexão física dedicada** entre uma rede on-premises e a AWS.
- Conexão física ou cruzada entre um roteador e um roteador da AWS.

**Amazon Route 53**
- Produto de DNS gerenciado da AWS.
- Permite:
    - Registrar domínios.
    - Hospedar zonas em servidores de nomes gerenciados.
- É um **serviço global** replicado entre as zonas (resiliente globalmente).

---

### Serviços de Armazenamento da AWS
- Opções de Armazenamento na AWS
    - Objetos
    - Arquivo
    - Bloco

**ARMAZENAMENTO DE OBJETOS**

**Amazon S3**
- Serviço resiliente global.
- Serviço público.
- Quantidade **ilimitada** de dados.
- Podemos criar ***buckets*** e **adicionar objetos a eles**.
    - Armazenam objetos como um contêiner.
- O bucket deve ter um nome globalmente exclusivo.


**ARMAZENAMENTO DE ARQUIVOS**

**Amazon Elastic File System (EFS)**
- Sistema de arquivos compartilhado para Linux (não pode ser utilizado para Windows).
- Pode ser utilizado por várias instâncias EC2 (Linux) que desejam acessar os mesmos arquivos.
    - Os arquivos estão na mesma VPC, mas não na mesma instância EC2, porém todos têm acesso a eles.
- Palavra-chave: LINUX.

**Amazon FSx**
- Servidor de arquivos similar ao EFS.
- Para Windows.

**ARMAZENAMENTO EM BLOCO**

**Amazon Elastic Block Store (EBS)**
- Exemplo: empresas que possuem um BD que necessita de acesso com baixa latência para cada host.
- Altamente resiliente.

---
**AWS Storage Gateway**
- Serviço que nos permite conectar nosso armazenamento de data center on-premises a um serviço de armazenamento da AWS e ajuda a migrar parte ou toda a sua plataforma de armazenamento para a AWS.

---

### Serviços de Inteligência Artificial e Machine Learning

**IA**
- **Amazon Translate:** traduzir ou localizar conteúdo de texto
- **Amazon Polly:** conversão de **texto em fala**.
- **Amazon Lex:** criar bots de bate-papo conversacional.
- **Amazon Comprehend**
- **Amazon Forecast**
- **Amazon CodeGuru**
- **Amazon Rekognition:** adicionar análise de imagens e vídeos às suas aplicações.

**Machine Learning**
- **AWS SageMaker:** permite que desenvolvedores e cientistas de dados criem, treinem e implantem modelos de *machine learning* de forma rápida e fácil em qualquer escala.
- **Amazon CodeWhisperer:** gerador de código baseado em *machine learning* que fornece recomendações de código em tempo real e também pode identificar problemas de segurança no código após verificação.

---

### Serviços de Análise da AWS

**Amazon Athena**
- Serviço de consultas interativas.
- Analise e consulte dados de armazenados no Amazon S3.
- Ótimo para gerar relatórios, consultar logs...

**Amazon Macie**
- Serviço de segurança da AWS.
- Descubra, classifique e proteja dados armazenados no Amazon S3.
- PII

**Amazon Redshift**
- Mecanismo de banco de dados baseado em colunas para cargas de trabalho analíticas.
- Processamento analítico on-line (OLAP).

**Amazon Kinesis**
- Processa e analisa os dados de streaming.
- Tempo real.

**AWS Glue**
- Serviço de integração de dados sem servidor para descobrir, preparar, mover e integrar dados.

**AWS QuickSight**
- Serviço de *business intelligence*.
- Fornece informações para todos em sua organização.

**Amazon OpenSearch**
- Banco de dados e mecanismo de pesquisa.

**Amazon EMR**
- Serviço que ajuda a executar *frameworks* de *Big Data* para processar **vastas quantidades de dados**.

---

### Outros serviços da AWS

**Serviços de Integração de Aplicações**
- **Amazon EventBridge**
- **Amazon Simple Notification Service (Amazon SNS):** sistema de mensagens de sub-rede pública (coordena o envio e entrega de mensagens).
- **Amazon Simple Queue Service (SQS):** sistema de enfileiramento que fornece filas de mensagens totalmente gerenciadas e altamente disponíveis.
- **Amazon CloudWatch**
- **Amazon EC2 Auto Scaling**

**Serviços de Aplicações Empresariais**
- **Amazon Connect**
- **Amazon Simple Email Service (SES)**

**Serviços de Envolvimento de Clientes**
- **AWS Activate:** fornece às startups qualificadas ferramentas, recursos e conteúdo gratuitos projetados para simplificar cada etapa da jornada de inicialização.
- **AWS IQ:** conecta você a especialistas certificados pela AWS para obter ajuda prática em seus projetos AWS.
- **AWS Managed Services (AMS):** gerenciamento de operações de infraestrutura para AWS e é um serviço corporativo que fornece gerenciamento contínuo de sua infraestrutura da AWS.
- **AWS Support:** oferece vários planos que disponibilizam acesso a ferramentas e conhecimento que respaldam o sucesso e a integridade operacional das suas soluções da AWS.

**Serviços de Desenvolvedor**
- **AWS AppConfig**
- **AWS CodePipeline**
- **AWS CodeCommit**
- **AWS CodeArtifact**
- **AWS CodeBuild**
- **AWS CodeStar**
- **AWS X-Ray**
- **AWS Cloud9**
- **AWS Cloud Shell**

**Serviços Computacionais de Usuário Final**
- **Amazon AppStream 2.0:** serviço de streaming de aplicações totalmente gerenciado que oferece aos usuários acesso instantâneo às suas aplicações desktop de qualquer lugar.
- **Amazon WorkSpaces:** ajuda a provisionar desktops virtuais do Microsoft Windows, Amazon Linux ou Ubuntu Linux baseado na nuvem para os usuários.
- **Amazon WorkSpaces Web:** serviço sob demanda totalmente gerenciado e baseado em Linux projetado para facilitar o acesso seguro do navegador a sites internos e aplicações de software como serviço.

**Serviços da Web e Móveis de Front-end**
- **AWS Amplify:** permite que desenvolvedores de serviços da web e móveis de front-end criem, enviem e hospedem facilmente aplicações de pilha completa na AWS.
- **AWS AppSync:** fornece uma interface GraphSQL robusta e dimensionável para desenvolvedores de aplicações combinarem dados de várias fontes.

**Serviços de IoT**
- **AWS IoT Core**
- **AWS IoT Greengrass**

---
## Domínio 4: Cobrança, Preços e Suporte
### Comparar os modelos de preços da AWS
- **Otimização de Custos**: capacidade de executar sistemas para entregar valor comercial pelo menor preço possível.
    - Serviços de Otimização de Custos:
        - **AWS Budget**
        - **AWS Cost Explorer**

- **Modelos de preços**
    - **Instâncias reservadas**: vêm com compromisso de 1 ou 3 anos (menor preço).
    - **Instâncias sob demanda**: usa quando necessário (apps que não toleram interrupções). 
    - **Instâncias spot**: modelo mais barato (ótimas para aplicações flexíveis, que podem ter suporte para interrupções)
    - **Instâncias dedicadas**
    - **Reservas de capacidade**
    - **Hosts dedicados**

### Ferramentas de gerenciamento de custos da AWS
Necessárias para compreender o que está sendo utilizado e gerando gastos na AWS.

CloudWatch pode ser configurado para ativar alarmes
- **AWS Cost Explorer**
- **AWS relatório de custo e uso**

### ❓ Perguntas de Orientação
**1. Que princípio de design de arquitetura da nuvem AWS oferece suporte para distribuição de cargas de trabalho em várias Zonas de Disponibilidade?**

<blockquote>
a. Implementar automação - <em>incorreta</em><br>  
b. Design para agilidade - <em>incorreta, não está relacionada à distribuição em várias zonas</em><br>  
<strong>c. Design à prova de falhas</strong> - <em><strong>CORRETA</strong></em><br>  
d. Implementar a elasticidade - <em>incorreta, pois elasticidade é a capacidade de utilizar mais ou menos recursos conforme a demanda</em>  
</blockquote>

**2. Um administrador de sistema está analisando um grupo de servidores encontrado durante uma descoberta de portfólio. Todos os servidores estão migrando para a AWS. Os servidores não têm proprietário atual. Há pouquíssimo tráfego para os servidores.**

**Qual estratégia de migração o administrador do sistema deve sugerir para esses servidores?**

<blockquote>
a. Redefinir hospedagem - <em>incorreta, pois significa apenas mudar a hospedagem sem modificar o servidor, nesse caso podem ser desligados para evitar gastos desnecessários (pois são pouco usados)</em><br>  
b. Redefinir plataforma - <em>incorreta, pois significa mover para AWS com modificações para otimizá-lo (deve-se desligar)</em><br>  
c. Reter - <em>incorreta, significa mantê-lo no contexto atual</em><br>  
<strong>d. Retirar</strong> - <em><strong>CORRETA</strong> (desligar pois não são mais utilizados)</em>  
</blockquote>

**3. Qual tarefa é responsabilidade do cliente de acordo com o Modelo de Responsabilidade Compartilhada da AWS?**
<blockquote>
a. Instalar patches nas instâncias de bancos de dados do Amazon RDS - <em>incorreta, a AWS gerencia patches para o Amazon RDS</em><br>  
b. Aplicar patches no sistema operacional das instâncias de banco de dados do Amazon RDS - <em>incorreta, não é responsável, a AWS fornece</em><br>  
<strong>c. Determinar quais serviços têm acesso a uma tabela do Amazon DynamoDB</strong> - <em><strong>CORRETA</strong></em><br>  
d. Aplicar patches nos dispositivos de rede da Amazon VPC - <em>incorreta, AWS instala os patches </em>  
</blockquote>

**4. Uma empresa tem um servidor de aplicações que executa em uma instância do Amazon EC2. O servidor de aplicações precisa acessar os conteúdos em um bucket privado do Amazon S3.**

**Qual é a abordagem recomendada para atender a esse requisito?**

<blockquote>
<strong>a. Criar um perfil do IAM com as permissões adequadas. Associar o perfil à instância do EC2 </strong> - <em><strong>CORRETA</strong></em><br>  
b. Configurar uma conexão de peering de VPC para permitir a comunicação privada entre a instância do EC2 e o bucket do S3 - <em>incorreta, não pode conectar um S3 e uma VPC</em><br>  
c. Criar uma chave de acesso compartilhada. Configurar a instância do EC2 para usar a chave codificada - <em>incorreta, não é uma boa prática, pode expor o código da aplicação</em><br>  
d. Configurar a aplicação para ler uma chave de acesso de uma fonte protegida - <em>incorreta, é mais recomendado utilizar usuários IAM (temporários, portanto reduz o risco)</em>  
</blockquote>

**5. Uma empresa deseja uma conexão privada dedicada para a nuvem AWS de suas operações on-premises.**

**Qual é serviço ou recurso da AWS fornecerá essa conexão?**

<blockquote>
a. AWS VPN - <em>incorreta</em><br>  
b. AWS PrivateLink - <em>incorreta</em><br>  
c. Endpoint de VPC - <em>incorreta</em><br>  
<strong>d. AWS Direct Connect </strong> - <em><strong>CORRETA</strong></em>  
</blockquote>

**6. Qual aspecto da infraestrutura da AWS fornece implantação global de computação e armazenamento?**

<blockquote>
a. Várias Zonas de Disponibilidade em uma Região AWS - <em>incorreta</em><br>  
<strong>b. Várias Regiões AWS</strong> - <em><strong>CORRETA</strong></em><br>  
c. Tags - <em>incorreta</em><br>  
d. Resource Groups - <em>incorreta</em>  
</blockquote>

**7. Uma empresa deve atender aos requisitos de conformidade e licenciamento de software que afirmam que uma carga de trabalho deve ser hospedada em um servidor físico.**

**Qual opção de preço da instância do Amazon EC2 atende a esses requisitos?**

<blockquote>
<strong>a. Hosts dedicados</strong> - <em><strong>CORRETA</strong></em><br>  
b. Instâncias dedicadas - <em>incorreta, pois são instâncias do EC2 executadas em uma VPC em hardware dedicado a um único cliente. Outras instâncias podem ser hospedadas no mesmo hardware.</em><br>  
c. Instâncias spot - <em>incorreta, pois com elas você pode aproveitar a capacidade não utilizada do EC2 na nuvem AWS.</em><br>  
d. Instâncias reservadas - <em>incorreta, pois oferecem economia significativa nos custos de EC2 em comparação com a definição de preço de instância sob demanda. Mas não são hospedadas em servidor público.</em>  
</blockquote>

**8. Qual opção é uma vantagem da cobrança consolidada da AWS?**

<blockquote>
<strong>a. Qualificação de preço por volume</strong> - <em><strong>CORRETA</strong></em><br>  
b. Permissões de acesso compartilhado - <em>incorreta</em><br>  
c. Várias faturas de cada conta - <em>incorreta, pois o objetivo da cobrança consolidada é ter uma fatura para várias contas.</em><br>  
d. Eliminação da necessidade de marcar recursos - <em>incorreta</em>  
</blockquote>

---

### DICAS para a PROVA
- ***Scaling vertical*** => tamanho maior
- ***Scaling horizontal*** => adicionar instâncias
- **Elasticidade** => usar automação com scaling horizontal.
- CONCENTRAR EM SERVIÇOS E DESIGNS, NÃO EM HARDWARE E SERVIDORES.
- Estudar **maneiras de proteger o root-user** (autenticação multifator, bloquear com segurança, credenciais, alternar chaves de acesso e a senha)
- Entender como funciona o **IAM**.
- Autoscaling fornece elasticidade

---

## JOGO AWS
### Amazon RDS
- Serviço de Banco de Dados **relacional**.
- Otimizado para memória, performance e entrada/saída.
- Paga apenas pelos recursos que são utilizados.
- Pode realizar *backups* no BD. 
    - *Retention period*: tempo que se deseja guardar os backups.
- Pode-se realizar deploy em mais de uma Zona de Disponibilidade => dados replicados de forma síncrona => maior disponibilidade.
- Para **aumentar performance:** deploy uma réplica apenas para leitura.
- **Três templates:**
    - **Production**
    - **Dev/Test**
    - **Free tier**

### Amazon Elastic File System (EFS)
- Serverless "set-and-forget" solution.
- Utilizada para **compartilhar arquivos** sem necessidade de gerenciar armazenamento.
- Provê armazenamento em escala petabyte que aumenta e/ou diminui conforme a adição/remoção de arquivos.
- Percentual de durabilidade: 99.99999999 => basicamente impossível de se perder os dados.

### Amazon DynamoDB
- Banco de Dados NoSQL
- Possui uma latência de um único dígito de milissegundos.
- Suporta petabytes de dados.

### Computação em Nuvem 
É a disponibilidade sob demanda de recursos computacionais (como armazenamento e infraestrutura), como serviços pela Internet.
- *pay as you go*

### Auto Scaling group
- Pode-se delimitar o número de instâncias a serem criadas para determinada demanda.
- Pode-se **agendar** essas execuções e encerramentos de instâncias.

___

### ↩️ [Retornar ao início](../README.md)