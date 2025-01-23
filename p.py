# import streamlit as st
# import pandas as pd

# # Judul Dashboard
# st.title("Dashboard Harga Komoditas")

# # Membaca dataset
# @st.cache_data
# def load_data():
#     data = pd.read_csv("konsumen.csv")
#     return data

# data = load_data()

# # Filter berdasarkan komoditas
# komoditas_list = data['Komoditas'].unique()
# selected_komoditas = st.selectbox("Pilih Komoditas", komoditas_list)

# # Menampilkan data berdasarkan komoditas yang dipilih
# filtered_data = data[data['Komoditas'] == selected_komoditas]
# st.write(f"### Data Harga {selected_komoditas}")
# st.write(filtered_data)

# # Visualisasi data
# st.write("### Grafik Harga per Bulan")
# st.line_chart(filtered_data.set_index('Bulan')['Harga'])

# # Filter berdasarkan tahun
# tahun_list = data['Tahun'].unique()
# selected_tahun = st.selectbox("Pilih Tahun", tahun_list)

# # Menampilkan data berdasarkan tahun yang dipilih
# filtered_data_tahun = data[data['Tahun'] == selected_tahun]
# st.write(f"### Data Harga Tahun {selected_tahun}")
# st.write(filtered_data_tahun)

# # Visualisasi data per tahun
# st.write("### Grafik Harga per Tahun")
# st.bar_chart(filtered_data_tahun.groupby('Bulan')['Harga'].mean())

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Harga Komoditas")

# Membaca dataset
@st.cache_data
def load_data():
    data = pd.read_csv("konsumen.csv")
    return data

data = load_data()

# Menambahkan teks "Anggota Kelompok" di sidebar
st.sidebar.write("Anggota Kelompok :")
st.sidebar.write("10122081 - Fajar Gustiana")
st.sidebar.write("10122092 - Muhlas Putra Siswaji")
st.sidebar.write("10122097 - Ryan Bachtiar")

# Membuat sidebar
st.sidebar.header("Filter Data")

# Filter berdasarkan komoditas di sidebar
komoditas_list = data['Komoditas'].unique()
selected_komoditas = st.sidebar.selectbox("Pilih Komoditas", komoditas_list)

# Filter berdasarkan tahun di sidebar
tahun_list = data['Tahun'].unique()
selected_tahun = st.sidebar.selectbox("Pilih Tahun", tahun_list)

# Menampilkan data berdasarkan komoditas yang dipilih
filtered_data = data[data['Komoditas'] == selected_komoditas]
st.write(f"### Data Harga {selected_komoditas}")
st.write(filtered_data)

# Visualisasi data per bulan
st.write("### Grafik Harga per Bulan")
st.line_chart(filtered_data.set_index('Bulan')['Harga'])

# Perbandingan Harga Antar Komoditas
st.sidebar.subheader("Perbandingan Harga Antar Komoditas")
komoditas_list = st.sidebar.multiselect("Pilih Komoditas untuk Dibandingkan", data['Komoditas'].unique(), default=data['Komoditas'].unique()[:3])

# Filter data untuk komoditas yang dipilih dan tahun yang dipilih
comparison_data = data[(data['Komoditas'].isin(komoditas_list)) & (data['Tahun'] == selected_tahun)]

# Plot perbandingan harga
if not comparison_data.empty:  # Cek apakah data tidak kosong
    plt.figure(figsize=(10, 6))
    sns.barplot(data=comparison_data, x='Komoditas', y='Harga')
    plt.title(f'Perbandingan Harga Antar Komoditas Tahun {selected_tahun}')
    plt.xlabel('Komoditas')
    plt.ylabel('Harga (Rp)')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.warning("Tidak ada data yang tersedia untuk tahun dan komoditas yang dipilih.")

# Menampilkan data berdasarkan tahun yang dipilih
filtered_data_tahun = data[data['Tahun'] == selected_tahun]
st.write(f"### Data Harga Tahun {selected_tahun}")
st.write(filtered_data_tahun)

# Visualisasi data per tahun
st.write("### Grafik Harga per Tahun")
st.bar_chart(filtered_data_tahun.groupby('Tahun')['Harga'].mean())