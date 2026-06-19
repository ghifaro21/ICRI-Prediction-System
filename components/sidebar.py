import streamlit as st


def render_sidebar() -> str:
    with st.sidebar:
        st.markdown("""
        <div class="nav-logo">
            <div class="nav-emoji">🚂</div>
            <div class="nav-name">ICRI System</div>
            <div class="nav-tag">Indonesian-Contextualized<br>Risk Index · Bandung</div>
        </div>
        <hr/>
        """, unsafe_allow_html=True)

        page = st.radio(
            "nav", ["🏠  Beranda", "🔍  Prediksi Risiko", "📊  Metodologi"],
            label_visibility="collapsed",
        )

        st.markdown("<hr/>", unsafe_allow_html=True)

        st.markdown("""
        <div style="padding:.9rem; background:rgba(255,255,255,.025); border-radius:12px; margin-top:.5rem;">
            <div style="font-size:.7rem; color:#374151; font-weight:600; text-transform:uppercase; letter-spacing:.07em; margin-bottom:.7rem;">
                Status Model
            </div>
            <div style="font-size:.8rem; color:#94a3b8; line-height:2;">
                <span class="status-dot pulse"></span>Stacking Ensemble<br>
                <span class="status-dot pulse"></span>RF + XGBoost + GB<br>
                <span class="status-dot pulse"></span>18 Fitur · 3 Kelas<br>
                <span class="status-dot pulse"></span>342 Perlintasan Bandung
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-footer">
            Proyek Terintegrasi 1 · ULBI · Data Science<br>© 2026 I.T Ghifari
        </div>
        """, unsafe_allow_html=True)

    return page


