#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int nivel, min_diversion, total_diversion = 0;

    cin >> nivel;
    min_diversion = nivel;
    total_diversion = nivel;

    // Leer los n-1 juguetes restantes
    for (int i = 1; i < n; ++i)
    {
        cin >> nivel;
        total_diversion += nivel; // Sumar el nivel de diversión al total
        if (nivel < min_diversion)
        { // Actualizar el juguete con el nivel de diversión mínimo
            min_diversion = nivel;
        }
    }

    // La mayor diversión posible es la suma total menos el juguete con menor diversión
    int max_diversion = total_diversion - min_diversion;

    // Imprimir el resultado
    cout << max_diversion << endl;

    return 0;
}
