#include <iostream>
#include <bitset>
#include <string>
using namespace std;

int main()
{
    unsigned int num;
    cin >> num;
    bitset<64> bin(num);
    string a = bin.to_string();
    a.erase(0, a.find_first_not_of('0'));
    string b = "";
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] == '0')
        {
            b += '1';
        }
        else
        {
            b += '0';
        }
    }
    bitset<64> reversa(b);
    int salida = static_cast<unsigned int>(reversa.to_ulong());
    cout << salida << " ";
    string invertida(a.rbegin(), a.rend());
    bitset<64> complemento(invertida);
    salida = static_cast<unsigned int>(complemento.to_ulong());
    cout << salida;
}