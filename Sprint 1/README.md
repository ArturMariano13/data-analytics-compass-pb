
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
  <img src="https://digilent.com/blog/wp-content/uploads/2015/05/1280px-Kernel_Layout.svg_.png?size=250" alt="Demonstração do Kernel do Linux">
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
- **<code>cd</code>:** *change directory* (muda de diretório)
    - <code>cd ..</code> - move para o diretório superior;
    - <code>cd -</code> - volta para o diretório anterior (em que se estava antes);
    - <code>cd ~</code> - volta para a '/home'.

    OBS.: pode ser concatenado com outro comando. Exemplo: ***cd /etc && ls***

- **<code>ls</code>:** *list directory contents* (lista o conteúdo do diretório)
    - <code>ls -l</code> - mostra com detalhes os arquivos e diretórios;
    - <code>ls -a</code> - mostra arquivos ocultos do diretório (*-all*);
    - <code>ls -la</code> - junta os dois de cima (com detalhes e todos os arquivos);
    - <code>ls -lh</code> - mostra dados para humanos lerem;
    - <code>ls -ltr</code> - mostra com detalhes e em ordem crescente de modificação;
    - <code>ls -lr</code> - mostra na ordem inversa;
    - <code>ls -R</code> - mostra subdiretórios/arquivos dos diretórios listados pelo ls;
    - <code>ls -lS</code> - ordena pelo tamanho do arquivo;
    - <code>ls -m</code> - lista com vírgulas os diretórios e arquivos.

- **<code>clear</code>:** limpa a tela do terminal.

- **<code>cat</code>:** cria arquivo ou permite-nos ver um arquivo.
    - <code>cat arq1 arq2 > arq3</code> - junta o conteúdo do arq1 e do arq2 em outro arquivo (3);
    - <code>cat -n</code> - adiciona números nas linhas do arquivo mostrado;
    - <code>cat -e</code> - adiciona um "$" a cada fim de linha;
    - <code>cat arq4 >> arq5</code> - concatena no arquivo 5 o conteúdo do arquivo 4.

- **<code>touch</code>:** cria arquivos e modifica a data de alteração de um arquivo.
    - Pode-se criar um ou mais arquivos.

- **<code>man</code>:** manual
    - <code>man ls</code> --> apresenta o manual do comando "ls".

OBS.: CTRL + R = para encontrar comandos já dados.

###### GERENCIAMENTO DE ARQUIVOS
- **<code>mkdir</code>:** cria diretórios.
    - <code>mkdir dir1 dir2 dir3</code> --> cria 3 diretórios em 1 comando;
    - <code>mkdir -v dir1 dir2</code> - cria os dois diretórios e mostra uma mensagem de confirmação;
    - <code>mkdir -p dir2/dir3/dir4</code> - cria o diretório 2, o diretório 3 dentro dele, e o diretório 4 dentro do 3.

- **<code>rm</code>:** remove/deleta arquivos.
    - <code>rm 1.txt 2.txt 3.txt</code> - remove os 3 arquivos em 1 comando;
    - <code>rm -i 1.txt</code> - pergunta se confirma a deleção ('y' or 'n');
    - <code>rm -dv dir1</code> - remove diretórios VAZIOS;
    - <code>rm -rfv dir1</code> - remove diretórios e arquivos/diretórios dentro dele.

- **<code>rmdir</code>:** remove apenas diretórios.
    - <code>rmdir dir1/dir2/dir3</code> - remove os 3 diretórios.

- **<code>cp</code>:** copia diretórios ou arquivos.
    - <code>cp doc.txt doc2.txt</code> - faz a cópia de doc para doc2;
    - <code>cp doc.txt dir1</code> - copia o arquivo 'doc' para dentro do diretório 'dir1';
    - <code>cp -r dir1 dir2</code> - copia um diretório para dentro de outro = mantém a estrutura do diretório copiado.
    - <code>cp -r dir1/* dir2</code> - o '*' faz com que todos os arquivos do dir1 sejam copiados.

- <code>mv</code>: mover arquivos (CTRL + X)
    - <code>mv doc1.txt doc2.txt</code> - doc1 não existe mais, agora chama-se doc2;
    - <code>mv docl.txt Downloads/</code> - move doc1 para Downloads;
    - <code>mv * dir</code> - move todos os arquivos para dentro de dir.

- **<code>pwd</code>:** mostra onde se está (caminho).

###### GERENCIAMENTO DE PACOTES

**1. Atualizar repositórios:** para estar na versão mais recente.
    - Busca as atualizações/versões + recentes.

    <code>sudo apt-get update</code>

**2. Atualizar aplicativos/pacotes:** atualiza o necessário.
    <code>sudo apt-get upgrade</code>

**3. Instalar pacotes/aplicativos**
    <code>sudo apt-get install nome-do-app</code>

**4. Deletar pacotes/aplicativos**
    <code>sudo apt-get purge nome-do-app</code>

**5. Atualizar Linux**
    <code>sudo apt-get dist-upgrade</code>

**6. Limpar pacotes/aplicativos desnecessários**
    <code>sudo apt-get autoremove</code>

**7. Buscar pacotes/aplicativos**
    <code>apt-cache search nome-do-app</code>

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
