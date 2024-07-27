## Komunikasi Aplikasi dengan Database dalam Python
Python memiliki beberapa pustaka yang memungkinkan aplikasi berkomunikasi dengan berbagai jenis database. Beberapa pustaka populer untuk database relasional termasuk sqlite3, psycopg2 (untuk PostgreSQL), dan mysql-connector-python (untuk MySQL). Pustaka-pustaka ini menyediakan API untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada database.

Berikut adalah langkah-langkah umum untuk berkomunikasi dengan database menggunakan Python:

- Menghubungkan ke Database: Membuat koneksi ke database menggunakan kredensial yang sesuai.

- Membuat Cursor: Menggunakan cursor untuk mengeksekusi perintah SQL.

- Menjalankan Query: Menjalankan perintah SQL menggunakan cursor.

- Mengambil Data: Mengambil hasil query jika diperlukan.

- Menutup Koneksi: Menutup cursor dan koneksi setelah operasi selesai.