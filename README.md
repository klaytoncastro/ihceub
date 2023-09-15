# Instruções para os Laboratórios da Disciplina de IHC (Interação Humano-Computador)

Olá, aluno(a)! Bem-vindo(a) aos laboratórios da disciplina de IHC (Interação Humano-Computador). Iniciaremos nossa jornada com os fundamentos do Design de Produto, UX (Experiência do Usuário) e UI (Interface do Usuário). Ao longo da disciplina, também discutiremos ferramentas e técnicas para promover um desenvolvimento ágil. Estabelecida essa base, teremos práticas com desenvolvimento de aplicações web, utilizando tecnologias front-end como HTML, CSS e Bootstrap. Em seguida, compreenderemos a comunicação back-end através do protocolo HTTP, utilizando o microframework Python Flask e explorando bancos de dados tanto relacionais quanto não relacionais para construção de aplicações com páginas dinâmicas. Este repositório foi projetado para auxiliá-lo a configurar e gerenciar essas ferramentas. Siga atentamente as instruções abaixo para configurar seu ambiente. 

### Configuração do Ambiente: 

Para garantir uma experiência mais uniforme, fornecemos uma máquina virtual (VM) pré-configurada. Essa abordagem garante que todos comecem o curso com o mesmo ambiente e configurações. Embora o Docker possa rodar diretamente em diversos sistemas operacionais, esta padronização simplifica nosso suporte e proporciona soluções mais ágeis e consistentes diante de eventuais desafios técnicos.

- **Nota**: Se você tem experiência com Docker e prefere executá-lo diretamente no seu sistema operacional, sinta-se à vontade. A estrutura do repositório suporta este modo de operação. Para os usuários dos hardwares mais recentes da Apple, como o M2 e outros processadores novos, é especialmente relevante considerar esta opção, visto que algumas versões do Oracle Virtual Box podem não ser compatíveis com esses dispositivos. 

## 1. Sobre a Imagem OVA

Oracle VirtualBox é um software de virtualização de código aberto que permite executar vários sistemas operacionais em uma única máquina física. Com ele, é possível criar e gerenciar máquinas virtuais, cada uma com seu sistema operacional, aplicativos e arquivos em um ambiente isolado. Ele é compatível com diversos sistemas, como Windows, Linux e MacOS.

OVA (Open Virtual Appliance) é um formato de arquivo para máquinas virtuais, contendo toda a configuração e discos virtuais necessários. Ele simplifica a portabilidade e implantação de ambientes virtualizados, permitindo importações fáceis em plataformas como o VirtualBox.

Utilizando um arquivo OVA, é possível distribuir ambientes pré-configurados, assegurando que os usuários tenham um ambiente consistente, independentemente da localização de execução. A imagem OVA fornecida já vem equipada com ferramentas como 'docker', 'docker-compose', 'git' e 'ssh', otimizando a configuração dos ambientes de laboratório.

