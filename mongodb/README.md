# Introdução ao MongoDB

## Visão Geral

### O que é o MongoDB?

O **MongoDB** é um sistema de gerenciamento de banco de dados (SGBD) amplamente utilizado, sendo um dos representantes mais populares da categoria NoSQL (Not-only Structured Query Language) baseada em documentos. Diferentemente dos bancos de dados relacionais tradicionais, o MongoDB se destaca por sua abordagem flexível para o armazenamento de dados. Vamos explorar algumas das características-chave do MongoDB e como elas podem ser vantajosas em diferentes contextos.

- **Modelagem de Dados Orientada a Documentos**: O MongoDB é projetado para trabalhar com dados semi-estruturados e não estruturados, como registros JSON (JavaScript Object Notation), dados de sensores IoT (Internet of Things) e muito mais. Isso o torna ideal para aplicações que lidam com dados variados, assim como para prototipagem. 

- **Armazenamento BSON**: O MongoDB armazena dados em um formato chamado BSON (Binary JSON), uma extensão do formato JSON. Isso torna o armazenamento e a recuperação de dados extremamente eficiente e compatível com muitas linguagens de programação.

- **Escalabilidade Horizontal**: Uma das vantagens mais significativas do MongoDB é a escalabilidade horizontal, que permite adicionar mais instâncias para lidar com cargas de trabalho crescentes de modo distribuído. 

- **Replicação e Tolerância a Falhas**: O MongoDB suporta replicação automática, proporcionando alta disponibilidade e tolerância a falhas. Isso é crucial para garantir que os dados estejam sempre disponíveis, mesmo em caso de problemas com a infraestrutura de servidores, tornando-o adequado para pipelines de dados que exigem confiabilidade.

- **Indexação Avançada**: O MongoDB oferece recursos avançados de indexação, acelerando as consultas e melhorando o desempenho de leitura. 

- **Flexibilidade de Esquema**: O MongoDB não impõe uma estrutura rígida para os dados. Cada documento pode ter campos diferentes, proporcionando flexibilidade no design do banco de dados. Isso é vantajoso em vários cenários, pois permite a evolução contínua do esquema à medida que novos requisitos surgem.

### O que é o MongoDB Express?

O **MongoDB Express** é uma interface gráfica que facilita a administração, gerenciamento e visualização de dados armazenados em bancos de dados MongoDB. Ele oferece uma série de recursos úteis, tornando a realização do trabalho com documentos muito mais acessível. Alguns aspectos importantes do MongoDB Express incluem:

- **Interface Gráfica Amigável**: oferece uma interface de usuário intuitiva que permite explorar e interagir com os dados de forma visual.

- **Gerenciamento de Coleções e Bancos de Dados**: é possível criar, editar e excluir coleções e bancos de dados, tornando o gerenciamento de dados mais conveniente.

- **Consultas Interativas**: os usuários podem realizar consultas interativas aos dados sem a necessidade de escrever consultas manualmente.

- **Visualização de Índices**: os índices existentes podem ser visualizados e gerenciados por meio da interface.

Dessa forma, MongoDB e MongoDB Express são ferramentas complementares que simplificam a gestão do ambiente, permitindo que os desenvolvedores e administradores trabalhem de forma eficiente com dados dinâmicos em uma abordagem robusta e, ao mesmo tempo, flexível. 

## Configurando o Ambiente

1. O dimensionamento apropriado de recursos depende das necessidades específicas do seu projeto. De modo a garantir um desempenho adequado e evitar problemas com os contêineres, ajuste a quantidade de memória nas configurações de Sistema na VM VirtualBox conforme orientações abaixo: 

- Se sua atividade estiver focada exclusivamente no MongoDB, é aconselhável alocar no mínimo 1536MB de RAM. Lembre-se que, para promover as alterações, sua VM deve estar desligada. 
- Caso pretenda utilizar outras ferramentas, como o Jupyter em conjunto com o MongoDB, é recomendável alocar no mínimo 3072MB de RAM. 

