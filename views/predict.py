import streamlit as st

from components.charts import make_bar, make_gauge
from core.model import predict_icri


def render_predict():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.75rem;font-weight:800;color:var(--text-1);">🔍 Prediksi Tingkat Risiko</div>
        <div style="font-size:.88rem;color:#475569;margin-top:.25rem;">
            Isi informasi perlintasan di bawah ini untuk mendapatkan prediksi risiko berbasis model ICRI
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ibox">
        🤖 <strong>Auto-Calculation Active</strong> — 5 fitur teknis (indeks kepatuhan, volume kendaraan,
        sudut perpotongan, jarak RS, jarak pandang) dihitung <em>otomatis</em> dari input Anda.
        Tidak perlu alat ukur khusus.
    </div>
    """, unsafe_allow_html=True)

    # ── BAGIAN 1 ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(59,130,246,.15);">🛤️</div>
        <div>
            <div class="sec-title">Bagian 1 — Kondisi Fisik Perlintasan</div>
            <div class="sec-desc">Informasi yang dapat dilihat langsung di lapangan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b1c1, b1c2, b1c3 = st.columns(3)

    with b1c1:
        jenis_perlintasan = st.selectbox(
            "Jenis Perlintasan",
            options=["resmi", "liar"],
            format_func=lambda x: "✅ Resmi (terdaftar PT KAI)" if x == "resmi" else "⚠️ Liar (tidak resmi)",
            help="Perlintasan resmi = terdaftar & dipantau PT KAI",
        )
        palang = st.selectbox(
            "Kondisi Palang Pintu",
            options=[0, 1, 2],
            format_func=lambda x: {0:"❌ Tidak Ada Palang", 1:"🔧 Palang Manual", 2:"⚡ Palang Otomatis"}[x],
        )
        kondisi_jalan = st.selectbox(
            "Kondisi Jalan",
            options=[0, 1, 2],
            format_func=lambda x: {0:"🔴 Buruk (berlubang/retak)", 1:"🟡 Sedang", 2:"🟢 Baik (mulus)"}[x],
        )

    with b1c2:
        dijaga_raw = st.radio(
            "Status Penjagaan Perlintasan",
            ["Ya — Dijaga", "Tidak — Tanpa Penjagaan"],
            help="Ada penjagaan oleh petugas atau sistem otomatis?",
        )
        dijaga = 1 if dijaga_raw.startswith("Ya") else 0

        lampu_raw = st.radio(
            "Lampu Sinyal / Warning Light",
            ["Ada", "Tidak Ada"],
            horizontal=True,
        )
        lampu_sinyal = 1 if lampu_raw == "Ada" else 0

        petugas_raw = st.radio(
            "Petugas Jaga Tetap",
            ["Ada", "Tidak Ada"],
            horizontal=True,
        )
        petugas_jaga = 1 if petugas_raw == "Ada" else 0

    with b1c3:
        rambu = st.selectbox(
            "Kelengkapan Rambu",
            options=[0, 1, 2],
            format_func=lambda x: {0:"❌ Tidak Ada Rambu", 1:"⚠️ Rambu Sebagian", 2:"✅ Rambu Lengkap"}[x],
        )
        st.markdown("""
        <div style="background:rgba(255,255,255,.025);border:1px solid var(--border);border-radius:11px;
                    padding:.85rem;margin-top:.9rem;">
            <div style="font-size:.7rem;color:#374151;font-weight:600;text-transform:uppercase;
                        letter-spacing:.06em;margin-bottom:.5rem;">🤖 Dihitung otomatis</div>
            <div style="font-size:.78rem;color:#818cf8;line-height:1.9;">
                • Jarak pandang (dari kondisi jalan)<br>
                • Indeks kepatuhan (dari status jaga)<br>
                • Jarak ke RS (default Bandung)
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── BAGIAN 2 ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(245,158,11,.15);">🚗</div>
        <div>
            <div class="sec-title">Bagian 2 — Kondisi Lalu Lintas</div>
            <div class="sec-desc">Karakteristik volume dan jenis kendaraan yang melintasi</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b2c1, b2c2, b2c3 = st.columns(3)

    with b2c1:
        kelas_jalan = st.selectbox(
            "Kelas Jalan",
            options=["arteri", "kolektor", "lokal"],
            format_func=lambda x: {
                "arteri"  : "🔴 Arteri — Volume tinggi (~850 kend/jam)",
                "kolektor": "🟡 Kolektor — Volume sedang (~380 kend/jam)",
                "lokal"   : "🟢 Lokal — Volume rendah (~110 kend/jam)",
            }[x],
            help="Volume kendaraan akan dihitung otomatis dari kelas jalan ini",
        )

    with b2c2:
        jenis_kendaraan = st.selectbox(
            "Jenis Kendaraan Dominan",
            options=["motor", "mobil", "truk", "angkot"],
            format_func=lambda x: {
                "motor" : "🏍️ Motor — Risiko tertinggi (87% kasus KAI)",
                "mobil" : "🚗 Mobil / Sedan",
                "truk"  : "🚛 Truk / Kendaraan Berat",
                "angkot": "🚌 Angkot / Minibus",
            }[x],
        )

    with b2c3:
        sesi_waktu_rawan = st.selectbox(
            "Waktu Penilaian",
            options=["pagi", "siang", "sore", "malam"],
            format_func=lambda x: {
                "pagi"  : "🌅 Pagi (06.00–10.00)",
                "siang" : "☀️  Siang (10.00–15.00)",
                "sore"  : "🌇 Sore (15.00–20.00)",
                "malam" : "🌙 Malam (20.00–06.00)",
            }[x],
        )

    # ── BAGIAN 3 ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="sec-hdr">
        <div class="sec-dot" style="background:rgba(239,68,68,.15);">🚆</div>
        <div>
            <div class="sec-title">Bagian 3 — Data Kereta &amp; Riwayat Insiden</div>
            <div class="sec-desc">Frekuensi lalu lintas KA dan catatan kecelakaan historis</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    b3c1, b3c2, b3c3 = st.columns(3)

    with b3c1:
        frekuensi_kereta = st.slider(
            "Frekuensi Kereta (KA / hari)",
            min_value=1, max_value=200, value=70, step=1,
            help="Bisa dicek via jadwal resmi KAI / Stasiun terdekat",
        )

    with b3c2:
        riwayat_insiden = st.selectbox(
            "Riwayat Insiden (3 tahun terakhir)",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "✅ 0 kejadian — Aman",
                1: "⚠️ 1 kejadian",
                2: "🟠 2 kejadian",
                3: "🔴 3+ kejadian — Sering terjadi",
            }[x],
        )

    with b3c3:
        jarak_stasiun_m = st.slider(
            "Estimasi Jarak ke Stasiun Terdekat (m)",
            min_value=100, max_value=10_000, value=1_200, step=100,
            help="Perkirakan via Google Maps / peta jalur KAI",
        )

    # ── TOMBOL PREDIKSI ───────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1.8, 1])
    with btn_col:
        run_predict = st.button("🔍  Analisis Tingkat Risiko Sekarang", use_container_width=True)

    # ── HASIL ─────────────────────────────────────────────────────────────────
    if run_predict:
        ui = {
            "jenis_perlintasan": jenis_perlintasan,
            "dijaga"           : dijaga,
            "palang"           : palang,
            "lampu_sinyal"     : lampu_sinyal,
            "petugas_jaga"     : petugas_jaga,
            "rambu"            : rambu,
            "kondisi_jalan"    : kondisi_jalan,
            "kelas_jalan"      : kelas_jalan,
            "jenis_kendaraan"  : jenis_kendaraan,
            "sesi_waktu_rawan" : sesi_waktu_rawan,
            "frekuensi_kereta" : frekuensi_kereta,
            "riwayat_insiden"  : riwayat_insiden,
            "jarak_stasiun_m"  : jarak_stasiun_m,
        }

        with st.spinner("⚙️  Menjalankan pipeline ICRI…"):
            res = predict_icri(ui)

        label = res["label"]
        probs = res["prob"]
        auto  = res["auto"]

        # Risk config
        cfg = {
            "Rendah": {
                "card" : "risk-rendah",
                "color": "#10b981", "icon": "🟢",
                "desc" : "Perlintasan ini memiliki tingkat risiko rendah. Infrastruktur cukup memadai dan kepatuhan pengendara relatif baik.",
                "act"  : "✅ Pertahankan kondisi & lakukan inspeksi rutin setiap 3 bulan",
            },
            "Sedang": {
                "card" : "risk-sedang",
                "color": "#f59e0b", "icon": "🟡",
                "desc" : "Perlintasan ini memerlukan perhatian lebih. Beberapa faktor risiko perlu segera ditangani.",
                "act"  : "⚠️ Segera evaluasi infrastruktur & tingkatkan frekuensi pengawasan",
            },
            "Tinggi": {
                "card" : "risk-tinggi",
                "color": "#ef4444", "icon": "🔴",
                "desc" : "PERHATIAN! Perlintasan ini berisiko TINGGI. Potensi kecelakaan signifikan berdasarkan kombinasi faktor ICRI.",
                "act"  : "🚨 Tindakan darurat! Segera koordinasi dengan PT KAI & Dinas Perhubungan",
            },
        }[label]

        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size:1.1rem;font-weight:700;color:var(--text-1);margin-bottom:1rem;">
            📊 Hasil Analisis ICRI
        </div>
        """, unsafe_allow_html=True)

        col_res, col_gauge, col_bar = st.columns([1.25, 0.95, 0.95])

        with col_res:
            st.markdown(f"""
            <div class="risk-card {cfg['card']}">
                <div style="font-size:2.8rem;">{cfg['icon']}</div>
                <div style="font-size:.78rem;color:#94a3b8;text-transform:uppercase;
                            letter-spacing:.12em;margin-top:.4rem;">Tingkat Risiko</div>
                <div class="risk-badge" style="color:{cfg['color']};">{label.upper()}</div>
                <div class="risk-desc">{cfg['desc']}</div>
                <div class="action-pill" style="color:{cfg['color']};">{cfg['act']}</div>
            </div>
            """, unsafe_allow_html=True)

        with col_gauge:
            st.markdown("<div style='font-size:.78rem;color:#475569;margin-bottom:0;'>Gauge Risiko Tinggi</div>",
                        unsafe_allow_html=True)
            st.plotly_chart(make_gauge(probs["Tinggi"]), use_container_width=True,
                            config={"displayModeBar": False})

        with col_bar:
            st.markdown("<div style='font-size:.78rem;color:#475569;margin-bottom:.3rem;'>Distribusi Probabilitas</div>",
                        unsafe_allow_html=True)
            st.plotly_chart(make_bar(probs), use_container_width=True,
                            config={"displayModeBar": False})

        # Prob detail bars
        st.markdown("<br>", unsafe_allow_html=True)
        p1, p2, p3 = st.columns(3)
        for col_p, (rname, rclr) in zip(
            [p1, p2, p3],
            [("Rendah","#10b981"),("Sedang","#f59e0b"),("Tinggi","#ef4444")]
        ):
            pv = probs[rname]
            with col_p:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,.03);border:1px solid var(--border);
                            border-radius:13px;padding:1rem;text-align:center;">
                    <div style="font-size:.72rem;color:#475569;text-transform:uppercase;letter-spacing:.08em;">P({rname})</div>
                    <div style="font-size:2rem;font-weight:800;color:{rclr};">{pv:.1%}</div>
                    <div style="height:5px;background:rgba(255,255,255,.05);border-radius:3px;margin-top:.5rem;">
                        <div style="width:{pv*100:.1f}%;height:100%;background:{rclr};border-radius:3px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Auto-calculated features expander
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🤖  Detail 5 Fitur Auto-Calculated — Lihat nilai yang dikirim ke model"):
            st.markdown("""
            <div style="font-size:.8rem;color:#475569;margin-bottom:1rem;line-height:1.7;">
                Fitur-fitur berikut dihitung otomatis dan digabung bersama 13 input manual Anda
                sebelum dikirim ke model Stacking Ensemble. Pipeline model <strong>tidak diubah</strong> — 
                tetap menerima 18 fitur lengkap.
            </div>
            """, unsafe_allow_html=True)

            af_items = [
                ("🧠", "indeks_kepatuhan", f"{auto['indeks_kepatuhan']:.2f}",
                 f"Dari status penjagaan ({'dijaga' if dijaga==1 else 'tidak dijaga'})", "#818cf8"),
                ("🚦", "volume_kendaraan", f"{auto['volume_kendaraan']} kend/jam",
                 f"Dari kelas jalan: {kelas_jalan}", "#34d399"),
                ("📐", "sudut_perpotongan", f"{auto['sudut_perpotongan']:.0f}°",
                 "Default rata-rata dataset Bandung", "#fb923c"),
                ("🏥", "jarak_rs_m", f"{auto['jarak_rs_m']:,} m",
                 "Default median kota Bandung (~5 km)", "#f472b6"),
                ("👁️", "jarak_pandang_m", f"{auto['jarak_pandang_m']:.0f} m",
                 f"Estimasi dari kondisi jalan: {['buruk','sedang','baik'][kondisi_jalan]}", "#38bdf8"),
            ]

            af_c1, af_c2, af_c3 = st.columns(3)
            cols_af = [af_c1, af_c2, af_c3]
            for i, (ico, name, val, src, clr) in enumerate(af_items):
                with cols_af[i % 3]:
                    st.markdown(f"""
                    <div class="af-pill">
                        <div class="af-name" style="color:{clr};">{ico} {name}</div>
                        <div class="af-val">{val}</div>
                        <div class="af-src">📍 {src}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("""
            <div class="wbox" style="margin-top:.6rem;">
                ⚠️ Nilai auto-calculated menggunakan asumsi rata-rata dataset Bandung.
                Pastikan input manual sudah akurat untuk hasil prediksi optimal.
            </div>
            """, unsafe_allow_html=True)



