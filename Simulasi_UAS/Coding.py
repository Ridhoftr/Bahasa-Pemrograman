import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data contoh
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product': ['Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X', 'Smartphone X'],
    'purchase_date': pd.to_datetime(['2023-07-01', '2023-07-01', '2023-07-02', '2023-07-02', '2023-07-02', '2023-07-03', '2023-07-03', '2023-07-03', '2023-07-03', '2023-07-03']),
    'delivery_date': pd.to_datetime(['2023-07-03', '2023-07-03', '2023-07-04', '2023-07-04', '2023-07-04', '2023-07-05', '2023-07-05', '2023-07-05', '2023-07-05', '2023-07-05']),
    'location': ['Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta'],
    'payment_method': ['Credit Card', 'E-Wallet', 'Credit Card', 'Credit Card', 'E-Wallet', 'E-Wallet', 'Credit Card', 'E-Wallet', 'E-Wallet', 'Credit Card'],
    'age': [28, 32, 25, 34, 29, 30, 27, 26, 31, 33],
    'gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
    'review': ['Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive']
}

df = pd.DataFrame(data)

# Analisis "What"
product_counts = df['product'].value_counts()
print("What: Produk yang dibeli\n", product_counts)

# Analisis "Who"
age_distribution = df['age'].describe()
gender_distribution = df['gender'].value_counts()
print("\nWho: Demografi pelanggan\n", age_distribution, "\n", gender_distribution)

# Analisis "Where"
location_distribution = df['location'].value_counts()
print("\nWhere: Lokasi pembelian\n", location_distribution)

# Analisis "When"
purchase_counts_by_date = df['purchase_date'].value_counts().sort_index()
print("\nWhen: Waktu pembelian\n", purchase_counts_by_date)

# Analisis "Why"
review_distribution = df['review'].value_counts()
print("\nWhy: Ulasan pelanggan\n", review_distribution)

# Analisis "How"
payment_method_distribution = df['payment_method'].value_counts()
print("\nHow: Metode pembayaran\n", payment_method_distribution)

# Visualisasi
plt.figure(figsize=(12, 8))

# Plot produk yang dibeli
plt.subplot(2, 2, 1)
sns.countplot(y='product', data=df, palette='viridis')
plt.title('Produk yang Dibeli')

# Plot demografi pelanggan
plt.subplot(2, 2, 2)
sns.histplot(df['age'], kde=True, color='blue')
plt.title('Distribusi Usia Pelanggan')

# Plot waktu pembelian
plt.subplot(2, 2, 3)
purchase_counts_by_date.plot(kind='bar', color='green')
plt.title('Jumlah Pembelian per Tanggal')
plt.xlabel('Tanggal Pembelian')
plt.ylabel('Jumlah Pembelian')

# Plot metode pembayaran
plt.subplot(2, 2, 4)
sns.countplot(y='payment_method', data=df, palette='magma')
plt.title('Metode Pembayaran')

plt.tight_layout()
plt.show()
