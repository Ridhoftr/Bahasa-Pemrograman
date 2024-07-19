import sqlite3

class Pembelian:
    def __init__(self, nama_barang, harga_barang, jumlah_barang):
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.jumlah_barang = jumlah_barang
        self.total_harga = harga_barang * jumlah_barang

    def tampilkan_info(self):
        print("\n=== Data Pembelian ===")
        print(f"Nama Barang   : {self.nama_barang}")
        print(f"Harga Barang  : Rp{self.harga_barang:.2f}")
        print(f"Jumlah Barang : {self.jumlah_barang}")
        print(f"Total Harga   : Rp{self.total_harga:.2f}")

def buat_tabel():
    conn = sqlite3.connect('pembelian.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pembelian (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_barang TEXT NOT NULL,
            harga_barang REAL NOT NULL,
            jumlah_barang INTEGER NOT NULL,
            total_harga REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def simpan_pembelian(pembelian):
    conn = sqlite3.connect('pembelian.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pembelian (nama_barang, harga_barang, jumlah_barang, total_harga)
        VALUES (?, ?, ?, ?)
    ''', (pembelian.nama_barang, pembelian.harga_barang, pembelian.jumlah_barang, pembelian.total_harga))
    conn.commit()
    conn.close()

def tampilkan_semua_pembelian():
    conn = sqlite3.connect('pembelian.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pembelian')
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("Tidak ada data pembelian.")
        return
    
    print("\n=== Semua Data Pembelian ===")
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"Nama Barang   : {row[1]}")
        print(f"Harga Barang  : Rp{row[2]:.2f}")
        print(f"Jumlah Barang : {row[3]}")
        print(f"Total Harga   : Rp{row[4]:.2f}\n")

def tambah_pembelian():
    print("=== Input Data Pembelian ===")
    nama_barang = input("Nama Barang: ")
    harga_barang = float(input("Harga Barang (dalam Rupiah): "))
    jumlah_barang = int(input("Jumlah Barang: "))
    total_harga = harga_barang * jumlah_barang
    
    return Pembelian(nama_barang, harga_barang, jumlah_barang)

def main():
    buat_tabel()
    
    while True:
        pembelian = tambah_pembelian()
        pembelian.tampilkan_info()
        simpan_pembelian(pembelian)
        
        lanjut = input("\nApakah Anda ingin menambahkan data pembelian lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    print("\nTerima kasih! Have a nice day :).")
    tampilkan_semua_pembelian()

if __name__ == "__main__":
    main()
