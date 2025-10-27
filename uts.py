# SOAL
# Buatalah sebuah program dengan algoritma backward chainning. untuk memvalidasi sebuah keadaan sebuah tanaman terkena suatu penyakit(penyakit bebas)minimal 7 fakta

from flask import Flask, render_template, request

app = Flask(__name__)

# Basis pengetahuan (knowledge base)
knowledge_base = {
    "Layu Bakteri": ["Daun menguning", "Batang layu"],
    "Busuk Akar": ["Akar membusuk", "Daun menguning"],
    "Karat Daun": ["Daun ada bercak coklat", "Permukaan daun berkarat"],
    "Hawar Daun": ["Daun ada bercak coklat", "Daun menguning"],
    "Klorosis": ["Daun menguning", "Pertumbuhan tanaman terhambat"],
    "Bercak Coklat": ["Daun ada bercak coklat", "Pertumbuhan tanaman terhambat"],
    "Busuk Pangkal Batang": ["Batang layu", "Akar membusuk"],
    "Layu Fusarium": ["Daun menguning", "Batang layu", "Pertumbuhan tanaman terhambat"]
}

# Daftar semua fakta yang mungkin
fakta_pertanyaan = [
    "Daun menguning",
    "Batang layu",
    "Ada lendir pada batang",
    "Akar membusuk",
    "Daun ada bercak coklat",
    "Permukaan daun berkarat",
    "Pertumbuhan tanaman terhambat"
]

@app.route('/')
def index():
    return render_template('index.html', fakta_pertanyaan=fakta_pertanyaan)

@app.route('/diagnosa', methods=['POST'])
def diagnosa():
    fakta_diketahui = request.form.getlist('fakta')

    # Backward Chaining
    hasil = []
    for penyakit, gejala in knowledge_base.items():
        if all(g in fakta_diketahui for g in gejala):
            hasil.append(penyakit)

    return render_template('result.html', hasil=hasil, fakta_diketahui=fakta_diketahui)

if __name__ == '__main__':
    app.run(debug=True)
