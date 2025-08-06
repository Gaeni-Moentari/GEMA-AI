from components.subcomponents.Options.OptionPage import *
from components.subcomponents.urlbase import url
import streamlit as st

def Option(option, lang):
    pages = {
        "Informasi Umum GEMA": {
            "question": "Masukkan Pertanyaan disini!",
            "info": """##### Informasi Umum GEMA FOUNDATION
Memberikan informasi terkait:
- Informasi umum mengenai GEMA FOUNDATION
- Profil tim GEMA FOUNDATION
- Gambaran umum tentang misi dan visi GEMA 
- Dampak GEMA pada industri lokal dan global
- Komitmen GEMA terhadap keberlanjutan dan inovasi""",
            "context": f"Pusat Informasi Umum GEMA FOUNDATION dengan website resmi {url}",
            "crew": GemaCrew.BaseCrew
        },
        "Informasi Training": {
            "question": "Cari Informasi Seputar Training GEMA FOUNDATION disini!",
            "info": """##### Informasi Training
Memberikan informasi terkait:
- Program pelatihan dan workshop yang tersedia
- Jadwal pelatihan dan prosedur pendaftaran
- Topik yang dibahas dalam pelatihan (misalnya: Teknopreneur, Storytelling, AI)
- Pelatihan untuk pendidik, profesional, dan siswa
- Proses sertifikasi dan akreditasi""",
            "context": f"Pusat Informasi Training GEMA FOUNDATION dengan website resmi {url}",
            "crew": GemaCrew.BaseCrew
        },
        "Informasi Golden Ticket PENS": {
            "question": "Cari Informasi Seputar Golden Ticket PENS disini!",
            "info": """##### Informasi Golden Ticket PENS
Memberikan informasi terkait:
- Gambaran umum tentang program Golden Ticket
- Cara mendaftar dan manfaat partisipasi
- Kriteria kelayakan untuk program Golden Ticket""",
            "context": f"Pusat Informasi Golden Ticket PENS dengan website resmi {url}",
            "crew": GemaCrew.BaseCrew
        },
        "Informasi Riset GEMA": {
            "question": "Cari Informasi Seputar Riset GEMA disini!",
            "info": """##### Informasi Riset GEMA
Memberikan informasi terkait:
- Proyek riset yang sedang berjalan dan yang akan datang
- Kemitraan riset dengan universitas dan institusi riset
- Kesempatan untuk kolaborasi dan kontribusi dalam riset""",
            "context": f"Pusat Informasi Riset GEMA dengan website resmi {url}",
            "crew": GemaCrew.BaseCrew
        },
        "Informasi Kerja Sama GEMA": {
            "question": "Cari Informasi Seputar Kerja Sama GEMA disini!",
            "info": """##### Informasi Kerja Sama GEMA
Memberikan informasi terkait:
- Cara menjadi mitra atau kolaborator dengan GEMA
- Manfaat kerja sama bagi para pemangku kepentingan
- Peran GEMA dalam mempromosikan kolaborasi lintas industri""",
            "context": f"Pusat Informasi Kerja Sama GEMA dengan website resmi {url}",
            "crew": GemaCrew.BaseCrew
        },
        "informasi Gbook gaeni": {
            "question": "Cari Informasi Seputar Gbook gaeni disini!",
            "info": """##### Informasi Gbook gaeni
Memberikan informasi terkait:
- Gambaran umum tentang Gbook gaeni
- Beberapa koleksi buku Gbook gaeni
- Cara mendapatkan buku Gbook gaeni""",
            "context": f"Pusat Informasi Gbook gaeni dengan website resmi {url}",
            "crew": GemaCrew.Bookcrew
        }
    }

    if option in pages:
        page = pages[option]
        OptionPage(page["question"], page["info"], page["context"], lang, page["crew"]).BaseIO()
    elif option is None:
        OptionPage("", "", "", "", "").StartPage()
    else:
        st.write("Masih dalam pengembangan")
