from flask import Flask, render_template

# Cria a aplicação Flask
app = Flask(__name__)


# Rota da página inicial: quando alguém acessa "/", mostra o index.html
@app.route("/")
def index():
    return render_template("index.html")


# Só roda o servidor quando executamos "python app.py"
# debug=True recarrega o site sozinho quando você salva o arquivo
if __name__ == "__main__":
    app.run(debug=True)