#include <iostream>
#include <bitset>
#include <string>
using namespace std;

int main()
{
    int num = 2;
    bitset<32> bin(num);
    string a = bin.to_string();
    a.erase(0, a.find_first_not_of('0'));
    cout<<a<<"\n";
    string b = "";
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] == '0')
        {
            b += '1';
        }
        else{
            b+= '0';
        }
    }
    cout<<b<<"\n";
    bitset<32> reversa(b);
    cout<<reversa<<"\n";
    int salida = static_cast<int>(reversa.to_ulong());
    cout<<salida;
}