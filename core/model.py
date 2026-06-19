import joblib
import numpy as np
import streamlit as st

from core.config import JOBLIB_DIR


@st.cache_resource(show_spinner="⚙️  Memuat model ICRI…")
def load_artifacts():
    model    = joblib.load(JOBLIB_DIR / "best_model_icri.pkl")
    scaler   = joblib.load(JOBLIB_DIR / "scaler_icri.pkl")
    encoders = joblib.load(JOBLIB_DIR / "encoders_icri.pkl")
    fcols    = joblib.load(JOBLIB_DIR / "feature_cols_icri.pkl")
    return model, scaler, encoders, fcols


def auto_calculate(ui: dict) -> dict:
    """
    Menghitung 5 fitur teknis secara otomatis dari input user.
    Model tetap menerima 18 fitur — tidak ada perubahan pipeline.

    Sumber asumsi:
      indeks_kepatuhan : pipeline S2 (0.6–0.9 jika dijaga, 0.1–0.4 jika tidak)
                         → pakai nilai tengah 0.75 / 0.25
      volume_kendaraan : nilai tengah distribusi training per kelas_jalan
      sudut_perpotongan: rata-rata dataset ~70° (sangat jarang diketahui user)
      jarak_rs_m       : median eksponensial skala 5000m kota Bandung
      jarak_pandang_m  : estimasi kualitas jalan (buruk=30, sedang=55, baik=90)
    """
    full = ui.copy()

    full["indeks_kepatuhan"]  = 0.75 if full["dijaga"] == 1 else 0.25
    full["volume_kendaraan"]  = {"arteri": 850, "kolektor": 380, "lokal": 110}[full["kelas_jalan"]]
    full["sudut_perpotongan"] = 70.0
    full["jarak_rs_m"]        = 5000
    full["jarak_pandang_m"]   = {0: 30.0, 1: 55.0, 2: 90.0}[full["kondisi_jalan"]]

    return full



def predict_icri(ui: dict) -> dict:
    """
    Wrapper predict_single() versi Streamlit dengan auto-calculation layer.
    Input : 13 fitur user-friendly
    Output: label, probabilitas per kelas, dan detail fitur auto-calculated
    """
    model, scaler, encoders, feature_cols = load_artifacts()
    full = auto_calculate(ui)
    row  = full.copy()

    # Encode kategorikal → sesuai urutan training
    for col, le_ in encoders.items():
        if col in row:
            row[col + "_enc"] = int(le_.transform([row.pop(col)])[0])

    X_raw    = np.array([[row.get(f, 0) for f in feature_cols]])
    X_scaled = scaler.transform(X_raw)
    pred     = model.predict(X_scaled)[0]
    proba    = model.predict_proba(X_scaled)[0]

    label_map = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}
    return {
        "label"    : label_map[int(pred)],
        "label_enc": int(pred),
        "prob"     : {"Rendah": float(proba[0]), "Sedang": float(proba[1]), "Tinggi": float(proba[2])},
        "auto"     : {
            "indeks_kepatuhan" : full["indeks_kepatuhan"],
            "volume_kendaraan" : full["volume_kendaraan"],
            "sudut_perpotongan": full["sudut_perpotongan"],
            "jarak_rs_m"       : full["jarak_rs_m"],
            "jarak_pandang_m"  : full["jarak_pandang_m"],
        },
    }



