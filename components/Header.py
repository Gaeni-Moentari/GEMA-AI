import components.subcomponents.Logo as Img
from components.subcomponents.Logo import *
import streamlit as st
import streamlit as st

def Header() :
    st.set_page_config(
        page_title="GAENI AI",
        page_icon="./Image/moentari.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    Img.image(["./Image/gema.png"])
    
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <h1 style="font-size: 52px; color: #333;">GEMA AI</h1>
            <p style="font-size: 18px; color: #555;">Selamat datang di Pusat AI GEMA! Kami siap membantu Anda.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")