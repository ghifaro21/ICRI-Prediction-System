import streamlit as st


def render_home():
    # Hero
    st.markdown("""
    <div class="hero-wrap">
        <div style="font-size:3.2rem; margin-bottom:.3rem;">🚂</div>
        <div class="hero-title">ICRI Prediction System</div>
        <div class="hero-sub">Indonesian-Contextualized Risk Index</div>
        <div class="hero-body">
            Sistem klasifikasi tingkat risiko perlintasan sebidang kereta api berbasis<br>
            <strong style="color:#c4b5fd;">Ensemble Machine Learning</strong> &amp; adaptasi metodologi
            <strong style="color:#c4b5fd;">ALCAM Australia</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stat tiles
    c1, c2, c3, c4 = st.columns(4)
    tiles = [
        ("🏙️", "342", "Perlintasan Bandung", "#6366f1"),
        ("🤖", "Stacking", "Ensemble Classifier", "#10b981"),
        ("📊", "18", "Fitur Analisis", "#f59e0b"),
        ("⚡", "3 Kelas", "Rendah · Sedang · Tinggi", "#ef4444"),
    ]
    for col, (ico, val, lbl, clr) in zip([c1,c2,c3,c4], tiles):
        with col:
            st.markdown(f"""
            <div class="stat-tile" style="border-top:3px solid {clr};">
                <div style="font-size:1.7rem;">{ico}</div>
                <div class="stat-val" style="color:{clr};">{val}</div>
                <div class="stat-lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Formula + Risk classes
    cl, cr = st.columns(2)
    with cl:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700; color:var(--text-1); margin-bottom:.9rem;">📐 Formula ICRI</div>
            <div style="background:rgba(99,102,241,.08); border-radius:10px; padding:1rem;
                        font-family:monospace; font-size:.84rem; color:#c4b5fd; line-height:2;">
                ICRI &nbsp;= 0.40 × <span style="color:#ef4444;">Perilaku</span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 0.30 × <span style="color:#f59e0b;">Paparan</span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 0.20 × <span style="color:#3b82f6;">Infrastruktur</span><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 0.10 × <span style="color:#8b5cf6;">Konsekuensi</span>
            </div>
            <div style="font-size:.76rem; color:#475569; margin-top:.75rem; line-height:1.65;">
                Bobot berdasarkan <strong>PT KAI 2026</strong> (87% kecelakaan = faktor manusia)
                dan adaptasi <strong>ALCAM Australia</strong>.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cr:
        st.markdown("""
        <div class="gc">
            <div style="font-weight:700; color:var(--text-1); margin-bottom:.9rem;">🎯 Klasifikasi Risiko</div>
            <div style="display:flex;flex-direction:column;gap:.6rem;">
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(16,185,129,.08);border-radius:10px;border-left:3px solid #10b981;">
                    <span style="font-size:1.3rem;">🟢</span>
                    <div>
                        <div style="font-weight:700;color:#10b981;font-size:.9rem;">RENDAH</div>
                        <div style="font-size:.72rem;color:#475569;">40% terendah ICRI · Infrastruktur memadai</div>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(245,158,11,.08);border-radius:10px;border-left:3px solid #f59e0b;">
                    <span style="font-size:1.3rem;">🟡</span>
                    <div>
                        <div style="font-weight:700;color:#f59e0b;font-size:.9rem;">SEDANG</div>
                        <div style="font-size:.72rem;color:#475569;">Q40–Q75 · Perlu monitoring & evaluasi rutin</div>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:.8rem;padding:.7rem;
                            background:rgba(239,68,68,.08);border-radius:10px;border-left:3px solid #ef4444;">
                    <span style="font-size:1.3rem;">🔴</span>
                    <div>
                        <div style="font-weight:700;color:#ef4444;font-size:.9rem;">TINGGI</div>
                        <div style="font-size:.72rem;color:#475569;">25% teratas · Tindakan darurat diperlukan!</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:1.2rem;margin-top:.5rem;">
        <span style="font-size:.88rem;color:#374151;">
            Gunakan menu
            <strong style="color:#a5b4fc;"> 🔍 Prediksi Risiko</strong>
            di sidebar untuk memulai analisis perlintasan
        </span>
    </div>
    """, unsafe_allow_html=True)



