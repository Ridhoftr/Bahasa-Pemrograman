#include <iostream>
using namespace std;

int main() {
    int num1, num2;
    char operasi;

    cout << "Masukan Angka Pertama : ";
    cin >> num1;

    cout << "Masukan Angka Kedua : ";
    cin >> num2;

    cout << "Penjumlahan : " << num1 + num2 << endl;
    cout << "Pengurangan : " << num1 - num2 << endl;
    cout << "Perkalian : " << num1 * num2 << endl;
    cout << "Pembagian : " << num1 / num2 << endl;

    return 0;
}