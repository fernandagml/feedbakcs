from flask import Flask as F, render_template as rt, request as rq, redirect as red

app = F(__name__)
app.secret_key = "acai"

lc = []

@app.route("/")
def index():
    return rt("index.html")

@app.route("/sobremim")
def sobremim():
    return rt("sobremim.html")

@app.route("/login", methods=["GET"])
def login():
    return rt("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    usuario = rq.form.get("usuario")
    senha = rq.form.get("senha")
    if usuario == "Fernanda" and senha == "123":
        return rt("comentarios.html")
    else:
        return rt("login.html", erro = "Acesso Negado!")

@app.route("/comentarios")
def comentarios():
    return rt("comentarios.html", lc = lc)

@app.route("/add_comentarios", methods=["POST"])
def add_comentario():
    comentario = rq.form.get("comentario")
    lc.append(comentario)
    print(lc)
    return red("/comentarios")

app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)