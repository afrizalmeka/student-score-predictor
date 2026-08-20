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

```bash
pip install -r requirements.txt
```

## Menjalankan

Setelah semua TODO diisi:

```bash
streamlit run app.py
```

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 9 (Linear Regression), dan Sesi 14 (Streamlit deployment).
