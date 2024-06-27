
# SPRINT 1 - Markdown, Linux e Git

## Resumo dos estudos

### Curso Linux para Desenvolvedores (Udemy)

#### Teoria
O Linux conta com várias versões, também conhecidas como distribuições. Diferentemente dos Sistemas Operacionais Windows e MacOS, o usuário tem mais liberdade para escolher qual deseja utilizar.
Algumas delas são: Ubuntu, Debian, LinuxMint (considerada leve, boa para situações de limitação de recursos), Fedora, etc.
- Utilizaremos Ubuntu, pois muitas empresas o adotam, além de a AWS também utilizar sistemas baseados em Linux.

##### Kernel
- É o *core* do sistema.
- Comunica-se com o hardware.
- Gerencia CPU, memória, etc.

<p align="center">
  <img src="https://digilent.com/blog/wp-content/uploads/2015/05/1280px-Kernel_Layout.svg_.png" alt="Demonstração do Kernel do Linux">
</p>

#### Por que utilizar Linux?
- Gratuito;
- Utilizado na maioria dos servidores web;
- Para usos "normais", o Windows é bom, mas para trabalho, programação, empresas, o Linux é superior;
- Requisito para trabalhar em diversas empresas;
- Comunidade muito ativa;
- Segurança (gerenciamento de acesso a arquivos e diretórios);
- Suporte nativo para muitas linguagens.

#### Linux Fundamental

**Terminal VS Shell**
**Terminal:** é a janela que executa um *shell*; envia para o *shell* um comando e recebe o resultado.
***Shell*:** executa os comandos enviados pelo terminal e retorna o resultado a ele.

**Comandos:** COMANDO    -OPÇÕES     ARQUIVOS/DIRETÓRIOS
    Exemplo:    ls         -la              /home 

**Estrutura de Diretórios**
- **'/':** raiz;
- **'/bin':** arquivos binários;
- **'/boot':** arquivos de inicialização do SO;
- **'/dev':** dispositivos conectados;
- **'/etc':** arquivos de configuração (download);
- **'/home':** arquivos e diretórios dos usuários;
- **'/lib':** arquivos de bibliotecas;
- **'/media':** apresenta os diretórios dos dispositivos "montados";
- **'/opt':** arquivos de *apps* não oficiais do Ubuntu (de terceiros);
- **'/sbin':** arquivos binários do sistema;
- **'/tmp':** arquivos temporários;
- **'/usr':** arquivos usados apenas para modo leitura;
- **'/var':** tem arquivos de log (variáveis).

##### COMANDOS
- **cd:** *change directory* (muda de diretório)
    - **cd ..** --> move para o diretório superior;
    - **cd -** --> volta para o diretório anterior (em que se estava antes);
    - **cd ~** --> volta para a '/home'.

    OBS.: pode ser concatenado com outro comando. Exemplo: ***cd /etc && ls***

- **ls:** *list directory contents* (lista o conteúdo do diretório)
    - **ls -l** --> mostra com detalhes os arquivos e diretórios;
    - **ls -a** --> mostra arquivos ocultos do diretório (*-all*);
    - **ls -la** --> junta os dois de cima (com detalhes e todos os arquivos);
    - **ls -lh** --> mostra dados para humanos lerem;
    - **ls -ltr** --> mostra com detalhes e em ordem crescente de modificação;
    - **ls -lr** --> mostra na ordem inversa;
    - **ls -R** --> mostra subdiretórios/arquivos dos diretórios listados pelo ls;
    - **ls -lS** --> ordena pelo tamanho do arquivo;
    - **ls -m** --> lista com vírgulas os diretórios e arquivos.

- **clear:** limpa a tela do terminal.

- **cat:** cria arquivo ou permite-nos ver um arquivo.
    - **cat arq1 arq2 > arq3** --> junta o conteúdo do arq1 e do arq2 em outro arquivo (3);
    - **cat -n** --> adiciona números nas linhas do arquivo mostrado;
    - **cat -e** --> adiciona um "$" a cada fim de linha;
    - **cat arq4 >> arq5** --> concatena no arquivo 5 o conteúdo do arquivo 4.

- **touch:** cria arquivos e modifica a data de alteração de um arquivo.
    - Pode-se criar um ou mais arquivos.

- **man:** manual
    - **man ls** --> apresenta o manual do comando "ls".

OBS.: CTRL + R = para encontrar comandos já dados.

