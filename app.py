"""
app.py - Student Score Predictor & Report Card (Sesi 15 - Mini Project).

Prediksi nilai akhir siswa berdasarkan jam belajar dan kehadiran,
memakai model regresi linear yang dilatih di Sesi 9.

Jalankan dengan:
    streamlit run app.py
"""
import sqlite3

import joblib
import pandas as pd
import streamlit as st

st.title("Student Score Predictor & Report Card")
st.write("Prediksi nilai akhir siswa berdasarkan jam belajar dan kehadiran, memakai model regresi yang dilatih di Sesi 9.")

bundle = joblib.load("score_model.pkl")
model = bundle["model"]
feature_cols = bundle["feature_cols"]

DB_PATH = "riwayat_nilai.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prediksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours REAL,
            attendance REAL,
            prediksi_nilai REAL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

st.write("### Form Prediksi")
with st.form("form_prediksi"):
    study_hours = st.slider("Jam Belajar per Hari", 0.0, 12.0, 4.0, step=0.5)
    attendance = st.slider("Persentase Kehadiran (%)", 0.0, 100.0, 80.0, step=1.0)
    submit = st.form_submit_button("Prediksi Nilai")

if submit:
    row = {"study_hours": study_hours, "attendance": attendance}
    X = pd.DataFrame([row])[feature_cols]
    prediksi_nilai = model.predict(X)[0]

    st.write("### Prediksi Nilai Akhir:", round(prediksi_nilai, 1))

    if prediksi_nilai >= 85:
        st.success("Kategori: Sangat Baik")
    elif prediksi_nilai >= 70:
        st.info("Kategori: Baik")
    elif prediksi_nilai >= 55:
        st.warning("Kategori: Cukup - perlu tingkatkan jam belajar")
    else:
        st.error("Kategori: Perlu Perhatian - konsultasi dengan pengajar disarankan")

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO prediksi (study_hours, attendance, prediksi_nilai) VALUES (?, ?, ?)",
        (study_hours, attendance, prediksi_nilai),
    )
    conn.commit()
    conn.close()

st.write("### Riwayat Prediksi")
conn = sqlite3.connect(DB_PATH)
riwayat_df = pd.read_sql_query("SELECT * FROM prediksi ORDER BY id DESC", conn)
conn.close()
st.dataframe(riwayat_df)

st.write("### Feature Importance (Koefisien Regresi)")
importances = pd.Series(model.coef_, index=feature_cols)
st.bar_chart(importances)
