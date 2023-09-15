# Use uma imagem base Python
FROM python:3.9-slim

# Defina um diretório de trabalho
WORKDIR /app

# Copie o requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie arquivos necessários, como scripts de inicialização ou configurações
# Deixaremos o conteúdo fora por enquanto, já que ele será montado como um volume
COPY serve.py .
COPY pelicanconf.py .

# Expõe a porta em que o Flask estará escutando
EXPOSE 5000

# Comando para iniciar o servidor Flask
CMD ["flask", "run", "--host=0.0.0.0"]