### Como Usar:
1. Baixe a imagem OVA através deste [link](https://1drv.ms/f/s!As9_hcVH7a82gpovWfhahtGkRSmriA?e=vFJ2u3).
2. Caso não esteja instalado, baixe o Oracle VirtualBox através deste [link](https://www.oracle.com/br/virtualization/technologies/vm/downloads/virtualbox-downloads.html). 
3. Escolha a versão correspondente ao seu sistema operacional e siga as instruções de instalação.
4. Execute o Oracle Virtual Box e clique em **Arquivo** > **Importar Appliance**.
5. Selecione o arquivo OVA baixado e siga as instruções na tela.
6. Após a importação, dimensione os recursos de memória compatíveis com o laboratório ou computador pessoal e inicie a máquina virtual (VM). 

### Credenciais para acesso à VM:

- **Usuário:** labihc
- **Senha:** L@b1hc

## 2. Descrição das Ferramentas Utilizadas

### Docker:

No universo do desenvolvimento web, enfrentamos o desafio de gerenciar vários serviços integrados. Configurar cada um deles para operar em sintonia pode ser uma tarefa complexa. Aqui entra o Docker: uma solução que simplifica este processo ao permitir que aplicações sejam desenvolvidas e executadas em contêineres. Estes contêineres são unidades de software que agrupam o código da aplicação e suas dependências, garantindo que ela opere de maneira consistente em diferentes ambientes de computação. Imagine os contêineres como um pacote isolado contendo sua aplicação e tudo o que ela precisa para funcionar, assegurando a performance esperada em qualquer ambiente que tenha suporte ao Docker. Leves e flexíveis, os contêineres Docker iniciam rapidamente e são altamente portáteis. Assim, é viável criar um contêiner no seu computador pessoal e transferi-lo sem problemas para uma plataforma de nuvem ou servidor.

### Docker Compose:

O Docker Compose é uma ferramenta dentro do ecossistema Docker que simplifica a definição e gestão de aplicações multicontêiner. Com ele, é possível orquestrar aplicações complexas compostas por vários contêineres interligados, usando um único arquivo: docker-compose.yml. Com um comando simples (docker-compose up -d), todos os contêineres definidos no arquivo são iniciados simultaneamente, garantindo a integração e configuração correta de cada componente.

Imagine uma aplicação que envolve um servidor web, um banco de dados MongoDB e um cache Redis. Em vez de iniciar e configurar cada contêiner manualmente, com o Docker Compose, é possível definir toda essa configuração em um arquivo e ativá-la de uma vez, assegurando que cada contêiner esteja devidamente configurado e interligado.

Dessa forma, com as ferramentas Docker e Docker Compose, ganhamos em conveniência e eficiência, focando no uso das aplicações e eliminando preocupações com instalações e configurações manuais. A imagem OVA padronizada amplia esse benefício, permitindo a evolução e integração do ambiente, aproveitando o poder computacional do laboratório.

### Flask, HTML, CSS, Javascript e Bootstrap: 

- **Flask**: é um micro-framework web escrito em Python. É classificado como micro-framework porque não exige determinadas ferramentas ou bibliotecas. É flexível e extensível, ideal para iniciar o desenvolvimento de aplicações web, APIs e até mesmo sistemas mais complexos.

- **HTML**: HTML (HyperText Markup Language) é a linguagem padrão para criar páginas e aplicações web. Combinada com tecnologias como JavaScript e CSS, permite a construção de sites interativos e visualmente atrativos.

- **CSS**: CSS (Cascading Style Sheets) é uma linguagem usada para estilizar documentos escritos em HTML. Ela define como os elementos da página devem ser exibidos na tela.

- **JavaScript**: Originalmente desenvolvimento pela Netscape, é uma linguagem de programação de alto nível, interpretada e orientada a objetos, amplamente utilizada para adicionar interatividade a páginas web, permitindo comportamentos dinâmicos e operações assíncronas.

- **Bootstrap**: É um framework front-end gratuito e de código aberto, utilizado para desenvolvimento web responsivo. Criado pelo Twitter (X.com), fornece uma variedade de componentes HTML, CSS e JavaScript pré-projetados para facilitar o desenvolvimento de aplicações web que se adaptam automaticamente a diferentes tamanhos de tela, desde dispositivos móveis a desktops. 

## 3. Preparando o Ambiente de Laboratório

Depois de acessar o ambiente virtual:

1. Baixe os arquivos do projeto:

```bash   
   sudo su -
   cd /opt
   git clone https://github.com/klaytoncastro/ihceub
```

3. Construa e inicie os serviços usando o Docker Compose. 

```bash
   cd /opt/ihceub
   docker-compose build
   docker-compose up -d
```

### Usando o SSH para para conexão

SSH (Secure Shell) é um protocolo que possibilita a conexão e controle de servidores remotos, como nossa VM no Virtual Box. Para gerenciar nossa VM nos laboratórios, recomendamos o uso de conexões SSH em vez da console física. O [Putty](https://www.putty.org/) é uma opção popular e confiável como cliente SSH, especialmente útil para sistemas Windows, embora esteja disponível para outras plataformas. Sua interface intuitiva e funcionalidades robustas o estabeleceram como preferência entre muitos administradores de sistemas e desenvolvedores ao longo dos anos. 

- **Nota**: Se você já possui outras ferramentas de SSH ou tem uma preferência particular, sinta-se à vontade para utilizá-las em nossos laboratórios. 

1. Conveniência e Eficiência

- **Copiar e Colar**: Ao utilizar SSH, fica muito mais fácil copiar e colar comandos, scripts ou até mesmo arquivos entre o host e a VM. Essa funcionalidade torna a execução de tarefas mais rápida e evita erros humanos que podem ocorrer ao digitar manualmente.

- **Multitarefa**: Com o SSH, é possível abrir várias sessões em paralelo, permitindo que você execute várias tarefas simultaneamente. 

2. Evita limitações da console "física"

- **Resolução e Interface**: A console física do Virtual Box pode apresentar limitações, como resolução de tela reduzida ou interações de interface de usuário não intuitivas. O SSH fornece uma interface padronizada, independentemente do software de virtualização usado.

- **Padrão de Gerenciamento**: Ao se familiarizar com o SSH, você estará equipando-se com uma habilidade crucial, não apenas para este ambiente de laboratório, mas para qualquer situação futura que envolva administração de sistemas, trabalho em cloud, times de infraestrutura, DevOps ou desenvolvimento de soluções profissionais.

### Pronto! 

Agora você está com o ambiente preparado e pronto para começar os laboratórios. Em caso de dúvidas, não hesite em me contactar: [klayton.castro@ceub.edu.br](klayton.castro@ceub.edu.br). 

