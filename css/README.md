# Instrodução ao CSS 

## 1. Visão Geral 	

Cascading Style Sheets (CSS), é uma linguagem destinada a simplificar o processo de design para tornar as páginas da web esteticamente mais atraentes. Ou seja, CSS lida com a aparência dos recursos de uma página da Web. Você pode controlar a cor do  texto, o  estilo das fontes,  o espaçamento entre parágrafos, como as colunas são dimensionadas e dispostas, quais imagens de  plano de fundo ou cores são usadas, bem como uma variedade de outros efeitos visuais, forneceNDO um controle poderoso sobre a apresentação de um documento HTML.

O CSS é criado e mantido através de um grupo de pessoas dentro do W3C chamado CSS Working Group. O Grupo de Trabalho CSS cria documentos chamados especificações. Quando uma  especificação é discutida e ratificada oficialmente pelos membros do W3C, ela se torna uma recomendação. Essas  especificações ratificadas  são chamadas de  recomendações porque o W3C não tem controle sobre a implementação real  da linguagem. Empresas  e organizações independentes  criam esse software.

**Nota**: O World Wide Web Consortium ou W3C é um grupo que faz recomendações sobre  como  a Internet funciona e como ela deve evoluir.

## 2. Vantagens do CSS 

- **Produtividade e Agilidade**: Você pode escrever CSS uma vez e, em  seguida, reutilizar a mesma planilha em várias páginas HTML. Você pode definir um estilo para cada elemento HTML e aplicá-lo a quantas páginas da web desejar.

- **Velocidade e Fluidez**: Se você estiver usando CSS, não precisará escrever atributos HTML todas as vezes. Basta codificar a regra de estilo para uma tag e aplicá-la a todas as ocorrências. Assim, as páginas serão carregadas mais rápido. 

- **Manutenibilidade**: Para fazer uma mudança global, basta alterar o estilo CSS, e todos os elementos em todas as páginas da web serão atualizados automaticamente.

- **Sofisticação da Experiência**: CSS possui uma matriz muito maior de atributos em relação ao que pode ser feito em HTML, então você pode dar uma aparência mais sofisticada à sua aplicação. Os atributos HTML estão sendo preteridos por CSS. 

- **Compatibilidade e Responsividade:**: CSS permite que o conteúdo seja otimizado para mais de um tipo de dispositivo. Assim, usando o mesmo documento HTML, diferentes versões de um site podem ser apresentadas para dispositivos portáteis, como tablets e smartphones. 

## 3. Estruturas de Layout

Para avançar mais na prática em CSS, é importante compreender sua estrutura e trazer alguns conceitos-chave que fundamentam a base para layouts mais sofisticados e dinâmicos, como Box Model, Sistemas de Layout (Flexbox / Grid) e Animações, cruciais para criar designs que se adaptam a diferentes tamanhos de tela e dispositivos, garantindo uma experiência de usuário consistente. 

### Box Model

O modelo de caixa do CSS (Box Model) é um conceito fundamental no design de páginas web, pois define como os elementos HTML são dispostos e estilizados na tela. Ele tem um papel crucial no cálculo do tamanho total de um elemento, o que é extremamente relevante no design de layouts responsivos. É composto por quatro componentes principais: content, padding, borda e margem:

- **Content**: O conteúdo (content) é a parte central do Box Model, onde o texto e as imagens de um elemento HTML são exibidos. O tamanho do conteúdo pode ser ajustado usando propriedades como `width` e `height`. É o núcleo sobre o qual são aplicados os atributos `padding`, `border` e `margin`. 

- **Padding**: É o espaço entre o conteúdo de um elemento e sua borda. Utilizado para criar espaço ao redor do conteúdo dentro de um elemento, sem alterar o tamanho da borda.

- **Border:** É a borda que circunda cada elemento HTML, que pode ser visível ou não. Usada para adicionar estilo, como largura, cor e design, ao redor de um elemento. 

- **Margin:** É o espaço ao redor de um elemento, fora de qualquer borda definida. Utilizado para criar espaço entre elementos, afetando o layout externo.

