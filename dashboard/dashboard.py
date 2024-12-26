import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset
dataset = pd.read_csv('E-commerce-public-dataset/products_dataset.csv')

# Membersihkan data
dataset_cleaned = dataset.dropna(subset=['product_weight_g', 'product_category_name'])

# Menambahkan judul dan deskripsi
st.title('Analisis Data E-Commerce')
st.write("Dashboard ini menunjukkan hasil analisis distribusi berat produk per kategori dan hubungan antara berat dan dimensi produk.")

# Menampilkan visualisasi distribusi berat produk per kategori
st.subheader('Distribusi Berat Produk per Kategori')
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.boxplot(data=dataset_cleaned, x='product_category_name', y='product_weight_g', ax=ax1)
plt.xticks(rotation=90)
st.pyplot(fig1)

# Menampilkan visualisasi hubungan antara berat dan panjang produk
st.subheader('Hubungan antara Panjang Produk dan Berat Produk')
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=dataset_cleaned, x='product_length_cm', y='product_weight_g', ax=ax2)
st.pyplot(fig2)

# Menampilkan hubungan antara berat dan tinggi produk
st.subheader('Hubungan antara Tinggi Produk dan Berat Produk')
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=dataset_cleaned, x='product_height_cm', y='product_weight_g', ax=ax3)
st.pyplot(fig3)

# Menampilkan hubungan antara berat dan lebar produk
st.subheader('Hubungan antara Lebar Produk dan Berat Produk')
fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=dataset_cleaned, x='product_width_cm', y='product_weight_g', ax=ax4)
st.pyplot(fig4)
