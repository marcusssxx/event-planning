from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inicializar o aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model para os produtos
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Produto {self.nome}>"

# Página principal com listagem de produtos
@app.route('/')
def index():
    produtos = Produto.query.all()  # Pega todos os produtos do banco de dados
    return render_template('index.html', produtos=produtos)

# Página do produto individual
@app.route('/produto/<int:id>')
def produto(id):
    produto = Produto.query.get_or_404(id)
    return render_template('produto.html', produto=produto)

# Página para adicionar produtos
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = float(request.form['preco'])
        imagem_url = request.form['imagem_url']

        novo_produto = Produto(nome=nome, descricao=descricao, preco=preco, imagem_url=imagem_url)
        db.session.add(novo_produto)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adicionar_produto.html')

# Rodar a aplicação
if __name__ == '__main__':
    db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
