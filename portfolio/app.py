from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(port=8085, host='0.0.0.0', debug=True, threaded=True)