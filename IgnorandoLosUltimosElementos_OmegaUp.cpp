#include <iostream>
using namespace std;
int main() {
  int a, k;
    cin>>a;
    int arr[a];
    for(int i = 0; i< a; i++){
        cin>>arr[i];
    }
    cin>>k;
    for(int i = 0; i< a - k; i++) {
        cout<<arr[i]<<" ";
    }

  return 0;
}