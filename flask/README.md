# Como criar seu primeiro aplicativo Web usando Flask e Python 3

## 1. Introdução

O Flask é um microframework Python para desenvolvimento ágil de aplicativos web, adequado tanto para iniciantes quanto para desenvolvedores experientes. Ele é bastante leve, ao passo que é flexível e permite expandir facilmente seu aplicativo para operar com bibliotecas avançadas em Python. Neste tutorial, você criará um aplicativo que exibe texto HTML, aprenderá sobre roteamento, interação através de rotas dinâmicas e utilizará o depurador para corrigir erros.

## 2. Implantação do Ambiente

### Pré-Requisitos

Siga as instruções contidas no repositório [IHCEUB](https://github.com/klaytoncastro/ihceub/) para implantação da VM com Docker. 

### Criando o aplicativo

Vá até o diretório `/opt/ihceub/flask` e crie o arquivo `app.py`. Insira o código para o seu primeiro aplicativo com a implementação do "Hello World!": 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
``` 

Salve o arquivo. 

### Executando o aplicativo 

Vá até o diretório `/opt/ihceub/flask` e suba o contêiner do Flask. 

```bash
docker-compose build
docker-compose up -d
```

Verifique se o contêiner está ativo e sem erros de implantação. 

```bash
docker-compose logs
docker-compose ps
```

Agora, acesse `http://127.0.0.1:8500/` em seu navegador e você verá "Olá, mundo!".

## 3. Roteamento e visualizações

Vamos adicionar mais algumas rotas ao nosso aplicativo. Vá até o diretório `/opt/ihceub/flask`, edite o arquivo `app.py` e acrecente: 

```python
@app.route('/sobre')
def sobre():
    return "Sobre o aplicativo..."

@app.route('/contato')
def contato():
    return "Página de contato."
```

Agora reinicialize o contêiner: 

```bash
docker-compose down && docker-compose up -d
```

Verifique se o contêiner está ativo e sem erros de implantação. 

```bash
docker-compose logs
docker-compose ps
```

Dessa forma, você poderá acessar os *end-points* `http://127.0.0.1:8500/sobre` ou `http://127.0.0.1:8500/contato`, e verá as respectivas páginas em seu navegador. 

## 4. Rotas Dinâmicas

Vamos permitir que os usuários interajam com o aplicativo por meio de rotas dinâmicas:

```python
@app.route('/usuario/<nome>')
def saudacao(nome):
    return f"Olá, {nome}!"
```

Agora reinicialize o contêiner: 

```bash
docker-compose down && docker-compose up -d
```

Verifique se o contêiner está ativo e sem erros de implantação: 

```bash
docker-compose logs
docker-compose ps
```

Pronto, se você acessar `http://127.0.0.1:8500/usuario/Jose`, verá "Olá, Jose!" em seu navegador. 

## 5. Depurando seu aplicativo

O Flask possui um depurador embutido. Se ocorrer um erro, uma página de erro detalhada será exibida, ajudando a identificar o problema. Como já ativamos o ambiente de desenvolvimento, o depurador está habilitado por padrão. Em ambientes de produção, você pode utilizar um web server mais robusto como o Gunicorn e uWSGI. Nesse caso, para desativar o modo de depuração, acrescente a diretiva `debug=false` ao aplicativo. 

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=false)
``` 


## Conclusão

Vamos entender o código parte por parte: 

```python
#Aqui, estamos importando a classe Flask da biblioteca flask.
from flask import Flask

#Aqui estamos criando uma instância da classe Flask e atribuindo-a à variável app. O argumento __name__ é uma variável especial que retorna o nome do módulo atual. Em scripts executados diretamente, __name__ é igual a __main__. Isso indica ao Flask onde começar a procurar por coisas como templates e arquivos estáticos.
app = Flask(__name__)

#Estamos definindo uma rota para o endereço base ('/') da nossa aplicação. Quando o usuário acessar o endereço base, a função hello() será chamada e retornará a string "Olá, mundo!".
@app.route('/')
def hello():
    return "Olá, mundo!"

#Aqui, definimos outra rota ('/sobre'). Quando o usuário acessar essa rota, ele verá a mensagem "Sobre o aplicativo...".
@app.route('/sobre')
def sobre():
    return "Sobre o aplicativo..."

#Similar ao anterior, essa rota direciona o usuário para a página de contato, retornando a mensagem "Página de contato.".
@app.route('/contato')
def contato():
    return "Página de contato."

#Esta rota é um pouco mais avançada. Ela espera um valor dinâmico na URL. Por exemplo, se você acessar '/usuario/Joao', a palavra 'Joao' será capturada e passada como argumento para a função saudacao(). O resultado será "Olá, Joao!".
@app.route('/usuario/<nome>')
def saudacao(nome):
    return f"Olá, {nome}!"

#Essa é a parte do código que executa a aplicação. O código dentro do bloco if só será executado se o script for rodado diretamente (e não importado em outro script). No caso, estamos fazendo a chamada do script com Docker, conforme definido em nosso Dockerfile e docker-compose.yml
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Nota 1:** O trecho `host='0.0.0.0'` indica que o servidor ficará acessível para qualquer IP que tenha conectividade ao servidor Flask. 

**Nota 2:** O trecho `port=5000` define a porta onde o servidor estará rodando. O padrão do Flask é 5000. Mas em nossa VM de laboratório, exploramos o conceito de NAT e estamos utilizando a porta 8500. 

Então, ao executar esse script e acessar `http://127.0.0.1:8500` no seu navegador, você verá a mensagem "Olá, mundo!". Ao acessar `http://127.0.0.1:8500/sobre`, você verá "Sobre o aplicativo...", e assim por diante.

### Pronto! 

Você criou um pequeno aplicativo web com o Flask, adicionou rotas estáticas e dinâmicas e aprendeu a usar o depurador. A partir daqui, você pode expandir seu aplicativo, integrando-o com bancos de dados, formulários e aprimorando seu visual com CSS e HTML. Nos próximos laboratórios veremos como aplicar estes recursos em maiores detalhes. 