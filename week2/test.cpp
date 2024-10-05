#include <bits/stdc++.h>
using namespace std;

int maxx4(int a, int b, int c, int d) {
  return max(max(max(a, b), c), d);
}

int m[256][256];

int main() {
  int q, n, sum, maxx;
  cin >> q;

  while (q--) {
    cin >> n;
    sum = 0;

    for (int i = 0; i < 2 * n; ++i) {
      for (int j = 0; j < 2 * n; ++j) {
        cin >> m[i][j];
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        sum += maxx4(m[i][j], m[i][2 * n - 1 - j], m[2 * n - 1 - i][j], m[2 * n - 1 - i][2 * n - 1 - j]);
      }
    }

    cout << sum << endl;
  }
  return 0;
}
