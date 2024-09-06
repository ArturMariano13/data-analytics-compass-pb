
# SPRINT 1 - Markdown, Linux e Git

## Certificados
Para maiores informações sobre os certificados, siga o link: [certificados](certificados)

## Desafio
Para maiores informações sobre o desafio final, siga o link: [desafio](desafio)

## Evidências
Para maiores informações sobre as evidências, siga o link: [evidências](evidencias)

## Exercícios
Para maiores informações sobre os exercícios, siga o link: [exercícios](exercicios)


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
  <img src="https://digilent.com/blog/wp-content/uploads/2015/05/1280px-Kernel_Layout.svg_.png" alt="Demonstração do Kernel do Linux" width="400">
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
- **`cd`:** *change directory* (muda de diretório)
    - `cd ..` - move para o diretório superior;
    - `cd -` - volta para o diretório anterior (em que se estava antes);
    - `cd ~` - volta para a '/home'.

    OBS.: pode ser concatenado com outro comando. Exemplo: ***cd /etc && ls***

- **`ls`:** *list directory contents* (lista o conteúdo do diretório)
    - `ls -l` - mostra com detalhes os arquivos e diretórios;
    - `ls -a` - mostra arquivos ocultos do diretório (*-all*);
    - `ls -la` - junta os dois de cima (com detalhes e todos os arquivos);
    - `ls -lh` - mostra dados para humanos lerem;
    - `ls -ltr` - mostra com detalhes e em ordem crescente de modificação;
    - `ls -lr` - mostra na ordem inversa;
    - `ls -R` - mostra subdiretórios/arquivos dos diretórios listados pelo ls;
    - `ls -lS` - ordena pelo tamanho do arquivo;
    - `ls -m` - lista com vírgulas os diretórios e arquivos.

- **`clear`:** limpa a tela do terminal.

- **`cat`:** cria arquivo ou permite-nos ver um arquivo.
    - `cat arq1 arq2 > arq3` - junta o conteúdo do arq1 e do arq2 em outro arquivo (3);
    - `cat -n` - adiciona números nas linhas do arquivo mostrado;
    - `cat -e` - adiciona um "$" a cada fim de linha;
    - `cat arq4 >> arq5` - concatena no arquivo 5 o conteúdo do arquivo 4.

- **`touch`:** cria arquivos e modifica a data de alteração de um arquivo.
    - Pode-se criar um ou mais arquivos.

- **`man`:** manual
    - `man ls` --> apresenta o manual do comando "ls".

OBS.: CTRL + R = para encontrar comandos já dados.

###### GERENCIAMENTO DE ARQUIVOS
- **`mkdir`:** cria diretórios.
    - `mkdir dir1 dir2 dir3` --> cria 3 diretórios em 1 comando;
    - `mkdir -v dir1 dir2` - cria os dois diretórios e mostra uma mensagem de confirmação;
    - `mkdir -p dir2/dir3/dir4` - cria o diretório 2, o diretório 3 dentro dele, e o diretório 4 dentro do 3.

- **`rm`:** remove/deleta arquivos.
    - `rm 1.txt 2.txt 3.txt` - remove os 3 arquivos em 1 comando;
    - `rm -i 1.txt` - pergunta se confirma a deleção ('y' or 'n');
    - `rm -dv dir1` - remove diretórios VAZIOS;
    - `rm -rfv dir1` - remove diretórios e arquivos/diretórios dentro dele.

- **`rmdir`:** remove apenas diretórios.
    - `rmdir dir1/dir2/dir3` - remove os 3 diretórios.

- **`cp`:** copia diretórios ou arquivos.
    - `cp doc.txt doc2.txt` - faz a cópia de doc para doc2;
    - `cp doc.txt dir1` - copia o arquivo 'doc' para dentro do diretório 'dir1';
    - `cp -r dir1 dir2` - copia um diretório para dentro de outro = mantém a estrutura do diretório copiado.
    - `cp -r dir1/* dir2` - o '*' faz com que todos os arquivos do dir1 sejam copiados.

- `mv`: mover arquivos (CTRL + X)
    - `mv doc1.txt doc2.txt` - doc1 não existe mais, agora chama-se doc2;
    - `mv docl.txt Downloads/` - move doc1 para Downloads;
    - `mv * dir` - move todos os arquivos para dentro de dir.

- **`pwd`:** mostra onde se está (caminho).

###### GERENCIAMENTO DE PACOTES

**1. Atualizar repositórios:** para estar na versão mais recente.
    - Busca as atualizações/versões + recentes.

`sudo apt-get update`

**2. Atualizar aplicativos/pacotes:** atualiza o necessário.
    
`sudo apt-get upgrade`

