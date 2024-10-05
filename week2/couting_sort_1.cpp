#include <bits/stdc++.h>
using namespace std;

int f[100] = {0};

int main() {
  int n, aux;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    cin >> aux;
    f[aux]++;
  }

  for (int i = 0; i < 100; ++i) {
    cout << f[i];

    if (i == n - 1) {
      cout << endl;
    } else {
      cout << " ";
    }
  }

  return 0;
}
