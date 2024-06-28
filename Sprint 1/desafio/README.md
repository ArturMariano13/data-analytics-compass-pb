# Desafio da Sprint 1
## Desafio
O desafio final da sprint 1 consistia em processar o arquivo "dados_de_vendas.csv" e gerar relatórios de vendas utilizando *shell script* e agendamento de execução. Posterior a três execuções do script, outro script deveria ser executado, gerando apenas um relatório final contendo os três anteriores gerados.

Posteriormente, deveríamos gravar um vídeo apresentando a realização do desafio e explicando o que fora feito, as dificuldades encontradas, soluções propostas, etc.

## Resolução
Para isso, foi necessário utilizar dos conceitos aprendidos no curso de Linux e em buscas em materiais alternativos (fora da plataforma de cursos).

Primeiramente, busquei formas de desenvolver o script para gerar um relatório partindo do arquivo "dados_de_vendas.csv". Para isso, tive de buscar vídeos no Youtube, materiais na web que me auxiliassem a elaborar o código. Uma vez isso concluído, criei o diretório "ecommerce" por meio do comando `mkdir ecommerce` e movi o arquivo "dados_de_vendas.csv" para dentro dele: `mv dados_de_vendas.csv ecommerce`.

Posterior a isso, testei a execução do script manualmente, obtendo um resultado estranho. Percebi que alguns itens estavam incorretos, com problemas de formatação. Para isso, tive de revisar o meu script e corrigir a parte de buscar a data no arquivo de vendas. Uma vez isso concluído, testei novamente e obtive o resultado esperado. Além disso, encontrei um problema de lógica, pois cada vez que eu executava o script, ele sobrescrevia o arquivo "relatorio.txt", o que representaria um problema para a criação de um relatório final. Com isso, desenvolvi uma maneira de diferenciar os relatórios criados pela data, inserindo no nome do arquivo a data em que foi gerado. Exemplo: "20242506-relatorio.txt", que corresponde ao relatório gerado dia 25/06/2024. Isso solucionou o problema supracitado.

Na sequência, busquei materiais que ensinassem a programar a execução de um script para um determinado horário em dias diferentes da semana (segunda a quinta-feira). Para isso, alterei o arquivo crontab `crontab -e`, inserindo a linha `27 15 * * 1-4 comando-para-execucao`. Alterei de forma fictícia o horário da execução e percebi que estava executando corretamente. 

Por conseguinte, foquei em desenvolver o arquivo "consolidador_de_processamento_de_vendas.sh", o qual ficaria responsável por gerar o relatório final. Nesse, confesso que tive um pouco mais de trabalho, haja vista que necessitei desenvolver um laço *for* para percorrer os relatórios gerados e buscar os seus respectivos dados, preenchendo e concatenando no relatório final criado. Porém, apesar de ter sofrido um pouco, consegui realizar esse script.

Finalmente, com isso pronto na terça-feira (25/06), necessitei esperar os três dias da execução corretamente, e em paralelo fui gravando o vídeo em partes separadas, mostrando o resultado e a geração do relatório diariamente.

## Vídeo
Para o vídeo, criei um roteiro para ele. Decidi dividir em três dias de gravação, haja vista que os meus scripts estavam prontos antes da terça-feira (data mínima para funcionar plenamente de acordo com o desafio).

- **Dia 1:** Apresentação, contextualização do desafio, scripts, crontab e relatório 1 (25/06).
- **Dia 2:** Relatório 2 (26/06).
- **Dia 3:** Relatório 3, execução do script "consolidador_de_processamento_de_vendas.sh" e apresentação do relatório final.

Vale ressaltar que utilizei o aplicativo *OBS Studio* para gravar os vídeos e o *CapCut* para editar e juntar as partes da gravação.