**3. Instalar pacotes/aplicativos**
   
`sudo apt-get install nome-do-app`

**4. Deletar pacotes/aplicativos**

`sudo apt-get purge nome-do-app`

**5. Atualizar Linux**

`sudo apt-get dist-upgrade`

**6. Limpar pacotes/aplicativos desnecessários**

`sudo apt-get autoremove`

**7. Buscar pacotes/aplicativos**

`apt-cache search nome-do-app`

OBS.: atualmente, o "-get" não é mais necessários, apenas o "apt" resolve.

###### FILTRO E BUSCAS DE ARQUIVOS E DIRETÓRIOS
- **`head`:** para ver as primeiras linhas de um arquivo
    - `head -n 1 documento.txt` - mostra 1 linha do documento.

- **`tail`:** para ver o fim de um arquivo. Mesma regra de cima.
    - `tail -f documento.txt` - motra alterações em tempo real. Utilizado para acompanhar LOGS.

- **`grep`:** buscar um trecho em um documento (*case-sensitive*).
    - `grep 'Artur' documento.txt` - destaca as ocorrências de 'Artur';
    - `grep -c 'Artur' documento.txt` - retorna o nº de vezes que aparece a palavra.
    - `grep 'Artur' -r**` - procura a palavra recursivamente em todos os arquivos.

- **`find`:** encontrar arquivos ou diretórios
    - `find -name 'documento.txt'` - busca o diretório pelo nome;
    - `find iname documento.txt'` - despreza *case-sensitive*;
    - `find -iname 'documento*'` - retorna tudo que começa com documento...;
    - `find -empty` - retorna diretórios e arquivos vazios.
        - **-type f** --> apenas arquivos.
        - **-type d** --> apenas diretórios.

- **`locate:`** busca na base de dados do SO --> maior desempenho.
    - Nem sempre encontra (quando é muito recente).
    - Bom para arquivos antigos.

###### EDITORES DE TEXTO

- **nano**
    - Vem por padrão com o Ubuntu.
    - **Comandos**
        - `nano` - apenas abre um arquivo em branco.
        - CTRL + O: salva e pede o nome do arquivo;
        - CTRL + X: sai do arquivo;
        - CTRL + R: adiciona um arquivo (outro) para esse que está aberto;
        - CTRL + K: recorta trecho selecionado;
        - CTRL + U: cola;
        - ALT + A: seleciona;
        - ALT + 6: copia trecho selecionado;
        - `nano nome-do-arquivo` - abre um arquivo para a edição.
    - **Movimentação dentro de um arquivo**
        - ALT + /: vai para o FIM do arquivo;
        - ALT + \: vai para o INÍCIO do arquivo;
        - ALT + G: pede a linha para onde se deseja ir.
    - **Busca e *replace***
        - CTRL + W: busca palavras;
        - ALT + R: *replace*.

