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

## Domínio 3: Tecnologia e Serviços da Nuvem
### Métodos de implantação e operação na AWS


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
c. Determinar quais serviços têm acesso a uma tabela do Amazon DynamoDB - <em><strong>CORRETA</strong></em><br>  
<strong>d. Aplicar patches nos dispositivos de rede da Amazon VPC </strong> - <em>incorreta, AWS instala os patches </em>  
</blockquote>

**4. Uma empresa tem um servidor de aplicações que executa em uma instância do Amazon EC2. O servidor de aplicações precisa acessar os conteúdos em um bucket privado do Amazon S3.**

**Qual é a abordagem recomendada para atender a esse requisito?**

<blockquote>
a. Criar um perfil do IAM com as permissões adequadas. Associar o perfil à instância do EC2 - <em><strong>CORRETA</strong></em><br>  
b. Configurar uma conexão de peering de VPC para permitir a comunicação privada entre a instância do EC2 e o bucket do S3 - <em>incorreta, não pode conectar um S3 e uma VPC</em><br>  
c. Criar uma chave de acesso compartilhada. Configurar a instância do EC2 para usar a chave codificada - <em>incorreta, não é uma boa prática, pode expor o código da aplicação</em><br>  
<strong>d. Configurar a aplicação para ler uma chave de acesso de uma fonte protegida </strong> - <em>incorreta, é mais recomendado utilizar usuários IAM (temporários, portanto reduz o risco)</em>  
</blockquote>



### DICAS para a PROVA
- ***Scaling vertical*** => tamanho maior
- ***Scaling horizontal*** => adicionar instâncias
- **Elasticidade** => usar automação com scaling horizontal.
- CONCENTRAR EM SERVIÇOS E DESIGNS, NÃO EM HARDWARE E SERVIDORES.
- Estudar **maneiras de proteger o root-user** (autenticação multifator, bloquear com segurança, credenciais, alternar chaves de acesso e a senha)
- Entender como funciona o **IAM**.




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


## AWS Pratictioner Essentials
### Computação em Nuvem 
É a disponibilidade sob demanda de recursos computacionais (como armazenamento e infraestrutura), como serviços pela Internet.
- *pay as you go*

### Auto Scaling group
- Pode-se delimitar o número de instâncias a serem criadas para determinada demanda.
- Pode-se **agendar** essas execuções e encerramentos de instâncias.




___

### ↩️ [Retornar ao início](../README.md)