# SPRINT 2 - Linguagem SQL para análise de dados e introdução AWS

## Certificados
Para maiores informações sobre os certificados, siga o link: [certificados](certificados)

## Desafio
Para maiores informações sobre o desafio final, siga o link: [desafio](desafio)

## Evidências
Para maiores informações sobre as evidências, siga o link: [evidências](evidencias)

## Exercícios
Para maiores informações sobre os exercícios, siga o link: [exercícios](exercicios)


## Resumo dos estudos

### Linguagem SQL para análise de dados
#### 🛠 Instalação
- Fazer download do ***PostgreSQL*** e do ***PGAdmin***.
- Criar *Schema* sales no *database* postgres.

#### 📚 Comandos Básicos
`SELECT`
- Usado para selecionar colunas de tabelas;
- Quando selecionar mais de uma coluna, elas devem ser separadas por vírgula sem conter vírgula antes do comando FROM;
- Pode-se utilizar o asterisco (*) para selecionar todas as colunas da tabela.

**Sintaxe:** `SELECT coluna_1, coluna_2, coluna_3 FROM schema_1.tabela_1` 

`DISTINCT`
- Usado para remover linhas duplicadas e mostrar apenas linhas distintas;
- Muito usado na etapa de exploração das bases; 
- Caso mais de uma coluna seja selecionada, o comando SELECT DISTINCT irá retornar todas as combinações distintas.

**Sintaxe:** `SELECT DISTINCT coluna_1, coluna_2, coluna_3 FROM schema_1.tabela_1`

`WHERE`
- Usado para filtrar linhas de acordo com uma condição;
- No PostgreSQL são utilizadas **aspas simples** para delimitar *strings*;
- *string* = sequência de caracteres = texto;
- Pode-se combinar mais de uma condição utilizando os operadores lógicos (*or*, *and*);
- No PostgreSQL as datas são escritas no formato 'YYYY-MM-DD' ou 'YYYYMMDD'.

**Sintaxe:** `SELECT coluna_1, coluna_2, coluna_3 FROM schema_1.tabela_1 WHERE condicao`

`ORDER BY`
- Usado para ordenar a seleção de acordo com uma regra definida;
- Por padrão o comando ordena na ordem crescente. Para mudar para a ordem decrescente, basta usar o comando DESC;
- No caso de *strings* a ordenação será seguirá a ordem alfabética.

**Sintaxe:** `SELECT coluna_1, coluna_2, coluna_3 FROM schema_1.tabela_1 WHERE condicao=true ORDER BY coluna_1`

`LIMIT`
- Usado para limitar o nº de linhas da consulta;
- Muito utilizado na etapa de exploração dos dados (com bases de dados muito grandes);
- Muito utilizado em conjunto com o comando ORDER BY quando o que importa são os TOP N. Exemplo: "N pagamentos mais recentes", "N produtos mais caros".

**Sintaxe:** `SELECT coluna_1, coluna_2, coluna_3 FROM schema_1.tabela_1 WHERE condicao=true ORDER BY coluna_1 LIMIT N`

#### 🔢 Operadores
##### Operadores Aritméticos
Servem para executar operações matemáticas.
- Muito utilizado para criar colunas calculadas;
- Alias (pseudônimos) são muito utilizados para dar nome as colunas calculadas (boa prática);
- Para criar pseudônimos que contém espaços no nome são utilizadas aspas duplas (ex: `... AS "nome completo ..."`);
- No caso de strings o operador de adição (||) irá concatenar as strings.

**Tipos**
- `+`
- `-`
- `*`
- `/`
- `^`
- `%`
- `||` - não é operador aritmético (faz concatenação de *strings*).
    - Exemplo: `SELECT first_name || ' ' || last_name AS nome_completo FROM schema_1.tabela_1` - irá mostrar o nome e sobrenome das pessoas

OBS.: `current_date` é uma função que retorna a data atual.
- Para dar nome à coluna criada, basta utilizar o *AS*. Exemplo: `SELECT birth_date, (current_date - birth_date) / 365 AS idade_do_cliente FROM schema_1.tabela_1`.

##### Operadores de Comparação
Servem para comparar dois valores retornando TRUE ou FALSE.
- Muito utilizado em conjunto com a função WHERE para filtrar linhas de uma seleção;
- Utilizados para criar colunas *Flag* que retornem TRUE ou FALSE.

**Tipos**
- `=`
- `>`
- `<`
- `>=`
- `<=`
- `<>` - "diferente de"

- Exemplo: `SELECT first_name, professional_status, (professional_status = 'clt') AS cliente_clt FROM schema_1.tabela_1`
- irá retornar TRUE para os profissionais que forem clt e FALSE para os que não forem.