- **vim**
    - `sudo apt-get install vim`
    - `vim nome-do-arquivo` - abre ou cria arquivo no modo de comandos
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
- **Adicionar:** `sudo adduser nome`
- **Deletar:** `sudo userdel --remove nome`
- **Renomear:** 
    - `sudo usermod -c 'novonome' 'nomeantigo'` - muda nome da pessoa (no display de login
    - `sudo usermod -l 'novonome' -d /home/novonome -m 'nomeantigo'` - muda nome do user e do diretório do user
    OBS.: não usar aspas
- **Bloquear e Desbloquear Usuários**
    - `sudo usermod -L nomeuser` - bloquear
    - ` sudo usermod -U nomeuser` - desbloquear
- **Grupos Linux**
    1. Criar
        - `sudo groupadd -g 9999 nomegrupo` - o número é o ID
    2. Deletar
        - `sudo groupdel nomegrupo`
    3. Mover Usuário para Grupo
        - `groups nomeuser` - mostra a quais grupos o usuário pertence
        - `sudo usermod -a -G nomegrupo nomeuser` - adiciona no grupo
        - `sudo gpasswd -d nomeuser nomegrupo` - remove do grupo
    OBS.: `sudo su` - para virar super usuário
        `passwd` - para mudar a senha do usuário

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
    `chmod xxx arquivo/diretorio`
    - 0: sem permissão (--)
    - 1: executar (--x)
    - 2: escrever (-w-)
    - 3: escrever e executar (-wx)
    - 4: ler (r--)
    - 5: ler e executar (r-x)
    - 6: ler e escrever (rw-)
    - 7: ler, escrever e executar (rwx)
    - **Exemplo**: 
        - `chmod 777` - todos têm todas as permissões
        - `chmod 400` - só o dono tem permissão de leitura

- **Alterar proprietário do arquivo**
    - `sudo chown novoproprietario nomearquivo`
    - `sudo chown nomeprop:nomegrupo nomearquivo` - muda dono e grupo
    - `sudo chgrp nomegrupo nomearquivo` - muda grupo do arquivo

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
    - `ping`
        - Exemplos: `ping google.com` - para o DNS
                    `ping 8.8.8.8` - para o IP
    - `netstat` - para ver as conexões, tabelas de roteamento e interfaces de rede.
    - `ifconfig` - mostra as interfaces de rede e informação delas.
    - `nslookup` - mostra o IP através do DNS.
    - `hostname -I` - mostra o IP da máquina

###### COMPACTAÇÃO E DESCOMPACTAÇÃO DE ARQUIVOS
- **tar**
    - Compactar: `tar -czvf nome.tar.gz diretorio`
    - Compactar múltiplos arquivos em um só: `tar -czvf nome.tar.gz nomearquivo nomearquivo2 ...`
    - Descompactar arquivos: `tar -xzvf nomepastacompactada` ou `tar -xzvf nomepastacompactada -C pastadestino`
- **zip**
    - Compactar: `zip -r nomedefinido.zip pasta-a-compactar`
    - Descompactar: `unzip nome-arq-compactado -d pasta-destino`
___

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
`git init` - cria os arquivos necessários - pasta '.git'


#### Git
1. Envio de Repositório  
`git init` 

`git add arquivos` 

`git commit -m "First commit"`

`git branch -M main` 

`git remote add origin endereco` 

`git push -u origin main` 

2. Verificar Alterações  

`git status`

3. Adicionar Arquivos 
- Serão monitorados pelo Git;
- Interessante fazer de tempos em tempos - depois *commit*.
`git add` 
`git add .` - adiciona tudo

4. Salvar Alterações no Projeto 
- Boa prática: enviar uma mensagem por commit ("-m");
- **"-a"**: para commitar todos os arquivos (*-all*). 
`git commit`

5. Enviar Arquivos ao Repositório Remoto 
`git push`

6. Receber Alterações
- Busca-se as alterações (atualizações) no servidor remoto. 
`git pull`

7. Clonar Repositórios
- Baixa um repositório de um servidor remoto;
- Quando se entra em um novo projeto (já criado);
- '.': clona no diretório atual. 
`git clone endereco`

8. Remover Arquivos do Repositório
- Deleta do monitoramento do git;
- Deleta da máquina local também. 
`git rm nomedoarquivo`

9. Histórico de Alterações
- Acessar um log de modificações do projeto;
- Retorna o histórico de *commits*. 
`git log`

10. Mover/Renomear Arquivos
- Pode-se renomear um arquivo;
- Pode-se mover o arquivo para outra pasta;
- Igual ao Linux. 
`git mv`

11. Desfazer Alterações
- Pode-se retornar ao estado original (do repositório);
- Reseta o arquivo. 
`git checkout`

12. Ignorar Arquivos
- Inserir *.gitignore* na raiz do projeto e nesse arquivo inserir os arquivos/diretórios que não se deseja enviar ao git.

13. Resetar Branches
- Geralmente usado com a flag "--hard";
- Reseta e exclui tudo até o último "push". 
`git reset` 
`git reset --hard origin/main`

##### BRANCHES
- Ramificações do projeto;
- Forma de separar as versões do projeto;
- Geralmente, cada *feature* nova de um projeto fica em uma *branch* separada;
- Ao final, as *branches* são unidas --> ***merge***

1. Criar Branches e Visualizar 
`git branch` - mostra as branches 
`git branch nome` - cria uma branch

2. Deletar
- Nâo é comum, apenas quando se cria errado. 
`git branch -d nomebranch`

3. Mudar de Branch
- **Atenção:** ao alterar a branch, podemos levar alterações que não foram commitadas junto.
- "-b": muda e cria a branch;
- Sempre criar uma branch a partir da main e fazer `git pull` 
`git checkout nome`

4. Unir Branches 
`git merge nome`

5. Stash
- Reseta a branch para a versão de acordo com o repositório;
- Não perde o código. 
`git stash`
- Recuperando Stash
    - `git stash list` - mostra as stashes criadas
    - `git stash nome` - recupera uma stash
        - `git stash apply 0`
- Remover Stash
    - `git stash clear` - limpa totalmente
    - `git stash drop numero` - deleta uma stash específica

6. Criar Tags
- Funcionam como *checkpoints* de branch. 
`git tag -a nome -m "mensagem"`

- `git tag` - mostra todas as tags.
- Verificar e Alterar Tags
    - `git show nome` - para ver
    - `git checkout nome` - para alterar
- Enviar Tags ao Repositório
    - `git push origin nome` - envia uma
    - `git push origin --tags` - envia várias tags

##### Encontrando Branches 
`git fetch`
- Atualiza-me de todas as branches e tags não reconhecidos por mim;
- "-a": all.

##### Receber Alterações
`git pull`

##### Remote
- Pode-se remover ou adicionar um repositório remoto.
- `git remote -v` - mostra o repositório remoto
- `git remote rm origin` - remove
- `git remote add origin url` - adiciona o repositório remoto

##### Submódulos
- Maneira de possuir dois ou mais projetos em um repositório.
- `git submodule` - mostra a lista dos submódulos
- `git submodule add repo` - adiciona um submódulo ao repositório

**Atualizar Submódulos**
- 1º commita
- Envio: `git push --recurse-submodules=on-demand`

##### Análise e Inspeção de Repositórios
**Exibindo detalhes de branches e tags**
- `git show` - informações do branch atual e de seus commits.
- `git show tag` - informações de uma tag

**Exibir diferenças**
- `git diff` - diferenças de uma branch com o repositório
- `git diff arq1 arq2` - diferenças entre dois arquivos

**Log resumido**
- `git shortlog` - dá um log resumido do projeto
- Cada commit será unido por nome do autor.

##### Administração de Repositórios
- `git clean` - vertifica e limpa arquivos não trackeados (sem git add) - usado geralmente para arquivos gerados automaticamente.

**Otimizar Repositório**
- `git gc` - garbage collector - identifica arquivos não necessários e os exclui

**Verificar Integridade de Arquivos**
- `git fsck` - verifica a integridade dos arquivos - comando de rotina

**Reflog**
- `git reflog` - mapeia todos os passos no repositório - salvos até 30 dias

**Comprimir Repositório**
- `git archive --format zip --output master_files.zip branch` - zipa uma branch de um repo.

##### Commits
- Precisam ser padronizados - facilita a **manutenção do projeto**.

**Técnica de *Private Branches***
- Quando criamos branches que não serão compartilhadas no repositório.
- Ao fim, fazemos um *rebase*.
- `git rebase branch1 branch2`

**Boas mensagens de commit**
- Separar assunto do corpo da mensagem;
- Assunto com no máximo 50 caracteres e letra inicial maiúscula;
- Corpo: máximo 72 caracteres;
- Explicar por que e como do commit.
- **Exemplo:** `git commit -a -m "Criada função de adição de produto`
    >> A função foi criada para os novos clientes, ...

#### GitHub
- Serviço para gerenciar repositórios;
- Pode-se enviar projetos para o GitHub;
- Dividido em abas.

##### Aba Code
- Possui os arquivos e o README.md.

##### Aba Issue
- Para reportar problemas/bugs/melhorias necessárias aos colaboradores do projeto.

##### Aba Pull Request
- Onde colaboradores enviam código para solucionar *issues*;
- Código deve ser analisado antes de ser inserido na *main*;
- Vem de novos *branches*.

##### Aba Actions
- Onde se cria as automatizações de *deploy* com integração em outros serviços;
- Incluindo CI/CD;
- Podemos criar uma rotina de atualizar a *main* automaticamente (exemplo).

##### Aba Projects
- Processo de criação é conhecido como *Kanban*;
- Tela lembra o *Trello*;
- *Backlog*, retorno de qualidade, teste, finalizadas.

##### Aba Wiki
- Podemos criar uma **documentação** mais extensa;
- Descrever funcionalidades, bugs conhecidos e não-solucionados.

##### Aba Insights
- Mostra as informações da evolução do repositório (*commits*, *forks*, etc).

#### Linguagem Markdown
Markdown é uma linguagem de marcação simples usada para formatar texto. Foi criada com o objetivo de ser fácil de escrever e ler.

## Comandos Básicos

### Títulos
Os títulos são criados usando o símbolo `#` seguido de um espaço. O número de `#` indica o nível do título.
```markdown
# Título 1
## Título 2
### Título 3
```

### Negrito e Itálico
- **Negrito**: `**texto**` ou `__texto__`
- *Itálico*: `*texto*` ou `_texto_`
- **_Negrito e Itálico_**: `***texto***` ou `___texto___`

### Listas
- Lista não ordenada:
```markdown
    - Item 1
    - Item 2
        - Subitem 2.1
        - Subitem 2.2
```
- Lista ordenada:
```markdown
1. Primeiro item
2. Segundo item
   1. Subitem 2.1
   2. Subitem 2.2
```

### Links e Imagens
- Link: `[Link](https://example.com)`
- Imagem: `![Imagem](https://example.com/imagem.jpg)`

### Código
- Código inline: ``código``
- Bloco de código: ```
```
Código
```