O tamanho total de um elemento é a soma do seu conteúdo (width e height), padding, border e margin. Cada um desses componentes contribui para as dimensões finais do elemento na página. Quando você define width e height para um elemento, essas propriedades controlam apenas o tamanho do conteúdo. O espaço ocupado pelo padding e border é adicionado ao tamanho final do elemento. Por exemplo, se um elemento tem uma largura (width) de 100px, um padding de 10px e uma border de 5px, a largura total será de 130px (100 + 10 + 10 + 5 + 5). 

### Sistemas de Layout e Animações

- **Flexbox**: Modelo de layout unidimensional que oferece um método eficiente para alinhar e distribuir espaço entre itens dentro de um contêiner. Ideal para layouts de componentes e situações onde o eixo principal é dinâmico ou desconhecido. As propriedades destacadas abaixo permitem um controle detalhado sobre o posicionamento e alinhamento de itens dentro de um contêiner Flexbox, tornando-o ideal para layouts responsivos. 

`flex-direction`: Controla a direção em que os itens flexíveis são colocados no contêiner flexível. Valores comuns incluem `row` (padrão) para uma disposição horizontal, e `column` para uma disposição vertical. 

`justify-content`: Alinha os itens flexíveis ao longo do eixo principal do contêiner (horizontalmente em `row`, verticalmente em `column`). Valores comuns são `flex-start`(alinha itens ao início), `flex-end` (ao fim), `center` (ao centro), `space-between` (espaço igual entre os itens) e `space-around` (espaço igual em torno dos itens).

`align-items`: Alinha itens flexíveis ao longo do eixo cruzado (perpendicular ao eixo principal). Valores comuns incluem `flex-start`, `flex-end`, `center`, `baseline`(alinhados pela linha de base dos itens) e `stretch` (estica os itens para preencher o contêiner). 

- **Grid**: Sistema bidimensional para CSS que facilita a criação de layouts complexos.
Uso: Permite a definição de áreas ou regiões principais em uma página, organizando o conteúdo de forma mais estruturada e alinhada. É bastante útil para criar layouts mais complexos e multidimensionais, de forma intuitiva e eficiente, por meio das propriedades abaixo: 

`grid-template-columns` e `grid-template-rows`: Definem o tamanho das colunas e linhas em um grid. Os valores podem ser fixos em pixels (`100px`), flexíveis (`1fr` para uma fração do espaço disponível) ou uma combinação de ambos. Por exemplo: 

```css
/* Cria três colunas, onde a coluna do meio é duas vezes mais larga que as outras */
grid-template-columns: 1fr 2fr 1fr;
```

`grid-gap`: Define o espaço entre as linhas e colunas em um grid. Por Exemplo: 

```css
/* Cria um espaço de 10px entre todas as linhas e colunas. */
grid-gap: 10px; 
```
`grid-column` e `grid-row`: Propriedades usadas dentro dos itens do grid para especificar sua localização e extensão nas colunas e linhas do grid. Por exemplo: 

```css
/* Faz com que um item abranja da primeira à terceira coluna. */
grid-column: 1 / 3; 
```
- **Animações**: Funcionalidade que permite a transição entre estilos de um elemento ao longo do tempo. Cria efeitos visuais dinâmicos, como mudanças graduais de cor, movimentos e transformações de elementos na interface do usuário. Para criar animações em CSS, você utiliza a regra `@keyframes` e estabelece suas propriedades, como os estados da animação, especificando o estilo do elemento em vários estágios. Por exemplo, você pode definir como um elemento deve aparecer no início, no meio e no final da animação. A estrutura básica envolve nomear a animação e definir porcentagens, onde 0% representa o início da animação e 100% o fim. Os principais atributos são: 

`animation-name`: Este atributo é usado para referenciar o nome dado à animação definida em `@keyframes`. Ele conecta o conjunto de regras ao elemento que você deseja animar.

`animation-duration`: Define quanto tempo a animação deve levar para completar um ciclo. Por exemplo, `animation-duration: 3s`; significa que a animação durará três segundos.

`animation-timing-function`: Especifica a velocidade da animação em diferentes pontos do ciclo de animação. Exemplos comuns incluem `linear`, `ease`, `ease-in`, `ease-out` e `ease-in-out`.

`animation-delay`: Define um atraso antes do início da animação. Por exemplo, `animation-delay: 2s`; fará a animação começar dois segundos após a página ser carregada. 

