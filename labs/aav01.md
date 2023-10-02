## Atividade Avaliativa 01

### Retrospectiva

Ao longo do curso, exploramos a relação entre pessoas e tecnologia. Entendemos o que é a Interação Humano-Computador (IHC) e como o User Centered Design (UCD) prioriza o usuário no processo de criação de produtos. Aprendemos sobre Experiência do Usuário (UX) e como ela se diferencia da Interface do Usuário (UI). Com o usuário no coração do processo de design, introduzimos o Design Thinking, uma metodologia que busca solucionar problemas de forma ágil, inovadora, iterativa, colaborativa e multidisciplinar. Com base nestes conceitos e nos conhecimentos discutidos em sala de aula, responda as questões a seguir. 

### Fundamentos: IHC, UCD, UX e UI no Design de Produtos (Total: 1,4 pontos) 

**Questão 1:** (0,35 pontos) O que é Interação Humano-Computador (IHC) e por que ela é importante no design de produtos de tecnologia? 

**Questão 2:** (0,35 pontos) Defina o User-Centered Design (UCD) e descreva três de seus princípios.

**Questão 3:** (0,35 pontos) No contexto de design de produtos, o que diferencia Experiência do Usuário (UX) de Interface do Usuário (UI)? Forneça um exemplo.

**Questão 4:** (0,35 pontos) Por que é importante ter um entendimento claro dos requisitos do usuário e de suas tarefas quando se cria uma solução de design? 

### Prática: Configuração do Ambiente de Laboratório e Execução do Flask (Total: 1,6 pontos)

Durante os encontros desta disciplina, introduzimos a prática de desenvolvimento web usando o microframework Flask. Enfatizamos a importância de uma infraestrutura portátil, baseada em contêineres, para garantir um ambiente de desenvolvimento isolado e replicável. Utilizamos Docker e Docker Compose como ferramentas essenciais para criar e orquestrar as aplicações. O foco da avaliação estará em sua capacidade de executar um contêiner Flask corretamente, um pré-requisito para realizar as atividades práticas mais avançadas no contexto de desenvolvimento de produtos web que abordaremos posteriormente no curso. 

**Questão 5:** 

a) Se estiver usando nossa VM pré-configurada (método preferencial), adote as instruções fornecidas no [README.md](https://github.com/klaytoncastro/ihceub/README.md) do repositório [https://github.com/klaytoncastro/ihceub](https://github.com/klaytoncastro/ihceub). Certifique-se de que a VM está executando e que você pode acessá-la via SSH. 

b) Caso tenha optado por hospedar os contêineres diretamente em sua máquina física, certifique-se de ter o Docker e o Docker Compose corretamente instalados. 

c) Em nosso repositório [ihceub](https://github.com/klaytoncastro/ihceub), adote as instruções fornecidas no [README.md](https://github.com/klaytoncastro/ihceub/blob/main/flask/README.md) da supbasta `flask`. Como vimos em sala de aula, trata-se de um tutorial para implementação de um aplicativo web básico utilizando o Flask. 

d) (0,6 pontos) Capture um print da tela do seu terminal com o resultado do comando `docker ps`, exibindo o contêiner Flask em execução. 

e) (1 ponto) Capture um print da tela do seu navegador ao acessar a URL da rota dinâmica que você implementou conforme o Item 4 do tutorial de Flask. Ao acessar o *end-point* `http://127.0.0.1:8500/usuario/<seu_nome>`, **o navegador deve mostrar o seu nome corretamente**.