##### Operadores Lógicos
Usados para unir expressões simples em uma expressão composta.
- `AND`: Verifica se duas comparações são simultaneamente verdadeiras;
    - Exemplo: `SELECT * FROM schema_1.tabela_1 WHERE price >= 100000 AND price <= 200000` - pode-se substituir por *beetwen*.
- `OR`: Verifica se uma ou outra comparação é verdadeiras;
    - Exemplo: `SELECT * FROM schema_1.tabela_1 WHERE price < 100000 OR price > 200000` - pode-se substituir por *NOT BETWEEN*
- `BETWEEN`: Verifica quais valores estão dentro do range definido;
    - Exemplo: `SELECT * FROM schema_1.tabela_1 WHERE price BETWEEN 100000 AND 200000`
- `IN`: Funciona como multiplos ORs;
    - Exemplo: `SELECT * FROM schema_1.tabela_1 WHERE brand IN ('brand_1', 'brand_2', 'brand_3')`
- `LIKE` e `ILIKE`: Comparam textos e são sempre utilizados em conjunto com o operador %, que funciona como um coringa, indicando que qualquer texto pode aparecer no lugar do campo;
    - Exemplo: `SELECT first_name FROM schema_1.tabela_1 WHERE first_name LIKE 'ARTUR%'` - o coringa poderia estar em qualquer outro lugar da palavra (começar com ARTUR, terminar com ARTUR...);
    - `ILIKE` ignora se o campo tem letras maiúsculas ou minúsculas na comparação.
- `IS NULL`: Verifica se o campo é nulo.
    - Exemplo: `SELECT * FROM schema_1.tabela_1 WHERE paid_date IS NULL` - retorna clientes em que as datas de pagamento nulas.

#### 🧮 Funções Agregadas
##### Funções de Agregação
Servem para executar operações aritmética nos registros de uma coluna.

**TIPOS**
- **`COUNT()`:** retorna o número de valores (não nulos) em um conjunto.
    - **Exemplo:** 
    ```sql
    SELECT COUNT(coluna)
    FROM tabela;
    ```
- **`SUM()`:** retorna a soma dos valores de uma coluna numérica.
    - **Exemplo:**
    ```sql
    SELECT SUM(coluna_numerica)
    FROM tabela;
    ```
- **`MIN()`:** retorna o menor valor de uma coluna.
    - **Exemplo:** 
    ```sql
    SELECT MIN(coluna)
    FROM tabela;
    ```
