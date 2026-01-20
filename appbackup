from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

SUPABASE_URL = "https://wicbydfuhxnsudoorsjf.supabase.co"
SECRET_KEY = "sb_secret_EzUAmnOCiurK8knt3GTvbA_o884xyRF"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viagens", methods=["POST"])
def viagens():
    try:
        data = request.get_json()
        
        dados = {
            "rota": data.get("rota"),
            "empresa": data.get("empresa"),
            "motorista": data.get("motorista"),
            "placa": data.get("placa"),
            "carga": data.get("carga"),
            "preco_km": data.get("preco_km"),
            "nf": data.get("nf"),
            "data": data.get("data")
        }
        
        url = f"{SUPABASE_URL}/rest/v1/viagens"
        headers = {
            "apikey": SECRET_KEY,
            "Authorization": f"Bearer {SECRET_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }
        
        res = requests.post(url, json=dados, headers=headers)
        
        if res.status_code in (200, 201, 204):
            return jsonify({"status": "ok", "detalhes": "Viagem salva"})
        else:
            return jsonify({"status": "erro", "detalhes": res.text}), res.status_code
            
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