2. Após os promover os ajustes, inicie a VM. Lembre-se que você deve trabalhar sempre com a versão mais recente do repositório [IHCEUB](https://github.com/klaytoncastro/ihceub). Navegue até o diretório onde você clonou o repositório (`cd /opt/ihceub`) e obtenha as respectivas atualizações com o comando abaixo: 

```bash
git pull origin main
```

3. Se este for seu primeiro acesso, vá até o diretório `/opt/ihceub/mongodb` e certifique-se que o script `wait-for-it.sh` tenha permissão de execução: 

```bash
cd /opt/ihceub/mongodb
chmod +x wait-for-it.sh
```

4. Execute os contêineres do MongoDB e MongoDB Express: 

```bash
docker-compose up -d
```

5. Verifique se os contêineres estão ativos e sem erros de implantação: 

```bash
docker ps
docker-compose logs
```
## Acesso GUI: MongoDB Express 

1. Acesse o MongoDB Express pelo navegador (`http:\\localhost:8081`). Clique em `Create Database` e crie uma base de dados chamada `AulaDemo`. Dentro da base de dados `AulaDemo`, clique em `Create Collection` e crie a coleção `Estudantes`. 

2. Clique na coleção `Estudantes` e depois em `Insert Document`. Insira um estudante com atributos como `nome`, `idade` e `curso`. Exemplo: 

```json
    {
        "nome": "João Leite",
        "idade": 22,
        "curso": "Engenharia da Computação",
        "email": "joao.leite@email.com"
    }
```

3. Insira mais um estudante. Exemplo: 

```json
    {
        "nome": "Domitila Canto",
        "idade": 22,
        "curso": "Letras",
        "email": "domitila.canto@email.com"
    }
```

4. Selecione um documento e clique em `Edit Document`. Altere algum campo. Por exemplo, mude a `idade` de um estudante. 
5. Na parte inferior da tela, observe o índice padrão `_id`. Crie um novo índice, por exemplo, para o campo `nome`. 
6. Selecione um documento e clique em `Delete Document`. 

## Acesso CLI: MongoDB 

1. Acesse o Shell do Contêiner MongoDB: 
```bash
docker exec -it mongo_service /bin/bash
```
2. Autentique-se no MongoDB: 
```bash
mongo -u root -p mongo
```
### Guia Básico: MongoDB Query Language

A linguagem de query do MongoDB (MQL) permite que você consulte, atualize e manipule documentos de forma eficiente. Seguem alguns exemplos de comandos:

```javascript
//Mostrar todas as bases de dados
show dbs
```

```javascript
//Mostrar a base de dados atual
db
```

```javascript
//Criar ou mudar de base de dados
use AulaDemo2
```

```javascript
//Apagar a base de dados
db.dropDatabase()
```

```javascript
//Mostrar as coleções
use AulaDemo
show collections
```

```javascript
//Criar uma coleção chamada "Estudantes2022"
db.createCollection("Estudantes2022")
```

```javascript
//Inserir um registro
db.Estudantes.insert(
    {
        "nome": "Fernando Campos",
        "idade": 22,
        "curso": "Engenharia da Computação",
        "email": "fernando.campos@email.com",
        "data": Date()
    }
)
```

```javascript
//Inserir vários registros
db.Estudantes.insertMany([
    {
        "nome": "Mariano Rodrigues",
        "idade": 20,
        "curso": "Design Gráfico",
        "email": "mariano.rodrigues@email.com"
    },
    {
        "nome": "Roberta Lara",
        "idade": 23,
        "curso": "Ciência da Computação",
        "email": "roberta.lara@email.com"
    },
    {
        "nome": "Juliano Pires",
        "idade": 21,
        "curso": "Artes Visuais",
        "email": "juliano.pires@email.com"
    },
    {
        "nome": "Felicia Cardoso",
        "idade": 22,
        "curso": "Matemática Aplicada",
        "email": "felicia.cardoso@email.com"
    }, 
    {
        "nome": "Haroldo Ramos",
        "idade": 22,
        "curso": "Ciência da Computação",
        "email": "haroldo.ramos@email.com",
        "matricula": "CC12345",
        "notas": { algoritmos: 85, poo: 90, calculo: 80 },
        "media": 85,
        "status": "Ativo",
        "anoIngresso": 2020
    }
  ]    
)
```
Como vimos, o MongoDB permite adotar um dinâmico. Aos poucos, podemos acrescentar campos mais detalhados para a base de estudantes. No exemplo acima, inserimos campos adicionais relativos ao estudante "Haroldo Ramos": 

`matricula`: Um identificador único para cada estudante.

`notas`: Um objeto contendo as notas do estudante em diferentes disciplinas. As disciplinas listadas são apenas exemplos e podem ser adaptadas conforme necessário.

`media`: A média de notas do estudante. Pode ser calculada com base nas notas fornecidas.

`status`: Indica se o estudante está ativo, inativo, formado, etc.

`anoIngresso`: O ano em que o estudante ingressou no curso.

Este modelo permite uma ampla gama de consultas, como buscar estudantes por curso, status, média de notas ou ano de ingresso. Além disso, você pode adicionar outros campos conforme necessário, como endereço, telefone de contato, entre outros. Adicionar um campo de `notas` como um objeto também permite que você adicione ou remova disciplinas facilmente sem alterar a estrutura do documento. 

Assim, à medida que novos requisitos surgem, você pode simplesmente adicionar novos campos aos documentos já inseridos, sem afetar a utilidade dos dados existentes. Os documentos não precisam conter campos em branco quando as informações não se aplicam a um determinado registro. Isso economiza espaço de armazenamento e torna os documentos mais concisos e evita a necessidade de migrações complexas de esquema. Adicione mais dados à sua coleção: 

```javascript
db.Estudantes.insertMany([
    {
        "nome": "Vladimir Silva",
        "idade": 22,
        "curso": "Engenharia da Computação",
        "email": "vladimir.silva@email.com",
        "matricula": "EC54321",
        "notas": {
            "matematica": 85,
            "programacao": 90,
            "fisica": 80
        },
        "media": 85,
        "status": "Ativo",
        "anoIngresso": 2020
    },
    {
        "nome": "Deocleciano Oliveira",
        "idade": 20,
        "curso": "Design Gráfico",
        "email": "deocleciano.oliveira@email.com",
        "matricula": "DG12345",
        "notas": {
            "designBasico": 92,
            "ilustracao": 89,
            "fotografia": 93
        },
        "media": 91.33,
        "status": "Ativo",
        "anoIngresso": 2021
    },
    // ... adicione mais estudantes seguindo o mesmo formato
])
```

### Uso de Operadores

No MongoDB, o operador `$` é usado para acessar as funcionalidades de consulta, atualização, projeção e agregação, ou seja, indica que determinada operação deve ser aplicada a um campo ou valor nos documentos. Seguem alguns exemplos de operadores frequentemente utilizados: 

```javascript
//Os operadores de comparação, como $eq, $ne, $gt, $lt, $gte e $lte, são usados em consultas para comparar valores em campos.

db.Estudantes.find({ idade: { $gte: 18 } }).pretty() // Aqui estamos encontrando documentos cuja idade dos estudantes seja maior ou igual a 18.
```

```javascript
//Os operadores de projeção são usados em operações de agregação para selecionar campos específicos para inclusão ou exclusão nos resultados. 

db.Estudantes.aggregate([
    { $project: { nome: 1, curso: 1, _id: 0 } } // Projeta (seleciona) apenas os campos 'nome' e 'curso'.
])
```

```javascript
//Os operadores também podem ser usados para definir os campos de agrupamento.

db.Estudantes.aggregate([
    { $group: { _id: "$curso", total: { $sum: 1 } } } // Agrupa documentos pelo campo 'curso'.
])
```

```javascript
//Ao trabalhar com arrays, podemos utilizar referenciar os elementos e usar operadores para refinar a consulta. 

db.Estudantes.find({ "notas.algoritmos": { $gte: 80 } }).pretty() // Aqui estamos encontrando os estudantes que tiraram nota maior ou igual a 80 em Algoritmos e formatando a saída com o método Pretty(). 
```

```javascript
//Ao trabalhar com atualização de documentos, podemos utilizar os operadores para modificar os campos desejados.  

db.Estudantes.updateOne({ nome: "Haroldo Ramos" }, { $set: { status: "Inativo" } })
```

A seguir, vamos praticar mais alguns comandos básicos do MongoDB, que permitem consultar, manipular e analisar documentos em suas coleções: 

```javascript
//Obter todos os registros
db.Estudantes.find()
```

```javascript
//Obter todos os registros formatados 
db.Estudantes.find().pretty()
```

```javascript
//Procurar registros por curso
db.Estudantes.find({curso: 'Engenharia da Computação'}).pretty()
```

```javascript
//Ordenar registros por nome, de forma ascendente
db.Estudantes.find().sort({nome: 1}).pretty()
```

```javascript
//Ordenar registros por nome, de forma descendente
db.Estudantes.find().sort({nome: -1}).pretty()
```
As variáveis desempenham um papel importante no MongoDB Aggregation Framework e permitem que você armazene valores intermediários durante a execução de uma operação. Elas podem ser declaradas e utilizadas para tornar mais legível a obtenção dos resultados. Seguem exemplos: 

```javascript
// Contar Registros
var count = db.Estudantes.find().count();
print("Número de registros na coleção Estudantes: " + count);
```

```javascript
// Contar Registros por curso
var count = db.Estudantes.find({ curso: 'Engenharia da Computação' }).count();
print("Número de registros na coleção Estudantes com curso 'Engenharia da Computação': " + count);
```

```javascript
//Limitar exibição de linhas
db.Estudantes.find().limit(2).pretty()
```

```javascript
//Encadeamento
db.Estudantes.find().limit(3).sort({nome: 1}).pretty()
```

```javascript
//Para buscar estudantes com média acima de 80:
db.Estudantes.find({ media: { $gt: 80 } }).pretty()
```

```javascript
//Para atualizar a média de um estudante específico (por exemplo, "Deocleciano Oliveira"):
db.Estudantes.update({ nome: "Deocleciano Oliveira" }, { $set: { media: 92 } })
```

```javascript
//Para criar um índice no campo "nome":
db.Estudantes.createIndex({ nome: 1 })
```

```javascript
//Para realizar agregação e contar quantos estudantes estão em cada curso. 
db.Estudantes.aggregate([
    {
        $sortByCount: "$curso"
    }
])
```

```javascript
//Para deletar um estudante específico:
db.Estudantes.remove({ nome: "Vladimir Silva" })
```

```javascript
//Para sair do shell do MongoDB:
exit
```

## Pipelines de Dados

Um pipeline constitui uma série de etapas pelas quais os documentos passam, onde cada etapa efetua uma operação específica no conjunto de dados. Essas etapas são executadas em sequência, permitindo que você processe e transforme os documentos de maneira controlada. 

### Operações do Pipeline

Cada etapa no pipeline é representada por um estágio. Os estágios podem incluir operações de filtro, projeção, ordenação, agrupamento, cálculos e muito mais. Alguns dos estágios comuns incluem:

`$match`: Filtra documentos com base em critérios específicos, permitindo que você selecione apenas os documentos que atendam a determinadas condições.

`$project`: Permite projetar (selecionar) campos específicos dos documentos, criando novos documentos com as informações desejadas.

`$sort`: Ordena os documentos com base nos valores de um campo específico, seja em ordem ascendente ou descendente.

`$group`: Agrupa os documentos com base em um ou mais campos-chave e realiza operações de agregação, como soma, média, contagem, entre outras.

`$unwind`: Desconstrói arrays em documentos, gerando um novo documento para cada elemento do array. Isso é útil quando você deseja realizar operações em elementos de arrays.

`$lookup`: Realiza uma operação de junção (join) entre duas coleções para combinar dados de diferentes fontes.

`$addFields`: Adiciona novos campos aos documentos ou modifica campos existentes.

`$out`: Escreve os resultados da agregação em uma nova coleção.

### Carga de Dados

Segue um exemplo básico de pipeline de dados utilizando recursos do MongoDB Aggregation Framework para análise de dados. Considerando uma coleção chamada `Vendas` com documentos que representam vendas de produtos, desejamos calcular a receita total por categoria de produto. Você pode usar os dados a seguir para inserir dados na coleção `Vendas`:

```javascript
db.Vendas.insertMany([
    {
        "produto": "Laptop",
        "categoria": "Eletrônicos",
        "valor": 1200.00
    },
    {
        "produto": "Smartphone",
        "categoria": "Eletrônicos",
        "valor": 800.00
    },
    {
        "produto": "Livros",
        "categoria": "Livraria",
        "valor": 300.00
    },
    {
        "produto": "Televisor",
        "categoria": "Eletrônicos",
        "valor": 1500.00
    },
    {
        "produto": "Tablet",
        "categoria": "Eletrônicos",
        "valor": 600.00
    },
    {
        "produto": "Fones de Ouvido",
        "categoria": "Eletrônicos",
        "valor": 100.00
    },
    {
        "produto": "Máquina de Café",
        "categoria": "Eletrodomésticos",
        "valor": 250.00
    },
    {
        "produto": "Console de Videogame",
        "categoria": "Eletrônicos",
        "valor": 450.00
    },
    {
        "produto": "Roupas",
        "categoria": "Moda",
        "valor": 50.00
    },
    {
        "produto": "Cadeira de Escritório",
        "categoria": "Móveis",
        "valor": 200.00
    },
    {
        "produto": "Instrumento Musical",
        "categoria": "Arte e Música",
        "valor": 700.00
    },
    {
        "produto": "Tênis Esportivo",
        "categoria": "Esportes",
        "valor": 120.00
    },
    {
        "produto": "Bicicleta",
        "categoria": "Esportes",
        "valor": 350.00
    },
    {
        "produto": "Ferramentas",
        "categoria": "Ferramentas",
        "valor": 80.00
    },
    {
        "produto": "Jogos de Tabuleiro",
        "categoria": "Jogos",
        "valor": 40.00
    },
    {
        "produto": "Decoração de Casa",
        "categoria": "Casa e Jardim",
        "valor": 120.00
    },
    {
        "produto": "Artigos de Beleza",
        "categoria": "Beleza",
        "valor": 90.00
    }
    // Adicione mais documentos conforme necessário
  ]
)
```

### Exemplo de Utilização

No exemplo abaixo, no primeiro estágio `$group`, estamos agrupando os documentos por categoria (`$categoria`) e calculando a receita total para cada categoria usando `$sum`. No segundo estágio `$sort`, estamos ordenando os resultados com base na receita total em ordem descendente. Isso nos dará uma lista das categorias de produtos com a receita total calculada para cada uma delas.

```javascript
db.Vendas.aggregate([
    {
        $group: {
            _id: "$categoria",
            receitaTotal: { $sum: "$valor" }
        }
    },
    {
        $sort: { receitaTotal: -1 }
    }
])
```

Suponha que você deseja calcular a média de preço por categoria de produto. Aqui está um exemplo de um pipeline de agregação: 

```javascript
db.Vendas.aggregate([
    {
        $group: {
            _id: "$categoria",
            totalPreco: { $sum: "$valor" },
            totalProdutos: { $sum: 1 }
        }
    },
    {
        $addFields: {
            mediaPreco: { $divide: ["$totalPreco", "$totalProdutos"] }
        }
    },
    {
        $project: {
            _id: 0,
            categoria: "$_id",
            mediaPreco: 1
        }
    }
])
```
Neste exemplo, estamos usando `$totalPreco` e `$totalProdutos` para armazenar os valores somados dos preços e a contagem total de produtos para cada categoria. Em seguida, usamos `$mediaPreco` para calcular a média, dividindo `$totalPreco` por `$totalProdutos`. Por fim, projetamos os resultados para tornar o formato de exibição mais amigável. 

## Ferramentas para Ingestão de Dados e Administração do Ambiente

### Importação de Dados

O `mongoimport` é uma ferramenta de linha de comando que permite importar dados de arquivos externos, como JSON ou CSV, para uma coleção. Isso pode ser útil quando você deseja preencher uma coleção com dados existentes ou migrar dados de uma fonte externa para o MongoDB, alimentando esta coleção com dados iniciais obtidos a partir de um arquivo. Exemplo de uso: 

```bash
mongoimport --db MeuBancoDeDados --collection MinhaColecao --file dados.json
```

### Backup e Restauração de Dados

O `mongodump` é uma ferramenta de linha de comando que permite criar backups completos ou parciais de seus bancos de dados MongoDB, que podem ser úteis para a recuperação de dados em caso de perda de dados devido a falhas ou erros de operação. Exemplo de uso: 

```bash
mongodump --db MeuBancoDeDados --out /caminho/para/diretorio_de_backup
```

Assim, em caso de falha do sistema ou perda de dados, você pode usar o `mongorestore` (ferramenta complementar ao `mongodump`) para restaurar seus dados a partir dos backups. 

### Outras Considerações e Ferramentas

Além do MongoDB Express, você também pode experimentar a ferramenta [MongoDB Compass](https://www.mongodb.com/try/download/compass) para obter uma experiência de visualização e consulta ainda mais avançada. É uma opção útil para desenvolvedores e administradores que preferem uma GUI (interface gráfica de usuário) para interagir com bancos de dados MongoDB.

O [Robo3T](https://robomongo.org/), anteriormente conhecido como Robomongo, é outra GUI para gerenciamento de bancos de dados MongoDB. Ela fornece uma interface intuitiva que permite criar, editar e consultar seus bancos de dados e também oferece recursos como autocompletar, formatação de consulta, suporte a múltiplas conexões e visualização de documentos BSON. 

O [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) é a proposta de banco de dados como serviço (DBaaS - Database as a Service) fornecida pela MongoDB Inc. Oferece uma plataforma de nuvem para hospedar, gerenciar e dimensionar seus bancos de dados MongoDB. Ao implantar bancos de dados como serviço gerenciado, você facilita tarefas de administração, tais como backup e restauração de dados, configuração de alta disponibilidade, recursos de elasticidade (escalabilidade rápida e automática), monitoramento de desempenho e disponibilidade de seus clusters, e muito mais. 

## Conclusão

Esta documentação fornece uma visão geral acerca dos aspectos essenciais do MongoDB, uma das soluções mais populares e poderosas para gerenciamento e análise de dados no contexto de Big Data e NoSQL. Exploramos a flexibilidade de esquema do MongoDB, sua linguagem e recursos avançados de consulta (MQL) e agregação (MAF). Vimos que o MongoDB Express proporciona uma interface gráfica (GUI) amigável para gerenciamento de bases de dados MongoDB, tornando mais acessível o trabalho com documentos. Para aprofundar seu conhecimento, consulte a documentação oficial do [MongoDB](https://docs.mongodb.com/). 