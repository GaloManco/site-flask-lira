from flask import Flask, render_template
#teste para heroku
app = Flask(__name__)

# Página main
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios/<string:name>')
def usuarioUser(name):
    return render_template('userLogin.html', userLogin=name)

# Página erro
@app.route('/<string:name>')
def erro(name):
    return render_template('erro.html', variavelErro=name)



if __name__=='__main__':
    app.run(debug=True)
