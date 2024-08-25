#include <iostream>
using namespace std;

int main()
{
    int par = 0, impar = 0, a = 0;
    for (int i = 0; i < 10; i++)
    {
        cin >> a;
        if (a % 2 == 0)
        {
            par++;
        }
        else
        {
            impar++;
        }
    }
    cout << par << " " << impar;
}