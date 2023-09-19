# Instruções para os Laboratórios da Disciplina de IHC (Interação Humano-Computador)

Prezado(a) aluno(a), 

Seja bem-vindo(a) aos laboratórios da disciplina de IHC (Interação Humano-Computador). Neste curso exploraremos os fundamentos de _Design_ de Produto, UX - _User eXperience_ (Experiência do Usuário) e UI - _User Interface_ (Interface do Usuário). Também discutiremos ferramentas e técnicas essenciais para promover um desenvolvimento ágil em IHC. 

Com essa base estabelecida, daremos ênfase às tecnologias HTML (_HyperText Markup Language_), CSS  (_Cascading Style Sheets_), JavaScript e Bootstrap. Introduziremos o protocolo HTTP (_Hypertext Transfer Protocol_), a arquitetura de microsserviços e o _microframework_ Python Flask. Também abordaremos o uso de bancos de dados, relacionais ou não relacionais, demonstrando a construção de interfaces web apoiadas por serviços dinâmicos. 

Este documento foi preparado para auxiliar a configuração e gerenciamento dessas ferramentas. Siga atentamente as instruções abaixo para preparar seu ambiente.

### Configuração do Ambiente: 

Para as atividades práticas, é fundamental ter um ambiente de desenvolvimento adequadamente configurado. Visando padronizar essa experiência, disponibilizamos uma máquina virtual (_Virtual Machine_ - VM) pré-configurada, que contém todas as ferramentas e dependências necessárias. Embora o Docker seja compatível para rodar diretamente em diversos sistemas operacionais, essa abordagem simplifica o suporte e agiliza a solução de eventuais desafios técnicos, assegurando que todos os estudantes tenham acesso a um ambiente consistente e minimizando complicações decorrentes de diferenças de hardware e versões de software. 

## 1. Sobre a Imagem OVA

OVA (_Open Virtual Appliance_) é um formato de arquivo para máquinas virtuais (VMs), contendo toda a configuração de sistema operacional e discos virtuais necessários. Ele simplifica a portabilidade e implantação de ambientes virtualizados, viabilizando uma importação fácil de imagens padronizadas em softwares de virtualização como o Oracle VirtualBox, dentre outros. 

O VirtualBox é um software de virtualização de código aberto, que permite executar vários sistemas operacionais em uma única máquina física. Com ele, é possível criar e gerenciar máquinas virtuais, cada uma com seu sistema operacional, aplicativos e arquivos em um ambiente isolado. Ele é compatível com diversos sistemas operacionais, tais como Windows, Linux e MacOS.

Ao utilizar um arquivo OVA, é possível preparar e distribuir imagens pré-configuradas de software, assegurando que os laboratórios possam ser reproduzidos em um ambiente consistente e reproduzível, independentemente da localidade de execução. A imagem OVA fornecida já vem equipada com ferramentas como `docker`, `docker-compose`, `git` e `ssh`, otimizando o tempo de configuração do laboratório.

Além disso, a imagem OVA padronizada facilita a integração, potencializando a infraestrutura do laboratório para uso distribuído dos recursos e configuração de serviços mais robustos. Por exemplo, enquanto uma estação pode ficar responsável pela hospedagem do banco de dados, outra pode disponibilizar o _front-end_ e outra pode executar o _back-end_, atuando de maneira colaborativa e autônoma. 

- **Nota**: O uso de uma VM busca uniformizar o funcionamento dos ambientes e facilitar o suporte. No entanto, valorizamos a autonomia de cada estudante, especialmente para a prática em seu computador pessoal. Se você já está familiarizado com Docker e deseja executá-lo nativamente em seu sistema operacional, este repositório está preparado para isso. Usuários(as) de hardwares recentes da Apple, como o M2, devem considerar esta opção, devido a possíveis incompatibilidades com versões do VirtualBox originalmente desenvolvidas para ambientes x86_64. Para quem utiliza Windows e prefere evitar VMs em função de limitação de recursos, especialmente quando seu dispositivo possui menos que 6GB de RAM, o _Windows Subsystem for Linux_ (WSL) é uma opção interessante. No entanto, lembre-se de que o WSL, apesar de eficiente, não oferece todas as vantagens de um sistema Linux completo e apresenta nuances entre suas versões (WSL e WSL 2). 