- **`MAX()`:** retorna o maior valor de uma coluna.
    - **Exemplo:**
    ```sql
    SELECT MAX(coluna)
    FROM tabela;
    ````
- **`AVG()`:** retorna a média dos valores de uma coluna numérica.
    - **Exemplo:**
    ```sql
    SELECT AVG(coluna_numerica)
    FROM tabela;
    ```
- Funções agregadas não computam células vazias (NULL) como zero;
- Na função COUNT() pode-se utilizar o asterisco (*) para contar os registros;
- Essas funções são frequentemente usadas em consultas SQL para realizar cálculos e análises de dados;
- COUNT(DISTINCT) irá contar apenas os valores exclusivos.

🗂 `GROUP BY`
- Serve para agrupar registros semelhantes de uma coluna;
- A cláusula `GROUP BY` é usada em conjunto com funções agregadas (`COUNT()`, `SUM()`, `MIN()`, `MAX()`, `AVG()`) para agrupar os resultados de uma consulta SQL por uma ou mais colunas;
- Pode-se referenciar a coluna a ser agrupada pela sua posição ordinal; 
- Ex: GROUP BY 1,2,3 irá agrupar pelas 3 primeiras colunas da tabela; 
- O GROUP BY sozinho funciona como um DISTINCT, eliminando linhas duplicadas.
- O __exemplo abaixo__ agrupa os registros da tabela empregados pelo campo departamento e conta o número de empregados em cada departamento.
    ```sql
    SELECT departamento, COUNT(empregado_id) AS numero_de_empregados
    FROM empregados
    GROUP BY departamento;
    ```

🎛 `HAVING`
Serve para filtrar linhas da seleção por uma coluna agrupada.
- Tem a mesma função do WHERE mas pode ser usado para filtrar os resultados das funções agregadas enquanto o WHERE possui essa limitação;
- A função HAVING também pode filtrar colunas não agregadas.
- O __exemplo abaixo__ agrupa os registros da tabela empregados pelo campo departamento, conta o número de empregados em cada departamento e retorna apenas os departamentos com mais de 10 empregados.
```sql
SELECT departamento, COUNT(empregado_id) AS numero_de_empregados
FROM empregados
GROUP BY departamento
HAVING COUNT(empregado_id) > 10;
```
- **Comparação com WHERE**
    ```sql
    -- Usando WHERE
    SELECT departamento, salario
    FROM empregados
    WHERE salario > 50000;

    -- Usando HAVING
    SELECT departamento, AVG(salario) AS media_salarial
    FROM empregados
    GROUP BY departamento
    HAVING AVG(salario) > 50000;
    ```
    - __Explicação:__ o primeiro exemplo usa WHERE para filtrar empregados com salário maior que 50.000 antes de qualquer agregação. O segundo exemplo usa HAVING para filtrar departamentos onde a média salarial é maior que 50.000 após a agregação.


🔗 `JOINS`
- Servem para combinar colunas de uma ou mais tabelas.
- **Sintaxe:**
    ``` sql
    -- A sintaxe é a mesma para todos os tipos de join
    SELECT tabela1.coluna, tabela2.coluna
    FROM tabela1
    LEFT JOIN tabela2
    ON tabela1.coluna_comum = tabela2.coluna_comum;
    ```
##### Tipos de JOIN
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLit1uPMgSEZLuA3W3hMJ_0h8CVirELz3dgw&s" alt="Demonstração do Kernel do Linux" width="400">
</p>

- `LEFT JOIN`: retorna todas as linhas da tabela à esquerda, e as linhas correspondentes da tabela à direita. Se não houver correspondência, os resultados da tabela à direita serão NULL.
- `RIGHT JOIN`: retorna todas as linhas da tabela à direita, e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, os resultados da tabela à esquerda serão NULL.
    - A sintaxe é a mesma do left join.
- `INNER JOIN`: retorna apenas as linhas que têm correspondência em ambas as tabelas.
- `FULL JOIN`: retorna todas as linhas quando há correspondência em uma das tabelas. Se não houver correspondência, os resultados serão NULL para a tabela sem correspondência.

🌐 `UNION`
- A cláusula `UNION` é usada para combinar os resultados de duas ou mais consultas `SELECT` em um único conjunto de resultados.
- Por padrão, o `UNION` remove as duplicatas. Para incluir todas as duplicatas, use `UNION ALL`.
    - `UNION ALL` é mais leve, quando se tiver certeza de que as duas tabelas são completamente distintas, optar por ele.
- **Regras**
    - As consultas combinadas devem ter o mesmo número de colunas.
    - As colunas correspondentes nas consultas devem ter tipos de dados compatíveis.
    - A ordem das colunas deve ser a mesma em todas as consultas.
- **Exemplo:**
    ```sql
    SELECT nome, cidade FROM clientes_2023
    UNION
    SELECT nome, cidade FROM clientes_2024;
    ```

📦 **SUBQUERIES**
Servem para consultar dados de outras consultas.
- Para que as subqueries no WHERE e no SELECT funcionem, elas devem retornar apenas um único valor;
- Não é recomendado utilizar subqueries diretamente dentro do FROM pois isso dificulta a legibilidade da query. 
##### Tipos de Subquery
1. *Subquery* no `WHERE`
- Exemplo: Informar qual é o produto mais barato da tabela "products".
``` sql
SELECT *
FROM sales.products
WHERE price = (SELECT MIN(price) FROM sales.products)
```
2. *Subquery* com `WITH`
- Exemplo: Calcular a idade média dos clientes por status profissional.
```sql
WITH alguma_tabela as (
    SELECT
        professional_status,
        (current_date - birth_date)/365 AS idade
    FROM sales.customers
)
SELECT 
    professional_status,
    AVG(idade) AS idade_media
FROM alguma_tabela
GROUP BY professional_status
``` 
- A tabela criada com *with* possui todos os status dos trabalhadores e os seus respectivos salários.
- A segunda consulta retorna apenas a média dos salários, agrupado por status.

3. *Subquery* no `FROM`
- Exemplo: Calcular a média de idade dos clientes por status profissional.
```sql
SELECT 
    professional_status,
    AVG(idade) AS idade_media
FROM (SELECT
        professional_status,
        (current_date - birth_date)/365 AS idade
    FROM sales.customers) AS alguma_tabela
GROUP BY professional_status
```
- Não muito recomendada, preferível utilizar a cláusula **WITH**.

4. *Subquery* no `SELECT`
- Exemplo: Criar uma coluna que informe o número de visitas acumuladas que a loja recebeu até o momento.
```sql
SELECT
    fun.visit_id,
    fun.visit_page_date,
    sto.store_name,
    (
        SELECT COUNT(*)
        FROM sales.funnel AS fun2
        WHERE fun2.visit_page_date <= fun.visit_page_date
        AND fun2.store_id = fun.store_id
    ) AS visitas_acumuladas
FROM sales.funnel AS fun
LEFT JOIN sales.stores AS sto
    ON fun.store_id = sto.store_id
