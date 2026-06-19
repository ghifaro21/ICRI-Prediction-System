import streamlit as st


def apply_theme() -> None:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ══ Reset & Root ══════════════════════════════════════════════════════════ */
:root {
    --bg-primary:   var(--background-color, #080c18);
    --bg-secondary: var(--secondary-background-color, #0d1424);
    --bg-card:      color-mix(in srgb, var(--secondary-background-color, #0d1424) 82%, transparent);
    --bg-hover:     color-mix(in srgb, var(--secondary-background-color, #0d1424) 92%, var(--text-color, #eef2ff) 8%);
    --border:       color-mix(in srgb, var(--text-color, #eef2ff) 14%, transparent);
    --border-glow:  color-mix(in srgb, var(--primary-color, #6366f1) 50%, transparent);
    --text-1:       var(--text-color, #eef2ff);
    --text-2:       color-mix(in srgb, var(--text-color, #eef2ff) 72%, transparent);
    --text-3:       color-mix(in srgb, var(--text-color, #eef2ff) 52%, transparent);
    --accent:       var(--primary-color, #6366f1);
    --green:        #10b981;
    --yellow:       #f59e0b;
    --red:          #ef4444;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

.stApp {
    background: var(--bg-primary) !important;
    color: var(--text-1) !important;
}

.main .block-container {
    padding: 1.5rem 2.5rem !important;
    max-width: 1380px;
}

/* ── Hide Streamlit chrome ── */
footer { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg-secondary) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }
[data-testid="stSidebar"] .stRadio > label { color: var(--text-2) !important; }
.sidebar-footer {
    margin-top: 2rem;
    padding: 1rem 0.4rem 0;
    border-top: 1px solid var(--border);
    text-align: center;
    font-size: .67rem;
    line-height: 1.55;
    color: var(--text-3);
}

/* ── Widget labels ── */
label, .stRadio > div > label { color: var(--text-2) !important; font-size: 0.85rem !important; }

/* ── Select boxes ── */
div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.12) !important;
    color: var(--text-1) !important;
    border-radius: 10px !important;
}
div[data-baseweb="select"] svg { fill: var(--text-2) !important; }

/* ── Slider ── */
[data-testid="stSlider"] .rc-slider-track { background: var(--accent) !important; }
[data-testid="stSlider"] .rc-slider-handle { border-color: var(--accent) !important; background: var(--accent) !important; }

/* ── Radio buttons ── */
[data-testid="stRadio"] > div { gap: 0.5rem; }
[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    color: var(--text-2) !important;
    font-size: 0.85rem !important;
}

/* ── Predict button ── */
.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.3s cubic-bezier(.4,0,.2,1) !important;
    box-shadow: 0 4px 20px rgba(99,102,241,0.45) !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 35px rgba(99,102,241,0.6) !important;
}
.stButton > button:active { transform: translateY(0px) !important; }

/* ── Expander ── */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
}
[data-testid="stExpander"] summary {
    color: var(--text-2) !important;
    font-size: 0.88rem !important;
}

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.07) !important; }

/* ═══════════════════════════════════════════════════════════════════════════
   CUSTOM COMPONENT STYLES
═══════════════════════════════════════════════════════════════════════════ */

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg,
        rgba(99,102,241,0.18) 0%,
        rgba(139,92,246,0.12) 40%,
        rgba(168,85,247,0.08) 70%,
        rgba(239,68,68,0.05) 100%);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 22px;
    padding: 2.8rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
}
.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%,
        rgba(99,102,241,0.14) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-size: 2.9rem; font-weight: 900;
    background: linear-gradient(130deg, #a5b4fc, #c084fc, #f472b6);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1.15; margin: 0 0 0.4rem 0;
}
.hero-sub {
    font-size: 1.1rem; font-weight: 500;
    color: #c4b5fd; margin: 0 0 0.6rem 0;
}
.hero-body { font-size: 0.9rem; color: #64748b; line-height: 1.7; }

/* ── Glass card ── */
.gc {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1rem;
    transition: border-color .25s, background .25s;
}
.gc:hover { background: var(--bg-hover); border-color: rgba(255,255,255,0.11); }

/* ── Stat tiles (home) ── */
.stat-tile {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: all .25s;
}
.stat-tile:hover { background: var(--bg-hover); transform: translateY(-2px); }
.stat-val { font-size: 1.55rem; font-weight: 800; margin: 0.3rem 0 0.15rem; }
.stat-lbl { font-size: 0.72rem; color: #475569; text-transform: uppercase; letter-spacing: .07em; }

/* ── Section header ── */
.sec-hdr {
    display: flex; align-items: center; gap: 0.8rem;
    padding: 1.2rem 0 0.8rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.1rem;
}
.sec-dot {
    width: 38px; height: 38px; border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
}
.sec-title { font-size: 1.05rem; font-weight: 700; color: var(--text-1); margin: 0; }
.sec-desc  { font-size: 0.77rem; color: var(--text-3); margin: 0.1rem 0 0; }

/* ── Info / warning boxes ── */
.ibox {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    font-size: 0.83rem; color: #a5b4fc;
    margin-bottom: 1.1rem;
}
.wbox {
    background: rgba(245,158,11,0.07);
    border: 1px solid rgba(245,158,11,0.2);
    border-radius: 10px;
    padding: 0.7rem 1rem;
    font-size: 0.8rem; color: #fcd34d;
}

/* ── Risk result cards ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
.risk-card {
    border-radius: 20px; padding: 2rem 1.5rem;
    text-align: center; animation: fadeUp .55s ease;
}
.risk-rendah { background: linear-gradient(135deg, rgba(16,185,129,.14), rgba(16,185,129,.04)); border: 2px solid rgba(16,185,129,.4); }
.risk-sedang { background: linear-gradient(135deg, rgba(245,158,11,.14), rgba(245,158,11,.04)); border: 2px solid rgba(245,158,11,.4); }
.risk-tinggi { background: linear-gradient(135deg, rgba(239,68,68,.14), rgba(239,68,68,.04)); border: 2px solid rgba(239,68,68,.4); }

.risk-badge {
    font-size: 3.2rem; font-weight: 900; letter-spacing: -1px; margin: 0.4rem 0;
}
.risk-desc { font-size: 0.85rem; color: #94a3b8; margin: 0.6rem 0 0; line-height: 1.6; }
.action-pill {
    margin-top: 1rem; padding: 0.65rem 1rem;
    background: rgba(0,0,0,.25); border-radius: 10px;
    font-size: 0.8rem; font-weight: 600; line-height: 1.4;
}

/* ── Prob bars ── */
.prob-row {
    display: flex; align-items: center; gap: .75rem;
    margin-bottom: .65rem;
}
.prob-label { width: 64px; font-size: .82rem; font-weight: 600; }
.prob-track { flex: 1; height: 10px; background: rgba(255,255,255,.06); border-radius: 99px; overflow: hidden; }
.prob-fill  { height: 100%; border-radius: 99px; transition: width .6s cubic-bezier(.4,0,.2,1); }
.prob-pct   { width: 46px; text-align: right; font-size: .82rem; font-weight: 700; }

/* ── Auto feature pill ── */
.af-pill {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 11px; padding: .7rem .85rem;
    margin-bottom: .5rem;
}
.af-name  { font-size: .78rem; font-weight: 600; margin-bottom: .18rem; }
.af-val   { font-size: 1.15rem; font-weight: 800; color: var(--text-1); }
.af-src   { font-size: .68rem; color: #475569; margin-top: .15rem; }

/* ── Sidebar nav ── */
.nav-logo  { text-align: center; padding: 1.2rem 0 1.5rem; }
.nav-emoji { font-size: 2.6rem; }
.nav-name  { font-weight: 800; font-size: 1.1rem; color: var(--text-1); margin-top: .4rem; }
.nav-tag   { font-size: .72rem; color: #374151; margin-top: .15rem; line-height: 1.4; }

.status-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--green); box-shadow: 0 0 7px var(--green);
    display: inline-block; margin-right: .5rem;
}

/* ── Methodology table ── */
.feat-table { width: 100%; border-collapse: collapse; font-size: .8rem; }
.feat-table th { color: var(--text-3); padding: .5rem .6rem; text-align: left; border-bottom: 1px solid var(--border); }
.feat-table td { padding: .38rem .6rem; border-bottom: 1px solid rgba(255,255,255,.03); color: var(--text-1); }
.badge-manual { background: rgba(16,185,129,.15); color: #6ee7b7; padding: .12rem .5rem; border-radius: 5px; font-size: .7rem; font-weight: 600; }
.badge-auto   { background: rgba(99,102,241,.15); color: #a5b4fc; padding: .12rem .5rem; border-radius: 5px; font-size: .7rem; font-weight: 600; }

/* ── ICRI weight bars ── */
.wbar-wrap { margin-bottom: .7rem; }
.wbar-row  { display: flex; align-items: center; gap: .6rem; margin-bottom: .35rem; }
.wbar-trk  { flex:1; height: 9px; background: rgba(255,255,255,.06); border-radius: 99px; overflow:hidden; }
.wbar-fill { height: 100%; border-radius: 99px; }

/* ── Pulse animation on live dot ── */
@keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:.45; } }
.pulse { animation: pulse 2.2s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)
