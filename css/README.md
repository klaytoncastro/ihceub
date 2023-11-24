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

## 3. Exercícios

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

## 4. Implementação 

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

g) Prepare a folha de estilo: 

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