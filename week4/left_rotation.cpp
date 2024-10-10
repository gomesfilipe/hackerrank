#include <bits/stdc++.h>
using namespace std;

void readArray(vector<int>& v, int n) {
  int aux;
  for (int i = 0; i < n; ++i) {
    cin >> aux;
    v.push_back(aux);
  }
}

int arr[100000];

int main() {
  int n, d;
  cin >> n >> d;

  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  if (d < n) {
    for (int i = d; i < n; ++i) {
      cout << arr[i] << " ";
    }
  }

  for (int i = 0; i < d; ++i) {
      cout << arr[i];

      if (i < d - 1) {
        cout << " ";
      } else {
        cout << endl;
      }
    }

  return 0;
}
