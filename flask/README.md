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