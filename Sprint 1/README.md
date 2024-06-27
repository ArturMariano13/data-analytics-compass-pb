
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
        - <code>nano</code> - apenas abre um arquivo em branco.
        - CTRL + O: salva e pede o nome do arquivo;
        - CTRL + X: sai do arquivo;
        - CTRL + R: adiciona um arquivo (outro) para esse que está aberto;
        - CTRL + K: recorta trecho selecionado;
        - CTRL + U: cola;
        - ALT + A: seleciona;
        - ALT + 6: copia trecho selecionado;
        - <code>nano nome-do-arquivo</code> - abre um arquivo para a edição.
    - **Movimentação dentro de um arquivo**
        - ALT + /: vai para o FIM do arquivo;
        - ALT + \: vai para o INÍCIO do arquivo;
        - ALT + G: pede a linha para onde se deseja ir.
    - **Busca e *replace***
        - CTRL + W: busca palavras;
        - ALT + R: *replace*.

- **vim**
    - <code>sudo apt-get install vim</code>
    - <code>vim nome-do-arquivo</code> - abre ou cria arquivo no modo de comandos
        - 'I': ativa modo de inserção (edição);
        - 'ESC': volta para o modo de comandos.
    - **Modo de comandos**
        - **:x** - salva e sai do arquivo;
        - **:w** - apenas salva alterações;
        - **:q** - apenas sai do arquivo;
        - **u** - desfaz alterações;
        - **CTRL + R** - refaz o que foi desfeito;
        - **dd** - deleta linha inteira;
        - **:q!** - sai sem salvar.
    - **Busca e *replace***
        - **/palavrabuscada** - vai até a próxima ocorrência a cada 'ENTER' (SHIFT + ENTER volta para a ocorrência anterior).
        - **:%s/palavraparasubstituir/palavraasersubstituida/g** - replace.

