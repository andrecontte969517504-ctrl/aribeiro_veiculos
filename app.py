
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# -----------------------------------------------
# CONFIGURAÇÃO SUPABASE
# -----------------------------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://wicbydfuhxnsudoorsjf.supabase.co")
SECRET_KEY = os.getenv("SECRET_KEY", "sb_secret_EzUAmnOCiurK8knt3GTvbA_o884xyRF")

# -----------------------------------------------
# ROTAS GET
# -----------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viagens")
def viagens_page():
    return render_template("viagens.html")

# -----------------------------------------------
# ROTA POST - INSERIR VIAGEM
# -----------------------------------------------
@app.route("/nova_viagem", methods=["POST"])
def nova_viagem():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "erro", "detalhes": "Nenhum dado recebido"}), 400

        url = f"{SUPABASE_URL}/rest/v1/viagens"
        headers = {
            "apikey": SECRET_KEY,
            "Authorization": f"Bearer {SECRET_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }

        res = requests.post(url, json=data, headers=headers)

        if res.status_code in (200, 201, 204):
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "erro", "detalhes": res.text}), res.status_code

    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500


# -----------------------------------------------
# EXECUTAR LOCALMENTE
# -----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
