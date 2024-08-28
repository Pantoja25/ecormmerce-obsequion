from django.apps import AppConfig
from flask import Flask, request, render_template
import mysql.connector


class TelavendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TelaVenda'


app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'seu_banco_de_dados'
}

@app.route('/')
def form():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    Cliente = request.form['Cliente']
    Produto = request.form['Produto']
    Quantidade = request.form['Quantidade']
    Preço = request.form['Preço']

    # Conectar ao banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Inserir dados no banco de dados
    query = "INSERT INTO sua_tabela (Cliente, Produto, Quantidade, Preço) VALUES (%s, %s)"
    cursor.execute(query, (Cliente, Produto, Quantidade, Preço))
    conn.commit()

    cursor.close()
    conn.close()

    return 'Dados enviados com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)