###### GERENCIAMENTO DE USUÁRIOS
- **Adicionar:** <code>sudo adduser nome</code>
- **Deletar:** <code>sudo userdel --remove nome</code>
- **Renomear:** 
    - <code>sudo usermod -c 'novonome' 'nomeantigo'</code> - muda nome da pessoa (no display de login
    - <code>sudo usermod -l 'novonome' -d /home/novonome -m 'nomeantigo'</code> - muda nome do user e do diretório do user
    OBS.: não usar aspas
- **Bloquear e Desbloquear Usuários**
    - <code>sudo usermod -L nomeuser</code> - bloquear
    - <code> sudo usermod -U nomeuser</code> - desbloquear
- **Grupos Linux**
    1. Criar
        - <code>sudo groupadd -g 9999 nomegrupo</code> - o número é o ID
    2. Deletar
        - <code>sudo groupdel nomegrupo</code>
    3. Mover Usuário para Grupo
        - <code>groups nomeuser</code> - mostra a quais grupos o usuário pertence
        - <code>sudo usermod -a -G nomegrupo nomeuser</code> - adiciona no grupo
        - <code>sudo gpasswd -d nomeuser nomegrupo</code> - remove do grupo
    OBS.: <code>sudo su</code> - para virar super usuário
        <code>passwd</code> - para mudar a senha do usuário

###### GERENCIAMENTO DE PERMISSÕES 
- Leitura (R);
- Escrita (W);
- Execução (X).
    
- **1 222 333 444**
    - 1: diretório/arquivo
    - 2: permissões do dono
    - 3: permissões do grupo
    - 4: permissões dos demais usuários
Exemplo:
    - **drw-rw-r--**: diretório, dono e grupo com permissão de ler e escrever, demais com permissão somente de ler.

- **Permissão Numérica**
    <code>chmod xxx arquivo/diretorio</code>
    - 0: sem permissão (--)
    - 1: executar (--x)
    - 2: escrever (-w-)
    - 3: escrever e executar (-wx)
    - 4: ler (r--)
    - 5: ler e executar (r-x)
    - 6: ler e escrever (rw-)
    - 7: ler, escrever e executar (rwx)
    - **Exemplo**: 
        - <code>chmod 777</code> - todos têm todas as permissões
        - <code>chmod 400</code> - só o dono tem permissão de leitura

- **Alterar proprietário do arquivo**
    - <code>sudo chown novoproprietario nomearquivo</code>
    - <code>sudo chown nomeprop:nomegrupo nomearquivo</code> - muda dono e grupo
    - <code>sudo chgrp nomegrupo nomearquivo</code> - muda grupo do arquivo

##### DICAS
- CTRL + SHIFT + C: copiar no terminal
- CTRL + SHIFT + V: colar no terminal
- "*history*" no terminal: mostra histórico de comandos

###### GERENCIAMENTO BÁSICO DE REDES
- **Como a Web funciona?**
    1. Envio de requisição para um domínio (DNS)
    2. Verificação de Domínio (IP == DNS)
    3. Requisição da resposta para o servidor que pertence a este domínio
    4. Retorno da resposta a quem solicitou
- **DNS**
    - *Domain Name System*;
    - Traduz IP em domínios;
    - Para não termos que gravar endereços IP.

- **Portas**
    - *Endpoint*;
    - Sempre associada a um IP.
    - Exemplos:
        - 20: FTP
        - 22: SSH
        - 80: HTTP
        - 443: HTTPS

- **TCP**
    - Protocolo para transmissão de dados pela rede (seguro).
    - Mais lento, garante a entrega.
    - SMTP (emails);
    - FTP (transferência de arquivos);
    - HTTP.

- **UDP**
    - Protocolo também para a transmissão de dados pela rede.
    - Preocupa-se mais com a velocidade do envio do que com a confiabilidade.
    - Exemplos: jogos online, *streaming*...

- **Comandos**
    - <code>ping</code>
        - Exemplos: <code>ping google.com</code> - para o DNS
                    <code>ping 8.8.8.8</code> - para o IP
    - <code>netstat</code> - para ver as conexões, tabelas de roteamento e interfaces de rede.
    - <code>ifconfig</code> - mostra as interfaces de rede e informação delas.
    - <code>nslookup</code> - mostra o IP através do DNS.
    - <code>hostname -I</code> - mostra o IP da máquina

###### COMPACTAÇÃO E DESCOMPACTAÇÃO DE ARQUIVOS
- **tar**
    - Compactar: <code>tar -czvf nome.tar.gz diretorio</code>
    - Compactar múltiplos arquivos em um só: <code>tar -czvf nome.tar.gz nomearquivo nomearquivo2 ...</code>
    - Descompactar arquivos: <code>tar -xzvf nomepastacompactada</code> ou <code>tar -xzvf nomepastacompactada -C pastadestino</code>
- **zip**
    - Compactar: <code>zip -r nomedefinido.zip pasta-a-compactar</code>
    - Descompactar: <code>unzip nome-arq-compactado -d pasta-destino</code>

### Curso Git e GitHub
#### Controle de Versão
- Ajuda a gerenciar o código-fonte de uma aplicação;
- Registrar todas as modificações do código, podendo reverter as mesmas (*rollback*);
- Cada nenbri oide trabalhar em uma versão diferente (*branch*).

#### Git
- Sistema de **controle de versão**;
- Baseado em **repositórios**, contendo todas as versões do código;
- Operações **otimizadas** para ter **alto desempenho**;
- Projeto de **código aberto**;
- Protegidos com **criptografia**.

#### Repositório
- É onde o código está armazenado;
- Criamos um ao iniciar o projeto;
- Pode ir para servidores que os gerenciam (*GitHub* e *GitBucket*).
- **Criação:**
<code>git init</code> - cria os arquivos necessários - pasta '.git'

#### GitHub
- Serviço para gerenciar repositórios;
- Pode-se enviar projetos para o GitHub.

1. Envio de Repositório <br/>
<code>git init</code><br/>
<code>git add arquivos</code><br/>
<code>git commit -m "First commit"</code><br/>
<code>git branch -M main</code><br/>
<code>git remote add origin endereco</code><br/>
<code>git push -u origin main</code><br/>

2. Verificar Alterações <br/>
<code>git status</code>