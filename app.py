import streamlit as st

from components.sidebar import render_sidebar
from views.home import render_home
from views.methodology import render_info
from views.predict import render_predict
from styles.theme import apply_theme


st.set_page_config(
    page_title="ICRI - Prediksi Risiko Perlintasan Sebidang",
    page_icon="\U0001F682",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()


def main() -> None:
    page = render_sidebar()

    if "Beranda" in page:
        render_home()
    elif "Prediksi" in page:
        render_predict()
    elif "Metodologi" in page:
        render_info()


if __name__ == "__main__":
    main()
