# 🧩 Desafio da Sprint 10
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

___

## 📝 Enunciado
O desafio da Sprint 10 é uma continuação do desafio iniciado na Sprint 6, sendo a quinta e última entrega do desafio final.

- **Consumo de dados**: momento de extrair *insights*, apresentando-os por meio do AWS QuickSight.

### Afazeres
Extrair insights dos dados ingeridos e processados nas Sprints anteriores. Isso deve ser realizado por meio da ferramenta de visualização de dados QuickSight.

- Criar um *dashboard* no AWS QuickSight, utilizando como única e exclusiva fonte de dados as tabelas da camada *Refined* do data lake.


--- 

## Resolução

### 1. Criação de Dataset no QuickSight

Primeiramente, criei um dataset (dados-refinados) no QuickSight para poder acessar os dados em minha análise.

![Imagem criação dataset QuickSight](../evidencias/1-criacaoDataset.png)

Dessa forma, selecionei como fonte de dados o Amazon Athena, mais especificamente a tabela "fato_filme", que é a tabela central da modelagem dos meus dados (tabela fato). Essa tabela, juntamente às tabelas de dimensões, foi criada pelo *crawler* que buscou os dados salvos no S3 camada *Refined*.

![Imagem seleção tabela fato_filme](../evidencias/1.1-escolhaTabelaPrincipal.png)



___

### ↩️ [Retornar ao início](../../README.md)