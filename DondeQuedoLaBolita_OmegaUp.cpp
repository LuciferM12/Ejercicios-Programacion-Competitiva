#include <iostream>
using namespace std;

void intercambio(int &a, int &b)
{
    int aux = 0;
    aux = a;
    a = b;
    b = aux;
}

int main()
{
    int nueces[4] = {0, 0, 0, 0};
    int bolita = 0;
    int movs = 0;
    int opc = 0;
    cin >> bolita;
    nueces[bolita - 1] = 1;
    cin >> movs;
    for (int i = 0; i < movs; i++)
    {
        cin >> opc;
        switch (opc)
        {
        case 1:
            intercambio(nueces[0], nueces[1]);
            break;
        case 2:
            intercambio(nueces[0], nueces[2]);
            break;
        case 3:
            intercambio(nueces[0], nueces[3]);
            break;
        case 4:
            intercambio(nueces[1], nueces[2]);
            break;
        case 5:
            intercambio(nueces[1], nueces[3]);
            break;
        case 6:
            intercambio(nueces[2], nueces[3]);
            break;
        }
    }
    for (int i = 0; i < 4; i++)
    {
        if (nueces[i] != 0)
        {
            cout << i + 1;
        }
    }

    return 0;
}