#include <iostream>

using namespace std;

// Function prototypes
void menu();
int tambah(int, int);
int kurang(int, int);
int kali(int, int);
int bagi(int, int);

int main() {
    menu();
    int num1, num2;
    int choice;
    cout << "Masukan dua angka: ";
    cin >> num1 >> num2;
    cout << "Menu" <<endl;
    cout << "1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\nMasukan pilihan anda: ";
    cin >> choice;
    switch (choice) {
        case 1:
            cout << "Hasilnya adalah: " << tambah(num1, num2) << endl;
            break;
        case 2:
            cout << "Hasilnya adalah: " << kurang(num1, num2) << endl;
            break;
        case 3:
            cout << "Hasilnya adalah: " << kali(num1, num2) << endl;
            break;
        case 4:
            if (num2 != 0)
                cout << "Hasilnya adalah: " << bagi(num1, num2) << endl;
            else
                cout << "Error: Pembagian dengan nol tidak bisa!." << endl;
            break;
        default:
            cout << "Pilihan tidak ada!" << endl;
            break;
    }
    return 0;
}

void menu() {
    cout << "KALKULATOR\n";
}

int tambah(int num1, int num2) {
    return num1 + num2;
}

int kurang(int num1, int num2) {
    return num1 - num2;
}

int kali(int num1, int num2) {
    return num1 * num2;
}

int bagi(int num1, int num2) {
    return num1 / num2;
}