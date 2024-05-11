#include <iostream>
#include <string>

using namespace std;
int main()
{
	int menu,jml,total;
    char pil;
	string namaMenu;
	const int harga1=12000, harga2=16000, harga3=9000;
	const string menu1="TEH", menu2="KOPI", menu3="CIRENG";
	
    menu :
	cout<<"~~~~~~~~~~DAFTAR MENU JUALAN~~~~~~~~~~"<<endl;
	cout<<"1. TEH"<<endl;
	cout<<"2. KOPI"<<endl;
	cout<<"3. CIRENG"<<endl;
    cout<<"4. BATAL ORDER"<<endl;
	cout<<"-------------------------------------"<<endl;
	
	cout<<"Masukan No Menu Pilihan = ";
	cin>>menu;
	
	switch(menu){
		case 1 :
            cout << "MENU TEH"<<endl;
            cout<<"Harga 1 "<<menu1<<" : Rp. "<<harga1<<endl;
			cout<<"Jumlah : ";
			cin>>jml;
			total=jml*harga1;
			cout<<"Total Harga : Rp. "<<total<<endl;
		    break;
		case 2 :
            cout<<"MENU KOPI"<<endl;
			cout<<"Harga 1"<<menu2<<" : Rp. "<<harga2<<endl;
			cout<<"Jumlah : ";
			cin>>jml;
			total=jml*harga2;
			cout<<"Total Harga : Rp. "<<total<<endl;
		    break;
		case 3 :
            cout<<"MENU CIRENG"<<endl;
			cout<<"Harga "<<menu3<<" : Rp. "<<harga3<<endl;
			cout<<"Jumlah : ";
			cin>>jml;
			total=jml*harga3;
			cout<<"Total Harga : Rp. "<<total<<endl;
			break;
        case 4 :
            goto keluar;
            break;

		default : 
        cout<<"Menu tidak tersedia";
	}
        keluar:
            cout << "\n TERIMA KASIH" << endl;
	return 0;
}