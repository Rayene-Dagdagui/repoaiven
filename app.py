from flask import Flask, jsonify, request
from flask_cors import CORS
from database_wrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)

#credenziali del db Aiven
db = DatabaseWrapper(
    host="mysql-1-projectrayenedagdagui.j.aivencloud.com",
    user="avnadmin",
    password="AVNS_R_pEgeChvcVP0iI8Ger",
    database="defaultdb",
    port=  18723
)


#restituisce tutta la lista
@app.route("/spesa", methods=["GET"])
def get_spesa():
    lista = db.get_lista_spesa()
    return jsonify(lista)

#aggiunge un elemento
@app.route("/spesa", methods=["POST"])
def aggiungi_spesa():
    dati = request.json           #prende il JSON inviato da Angular
    elemento = dati["elemento"]   #lo mettiamo in una variabile
    db.aggiungi_elemento(elemento)
    return jsonify({"msg": "Aggiunto"})
    
if __name__ == '__main__':
    app.run(debug=True)