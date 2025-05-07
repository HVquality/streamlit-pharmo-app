import streamlit as st
import os

# Set up Streamlit page config and title
st.set_page_config(
    page_title="Farmakokinetika Apps",  # Browser tab title
    page_icon="💊",  # Browser tab icon (emoji or image)
)

st.title("Aplikasi Farmakokinetika 💊")  # Main title
st.markdown("""
Selamat datang di simulasi farmakokinetika!

**Navigasi halaman:** Gunakan sidebar di sebelah kiri untuk berpindah antara:
1. **Farmakokinetika IV Bolus**  
2. **Farmakokinetika Pemberian Oral**  
3. **Farmakokinetika Michaelis-Menten**
""")

# Navigation for sidebar
pages = {
    "Farmakokinetika IV Bolus": "pages/1_Farmakokinetika_IV_Bolus.py",
    "Farmakokinetika Pemberian Oral": "pages/2_Farmakokinetika_Pemberian_Oral.py",
    "Farmakokinetika Michaelis-Menten": "pages/3_Farmakokinetika_Michaelis-Menten.py"
}

page = st.sidebar.radio("Navigasi Halaman", list(pages.keys()))

# Open the correct page based on user selection
with open(pages[page]) as f:
    exec(f.read())
