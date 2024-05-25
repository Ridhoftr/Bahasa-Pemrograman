#include <iostream>

using namespace std;
int main() {
    int n, s, i, j;
    cout << "Masukan jumlah baris : ";
    cin >> n;
    for (i = 1; i <= n; i++) {
        for (s = i; j < n; j++)
            cout << " ";
        for (j = 1; j <= i; j++)
            cout << "*";
        cout << "\n";
    }
}

// Penjelasan : 
// Ini adalah pola segitiga terbalik dengan spasi di sebelah kiri. Jumlah barisnya sesuai dengan input pengguna,
// dan setiap baris memiliki jumlah bintang yang sesuai dengan nomor barisnya.
// Spasi sebelum bintang juga bertambah seiring dengan peningkatan nomor baris.



