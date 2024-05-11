#include <iostream>

using namespace std;

int main() {
    for(int i = 1; i <=10;++i) {
        cout << i << 
        char z = 'A' + i - 1;
        if(z<= 'J'){
            cout << z << endl;
        }
    }
}