###### GERENCIAMENTO DE ARQUIVOS
- **mkdir:** cria diretórios.
    - **mkdir dir1 dir2 dir3** --> cria 3 diretórios em 1 comando;
    - **mkdir -v dir1 dir2** --> cria os dois diretórios e mostra uma mensagem de confirmação;
    - **mkdir -p dir2/dir3/dir4** --> cria o diretório 2, o diretório 3 dentro dele, e o diretório 4 dentro do 3.

- **rm:** remove/deleta arquivos.
    - **rm 1.txt 2.txt 3.txt** --> remove os 3 arquivos em 1 comando;
    - **rm -i 1.txt** --> pergunta se confirma a deleção ('y' or 'n');
    - **rm -dv dir1** --> remove diretórios VAZIOS;
    - **rm -rfv dir1** --> remove diretórios e arquivos/diretórios dentro dele.

- **rmdir:** remove apenas diretórios.
    - **rmdir dir1/dir2/dir3** --> remove os 3 diretórios.

- **cp:** copia diretórios ou arquivos.
    - **cp doc.txt doc2.txt** --> faz a cópia de doc para doc2;
    - **cp doc.txt dir1** --> copia o arquivo 'doc' para dentro do diretório 'dir1';
    - **cp -r dir1 dir2** --> copia um diretório para dentro de outro = mantém a estrutura do diretório copiado.
    - **cp -r dir1/* dir2** --> o '*' faz com que todos os arquivos do dir1 sejam copiados.

- **mv:** mover arquivos (CTRL + X)
    - **mv doc1.txt doc2.txt** --> doc1 não existe mais, agora chama-se doc2;
    - **mv docl.txt Downloads/** --> move doc1 para Downloads;
    - **mv * dir** --> move todos os arquivos para dentro de dir.

- **pwd:** mostra onde se está (caminho).

###### GERENCIAMENTO DE PACOTES

**1. Atualizar repositórios:** para estar na versão mais recente.
    - Busca as atualizações/versões + recentes.

<center><code>sudo apt-get update</code></center>

**2. Atualizar aplicativos/pacotes:** atualiza o necessário.
<center><code>sudo apt-get upgrade</code></center>

**3. Instalar pacotes/aplicativos**
<center><code>sudo apt-get install nome-do-app</code></center>

**4. Deletar pacotes/aplicativos**
<center><code>sudo apt-get purge nome-do-app</code></center>

**5. Atualizar Linux**
<center><code>sudo apt-get dist-upgrade</code></center>

**6. Limpar pacotes/aplicativos desnecessários**
<center><code>sudo apt-get autoremove</code></center>

**7. Buscar pacotes/aplicativos**
<center><code>apt-cache search nome-do-app</code></center>

OBS.: atualmente, o "-get" não é mais necessários, apenas o "apt" resolve.

###### FILTRO E BUSCAS DE ARQUIVOS E DIRETÓRIOS
- **<code>head</code>:** para ver as primeiras linhas de um arquivo
    - <code>head -n 1 documento.txt</code> - mostra 1 linha do documento.

- **<code>tail</code>:** para ver o fim de um arquivo. Mesma regra de cima.
    - <code>tail -f documento.txt</code> - motra alterações em tempo real. Utilizado para acompanhar LOGS.

- **<code>grep</code>:** buscar um trecho em um documento (*case-sensitive*).
    - <code>grep 'Artur' documento.txt</code> - destaca as ocorrências de 'Artur';
    - <code>grep -c 'Artur' documento.txt</code> - retorna o nº de vezes que aparece a palavra.
    - <code>grep 'Artur' -r**</code> - procura a palavra recursivamente em todos os arquivos.

- **<code>find</code>:** encontrar arquivos ou diretórios
    - <code>find -name 'documento.txt'</code> - busca o diretório pelo nome;
    - <code>find iname documento.txt'</code> - despreza *case-sensitive*;
    - <code>find -iname 'documento*'</code> - retorna tudo que começa com documento...;
    - <code>find -empty</code> - retorna diretórios e arquivos vazios.
        - **-type f** --> apenas arquivos.
        - **-type d** --> apenas diretórios.

- **<code>locate:</code>** busca na base de dados do SO --> maior desempenho.
    - Nem sempre encontra (quando é muito recente).
    - Bom para arquivos antigos.

###### EDITORES DE TEXTO

- **nano**
    - Vem por padrão com o Ubuntu.
    - **Comandos**