### Como Usar:
1. Baixe a imagem OVA através deste [link](https://1drv.ms/f/s!As9_hcVH7a82gpovWfhahtGkRSmriA?e=vFJ2u3).
2. Caso não esteja instalado, baixe o VirtualBox através deste [link](https://www.oracle.com/br/virtualization/technologies/vm/downloads/virtualbox-downloads.html). 
3. Escolha a versão correspondente ao seu sistema operacional e siga as instruções de instalação.
4. Execute o VirtualBox e clique em **Arquivo** > **Importar Appliance**.
5. Selecione o arquivo OVA baixado e siga as instruções na tela.
6. Após a importação, dimensione os recursos de memória compatíveis com o laboratório ou computador pessoal. A imagem vem pré-configurada com 512MB de RAM, o que é inicialmente suficiente para prosseguir com nossos laboratórios. 
7. Em configurações da VM, pode ser necessário alterar a porta USB para suporte à versão 1.1 ao invés da 2.0.
8. Configure a placa de rede em modo [NAT](https://www.simplified.guide/virtualbox/port-forwarding#:~:text=Right%20click%20on%20the%20virtual%20machine%20and%20click,of%20the%20window.%20Click%20on%20Port%20Forwarding%20button).
9. Inicie a máquina virtual (VM). 

### Credenciais para acesso à VM:

- **Usuário:** labihc
- **Senha:** L@b1hc

## 2. Compreendendo o modo NAT no VirtualBox

NAT (_Network Address Translation_) é a implementação de um recurso para tradução de endereços de rede. No contexto do VirtualBox, ao configurar uma VM para usar NAT, você está permitindo que essa VM se comunique com redes externas, incluindo a Internet, usando o mesmo endereço IP (_Internet Protocol_) do host. Assim, a máquina _host_ (seu _desktop_ de laboratório ou _notebook_ pessoal) age como um _gateway_ e a VM parece estar atrás de uma rede privada.

Além de fornecer acesso à Internet, o recurso de NAT do VirtualBox também permite o redirecionamento de portas. Isso significa que você pode encaminhar o tráfego de uma porta específica no _host_ para uma porta na VM. Isso é bastante útil quando você deseja acessar serviços hospedados na VM, que poderão ser alcançados diretamente do _host_ ou a partir de outras máquinas na mesma rede, a exemplo das aplicações web e interfaces de gerenciamento com as quais iremos trabalhar no laboratório. 

### Como configurar o Redirecionamento de Portas no VirtualBox:

1. **Abra o VirtualBox** e selecione a máquina virtual que você deseja configurar.
2. Clique em **Configurações** (ou _Settings_).
3. Na janela de configurações, vá para **Rede**.
4. Sob a aba **Adaptador 1** e certifique-se de que está configurado para **Conectado a: NAT**.
5. Clique em **Avançado** para expandir as opções.
6. Clique em **Redirecionamento de Portas**.
7. Na janela de redirecionamento de portas, você pode adicionar algumas regras para encaminhar portas da sua máquina host para a sua máquina virtual.

### Exemplo de Tabela de Configuração de Portas:

| Nome da Regra | Protocolo | Endereço IP do Host | Porta do Host | Endereço IP da VM | Porta da VM |
|---------------|-----------|---------------------|---------------|-------------------|-------------|
| Acesso SSH    |    TCP    |      127.0.0.1      |      2222     |     10.0.2.15     |      22     |
| FlaskApp 1    |    TCP    |      127.0.0.1      |      8500     |     10.0.2.15     |     5000    |
| FlaskApp 2    |    TCP    |      127.0.0.1      |      8501     |     10.0.2.15     |     5001    |
| FlaskApp 3    |    TCP    |      127.0.0.1      |      8502     |     10.0.2.15     |     5002    |

- **Nota**: Ao configurar o redirecionamento de portas, evite utilizar as portas 0-1023 (exceto 80 e 443, para aplicações web), pois elas são reservadas. A porta 2222 é comumente usada para SSH devido à sua semelhança com a porta padrão 22 e por estar acima da faixa de portas reservadas, reduzindo a possibilidade de conflitos. Uma boa prática para servidores de aplicação é começar com a porta 8500. Sempre certifique-se de que a porta escolhida **não esteja em uso**. Ferramentas nativas do sistema operacional, como `netstat`, podem ajudar na verificação. 

## 3. Descrição da Arquitetura e Ferramentas Utilizadas

Um _Framework_ é uma estrutura pré-projetada que fornece aos desenvolvedores um conjunto de componentes que serve de base para a criação de aplicações, eliminando a necessidade de começar do zero. Essa abordagem oferece uma série de funcionalidades, ferramentas padrão e práticas reconhecidas na indústria de software, permitindo que os desenvolvedores se concentrem na lógica específica da aplicação, otimizando o processo de desenvolvimento e minimizando erros de implementação. Ao se optar por determinado _framework_, busca-se alinhar-se às melhores práticas estabelecidas pelo mercado. No contexto da construção de aplicações web modernas e prática dos conceitos de IHC, é imperativo explorar os _frameworks_ de destaque no mercado, cada um com suas peculiaridades e benefícios. 

As aplicações web modernas são frequentemente baseadas no uso de  _frameworks_ e organizadas em três camadas fundamentais: _Front-End, Back-End_ e Infraestrutura. O _Front-End_ representa a interface visível ao usuário, os componentes com os quais ele interage diretamente, exemplificado pelos navegadores web em _desktops_ e dispositivos móveis. Em contraste, o _Back-End_ gerencia a lógica, o processamento e comunicação com os bancos de dados, estabelecendo o cerne da aplicação, onde os processos vitais são executados. A Infraestrutura, por sua vez, é a base técnica onde a aplicação opera, incluindo a hospedagem e soluções focadas na estabilidade, escalabilidade, disponibilidade e segurança. 

Em conjunto, estas camadas proporcionam uma experiência homogênea ao usuário e uma arquitetura de referência para engenheiros de software e plataforma. A seguir, temos o diagrama simplificado de nossa arquitetura de referência: 

![Arquitetura de Referência](./puml/app-architecture.svg)

### Front-End:

- **HTML**: é a linguagem padrão para criar páginas e aplicações web, sendo fundamental para definir a estrutura de uma página web, como cabeçalhos, parágrafos, _links_, imagens e outros elementos.

- **CSS**: é a linguagem usada para estilizar documentos escritos em HTML, que define como os elementos da página devem ser personalizados e exibidos. CSS é essencial para aprimorar a aparência de um _site_, pois permite que os desenvolvedores apliquem estilos, animações e _layouts_ consistentes. 

- **JavaScript**: é uma linguagem de programação de alto nível, interpretada e orientada a objetos, amplamente utilizada para adicionar interatividade a páginas web, permitindo comportamentos dinâmicos e operações assíncronas. Com o JavaScript, os desenvolvedores podem criar aplicações web mais atraentes, contendo carrosséis de imagens, formulários interativos, gráficos animados e até mesmo jogos. 

- **Bootstrap**: É um _framework_ gratuito e de código aberto, utilizado para desenvolvimento web e responsivo. Criado pelo Twitter (X.com), fornece uma variedade de componentes HTML, CSS e JavaScript projetados para facilitar o desenvolvimento de aplicações web que se adaptam automaticamente a diferentes tamanhos de tela, desde dispositivos móveis até desktops. É uma escolha popular entre os desenvolvedores, pois fornece uma base sólida para criar _sites_ responsivos rapidamente. Com sua ampla gama de componentes já prontos para uso, podemos acelerar o processo de desenvolvimento e manter a consistência do _design_. 

### Back-End:

- **Flask**: Trata-se de um _microframework_ para desenvolvimento em Python na web. É reconhecido por sua flexibilidade, extensibilidade e sua natureza minimalista, características que o tornam perfeito para iniciar o desenvolvimento de aplicações web, APIs (_Application Programming Interfaces_) e até mesmo sistemas de maior complexidade. Ele é denominado _microframework_ porque, diferentemente de outras soluções, não vem pré-carregado com uma vasta gama de ferramentas ou bibliotecas que nem sempre serão utilizadas em seu projeto. Isso o torna uma escolha popular para projetos que buscam um começo ágil, permitindo aos desenvolvedores implementar apenas as extensões necessárias, sem a sobrecarga inerente a um _framework_ mais abrangente.

- **SQLite**: É um sistema de gerenciamento de banco de dados (SGDB) relacional, leve e autônomo, com suporte à SQL (_Structured Query Language_). Todo o banco de dados SQLite é armazenado em um único arquivo, tornando-o altamente portátil e eficiente para aplicações que requerem um armazenamento estruturado e ágil. É ideal para prototipação rápida de aplicações web e projetos de soluções que não necessitam de um banco de dados de grande escala. Para aplicações em produção com uma quantidade significativa de tráfego ou necessidades complexas de banco de dados, você pode considerar opções como MySQL e PostgreSQL. 

- **MongoDB**: Trata-se de um banco de dados NoSQL (Not-only SQL) orientado a documentos. Diferentemente dos SGBDs relacionais, que utilizam tabelas, colunas, registros, são estritamente baseados em esquemas tipados e estruturados em relacionamentos, o MongoDB emprega uma arquitetura voltada a coleções e documentos. Esta abordagem de esquema dinâmico facilita o armazenamento de dados semi-estruturados, oferecendo escalabilidade e flexibilidade notáveis, tornando-o uma escolha preferencial para muitas aplicações modernas.

### Infraestrutura:

Docker e Docker Compose são ferramentas essenciais ao desenvolvedor moderno, facilitando a criação e acelerando a distribuição e execução de aplicações em ambientes consistentes, isolados e reproduzíveis. Com isso, eliminamos a complexidade das instalações manuais, aumentando a conveniência e eficiência. Há uma extensa documentação disponível e uma comunidade bastante ativa. 

- **Docker**: No desenvolvimento web, gerenciar serviços integrados pode ser desafiador. O Docker simplifica essa tarefa, permitindo que aplicações sejam encapsuladas em contêineres, que contêm o código e suas dependências, assegurando uma operação consistente em diferentes ambientes. Imagine contêineres como pacotes isolados com tudo necessário para sua aplicação funcionar, prontos para operar onde o Docker estiver disponível. Esses contêineres são leves, rápidos de iniciar e facilmente transferidos entre seu computador, servidores e plataformas em nuvem. Assim, ele proporciona um modo eficaz de encapsular uma aplicação com todas as suas dependências, garantindo que ela funcione de maneira idêntica, independentemente de onde seja executada.

- **Docker Compose**: Por outro lado, o Docker Compose é uma ferramenta que facilita a definição e execução de aplicações multi-contêiner com o Docker. Com ele, é possível definir um conjunto de contêineres, suas configurações e dependências em um único arquivo e, em seguida, executar todo o conjunto com um único comando, sendo ideal para desenvolvimento local, teste e integração contínua. Assim, o Docker Compose facilita a configuração de aplicações multicontêiner através de um arquivo `docker-compose.yml`. Com o comando `docker-compose up -d`, todos os contêineres no arquivo são ativados juntos, assegurando sua correta configuração e integração. Por exemplo, ao invés de configurar manualmente contêineres para um servidor web, MongoDB e Redis, o Docker Compose permite fazer isso de maneira centralizada, orquestrada em um só arquivo. 

## 4. Preparando o Ambiente de Laboratório

### Usando o SSH: Guia Básico

SSH (_Secure Shell_) é um protocolo que possibilita a conexão e controle de servidores remotos, como a VM instanciada no VirtualBox. Para gerenciar nossa VM, recomendamos o uso de conexões SSH em vez da console física. O [Putty](https://www.putty.org/) é uma opção popular e confiável. A versão _portable_ pode ser baixada e usada diretamente em nossos laboratórios. 

- **Nota 1**: Se você já possui outras ferramentas de SSH instaladas ou tem uma preferência particular, sinta-se à vontade para utilizá-las. 

### Conveniência e Eficiência

- **Copiar e Colar**: Ao utilizar SSH, fica muito mais fácil copiar _logs_ de erros, colar comandos, _scripts_, código, ou até mesmo movimentar arquivos entre _host_, VM e vice-versa. Essa funcionalidade torna a execução de tarefas muito mais rápida e evita erros humanos que podem ocorrer ao digitar manualmente.

- **Multitarefa**: Com o SSH, é possível estabelecer várias sessões em paralelo, permitindo que você execute várias tarefas simultaneamente. 

### Evita as limitações da console "física"

- **Resolução e Interface**: A console física do VirtualBox pode apresentar limitações, como resolução de tela reduzida ou interações de interface de usuário não intuitivas. O SSH fornece uma interface padronizada, independentemente do software de virtualização usado.

- **Padrão de Gerenciamento**: Ao se familiarizar com o SSH, você estará equipando-se com uma habilidade crucial, não apenas para este ambiente de laboratório, mas para o desenvolvimento de soluções profissionais e situações futuras que envolvam a administração de sistemas, times de infraestrutura, DevOps, SRE e Cloud. 

### Como se conectar ao ambiente virtual:

1. Execute o PuTTY e no campo `Host Name (or IP address)`, digite: `127.0.0.1`. No campo `Port`, digite: `2222`. Isso é possível pois configuramos previamente o NAT com redirecionamento de portas no VirtualBox, de modo a encaminhar a porta `2222` do _host_ para a porta `22` da VM. 

2. Certifique-se de que a opção `Connection type` esteja definida como `SSH`. Clique no botão `Open` na parte inferior da janela. Uma janela de terminal será aberta. 

3. Na primeira vez que você se conectar, pode ser solicitado que você confie na chave SSH da sua VM. Se isso acontecer, clique em `Yes` para aceitar a chave e continuar. 

4. Você será solicitado a fornecer um nome de usuário. Digite `labihc` e pressione `Enter`. Em seguida, será solicitada a senha. Digite `L@b1hc` e pressione `Enter`.

- **Nota 1**: No ambiente do laboratório trabalharemos predominantemente com o modo NAT e, em princípio, com apenas uma VM instanciada. A escolha de adotar NAT em laboratório é motivada por questões de isolamento e segurança, uma vez que este modo permite que a VM acesse a Internet (através do _host_), mas não torna a VM diretamente acessível de outras máquinas na rede externa.

- **Nota 2**: A reinicialização da VM não impacta a conexão SSH em função da configuração do modo NAT e redirecionamento de portas. Acessos de nossas aplicações e interfaces de gerenciamento via navegador seguem uma lógica similar, usando a URL (_Uniform Resource Locator_) `http://localhost:<numero_da_porta_redirecionadora>`.

- **Nota 3**: Em redes domésticas, utilizar o modo _Bridge_ pode ser uma alternativa interessante, pois ele integra a VM diretamente à rede local e dispensa as configurações de redirecionamento de portas, especialmente útil quando se trabalha com mais de uma VM instanciada. Isso implica que, para acessar serviços na VM, você usará o endereço IP da VM, por exemplo: `http://<ip_da_vm>:<numero_da_porta_da_vm>`. Este endereço IP também será necessário para futuras conexões SSH diretamente na porta `22`. Para conhecer o IP da VM, execute o comando `ifconfig` a partir de sua console física. 

### Como baixar e iniciar as aplicações básicas: 

1. Depois de acessar o ambiente virtual, baixe os arquivos do projeto:

```bash   
   sudo su -
   cd /opt
   git clone https://github.com/klaytoncastro/ihceub
```

2. Construa e inicie os serviços usando o Docker Compose. 

```bash
   cd /opt/ihceub/<diretorio_da_aplicacao>
   docker-compose build
   docker-compose up -d
```

3. Para criar e alterar os arquivos de configuração diretamente na VM, pode ser utilizado o editor Vim, opção robusta e versátil para terminais Linux. O Vim é uma ferramenta bastante útil administradores de sistemas e desenvolvedores, permitindo que usuários mais experientes editem arquivos com poucos comandos. 

### Usando o Vim: Guia Básico

Neste guia, focaremos apenas em algumas operações básicas, tais como: abrir, editar e salvar arquivos. 

1. **Abrir um arquivo**
    ```bash
    vim <nome_do_arquivo>
    ```

2. **Modo de Inserção**

    Após abrir ou criar um arquivo com o Vim, você estará no modo normal. Para inserir ou editar texto, você deve entrar no modo de inserção pressionando `Insert`.

3. **Salvar alterações**

    Para salvar as alterações feitas no arquivo, primeiro pressione `Esc` para retornar ao modo normal, depois digite `:w` e pressione `Enter`.

4. **Sair do Vim**

    - Sem salvar as alterações: Pressione `Esc` (para garantir que você está no modo normal), depois digite `:q!` e pressione `Enter`.
    - Após salvar as alterações: Digite `:wq` e pressione `Enter` ou apenas `:x`.

5. **Editar texto**

    No modo de inserção (após pressionar `Insert`), você pode editar o texto como em qualquer outro editor. Quando terminar, pressione `Esc` para voltar ao modo normal.

6. **Exibindo Números de Linha**

    Para exibir os números de linha no Vim, no modo normal, digite:
    
    ```bash
    :set number
    ```
    - Isso é útil porque facilita a navegação, a leitura e a referência a partes específicas do arquivo, especialmente em arquivos grandes ou quando se está fazendo depuração de código.

7. **Deletar uma Linha**

    No modo normal, posicione-se na linha que deseja deletar e digite `dd`.

### Dicas

- O Vim é uma ferramenta robusta, repleta de comandos e atalhos que podem otimizar sua produtividade ao editar arquivos em sistemas operacionais baseados em terminal. À medida que se familiariza com os comandos básicos, você descobrirá as potencialidades desta ferramenta. Para quem ainda não está habituado com ambientes de terminal, caso se sinta perdido ou incerto sobre uma ação, simplesmente pressione `Esc` e digite `:q!`. Este comando retornará ao terminal, ignorando quaisquer mudanças não salvas.

- Em busca de uma experiência mais amigável ao trabalhar com o **código das suas aplicações**, em casa, uma ótima opção é o [Visual Studio Code](https://visualstudio.microsoft.com/pt-br/downloads/). Com o _plugin SSH Remote_, o VS Code permite conexões diretas via SSH. Além disso, para a transferência de arquivos, como código e imagens entre o _host_ e a VM, recomendamos o uso de uma ferramenta com suporte a SFTP (_Secure File Transfer Protocol_), como o [Filezilla](https://filezilla-project.org/download.php). 

- Como alternativa mais colaborativa e orientada à produtividade, podemos considerar o uso de plataformas de controle de versão, como o GitHub. Com o GitHub, você pode gerenciar e rastrear as mudanças no seu código e colaborar com outros desenvolvedores, facilitando o fluxo de trabalho e a integração contínua. 

- **Nota**: Discutiremos e apresentaremos a configuração, vantagens e desvantagens de cada uma destas abordagens em sala de aula. 

### Usando Docker e Docker Compose: Guia Básico

Recomenda-se a leitura da documentação oficial para se aprofundar, mas este guia básico é suficiente para iniciar a utilizar utilização das ferramentas. 

### Comandos do Docker:

1. **Baixar uma imagem do Docker Hub**
    ```bash
    docker pull <imagem>:<tag>
    ```

2. **Listar todas as imagens no seu sistema**
    ```bash
    docker images
    ```

3. **Rodar um contêiner a partir de uma imagem**
    ```bash
    docker run <opções> <imagem>
    ```

4. **Listar contêineres em execução**
    ```bash
    docker ps
    ```

5. **Listar todos os contêineres**
    ```bash
    docker ps -a
    ```

6. **Parar um contêiner**
    ```bash
    docker stop <contêiner_id_ou_nome>
    ```

7. **Visualizar logs de um contêiner**
    ```bash
    docker logs <contêiner_id_ou_nome>
    ```

8. **Remover um contêiner**
    ```bash
    docker rm <contêiner_id_ou_nome>
    ```

### Comandos do Docker Compose: 

1. **Iniciar serviços definidos no `docker-compose.yml` em modo interativo**
    ```bash
    docker-compose up
    ```

2. **Iniciar serviços definidos no `docker-compose.yml` em segundo plano**
    ```bash
    docker-compose up -d
    ```

3. **Parar serviços**
    ```bash
    docker-compose down
    ```

4. **Listar os serviços em execução**
    ```bash
    docker-compose ps
    ```

5. **Visualizar logs**
    ```bash
    docker-compose logs
    ```

### Limpeza de Imagens, Contêineres e Volumes: 

Na pasta `docker` deste repositório, você encontrará o script `docker-cleanup.sh` que faz a remoção de imagens antigas e desnecessárias. Isso pode ser útil para recuperar espaço no ambiente de desenvolvimento. 

1. Navegue até a pasta onde o script está localizado: 

```bash
cd caminho/para/pasta/docker
```

2. Para tornar o script executável, utilize o comando:

```bash
chmod +x docker-cleanup.sh
```

3. Execute o script:

```bash
./docker-cleanup.sh
```

- **Nota**: Este script remove recursos não utilizados e imagens antigas para recuperar espaço. Para evitar a remoção inadvertida de recursos importantes, certifique-se de entender o que ele faz antes de executá-lo. Lembre-se que, ao executá-lo, apenas os contêineres em execução serão mantidos no armazenamento da VM. 

### Pronto! 

Agora que você está com o ambiente preparado e pronto para começar os laboratórios. Em caso de dúvidas, não hesite em me contactar: [klayton.castro@ceub.edu.br](klayton.castro@ceub.edu.br). 
