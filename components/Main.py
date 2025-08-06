from components.subcomponents.Options.OptionPage import *
from components.subcomponents.Options.OptionHandler import *

def Main():
    option = st.selectbox(
        " Apa yang bisa kami bantu ? ",
        (
            "Informasi Umum GEMA",
            "Informasi Training",
            "Informasi Golden Ticket PENS",
            "Informasi Riset GEMA",
            "Informasi Kerja Sama GEMA",
            "informasi Gbook gaeni",
        ),index=None,
        placeholder="Pilih Menu"
    )
    bahasa = st.selectbox(
        "Bahasa",
        (
            "Bahasa Indonesia",
            "Bahasa Inggris",
            "Bahasa Jepang",
            "Bahasa Jerman",
            "Bahasa Mandarin",
            "Bahasa Arab",  
            "Bahasa Melayu", 
            "Bahasa Tagalog",  
            "Bahasa Thailand",  
            "Bahasa Vietnam",  
            "Bahasa Burma",  
            "Bahasa Tetum" 
        ),index=None
    )
    Option(option,bahasa)
