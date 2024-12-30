from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route utama untuk menampilkan form penyakit jantung
@app.route('/heart-disease-form', methods=['GET'])
def heart_disease_form():
    return render_template('form.html')

# Route untuk menerima data dari form
@app.route('/heart-disease', methods=['POST'])
def heart_disease():
    # Ambil data dari form
    data = {
        "age": request.form.get("age"),
        "sex": request.form.get("sex"),
        "cp": request.form.get("cp"),
        "trestbps": request.form.get("trestbps"),
        "chol": request.form.get("chol"),
        "fbs": request.form.get("fbs"),
        "restecg": request.form.get("restecg"),
        "thalach": request.form.get("thalach"),
        "exang": request.form.get("exang"),
        "oldpeak": request.form.get("oldpeak"),
        "slope": request.form.get("slope"),
        "ca": request.form.get("ca"),
        "thal": request.form.get("thal")
    }

    # Validasi jika semua field ada
    required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    missing_fields = [field for field in required_fields if not data.get(field)]

    if missing_fields:
        return jsonify({"error": "Missing fields", "fields": missing_fields}), 400

    # Lakukan sesuatu dengan data, misalnya prediksi atau menyimpan ke database (di sini hanya menampilkan kembali data)
    return jsonify({"message": "Data received successfully", "data": data}), 200

# Route untuk mengecek apakah API berjalan
@app.route('/')
def home():
    return "Heart Disease Form API is running!"

if __name__ == '__main__':
    app.run(debug=True)
