#include <iostream>

using namespace std;

int main()
{
    int length = 0, pos = 0, neg = 0, sum = 0, num = 0;
    cin >> length;
    for (int i = 0; i < length; i++)
    {
        cin >> num;
        if (num < 0)
        {
            neg++;
        }
        else
        {
            pos++;
        }
        sum += num;
    }
    cout << sum << "\n";
    cout << pos << "\n";
    cout << neg << "\n";

    return 0;
}