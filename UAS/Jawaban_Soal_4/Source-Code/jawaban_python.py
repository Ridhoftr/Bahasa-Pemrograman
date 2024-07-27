import sqlite3

# Membuat koneksi ke database (atau membuat database baru jika belum ada)
conn = sqlite3.connect('example.db')

# Membuat cursor
cursor = conn.cursor()

# Membuat tabel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Menambahkan data
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ("Alice", 30))

cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ("Bob", 25))

# Menjalankan query untuk mengambil data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Menampilkan data
for row in rows:
    print(row)

# Menutup cursor dan koneksi
cursor.close()
conn.close()
