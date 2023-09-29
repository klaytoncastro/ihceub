# Como criar seu primeiro aplicativo Web usando Flask e Python 3

## 1. Introdução

O Flask é um microframework Python para desenvolvimento ágil de aplicativos web, adequado tanto para iniciantes quanto para desenvolvedores experientes. Ele é bastante leve, ao passo que é flexível e permite expandir facilmente seu aplicativo para operar com bibliotecas avançadas em Python. Neste tutorial, você criará um aplicativo que exibe texto HTML, aprenderá sobre roteamento, interação através de rotas dinâmicas e utilizará o depurador para corrigir erros.

## 2. Implantação do Ambiente

### Pré-Requisitos

Siga as instruções contidas no repositório [IHCEUB](https://github.com/klaytoncastro/ihceub/) para implantação da VM com Docker. 

### Criando o aplicativo

Vá até o diretório `/opt/ihceub/flask` e edite o arquivo `app.py`. Insira o código para o seu primeiro aplicativo, com o clássico "Hello World!". 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
``` 

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

Você criou um pequeno aplicativo web com o Flask, adicionou rotas estáticas e dinâmicas e aprendeu a usar o depurador. A partir daqui, você pode expandir seu aplicativo, integrando-o com bancos de dados, formulários e aprimorando seu visual com CSS e HTML. Nos próximos laboratórios veremos como aplicar estes recursos em maiores detalhes. 

