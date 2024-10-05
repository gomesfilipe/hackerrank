#include <bits/stdc++.h>
using namespace std;

int r[101] = {0};

int main() {
  int n, k, aux, count = 0, pos;

  cin >> n >> k;

  for (int i = 0; i < n; ++i) {
    cin >> aux;

    pos = aux % k;

    if (pos == 0) {
      count += r[pos];
    } else {
      count += r[k - pos];
    }

    r[pos]++;
  }

  cout << count << endl;
  return 0;
}
