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

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