`animation-iteration-count`: Indica quantas vezes a animação deve ser repetida.
Valores comuns incluem números ou a palavra-chave `infinite` para uma animação contínua.

`animation-direction`: Define se a animação deve ser executada para frente, para trás ou alternar entre ambas as direções. Exemplos incluem `normal`, `reverse`, `alternate` e `alternate-reverse`.

`animation-fill-mode`: Determina o estilo do elemento antes e depois da execução da animação.Opções incluem `none`, `forwards`, `backwards` e `both`.

Esses atributos podem ser combinados em uma propriedade abreviada `animation` facilitando a especificação de múltiplos valores de uma só vez. Por exemplo: `animation: myAnimation 3s ease-in 1s infinite reverse;` combina nome, duração, função de tempo, atraso, contagem de iteração e direção. Ao utilizar esses atributos, os desenvolvedores podem criar uma variedade de efeitos animados, desde simples transições até animações complexas e interativas, enriquecendo a experiência do usuário. 

## 4. Exercícios

### Exercício 01: Alterando Cores e Fontes

- Crie uma rota Flask em que você exiba um parágrafo simples no arquivo HTML.
- Use CSS para estilizar o parágrafo. 
- Altere a cor do texto, o tamanho da fonte e a fonte em si. 
- Tente escolher combinações de cores e fontes atraentes. Adicione um fundo colorido ao parágrafo para realçar ainda mais a estilização.

### Exercício 02: Estilizando Botões
- Crie um botão em sua página HTML usando um elemento <button>.
- Use CSS para estilizar o botão. Altere a cor de fundo, a cor do texto, o espaçamento interno (padding) e o espaçamento externo (margin).
- Adicione uma transição suave para que a cor de fundo mude quando você passar o mouse sobre o botão.

### Exercício 03: Layout Responsivo
- Crie um layout de duas colunas em sua página HTML. Uma coluna deve ocupar 70% da largura e a outra 30%.
- Use CSS para tornar o layout responsivo. Quando a largura da tela for menor que um determinado valor (por exemplo, 768 pixels), faça as colunas se empilharem verticalmente uma sobre a outra.

### Exercício 04: Menu de Navegação
- Crie um menu de navegação horizontal em sua página HTML usando uma lista não ordenada (`<ul>`) e links de âncora (`<a>`).
- Use CSS para estilizar o menu de navegação. Adicione cores de fundo aos itens do menu quando o mouse passar por cima deles e crie um efeito de sublinhado para os links.

### Exercício 05: Formulário Estilizado
- Crie um formulário simples com campos de entrada de texto, caixas de seleção e botões.
- Use CSS para estilizar o formulário. Personalize as bordas dos campos de entrada, adicione margens, altere a fonte e a cor do texto.
- Adicione um estilo de foco para os campos de entrada, alterando a cor da borda quando o usuário os selecionar.

### Exercício 06: Utilizando uma Animação

- Criar uma animação simples que altera a cor de fundo de um elemento HTML de vermelho para amarelo. 

## 5. Implementação 

a) Edite o arquivo `app.py` e prepare as rotas conforme abaixo: 

```python
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
#    return "Olá Mundo"
    return render_template('index.html')

@app.route('/exercicio01')
def exercicio1():
    return render_template('exercicio01.html')

@app.route('/exercicio02')
def exercicio2():
    return render_template('exercicio02.html')

@app.route('/exercicio03')
def exercicio3():
    return render_template('exercicio03.html')

@app.route('/exercicio04')
def exercicio4():
    return render_template('exercicio04.html')

@app.route('/exercicio05')
def exercicio5():
    return render_template('exercicio05.html')

@app.route('/exercicio06')
def exercicio6():
    return render_template('exercicio06.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
b) Edite o arquivo `...templates/exercicio01.html` conforme abaixo: 

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 1</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <p class="paragrafo-estilizado">Este é um parágrafo estilizado.</p>
</body>
</html>
```

c) Edite o arquivo `...templates/exercicio02.html` conforme abaixo: 

```html

<!DOCTYPE html>
<html>
<head>
    <title>Exercício 2</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <button class="botao-estilizado">Clique Aqui</button>
</body>
</html>


```

d) Edite o arquivo `...templates/exercicio03.html` conforme abaixo: 

