import streamlit as st
from AIComponents.Crew import *

class OptionPage:
    def __init__(self,question : str, info : str, Context, lang, crew_method):
        self.crew_method = crew_method
        self.question = question
        self.Context = Context
        self.info = info
        self.lang = lang

    def BaseIO(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI sedang memproses Pertanyaan!") : 
                gema_instance = GemaCrew(UserQueries, Konteks, language)
                results = self.crew_method(gema_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    
    def Book(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI sedang memproses Pertanyaan!") : 
                book_instance = GemaCrew(UserQueries, Konteks, language)
                results = self.crew_method(book_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    def StartPage(self) : 
        st.info("Silahkan memilih menu diatas untuk memulai berikut penjelasan setiap menu yang tersedia!")
        st.markdown("""##### GEMA FOUNDATION 
menyediakan Informasi yang umum mengenai berbagai hal tentang GEMA FOUNDATION       
##### Informasi Umum GEMA
Memberikan informasi terkait:

- Informasi umum mengenai GEMA FOUNDATION
- Profil tim GEMA FOUNDATION
- Gambaran umum tentang misi dan visi GEMA
- Dampak GEMA pada industri lokal dan global
- Komitmen GEMA terhadap keberlanjutan dan inovasi

##### Informasi Training
Memberikan informasi terkait:

- Program pelatihan dan workshop yang tersedia
- Jadwal pelatihan dan prosedur pendaftaran
- Topik yang dibahas dalam pelatihan (misalnya: Teknopreneur, Storytelling, AI)
- Pelatihan untuk pendidik, profesional, dan siswa
- Proses sertifikasi dan akreditasi

##### Informasi Golden Ticket PENS
Memberikan informasi terkait:

- Gambaran umum tentang program Golden Ticket
- Cara mendaftar dan manfaat partisipasi
- Kriteria kelayakan untuk program Golden Ticket
                    
##### Informasi Riset GEMA
Memberikan informasi terkait:

- Proyek riset yang sedang berjalan dan yang akan datang
- Kemitraan riset dengan universitas dan institusi riset
- Kesempatan untuk kolaborasi dan kontribusi dalam riset

##### Informasi Kerja Sama GEMA
Memberikan informasi terkait:

- Cara menjadi mitra atau kolaborator dengan GEMA
- Manfaat kerja sama bagi para pemangku kepentingan
- Peran GEMA dalam mempromosikan kolaborasi lintas industri
                    
##### Informasi Gbook gaeni
Memberikan informasi terkait:

- E-Perpustakaan Gema Foundation
- Buku-buku yang tersedia dan dapat diakses secara online
""")