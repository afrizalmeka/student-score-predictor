# Student Score Predictor & Report Card

Mini Project Sesi 15 (Python Programming for AI - Batch 8) - Project 1 dari 5 opsi. Memprediksi nilai akhir siswa berdasarkan jam belajar dan kehadiran, memakai model regresi linear yang dilatih di Sesi 9.

Cocok untuk peserta dengan latar belakang campuran / non-IT - project paling sederhana, tanpa dependensi eksternal (tidak pakai LLM API).

## Status

Aplikasi ini **sudah 100% jadi** dan siap dijalankan langsung - tidak ada bagian kosong yang perlu diisi. Cocok dipakai sebagai referensi belajar: baca `app.py` untuk lihat bagaimana model regresi (Sesi 9), SQLite (Sesi 6), dan Streamlit (Sesi 14) digabung jadi 1 aplikasi utuh, termasuk feature importance (koefisien regresi) sebagai bar chart.

## Struktur Folder

```
student-score-predictor/
├── app.py                     # Streamlit - dashboard (skeleton, ada TODO)
├── score_model.pkl            # Model regresi terlatih dari Sesi 9
├── student_performance.csv    # Dataset asli
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalasi

Gunakan virtual environment agar paket project ini tidak bentrok dengan paket Python lain yang sudah terpasang di sistem kamu (mis. error `command not found: streamlit` atau `ImportError` pada scipy/sklearn biasanya disebabkan oleh instalasi global yang tercampur):

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan

Setelah semua TODO diisi:

```bash
source .venv/bin/activate      # jika belum aktif
streamlit run app.py
```

## Troubleshooting

- **`zsh: command not found: streamlit`** — venv belum diaktifkan, atau instalasi sebelumnya masuk ke `~/Library/Python/...` yang tidak ada di PATH. Aktifkan venv (`source .venv/bin/activate`) lalu jalankan lagi, atau jalankan sementara dengan `python3 -m streamlit run app.py`.
- **`ImportError` dari `scipy/sparse/linalg/_propack/...`** — biasanya wheel scipy yang ter-install rusak/tidak cocok dengan arsitektur CPU (Apple Silicon vs Intel). Perbaiki dengan menginstal ulang di dalam venv:
  ```bash
  pip uninstall -y scipy numpy
  pip install --no-cache-dir numpy scipy
  ```
- Pastikan `python3 -c "import platform; print(platform.machine())"` dan `uname -m` menunjukkan arsitektur yang sama. Jika berbeda, Python kamu berjalan dalam mode emulasi (Rosetta) — install ulang Python versi native untuk arsitektur mesin kamu.

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 9 (Linear Regression), dan Sesi 14 (Streamlit deployment).