```html

<!DOCTYPE html>
<html>
<head>
    <title>Exercício 3</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="layout">
        <div class="coluna-principal">
            <p>Conteúdo da Coluna Principal</p>
        </div>
        <div class="coluna-lateral">
            <p>Conteúdo da Coluna Lateral</p>
        </div>
    </div>
</body>
</html>


```

e) Edite o arquivo `...templates/exercicio04.html` conforme abaixo: 

```html

<!DOCTYPE html>
<html>
<head>
    <title>Exercício 4</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <ul class="menu-navegacao">
        <li><a href="#">Página Inicial</a></li>
        <li><a href="#">Sobre Nós</a></li>
        <li><a href="#">Serviços</a></li>
        <li><a href="#">Contato</a></li>
    </ul>
</body>
</html>


```

f) Edite o arquivo `...templates/exercicio05.html` conforme abaixo: 

```html

<!DOCTYPE html>
<html>
<head>
    <title>Exercício 5</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <form>
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome">
        <br>
        <label for="email">Email:</label>
        <input type="text" id="email" name="email">
        <br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>

```

g) Edite o arquivo `...templates/exercicio06.html` conforme abaixo: 

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 6</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="box-animacao"></div>
</body>
</html>
```

h) Prepare a folha de estilo `.../static/style.css`: 

```css
/* Estilos para o Exercício 1 */
.paragrafo-estilizado {
    color: blue;
    font-size: 24px;
    font-family: Arial, sans-serif;
    background-color: yellow;
}

/* Estilos para o Exercício 2 */
.botao-estilizado {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    margin: 5px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
}

.botao-estilizado:hover {
    background-color: #0056b3;
}

/* Estilos para o Exercício 3 */
.layout {
    display: flex;
}

.coluna-principal {
    flex: 70%;
    background-color: lightgray;
    padding: 20px;
}

.coluna-lateral {
    flex: 30%;
    background-color: darkgray;
    padding: 20px;
}

@media (max-width: 768px) {
    .layout {
        flex-direction: column;
    }
}
/* Estilos para o Exercício 4 */
.menu-navegacao {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

.menu-navegacao li {
    display: inline;
    margin-right: 20px;
}

.menu-navegacao a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
}

.menu-navegacao a:hover {
    color: #007bff;
    text-decoration: underline;
}

/* Estilos para o Exercício 5 */
form {
    max-width: 300px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}

/* Estilos para o Exercício 6 */

.box-animacao {
    width: 100px;
    height: 100px;
    background-color: red;
}

@keyframes mudanca-cor {
    from { background-color: red; }
    to { background-color: yellow; }
}

.box-animação {
    animation-name: mudanca-cor;
    animation-duration: 2s;
}
```
## 6. Conclusão

A compreensão do Box Model, Flexbox, Grid Layout e das animações em CSS é fundamental para desenvolvedores envolvidos na criação de designs interativos, responsivos e estruturas de layout modernas, permitindo a elaboração de interfaces de usuário que não apenas se ajustam a diferentes tamanhos de tela, mas também proporcionam uma experiência agradável e dinâmica. A prática contínua e a exploração desses elementos serão cruciais para aprimorar suas habilidades em CSS. Para um estudo prático mais aprofundado em CSS, os seguintes recursos são recomendados: 

- **W3Schools - CSS Tutorial**: Uma fonte abrangente para aprender todos os aspectos do CSS, incluindo Flexbox e Grid Layout. Acesse [aqui](https://www.w3schools.com/css/). 

- **MDN Web Docs - CSS**: Documentação detalhada e tutoriais sobre CSS, oferecidos pela Mozilla, incluindo guias sobre Box Model, Flexbox e Grid Layout. Acesse [aqui](https://developer.mozilla.org/en-US/docs/Web/CSS).

- **CSS Tricks - A Complete Guide to Flexbox**: Um guia visual e detalhado para entender e usar o Flexbox. Acesse [aqui](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

- **CSS Tricks - A Complete Guide to Grid**: Guia abrangente e visual para aprender o Grid Layout. Acesse [aqui](https://css-tricks.com/snippets/css/complete-guide-grid/).

Esses recursos oferecem instruções passo a passo, exemplos práticos e dicas para aprimorar suas habilidades em CSS, apoiando a prática no desenvolvimento de layouts modernos e responsivos. 