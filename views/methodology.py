import streamlit as st


def render_info():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.75rem;font-weight:800;color:var(--text-1);">📊 Metodologi ICRI</div>
        <div style="font-size:.88rem;color:#475569;margin-top:.25rem;">
            Penjelasan teknis pipeline machine learning, formula ICRI, dan pemetaan fitur
        </div>
    </div>
    """, unsafe_allow_html=True)

    cl, cr = st.columns(2)

    with cl:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">🏗️ Pipeline S1–S7</div>
            <div style="display:flex;flex-direction:column;gap:.45rem;">
        """, unsafe_allow_html=True)
        steps = [
            ("S1", "#6366f1", "rgba(99,102,241,.1)", "Load & Validasi Dataset", "342 perlintasan KA kota Bandung"),
            ("S2", "#10b981", "rgba(16,185,129,.1)",  "ICRI Construction",       "Formula 4 komponen berbobot"),
            ("S3", "#f59e0b", "rgba(245,158,11,.1)",  "Preprocessing",           "Encoding · Scaling · SMOTE"),
            ("S4", "#3b82f6", "rgba(59,130,246,.1)",  "EDA",                     "Distribusi · Korelasi · Profil kelas"),
            ("S5", "#a855f7", "rgba(168,85,247,.1)",  "Ensemble ML",             "RF + XGBoost + GB → Stacking"),
            ("S6", "#06b6d4", "rgba(6,182,212,.1)",   "Visualisasi Performa",    "CM · ROC · Perbandingan model"),
            ("S7", "#ec4899", "rgba(236,72,153,.1)",  "Export + Predict",        "4 joblib artifacts · predict_single()"),
        ]
        for code, clr, bg, title, desc in steps:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:.7rem;padding:.55rem;
                        background:{bg};border-radius:9px;">
                <div style="width:28px;height:28px;border-radius:50%;background:{clr};
                            display:flex;align-items:center;justify-content:center;
                            font-size:.65rem;font-weight:800;color:#fff;flex-shrink:0;">{code}</div>
                <div>
                    <div style="font-size:.82rem;font-weight:600;color:var(--text-1);">{title}</div>
                    <div style="font-size:.7rem;color:#475569;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    with cr:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">⚖️ Bobot Komponen ICRI</div>
        """, unsafe_allow_html=True)
        weights = [
            ("Perilaku Manusia",  0.40, "#ef4444", "PT KAI 2026: 87% kecelakaan = faktor manusia"),
            ("Paparan Lalu Lintas",0.30, "#f59e0b", "ALCAM: Exposure = Volume × Frekuensi KA"),
            ("Infrastruktur",     0.20, "#3b82f6", "PT KAI 2026: hanya 3% kasus terkait palang"),
            ("Konsekuensi",       0.10, "#8b5cf6", "Riwayat insiden, jarak fasilitas kesehatan"),
        ]
        for name, w, clr, src in weights:
            st.markdown(f"""
            <div style="margin-bottom:.7rem;">
                <div style="display:flex;justify-content:space-between;margin-bottom:.25rem;">
                    <span style="font-size:.82rem;font-weight:600;color:var(--text-1);">{name}</span>
                    <span style="font-size:.82rem;font-weight:700;color:{clr};">{w:.0%}</span>
                </div>
                <div style="height:8px;background:rgba(255,255,255,.05);border-radius:99px;overflow:hidden;margin-bottom:.2rem;">
                    <div style="width:{w*100:.0f}%;height:100%;background:{clr};border-radius:99px;"></div>
                </div>
                <div style="font-size:.68rem;color:#374151;">{src}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Feature table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="gc">
        <div style="font-weight:700;color:var(--text-1);margin-bottom:1rem;">
            📋 Pemetaan 18 Fitur Model — Input User &amp; Auto-Calculation
        </div>
        <div style="overflow-x:auto;">
        <table class="feat-table">
            <thead>
                <tr>
                    <th>#</th><th>Fitur Backend</th><th>Komponen ICRI</th>
                    <th>Sumber Input</th><th>Metode</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>1</td><td>jenis_perlintasan</td><td>Perilaku</td><td>User — selectbox</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>2</td><td>dijaga</td><td>Perilaku / Infrastruktur</td><td>User — radio Ya/Tidak</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>3</td><td>palang</td><td>Infrastruktur</td><td>User — selectbox 0/1/2</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>4</td><td>lampu_sinyal</td><td>Infrastruktur</td><td>User — radio Ada/Tidak</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>5</td><td>petugas_jaga</td><td>Infrastruktur</td><td>User — radio Ada/Tidak</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>6</td><td>rambu</td><td>Infrastruktur</td><td>User — selectbox 0/1/2</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>7</td><td>jarak_pandang_m</td><td>Infrastruktur</td><td>Auto dari kondisi_jalan</td><td><span class="badge-auto">🤖 Auto</span></td></tr>
                <tr><td>8</td><td>sudut_perpotongan</td><td>Infrastruktur</td><td>Default 70° (rata-rata)</td><td><span class="badge-auto">🤖 Auto</span></td></tr>
                <tr><td>9</td><td>kondisi_jalan</td><td>Infrastruktur</td><td>User — selectbox 0/1/2</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>10</td><td>kelas_jalan</td><td>Paparan</td><td>User — selectbox</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>11</td><td>volume_kendaraan</td><td>Paparan / Konsekuensi</td><td>Auto dari kelas_jalan</td><td><span class="badge-auto">🤖 Auto</span></td></tr>
                <tr><td>12</td><td>frekuensi_kereta</td><td>Paparan</td><td>User — slider 1–200</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>13</td><td>sesi_waktu_rawan</td><td>Paparan</td><td>User — selectbox</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>14</td><td>jarak_stasiun_m</td><td>Paparan</td><td>User — slider 100–10.000m</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>15</td><td>jenis_kendaraan</td><td>Perilaku</td><td>User — selectbox</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>16</td><td>indeks_kepatuhan</td><td>Perilaku</td><td>Auto dari dijaga</td><td><span class="badge-auto">🤖 Auto</span></td></tr>
                <tr><td>17</td><td>riwayat_insiden</td><td>Konsekuensi</td><td>User — selectbox 0–3+</td><td><span class="badge-manual">✅ Manual</span></td></tr>
                <tr><td>18</td><td>jarak_rs_m</td><td>Konsekuensi</td><td>Default 5.000m (Bandung)</td><td><span class="badge-auto">🤖 Auto</span></td></tr>
            </tbody>
        </table>
        </div>
        <div style="margin-top:.85rem;font-size:.75rem;color:#374151;">
            <span class="badge-manual">✅ Manual</span> = 13 input user-friendly &nbsp;·&nbsp;
            <span class="badge-auto">🤖 Auto</span> = 5 fitur dihitung otomatis (tidak perlu alat ukur)
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Model comparison
    st.markdown("""
    <div class="gc" style="margin-top:0;">
        <div style="font-weight:700;color:var(--text-1);margin-bottom:.9rem;">🏆 Perbandingan Model Ensemble</div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;">
            <div style="background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.2);border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:#475569;text-transform:uppercase;letter-spacing:.06em;">Random Forest</div>
                <div style="font-size:1.4rem;font-weight:800;color:#3b82f6;margin:.3rem 0;">RF</div>
                <div style="font-size:.72rem;color:#475569;">300 estimators · depth=8</div>
            </div>
            <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:#475569;text-transform:uppercase;letter-spacing:.06em;">XGBoost</div>
                <div style="font-size:1.4rem;font-weight:800;color:#f59e0b;margin:.3rem 0;">XGB</div>
                <div style="font-size:.72rem;color:#475569;">300 est · lr=0.05</div>
            </div>
            <div style="background:rgba(168,85,247,.08);border:1px solid rgba(168,85,247,.2);border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:#475569;text-transform:uppercase;letter-spacing:.06em;">Gradient Boosting</div>
                <div style="font-size:1.4rem;font-weight:800;color:#a855f7;margin:.3rem 0;">GB</div>
                <div style="font-size:.72rem;color:#475569;">200 est · lr=0.08</div>
            </div>
            <div style="background:rgba(239,68,68,.08);border:2px solid rgba(239,68,68,.3);border-radius:11px;padding:.9rem;text-align:center;">
                <div style="font-size:.72rem;color:#475569;text-transform:uppercase;letter-spacing:.06em;">⭐ Best Model</div>
                <div style="font-size:1.4rem;font-weight:800;color:#ef4444;margin:.3rem 0;">Stack</div>
                <div style="font-size:.72rem;color:#64748b;">RF+XGB+GB → LogReg meta</div>
            </div>
        </div>
        <div style="margin-top:.85rem;">
            <div style="font-size:.75rem;color:#374151;margin-bottom:.4rem;">Preprocessing chain:</div>
            <div style="font-size:.78rem;color:#94a3b8;font-family:monospace;
                        background:rgba(255,255,255,.02);border-radius:8px;padding:.65rem;">
                Raw Data → LabelEncoder (4 cat.) → StandardScaler → SMOTE (k=4) → Stacking Classifier
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