ORDER BY sto.store_name, fun.visit_page_date
```

#### 🛠 Tratamento de Dados
1. Conversão de Unidades
    - O operador `::` e o `CAST()` são funções utilizadas para converter um dado para a unidade desejada. 
    - O operador `::` é mais "clean", porém, em algumas ocasiões não funciona, sendo necessário utilizar a função `CAST()`.
    1. Operador `::`
        - Exemplo 1: Conversão de texto em data.
        ```sql
        SELECT '2024-06-29' - '2024-07-01' -- INCORRETO

        SELECT '2024-06-29'::date - '2024-07-01'::date 
        ```
        - Exemplo 2: Conversão de texto em número.
        ```sql
        SELECT '100' - '10' -- INCORRETO

        SELECT '100':numeric - '10'::numeric
        ```
        - Exemplo 3: Conversão de número em texto.
        ```sql
        SELECT REPLACE(112122, '1', 'A') -- INCORRETO

        SELECT REPLACE(112122::text, '1', 'A')
        ```
    2. Cast
        - Exemplo 1: conversão de texto em data.
        ```sql
        SELECT CAST('2024-06-29' AS DATE) - CAST('2024-07-01' AS DATE)
        ```

2. Tratamento Geral
    1. `CASE WHEN()`: é o comando utilizado para criar respostas específicas para diferentes condições e é muito utilizado para fazer agrupamento de dados.
        - **Agrupamento de Dados com CASE WHEN**
            - Exemplo: calcular o número de clientes que ganham abaixo de 5k, entre 5k e 10k, entre 10k e 15k e acima de 15k.
            ```sql
            WITH faixa_de_renda AS(
                SELECT
                    income,
                    CASE
                        WHEN income < 5000 then '0-5000'
                        WHEN income >= 5000 and income < 10000 then '5000-10000'
                        WHEN income >= 10000 and income < 15000 then '10000-15000'
                        ELSE '15000+'
                        END AS faixa_renda
            )
            
            SELECT faixa_renda, COUNT(*)
            FROM faixa_de_renda
            GROUP BY faixa_renda
            ```
    2. `COALESCE()` é o comando utilizado para preencher campos nulos com o primeiro valor não nulo de uma sequência de valores.
        - **Tratamento de dados nulos com COALESCE**
            - Exemplo: criar uma coluna chamada populacao_ajustada na tabela temp_tables.regions e preencher com os dados da coluna *population*, mas caso esse campo estiver nulo, preencha com a população média (geral) das cidades do Brasil.
            ```sql
            SELECT 
                *,
                COALESCE(population, (SELECT AVG(population) FROM temp_tables.regions) AS populacao_ajustada)
            FROM temp_tables.regions
            WHERE population IS NULL
            ```
3. Tratamento de Texto
    1. `LOWER()` é utilizado para transformar todo texto em letras minúsculas.
        - Exemplo:
        ```sql
        SELECT LOWER('Artur') = 'artur'
        ```
    2. `UPPER()` é utilizado para transformar todo texto em letras maiúsculas.
        - Exemplo:
        ```sql
        SELECT UPPER('Artur') = 'ARTUR'
        ```
    3. `TRIM()` é utilizado para remover os espaços das extremidades de um texto.
        - Exemplo: 
        ```sql
        SELECT TRIM('Artur Mariano     ') = 'Artur'
        ```
    4. `REPLACE()` é utilizado para substituir uma *string* por outra *string*.   
        - Exemplo: 
        ```sql
        SELECT REPLACE('Arthur Mariano', 'Arthur', 'Artur') = 'Artur Mariano'
        ```

4. Tratamento de Datas
    1. `INTERVAL()`: é utilizado para somar datas na unidade desejada. Caso a unidade não seja informada, o SQL irá entender que a soma foi feita em dias.
    2. `DATE_TRUNC()`: é utilizado para truncar uma data no início do período.
        - Exemplo: calcular quantas visitas ocorreram por mês no site da empresa.
        ```sql
        SELECT 
            DATE_TRUNC('month', visit_page_date)::date AS visit_page_month,
            COUNT(*)
        FROM sales.funnel
        GROUP BY visit_page_month
        ORDER BY visit_page_month DESC
        ```
        - Nesse caso, ele trunca as datas no começo de cada mês (dia 01) e a contagem é feita mês a mês.
    3. `EXTRACT()`: é utilizado para extrair unidades de uma data/timestamp.
        - Exemplo: calcular qual é o dia da semana que mais recebe visitas.
        ```sql
        SELECT 
            EXTRACT('dow' FROM visit_page_date) AS dia_da_semana,
            COUNT(*)
        FROM sales.funnel
        GROUP BY dia_da_semana
        ORDER BY dia_da_semana DESC
        ``` 
    4. `DATE_DIFF()`: existe em várias linguagens SQL, porém **no PostgreSQL não existe**.
        ```sql
            SELECT 
                DATEDIFF('weeks', '2018-06-10', current_date)
        ```
    - O cálculo da diferença entre datas com o operador de subtração (-) retorna valores em dias. Para calcular a diferença entre datas em outra unidade é necessário fazer uma transformação de unidades (ou criar uma função para isso).

5. Funções
    Servem para criar comandos personalizados de scripts usados recorrentemente.
    - Para criar funções, utiliza-se o comando CREATE OR REPLACE FUNCTION;
    - Para que o comando funcione é obrigatório informar (a) quais as unidades dos INPUTS (b) quais as unidades dos OUTPUTS e (c) em qual linguagem a função será escrita;
    - O script da função deve estar delimitado por $$;
    - Para deletar uma função utiliza-se o comando DROP FUNCTION.
    - **Exemplo**
    ```sql
    CREATE OR REPLACE FUNCTION datediff(unidade varchar, data_inicial date, data_final date)
    RETURNS INTEGER
    LANGUAGE sql
    AS

    $$
        SELECT
            CASE
                WHEN unidade IN ('d', 'day', 'days') THEN (data_final - data_inicial)
                WHEN unidade IN ('w', 'week', 'weeks') THEN (data_final - data_inicial) / 7
                WHEN unidade IN ('m', 'month', 'months') THEN (data_final - data_inicial) / 30
                WHEN unidade IN ('y', 'year', 'years') THEN (data_final - data_inicial) / 365
                END AS diferenca
    $$

    SELECT datediff('w', '2023-10-20', current_date)
    ```

#### Manipulação de Tabelas
##### Tabelas
1. Criação
    1. **Criação a partir de uma *query***: para criar tabelas a partir de uma *query* basta escrever a *query* normalmente e colocar o comando `INTO` antes do `FROM` informando o *schema* e o nome da tabela a ser criada.

        ```sql
        SELECT
            customer_id,
            datediff('years', birth_date, current_date) idade_cliente
            INTO temp_tables.customers_age
        FROM sales.customers
        -- CRIA A TABELA CUSTOMERS_AGE NO ESQUEMA TEMP_TABLES
        ```
    2. **Criação de uma tabela partindo do "zero":** para criar tabelas a partir do zero é necessário criar uma tabela vazia com o comando `CREATE TABLE`, informar quais valores serão inseridos com o comando `INSERT INTO` seguido do nome das colunas e inserir os valores manualmente em forma de lista após o comando `VALUES`.

        ```sql
        CREATE TABLE temp_tables.profissoes(
            professional_status varchar,
            status_profissional varchar
        )
        ```

2. **Deleção:** para deletar uma tabela utiliza-se o comando `DROP TABLE`.

```sql
    DROP TABLE temp_tables.profissoes
