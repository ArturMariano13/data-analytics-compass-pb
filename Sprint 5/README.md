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
### Amazon S3
- Serviço de armazenamento.
- Qualquer tipo de arquivo e qualquer metadado que descreve aquele arquivo é chamado de **objeto**.
- Objetos são armazenados em containers S3, chamados **buckets**.


___
## Curso Preparatório para o Exame
### Estrutura da prova
- **Domínio 1** - Conceitos da nuvem: 24%
- **Domínio 2** - Segurança e conformidade: 30% 
- **Domínio 3** - Tecnologia e serviços da nuvem: 34%
- **Domínio 4** - Cobrança, preços e suporte: 12%

### Domínio 1: Conceitos de Nuvem
- **O que é computação em nuvem?**
1. Autoatendimento sob demanda
2. Acesso à rede
3. Agrupamento de recursos
4. Elasticidade
5. Uso de recursos monitorado e cobrado

- **Vantagens**
    - **Alta disponiblidade:** tempo mínimo de inatividade.
    - **Tolerância a falhas:** projetar para tempo de inatividade zero.
    - **Recuperação de desastres:** projetar sistemas para operar durante um desastre.

- **Princípios de criação**
    - Parar de tentar adivinhar a capacidade
    - Testar sistemas em escala de produção
    - Automatizar a arquitetura
    - Permitir alterações evolucionárias

**PILARES DO WELL ARCHITECTED FRAMEWORK**
1. EXCELÊNCIA OPERACIONAL
    - Executar operações como código
    - Fazer alterações frequentes
    - Prever falhas
    - Aprender com todas as falhas operacionais

2. SEGURANÇA
    - Implementar uma base de identidade sólida
    - Manter a rastreabilidade
    - Aplicar segurança em todas as camadas
    - Proteger dados em trânsito e ociosos

3. CONFIABILIDADE
    - Recuperar-se automaticamente de falhas
    - Testar os procedimentos de recupração
    - Dimensionar horizontalmente para aumentar a disponibilidade agregada da carga de trabalho
    - Parar de tentar adivinhar a capacidade
    - Gerenciar alterações na automação

4. EFICIÊNCIA DE DESEMPENHO
    - Democratizar tecnologias avançadas
    - Ter alcance global em minutos
    - Usar arquiteturas sem servidor (*serverless*)
    - Experimentar com mais frequência
    - Considerar a afinidade mecânica

5. OTIMIZAÇÃO DE CUSTOS
    - Capacidade de executar sistemas para entregar valor comercial pelo menor valor possível.

6. SUSTENTABILIDADE
    - Compreensão do seu impacto
    - Estabelecer metas de sustentabilidade
    - Usar serviços gerenciados
    

### DICAS para a PROVA
- ***Scaling vertical*** => tamanho maior
- ***Scaling horizontal*** => adicionar instâncias
- **Elasticidade** => usar automação com scaling horizontal.




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