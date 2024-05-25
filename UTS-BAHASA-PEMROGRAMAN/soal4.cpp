#include <iostream>

using namespace std;

int main() {
    int tahun_lahir, usia;

    cout << "Tulis Tahun Lahir Anda: ";
    cin >> tahun_lahir;

    usia = 2024 - tahun_lahir;

    cout << "Berarti usia kalian sekarang adalah " << usia << " tahun." << endl;

    return 0;
}