```

##### Linhas

1. **Inserção:** para inserir linhas em uma tabela é necessário informar que valores serão inseridos com o comando `INSERT INTO` seguido do nome da tabela e nome das colunas e inserir os valores manualmente em forma de lista após o comando `VALUES`.

    ```sql
    INSERT INTO temp_tables.profissoes 
        (professional_status, status_profissional) VALUES
        ('freelancer', 'freelancer'),
        ('retired', 'aposentado(a)'),
        ('clt', 'clt'),
        ('self_employed', 'autônomo(a)'),
        ('other', 'outro'),
        ('businessman', 'empresário(a)'),
        ('civil_servant', 'funcionário público(a)'),
        ('student', 'estudante'),
        ('trainee', 'estagiario(a)')
    ```    

2. **Atualização:** para atualizar as linhas de uma tabela é necessário informar qual tabela será atualizada com o comando `UPDATE`. Informar qual o novo valor com o comando `SET`. Delimitar qual linha será modificada utilizando o filtro `WHERE`.

    ```sql
    UPDATE temp_tables.profissoes
    SET professional_status = 'intern'
    WHERE status_profissional = 'estagiario(a)'
    ```

3. **Deleção:** para deletar linhas de uma tabela é necessário informar de qual tabela as linhas serão deletadas com o comando `DELETE FROM`. Para delimitar qual linha será deletada, utiliza-se o filtro `WHERE`.

    ```sql
    DELETE FROM temp_tables.profissoes
    WHERE status_profissional = 'desempregado(a)'
    OR status_profissional = 'estagiario(a)'
    ```

##### Colunas
Para fazer qualquer modificação nas colunas de uma tabela utiliza-se o comando `ALTER TABLE` seguido do nome da tabela.
1. **Inserção:** para adicionar colunas utiliza-se o comando `ADD` seguido do nome da coluna e da unidade da nova coluna.

    ```sql
    ALTER TABLE sales.customers
    ADD customer_age INTEGER
    ```

2. **Atualização:** para mudar o tipo de unidade de uma coluna utiliza-se o comando `ALTER COLUMN`.

    ```sql
    ALTER TABLE sales.customers
    ALTER column customer_age TYPE VARCHAR
    ```
    - Para renomear uma coluna utiliza-se o comando `RENAME COLUMN`.

    ```sql
    ALTER TABLE sales.customers
    RENAME COLUMN customer_age TO age
    ```

3. **Deleção:** para deletar uma coluna utiliza-se o comando `DROP COLUMN`.

    ```sql
    ALTER TABLE sales.customers
    DROP column age
    ```
___
### AWS Skill Builder - AWS Partner: Sales Accreditation (Business)
#### 🌥️ Conceitos de Nuvem e Serviços da AWS ☁️
**💡 O que é Computação em Nuvem?**

Computação em nuvem é a entrega de recursos de TI sob demanda pela Internet com pagamento conforme o uso. Em vez de comprar e manter data centers e servidores físicos, você acessa os serviços de tecnologia conforme sua necessidade. 

**📈 Padrões entre clientes da AWS**

Em relação ao caminho para a adoção da nuvem, cada cliente traça um roteiro diferente. Muitos fatores internos e externos influenciam o processo de tomada de decisões e determinam onde eles começam na jornada. As adoções nem sempre são lineares, e os clientes podem estar em qualquer uma das quatro fases diferentes (às vezes ao mesmo tempo). 

🔍 Observação: “Integral” não significa estar 100% na nuvem. Poucos clientes estão 100% na nuvem, principalmente aqueles que começaram com sistemas on-premises.

**🛠️ Serviços da AWS**

A variedade de serviços refere-se à ampla gama de produtos e serviços da AWS. A profundidade do serviço refere-se às muitas e crescentes funcionalidades desses serviços.

Um motivo que leva os clientes a migrar tão rapidamente para a nuvem é a vasta gama de serviços oferecidos, especialmente pela AWS. Cerca de 90% do que criamos é baseado no que é importante para clientes e parceiros segundo eles mesmos, e os demais 10% são invenções em nome do cliente. 

- 📊 Análise;
- 🔗 Integração de Aplicativos;
- 💻 Computação;
- 🗄️ Bancos de Dados;
- 🤖 *Machine Learning*;
- 🗂️ Armazenamento;
- 📺 Serviços de Mídia;
- ...

**📦 Categorias de Serviço**
1. **💻 Computação**: a *Amazon Elastic Compute Cloud* (Amazon EC2) oferece computação segura e dimensionável aos clientes. Os clientes podem escolher o processador, o armazenamento, a redes e o SO de acordo com as exigências da carga de trabalho. Entre os casos de uso estão aplicativos empresariais, computação de alto desempenho (HPC) e ML.
2. **🗂️ Armazenamento**: com o armazenamento na nuvem da AWS, os clientes acessam rapidamente o objeto, o arquivo ou o armazenamento em bloco, sem o complexo planejamento de capacidade. Entre os casos de uso comum estão data lakes, backup e restauração, arquivo e desenvolvimento de aplicativos modernos.
3. **🗄️ Banco de Dados**: a AWS oferece bancos de dados com propósito específico para cargas de trabalho empresariais essenciais, que entregam aos clientes alta disponibilidade, confiabilidade e segurança. Os mecanismos de banco de dados incluem estes tipos: relacional, chave-valor, documentos, na memória, gráficos, séries temporais e livros contábeis.
4. **🔐 Segurança**: com os serviços de segurança da AWS, os clientes podem automatizar tarefas manuais como proteção de dados, gerenciamento de identidade e acesso, proteção de rede e aplicativo, resposta a incidentes e relatórios de conformidade. 
5. **🛠️ Gerenciamento**: com os serviços de gerenciamento e governança da AWS, os clientes podem provisionar e operar seus ambientes para obter agilidade de negócios e controle de governança. Os casos de uso comuns incluem gerenciamento centralizado, nuvem, gerenciamento financeiro e conformidade automatizada. 
6. **🌐 Redes**: com os serviços de redes e entrega de conteúdo da AWS, os clientes podem executar toda carga de trabalho em uma rede global, segura e confiável. Alguns casos de uso comum são: simplificar a execução de recursos, conectar infraestrutura híbrida e fornecer aplicativos mais rapidamente com redes Edge. 


#### 🌐 Modernização de Aplicativos

##### 🏗️ Evolução da Arquitetura

Os clientes estão migrando de aplicativos monolíticos para microsserviços, que são serviços menores e independentes, implantados separadamente, mas capazes de interagir entre si para alcançar um objetivo maior. Essa mudança torna os aplicativos mais simples de criar e manter, já que são menores e mais gerenciáveis.

##### 🌟 Benefícios dos Microsserviços

- **Facilidade de Criação e Manutenção**: Devido ao menor tamanho e complexidade.
- **Atividades Complexas em Grande Escala**: Sistemas divididos em partes menores podem realizar atividades complexas de maneira mais eficiente.

##### ⚠️ Limitações dos Aplicativos Monolíticos

- **Dimensionamento Difícil**
- **Incapacidade de Lidar com Falhas de Componentes**
- **Processo de Implantação Lento**
- **Opções Limitadas**

##### 🛠️ Solução da AWS

A AWS oferece uma plataforma completa para microsserviços, incluindo serviços de:

- Computação
- Armazenamento
- Banco de Dados
- Redes
- Sistema de Mensagens
- Registro e Monitoramento
- DevOps

Para mais informações, acesse [Microsserviços da AWS](https://aws.amazon.com/microservices/).

##### 🚀 Aplicativos Modernos

As organizações buscam maior agilidade para inovar e responder rapidamente às mudanças. Os aplicativos modernos precisam escalar rapidamente, ter disponibilidade global, gerenciar grandes volumes de dados e responder em milissegundos. Esses aplicativos podem ser construídos ou adquiridos por meio de parceiros.

##### 📊 Benefícios Comerciais e Características

| Benefícios Comerciais | Características dos Aplicativos Modernos |
|-----------------------|-----------------------------------------|
| 💰 Melhora o retorno do investimento e reduz o custo total de propriedade | 🌍 Dimensionamento para milhões de usuários |
| ⚙️ Aumenta a eficiência dos desenvolvedores | 🌐 Disponibilidade global |
| 📈 Aumenta a agilidade empresarial | ⏱️ Responde em milissegundos |
| 💾 Lida com petabytes de dados | |

##### 🤖 Transformação Digital

O Machine Learning (ML) está melhorando a experiência do cliente, tornando operações comerciais mais eficientes e decisões mais rápidas e precisas. Com o aumento do poder computacional e a proliferação dos dados, o ML se tornou um diferencial importante em várias indústrias. Segundo o Gartner, o valor comercial derivado da IA deve alcançar USD 3,9 trilhões em 2022.


#### 💼 Valor Comercial e Cloud Value Framework

##### 📊 O Que é Valor Comercial?

O conceito de valor comercial ajuda a determinar a integridade e o bem-estar de um negócio no longo prazo, incluindo, mas não se limitando ao seu valor econômico. Pode aparecer como:

- 📉 **Custos Reduzidos**
- 🔓 **Recursos Liberados**
- ⏲️ **Tempo de Inatividade Reduzido**
- 📈 **Tomada de Decisão Aprimorada**

O **AWS Cloud Value Framework** fornece orientação sobre como alcançar esses benefícios, mostrando as diferentes áreas de valor comercial percebidas pelos clientes ao migrar para a AWS.

##### 🏛️ Cloud Value Framework

Desenvolvido pela AWS Cloud Economics, o **Cloud Value Framework** é uma estrutura conceitual destinada a criar um caso de negócio abrangente para a adoção da nuvem, articulando o valor da adoção da nuvem. Ele mede e rastreia o progresso dos clientes que migraram para a AWS em relação a quatro pilares principais de valor:

**1. 💰 Economia de Custos**
- Reduções nos gastos com TI e gastos com infraestrutura;

**2. 👥 Produtividade da Equipe**
- Após a migração para a AWS, as organizações obtêm maior produtividade da equipe em muitas áreas da empresa, incluindo capacidade de gerenciamento administrativo, foco no trabalho estratégico e capacidade de se concentrar no desenvolvimento de novos recursos.
- Exemplo: tarefas como reparo de hardware e planejamento de servidor podem ser reduzidas ou eliminadas totalmente, o que libera capacidade para que a equipe se dedique a trabalhos mais estratégicos.

**3. 🛡️ Resiliência Operacional**
- Inclui maior disponibilidade do sistema, latência reduzida, maior alcance de SLA e melhor segurança;
- É importante porque o custo do tempo de inatividade e das violações de segurança pode ser alto.

**4. ⚡ Agilidade Empresarial**
- Agilidade refere-se à capacidade de responder de forma rápida e eficaz a mudanças nas condições de negócios ou eventos de negócios inovadores.

#### Como lidar com objeções à nuvem
- Para oferecer a solução apropriada ao seu cliente, é essencial entender os desafios e as preocupações subjacentes.

**💸 Custo**
- "A nuvem é muito cara";
- Preocupação com custo-benefício da nuvem;
- Alto custo migrar para nuvem;
- Reduz o tempo de trabalho;
- Os clientes estão migrando para uma abordagem de nuvem híbrida para complementar sua presença atual em *data centers*. Isso os ajuda a crescer e a pagar apenas pelos recursos usados, sem pagar pela capacidade máxima.

**🔓 Segurança, Conformidade e Privacidade**
- "Vamos manter a privacidade dos dados?";
- Perda de controle ou visibilidade;
- Todos os serviços da AWS têm recursos de criptografia;
- Tamanho é o cuidado com segurança, que agências governamentais utilizam dos serviços da AWS.

**🚫👀 Perda de Controle ou Visibilidade**
- “Como vocês impedem a exposição acidental de dados sigilosos?”;
- A AWS apresenta ferramentas centralizadas de monitoramento e governança como AWS Cost Explorer, AWS Security Hub, Amazon CloudWatch, AWS Config e AWS Organizations.

**🏗️ Infraestrutura Existente**
- “Investimos pesadamente em nossa infraestrutura on-premises.”
- A maioria dos clientes da AWS opera **infraestruturas híbridas**, com uma parte em *data centers on-premises* tradicionais e outras partes na nuvem. A migração para a AWS não significa mover tudo e abandonar o investimento atual. Trata-se de **otimizar e simplificar sua infraestrutura**, o que significa que eles migram para a nuvem apenas o que faz sentido.

**📉👩‍💻 Déficit de habilidades**
- “Nossa equipe não tem as habilidades de nuvem necessárias para dar suporte a este projeto.”

**🔗🏢 Atrelamento a fornecedor**
- “Se migrarmos para a nuvem, vamos ficar dependentes de um fornecedor de plataforma e suas ofertas.”
- Troca de custos.

**🌱 Sustentabilidade**
- “A AWS pode ajudar a melhorar o uso sustentável do nosso ambiente de TI?”
- A infraestrutura da AWS é 3,6 vezes mais eficiente em termos de energia do que a média dos data centers empresariais dos EUA pesquisados. E a AWS executa as mesmas tarefas com uma pegada de carbono 88% menor.

#### 🌟 Venda conjunta com a AWS

**🤝 O Que é a Venda Conjunta?**

A venda conjunta é uma colaboração entre a AWS e os AWS Partners para trabalhar juntos em oportunidades de clientes. Isso permite a entrega de valor de forma mais rápida, com soluções especializadas, conhecimento do setor e modelos flexíveis de engajamento.

- **🎯 Motivos para a Venda Conjunta**
    - Aumentar a Receita: Descobrir novas oportunidades de vendas, gerar mais receita, acelerar negócios e conquistar clientes juntos.
    - Melhorar Relacionamentos com Clientes: Fornecer as melhores soluções aos clientes, compartilhar dados sobre ganhos comprovados e ajudar a fechar negócios.
    - Ganhar Incentivos Financeiros: Acessar financiamento, descontos e créditos de treinamento à medida que oportunidades são compartilhadas com a AWS.

**🔗 Programa APN Customer Engagements (ACE)**

Os parceiros interagem com a AWS através do ACE para colaborar durante todo o ciclo de vida das vendas. Todos os AWS Partners podem começar a obter valor do ACE imediatamente.

**📜 Princípios de Engajamento do AWS Partner**
- **Segurança:** Prioridade máxima na AWS. Proteção da privacidade e consentimento antes de compartilhar informações.
- **Obsessão pelo Cliente:** Clientes em primeiro lugar, com recomendações baseadas no melhor para o cliente.
- **Obsessão pelo Parceiro:** Ferramentas personalizadas para garantir a privacidade, segurança e exatidão das informações compartilhadas.
- **Somente as Informações:** Abordagem baseada em fatos para recomendar soluções aos clientes, respeitando suas decisões.

**🧑‍🤝‍🧑 Equipes de Interface com Parceiros**
1. AWS Marketplace
    - Ajudam parceiros a incluir produtos/serviços no Marketplace.
    - Ajudam clientes a encontrar soluções.
    - Facilitam a aquisição rápida e suporte global.
2. Segmentação de Clientes
    - Comercial
        - **DNB (Negócios Nativos Digitais)**: Empresas voltadas ao consumidor, nascidas na nuvem.
        - **ENT (Empresas de Suporte Empresarial)**: Grandes empresas tradicionais com investimentos legados.
        - **ISV (Provedores Independentes de Software)**: Organizações que desenvolvem e vendem software B2B.
        - ***Startup***: Empresas jovens afiliadas a investidores ou programas de aceleração.
        - **SMB (Pequenas e Médias Empresas)**: Inclui revendedores e empresas não listadas em outros segmentos.
    - Setor Público
        - **Governo**: Agências governamentais locais, estaduais e federais.
        - **Educação**: Instituições de ensino superior, escolas e empresas de EdTech.
        - **Organizações sem Fins Lucrativos**: ONGs e instituições que usam AWS para melhorar desempenho e práticas de dados.
        - **Saúde**: Organizações de saúde públicas que usam AWS para análise de dados e atendimento ao paciente.

**🏛️ Princípios de Engajamento**
1. Segurança
    - Prioridade máxima, proteção da privacidade e consentimento antes de compartilhar informações.

2. Obsessão pelo Cliente
    - Clientes em primeiro lugar, recomendações baseadas no melhor para o cliente.

3. Obsessão pelo Parceiro
    - Ferramentas personalizadas para privacidade, segurança e exatidão das informações.

4. Somente as Informações
    - Abordagem baseada em fatos, respeitando as decisões dos clientes.

**🚀 Conquistando a Confiança**
    - Definir, validar e promover capacidades individuais dos AWS Partners.
    - Divulgar os recursos aos clientes e equipes de vendas da AWS.

