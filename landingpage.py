import streamlit as st
from PIL import Image 

def main():
    """
    Fungsi utama untuk membangun dan menjalankan aplikasi landing page.
    """
    # --- KONFIGURASI HALAMAN ---
    # Ini harus menjadi perintah Streamlit pertama yang dijalankan
    st.set_page_config(
        page_title="ABSA:Feedback Survei Wisnus 2024",
        page_icon="📊",
        layout="centered",  # 'centered' atau 'wide'
        initial_sidebar_state="auto"
    )

    # --- KODE CSS KUSTOM UNTUK TAMPILAN ---
    # Gunakan CSS untuk menata tampilan agar lebih menarik
    CUSTOM_CSS = """
    <style>
        /* Mengatur kontainer utama aplikasi */
        [data-testid="stAppViewContainer"] {
            background-color: #070F2B; /* Latar belakang biru tua */
            color: #E5E1DA; /* Warna teks default krem */
        }
        
        /* ✅ CSS BARU UNTUK JUDUL DUA BARIS */
        .custom-title-container {
            text-align: center;
            padding: 20px 0;
        }
        .custom-title-container .title-line-1 {
            font-family: 'Verdana', sans-serif;
            color: #FFFFFF;
            font-size: 1.5rem; /* Ukuran font untuk baris pertama */
            font-weight: bold;
            line-height: 1.2;
        }
        .custom-title-container .title-line-2 {
            font-family: 'Verdana', sans-serif;
            color: #FFFFFF;
            font-size: 2.1rem; /* Ukuran font untuk baris kedua */
            font-weight:  bold;
            line-height: 1.2;
        }


        /* Mengatur teks deskripsi */
        .description-text {
            font-size: 1.1rem;
            text-align: center;
            color: #D9EAFD;
            padding: 0 20px;
        }

        /* Mengatur gambar agar memiliki sudut membulat dan bayangan */
        [data-testid="stImage"] img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Mengatur header untuk daftar link */
        .custom-subheader {
            color: #FFFFFF;
            text-align: center;
            border-bottom: 2px solid #1B1A55;
            padding-bottom: 10px;
            margin-top: 50px;
            font-size: 2rem; /* Atur ukuran font sesuai keinginan Anda */
            font-weight: bold;
        }

        /* Mengatur daftar link */
        .link-list {
            line-height: 2; /* Memberi jarak antar baris */
            font-size: 1.1rem;
        }
        .link-list a {
            color: #9DB2BF; /* Warna link abu-abu kebiruan */
            text-decoration: none;
            transition: color 0.2s;
        }
        .link-list a:hover {
            color: #FFFFFF; /* Warna link menjadi putih saat di-hover */
            text-decoration: underline;
        }
    </style>
    """
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # --- KONTEN HALAMAN ---

    # 1. Judul Utama
    st.markdown(
        """
        <div class="custom-title-container">
            <p class="title-line-1">📊Analisis Sentimen Berbasis Aspek</p>
            <p class="title-line-2">Dataset Feedback Survei Digital Wisnus 2024</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2. Penjelasan
    st.markdown(
        '<p class="description-text">Website merupakan penerapan dari pemodelan analisis sentimen berdasarkan aspek menggunakan'
        ' dataset feedback Survei Digital Wisnus 2024.</p>',
        unsafe_allow_html=True
    )
    
    # Memberi jarak
    st.write("")

    st.markdown(
        '<p class="description-text">Prediksi sentimen didapatkan dengan metode pseudo labelling menggunakan IndoBERT</p>',
        unsafe_allow_html=True
    )

    # Memberi jarak
    st.write("---")

    # 3. Gambar
    # Ganti URL gambar di bawah dengan URL gambar Anda sendiri
    #image_url = "https://drive.google.com/uc?export=view&id=12KXjX3mSJK6OSC2hEuaY2HF6g71e6ER3" #https://drive.google.com/file/d/12KXjX3mSJK6OSC2hEuaY2HF6g71e6ER3/view?usp=drive_link
    st.image("visualisasi.png", caption="Visualisasi Distribusi Sentimen")

    # Memberi jarak
    st.write("")

    try:
        img_negatif = Image.open("wc n.jpg")
        img_positif = Image.open("wc p.jpg")
        
        col1, col2 = st.columns(2)

        with col1:
            st.image(img_negatif, caption="wordcloud sentimen negatif", use_container_width=True)

        with col2:
            st.image(img_positif, caption="wordcloud sentimen positif", use_container_width=True)

    except FileNotFoundError:
        st.error("Pastikan file 'wc n.JPG' dan 'wc p.JPG' ada di folder yang sama.")

    # Memberi jarak
    st.write("---")

    st.markdown(
        '<p class="custom-subheader">Prediksi Aspek dan Sentimen Teks Feedback</p>',
        unsafe_allow_html=True
    )


    # 5. Daftar Link ke Aplikasi Lain
    # PENTING: Ganti URL placeholder di bawah ini dengan URL aplikasi Streamlit Anda yang sebenarnya.
    st.markdown(
        """
        <div class="link-list">
        <ol>
            <li><a href="https://aspek1sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Konten Kuesioner Web</a></li>
            <li><a href="https://aspek2sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Presentasi Kuesioner Web</a></li>
            <li><a href="https://aspek3sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Metode Pengumpulan Data</a></li>
            <li><a href="https://aspek4sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Undangan Survei</a></li>
            <li><a href="https://aspek5sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Pra-pemberitahuan dan Pengingat Survei</a></li>
            <li><a href="https://aspek6sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Insentif</a></li>
            <li><a href="https://aspek7sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Kemudahan Penggunaan</a></li>
            <li><a href="https://aspek8sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Keandalan Aplikasi</a></li>
            <li><a href="https://aspek9sentimen00vh3lp027z3l0kkz.streamlit.app/" target="_blank">Prediksi Aspek dan Sentimen: Kebermanfaatan</a></li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Memberi jarak
    st.write("---")
    # Memberi jarak
    st.write("---")

    st.markdown(
        '<p class="description-text">oleh: Hanun Nabila Azis (222112090)</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

