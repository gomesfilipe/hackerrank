#include <bits/stdc++.h>
using namespace std;

int m[100][100];

int main() {
  int n, sum = 0;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cin >> m[i][j];
    }
  }

  for (int i = 0, j = n - 1; i < n; ++i, j--) {
    sum += m[i][i] - m[i][j];
  }

  cout << abs(sum) << endl;
  return 0;
}
